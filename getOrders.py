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
responseCount = requests.request("GET", countURL, headers=headers, data=payload)

count = json.loads(responseCount.text)
while True:

    print("*" * 25)
    print("What would you like to do?")
    print("*" * 25)
    print("c = Get New Order Count")
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

    if answerMenu == "u":

        updateURL = "https://api.reptimeqa.com/reptime/public/api/import/M32685/orders/{orderID}/status/update"
        updateID = input("Enter the ID of the order to be updated: ", )
        replacedURL = updateURL.replace("{orderID}", updateID)
        # print for testing purposes
        print(replacedURL)
        responseUpdate = requests.request("POST", replacedURL, headers=headers, data=payload)

        # Make payload variable too, potential options for user.
        payload = "Backorder"
        headers = {
            'x-api-key': 'd843ec7a50cf568b220e3ec6fb2bc795',
            'Content-Type': 'text/plain',
        }

        print("Order(s) have been updated!")

    if answerMenu == "c":

        # Currently functional, but need to wildcard search for response, not sure how to do that yet.
        if ":1" in responseCount.text:

            print('\nYou have', count['response'], 'new order(s), would you like to download them?\n')

            answer = input("Type y for yes, n for no: ", )

            if answer == "y":
                detailsURL = "https://api.reptimeqa.com/reptime/public/api/orders/export/M32685/open"

                # GET API to obtain new order details
                response = requests.request("GET", detailsURL, headers=headers, data=payload)
                results = response.json()
                print("Your orders have been marked as RECEIVED.\n")

            if answer == "n":
                print("Thank you, see you later!")

else:
    print("There are no new orders")
