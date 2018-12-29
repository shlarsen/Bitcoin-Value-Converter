"""#Python 3.7.1 Bitcoin Value Converter by Sam Henry Larsen"""
import requests

apiStatus1 = requests.get("https://blockchain.info/ticker")

apiStatus2 = requests.get("https://blockchain.info/tobtc?currency=USD&value=500")

if apiStatus1.status_code and apiStatus2.status_code == 200:
    print("API Status: OK")
else:
    print("API Status: OFFLINE")

print("\nWelcome to the Bitcoin Price and Conversion Application!\n")

stop = False

while not stop:
    menu = input("Press 'p' for current BTC price, 'c' to convert USD to BTC, or 'q' to quit: ")
    print()

    api1 = requests.get("https://blockchain.info/ticker")

    json_out1 = api1.json()
    price = json_out1["USD"]["last"]

    if menu == 'p':
        print("${}".format(price))
        print("\n----------------------------------------")
    elif menu == 'c':
        num = input("Enter the USD amount you would like to convert to BTC: ")
        print()
        api2 = requests.get("https://blockchain.info/tobtc?currency=USD&value={}".format(num))
        print(api2.content.decode("utf-8"), "BTC")
        print("\n----------------------------------------")
    else:
        stop = True
        print("Process has ended. Thank you!")
