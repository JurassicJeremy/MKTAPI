import requests
import json
import os

countURL = "https://api.reptimeqa.com/reptime/public/api/orders/export/M32685/count"

payload = {}
headers = {
    # API Key provided by MarketTime
    'x-api-key': 'd843ec7a50cf568b220e3ec6fb2bc795'
}
# GET API to obtain count of new orders
response = requests.request("GET", countURL, headers=headers, data=payload)

#need to allow for any numbers
if ":1" in response.text:
    #need to show how many new orders there are
    print('\nYou have','new orders, would you like to download them?\n')

    answer = input("Type y for yes, n for no: ", )

    if answer == "y":
        detailsURL = "https://api.reptimeqa.com/reptime/public/api/orders/export/M32685/open"

        # GET API to obtain new order details
        response = requests.request("GET", detailsURL, headers=headers, data=payload)
        results = response.json()

        #Creates TXT file, and adds API response to file
        with open("apiResults1.txt", "w") as file:
            file.write(json.dumps(results))
            print("\nOrders downloaded and marked as RECEIVED.\n")
            file.close()

            print("*" * 25)
            print("What would you like to do?")
            print("*" * 25)
            print("d = Download Data File")
            print("u = Update Order Status")
            print("q = Quit")
            print("*" * 25)
            input_ = input(":")

            answerPrint = input("Type y for yes, n for no: ", )

            if answerPrint == "y":
                #Opens the TXT file
                os.startfile("apiResults1.txt")
                print("Enjoy!")

            if answerPrint == "n":
                print("\nThank you, see you soon!")


        # updateURL = "https://api.reptimeqa.com/reptime/public/api/import/M32685/orders/a87e7307-ffc6-490a-b1ac-f1a5d8f6c719/status/update"
        #
        # payload = "Pending"
        # headers = {
        #     'x-api-key': 'd843ec7a50cf568b220e3ec6fb2bc795',
        #     'Content-Type': 'text/plain',
        # }
        #
        # response = requests.request("POST", updateURL, headers=headers, data=payload)

    if answer == "n":
        print("Thank you, come again!")

else:
    print("There are no new orders")
