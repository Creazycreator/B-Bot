<p align="center">
    <img src="https://github.com/Creazycreator/B-Bot/assets/77204986/cb6ab57a-cbc4-4246-b057-238b8411f4b2" alt="B-Bot logo">
</p>

## B-Bot
A Binance bot that buys new cryptocurrencies.
  - Uses WebSockets for better performance. 🚀
  - Semi-automatic bot. 🤖

## Features
- Help to configure your API key
- Choose the cryptocurrency you want to monitor
- Set the time at which you want the code to launch.
    - This option will likely change.
- Executes trades only in USDT

## Resource Table

| Resource                        | Links                                   |
| ------------------------------- | --------------------------------------- |
| 💿 **Installation**             | [Installation](https://github.com/Creazycreator/B-Bot?tab=readme-ov-file#installation)|
| 📚 **How to use**               | [How to use](https://github.com/Creazycreator/B-Bot?tab=readme-ov-file#how-to-use)|
| 🔑 **Binance API Key**          | [Binance API Key](https://github.com/Creazycreator/B-Bot?tab=readme-ov-file#binance-api-key)|
| ⌚ **Coming soon**              | [Coming soon](https://github.com/Creazycreator/B-Bot?tab=readme-ov-file#coming-soon)
| 📰 **General Information**      | [General Information](https://github.com/Creazycreator/B-Bot?tab=readme-ov-file#general-information)|
| 📑 **Additional Information**   | [Additional Information](https://github.com/Creazycreator/B-Bot?tab=readme-ov-file#additional-information)|

## Installation
This code has been tested on **Windows 10** with **Python 3.10.X**

1. Install the necessary dependencies

```bash
pip install -r requirements.txt
```

2. Run the code
    - You can launch it either with the **launch.bat** file or in a terminal with the following command:

```bash
python main.py
```

## How to use

1. At first, you will be asked for the API key. Just follow the instructions; if you don't have an API key, the process is explained below
2. Then, once the API keys are validated, you will need two pieces of information:
    - The name of the upcoming new listing
    - The date on which the new listing will be available
3. Once these pieces of information are known, enter the pair name (case insensitive, and do not add USDT as it will be added automatically)
    - [❌] BTCUSDT, btcusdt
    - [✔] BTC, btc
4. Next, for the date, I recommend setting it to 20 seconds before the arrival of the new listing, for example:
    - For example, if the pair is scheduled to be listed at 10:00 AM
    - You should set it to 9:59:40
    - The 20 seconds will be dedicated to launching the WebSocket; this manipulation will be corrected in future versions
5. Once all these parameters are entered, you just have to wait for the bot to buy as soon as it receives information about the new pair
6. It is crucial to **_keep the program open until the end_**; otherwise, the purchase of the new pair will not occur (unless you want to stop the program with CTRL+C)

## Binance API Key
For Binance API keys, you can follow this link that explains how to obtain them: [How to Create API Keys on Binance?](https://www.binance.com/en/support/faq/how-to-create-api-keys-on-binance-360002502072)

Additionally, it is necessary to activate the Trade permission.
You will need to _**whitelist your IP**_ first to secure the use of your API keys.
To find out your IP, you can use one of the following two sites:
- [What Is My IP?](https://www.whatismyip.com/)
- [What Is My IP Address](https://whatismyipaddress.com/)

Make sure to **take the IPv4** and not the IPv6 because Binance does not accept IPv6. It should look something like this: 8.8.8.8.

![IP](https://github.com/Creazycreator/B-Bot/assets/77204986/91a13f5b-be3b-4276-bb2f-a997ceadf193)

Don't forget to authorize trades, otherwise, the bot will return an error during the buy order.
- The other parameters are not necessary.

![Trading](https://github.com/Creazycreator/B-Bot/assets/77204986/4d40e1a1-91c2-48f4-89bf-ed2adf03f2a9)

## Coming soon

- [ ] Possibility to set the amount in USDT for the buy order.
- [ ] Write a more organized code
- [ ] Subtract 10 seconds from the requested launch time of the code (WebSocket launch time)

## General Information

### Change the amount to be traded
1. At the moment, the bot only allows trading on the USDT pair
2. The amount to be placed in the buy order can be modified within the code for now
   - It is not recommended to set a value too high, as it may result in losses
   
```python
amount_in_usdt = 5  # (Line 145) Change the value here to increase or decrease how much you want to buy on a dip (currently set to 5 USDT)
symbol_to_buy = pair_to_watch

order = client.create_order(
    symbol=symbol_to_buy,
    side=SIDE_BUY,
    type='MARKET',
    quoteOrderQty=amount_in_usdt,
)
```

### Compatible versions:

- [❌] Python 3.8.X
- [✔] Python 3.9.X
- [✔] Python 3.10.X
- [✔] Python 3.11.X
- [❌] Python 3.12.X

## Additional information

### Risk of using the trading bot

Trading bots come with inherent risks, and the volatile nature of the cryptocurrency market can lead to financial losses. Users should exercise caution, thoroughly understand the functionalities of the bot, and be aware that past performance is not indicative of future results. It is crucial to trade responsibly and only invest what one can afford to lose.

By using this bot, you accept the associated risks :

- The high volatility of cryptocurrencies can result in the partial or complete loss of your capital.
- You will be solely responsible for the loss of this capital. Neither I or anyone else will be required to reimburse the lost amount.
- Do not use a large amount for the purchase, as you may risk losing a significant sum.

Seeking professional financial advice is recommended, especially for those unfamiliar with the complexities of trading. Remember that the cryptocurrency market is dynamic, and adjustments may be necessary to adapt to changing conditions. Please trade responsibly and be aware of the evolving nature of the crypto space.
