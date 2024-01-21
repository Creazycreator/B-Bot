from binance.enums import SIDE_BUY
from binance.client import Client
from datetime import datetime
from pystyle import *
import threading
import websocket
import logging
import time
import json
import re
import os

lock = threading.Lock()

# Configuration file
config_file_path = 'config.json'

# Create a 'logs' folder if it doesn't already exist
log_folder = 'logs'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

log_filename = os.path.join(log_folder, datetime.now().strftime('%Y_%m_%d-%H_%M_%S')+'.log')

# Configure the log system
logging.basicConfig(
    filename=log_filename, 
    filemode='a', 
    format='[%(asctime)s] - %(levelname)s - %(message)s', 
    level=logging.INFO, 
    encoding='utf-8', 
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.warning("/!\ If you encounter any issues with the code, NEVER share your API key and secret key /!\\")

def on_message(ws, message):
    json_message= json.loads(message)
    
    updateId=json_message['u']
    symbol=json_message['s']
    best_bid_price=json_message['b']
    best_bid_qty=json_message['B']
    best_ask_price=json_message['a']
    best_ask_qty=json_message['A']
    
    print(f'Update ID : {updateId}')
    print(f'Symbol : {symbol}')
    print(f'Best bid price : {float(best_bid_price)}')
    print(f'Best bid quantity : {float(best_bid_qty)}')
    print(f'Best ask price : {float(best_ask_price)}')
    print(f'Best ask quantity : {float(best_ask_qty)}')
    logging.info(f'Update ID : {updateId}')
    logging.info(f'Symbol : {symbol}')
    logging.info(f'Best bid price : {float(best_bid_price)}')
    logging.info(f'Best bid quantity : {float(best_bid_qty)}')
    logging.info(f'Best ask price : {float(best_ask_price)}')
    logging.info(f'Best ask quantity : {float(best_ask_qty)}')
    
    # Release the lock to allow the main program to continue
    lock.release()

    # Close the connection after receiving information
    ws.close()

def listen_to_websocket(socket_url):
    ws = websocket.WebSocketApp(socket_url, on_message=on_message)
    ws.run_forever()

# Just an interface
def interface():
    os.system('cls' if os.name == 'nt' else 'clear')
    bbot = """
     /$$$$$$$          /$$$$$$$              /$$    
    | $$__  $$        | $$__  $$            | $$    
    | $$  \ $$        | $$  \ $$  /$$$$$$  /$$$$$$  
    | $$$$$$$  /$$$$$$| $$$$$$$  /$$__  $$|_  $$_/  
    | $$__  $$|______/| $$__  $$| $$  \ $$  | $$    
    | $$  \ $$        | $$  \ $$| $$  | $$  | $$ /$$
    | $$$$$$$/        | $$$$$$$/|  $$$$$$/  |  $$$$/
    |_______/         |_______/  \______/    \___/  
    
    """
    print(Colorate.Vertical(Colors.blue_to_purple, Center.XCenter(bbot), 2))

# Checking the validity of the API key
def is_api_key_valid(api_key, api_secret):
    try:
        client = Client(api_key=api_key, api_secret=api_secret)
        client.get_account()
        return True
    except Exception as e:
        print("Your API key doesn't seem to be working. Please verify the information.")
        print(f"Error during API key validation: {e}")
        logging.error(f"Error during API key validation: {e}")
        time.sleep(6)
        return False

# Execute the configuration of the config.json file
def apikey():
    while True:
        interface()
        already_created = input("Do you already have a Binance API key (Y | N): ")
        logging.info("Request API Key.")

        if already_created.lower() == "y":
            binance_api_key = input("Enter your Binance API Key: ")
            binance_api_secret = input("Enter your Binance API Secret Key: ")
            logging.info("Verifying the API key.")

            if is_api_key_valid(binance_api_key, binance_api_secret):
                config_data = {'binance': {'api_key': binance_api_key, 'api_secret': binance_api_secret}}
                with open(config_file_path, 'w') as config_file:
                    json.dump(config_data, config_file, indent=4)
                print('')
                print("The API key is functional!")
                logging.info("The API key is functional!")
                time.sleep(2)
                break 
            else:
                continue
            
        elif already_created.lower() == "n":
            print('')
            print('To create an API key, visit the link below: ')
            print('https://www.binance.com/en/support/faq/how-to-create-api-keys-on-binance-360002502072')
            print('')
            print("Once created, you will need to activate the permission to perform trades.")
            print('For more information, visit the following GitHub page: ')
            print('https://github.com/Creazycreator/B-Bot?tab=readme-ov-file#binance-api-key')
            print('')
            exit()
            
        else:
            print('The only choices are YES (Y) or NO (N).')
            logging.error("The only choices are YES (Y) or NO (N).")
            time.sleep(2)
            continue
        
    return True

def makebuy(pair_to_watch):
# Place a buy order if the WebSocket receives information about the pair
    try:
        amount_in_usdt = 5  # Amount in USDT you want to spend
        symbol_to_buy = pair_to_watch

        # Create a market buy order
        order = client.create_order(
            symbol=symbol_to_buy,
            side=SIDE_BUY,  # Use SIDE_BUY to indicate a buy order
            type='MARKET',  # Market price order
            quoteOrderQty=amount_in_usdt,
        )

        # Display order details
        print("Buy order successfully created:")
        print(f"Symbol: {order['symbol']}")
        print(f"Quantity: {order['origQty']}")
        print(f"Price: {order['price']}")
        print(f"Type: {order['type']}")
        print(f"Status: {order['status']}")
        logging.info("Buy order successfully created:")
        logging.info(f"Symbol: {order['symbol']}")
        logging.info(f"Quantity: {order['origQty']}")
        logging.info(f"Price: {order['price']}")
        logging.info(f"Type: {order['type']}")
        logging.info(f"Status: {order['status']}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        # Log an error
        logging.error(f"General error: {e}")
    
# Initialize the Binance client
binance_api_key = None
binance_api_secret = None

# Load API keys from the config.json file
if os.path.exists(config_file_path) and os.path.getsize(config_file_path) > 0:
    with open(config_file_path) as config_file:
        config_data = json.load(config_file)
    if 'binance' in config_data and 'api_key' in config_data['binance'] and 'api_secret' in config_data['binance']:
        binance_api_key = config_data['binance']['api_key']
        binance_api_secret = config_data['binance']['api_secret']

if not binance_api_key or not binance_api_secret or not is_api_key_valid(binance_api_key, binance_api_secret):
    if not apikey():
        exit()

# Initialize the Binance client after verifying the keys
client = Client(api_key=binance_api_key, api_secret=binance_api_secret)

try:
    interface()
    pair_to_watch = input("Enter the pair you want to monitor (e.g., 'BTC'): ")
    
    # Check if the pair name is valid
    if bool(re.match('^[a-zA-Z]+$', pair_to_watch)):
        pair_to_watch = pair_to_watch.lower() + 'usdt'
        logging.info(f"Program launched for the pair {pair_to_watch.upper()}")
        
        # Ask the user to enter the time to activate the code
        activation_time_str = input("Enter the time to activate the code (HH:MM:SS): ")
        activation_time = datetime.strptime(activation_time_str, '%H:%M:%S')
        logging.info(f"Activation time is: {activation_time_str}")
        
        while datetime.now().time() < activation_time.time():
            time_difference = datetime.combine(datetime.now().date(), activation_time.time()) - datetime.now()
            print(f"Waiting until activation time: {time_difference}", end='\r')
            
        print("\nActivation time reached. The program starts now...")
        logging.info("Activation time reached. The program starts now...")
        
        # Configure the socket
        socket_url = f"wss://stream.binance.com:9443/ws/{pair_to_watch}@bookTicker"
        # Create a WebSocket connection
        websocket_thread = threading.Thread(target=listen_to_websocket, args=(socket_url,))
        
        try:
            websocket_thread.start()
            lock.acquire()
            print('')
            print(f"The pair {pair_to_watch} is listening. Waiting for information... (Press Ctrl+C to interrupt.)")
        
        except KeyboardInterrupt:
            print("\nInterruption par l'utilisateur. WebSocket connection closed.")
        
        finally:
            # Wait for the end of the WebSocket thread
            websocket_thread.join()
            print('Attempting to send a buy order signal.')
            logging.info("Attempting to send a buy order signal.")
            makebuy(pair_to_watch.upper())
    else:
        print("The pair name is not valid. Use only alphabet letters.")
        logging.error(f"The pair name is not valid: {pair_to_watch}")
        
except KeyboardInterrupt:
    print("\n /!\ The program has been interrupted!")
    logging.info("Program interrupted by the user")
    exit()
    
except Exception as e:
    print(f"An error occurred: {e}")
    logging.error(f"General error: {e}")
