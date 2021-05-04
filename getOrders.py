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

count = json.loads(response.text)

#resolve issue with incorrect data showing. Shows count even when there are no orders.
for count['response'] in response.text:
    if count['response'] >= '0':

        print('\nYou have', count['response'], 'new order(s), would you like to download them?\n')

        answer = input("Type y for yes, n for no: ", )

        if answer == "y":
            detailsURL = "https://api.reptimeqa.com/reptime/public/api/orders/export/M32685/open"

            # GET API to obtain new order details
            response = requests.request("GET", detailsURL, headers=headers, data=payload)
            results = response.json()

            while True:
                print("*" * 25)
                print("What would you like to do?")
                print("*" * 25)
                print("d = Download Data File")
                print("v = View Raw Order Data")
                print("u = Update Order Status")
                print("q = Quit")
                print("*" * 25)
                answerMenu = input(":")


                if answerMenu == "d":
                    # Creates TXT file, and adds API response to file
                    with open("apiResults1.txt", "w") as file:
                        file.write(json.dumps(results))
                        print("File Opened")
                        os.startfile("apiResults1.txt")

                if answerMenu == "v":
                    print("Here is the raw data:\n", response.content)


                if answerMenu == "q":
                    print("\nThank you, see you soon!")
                    break

                # if answerPrint == "u":

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
            print("Thank you, see you later!")

    else:
        print("There are no new orders")
