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

## Additional information

### Risk of using the trading bot

Trading bots come with inherent risks, and the volatile nature of the cryptocurrency market can lead to financial losses. Users should exercise caution, thoroughly understand the functionalities of the bot, and be aware that past performance is not indicative of future results. It is crucial to trade responsibly and only invest what one can afford to lose.

By using this bot, you accept the associated risks :

- The high volatility of cryptocurrencies can result in the partial or complete loss of your capital.
- You will be solely responsible for the loss of this capital. Neither I or anyone else will be required to reimburse the lost amount.

Seeking professional financial advice is recommended, especially for those unfamiliar with the complexities of trading. Remember that the cryptocurrency market is dynamic, and adjustments may be necessary to adapt to changing conditions. Please trade responsibly and be aware of the evolving nature of the crypto space.
