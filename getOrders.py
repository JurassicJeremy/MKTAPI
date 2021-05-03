import requests
import json

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
    print('You have','new orders, would you like to download them?')

    answer = input("Type y for yes, n for no: ", )

    if answer != "n":
        detailsURL = "https://api.reptimeqa.com/reptime/public/api/orders/export/M32685/open"

        # GET API to obtain new order details
        response = requests.request("GET", detailsURL, headers=headers, data=payload)

        results = response.json()

        print(results['response'][0]['pONumber'])

        # updateURL = "https://api.reptimeqa.com/reptime/public/api/import/M32685/orders/a87e7307-ffc6-490a-b1ac-f1a5d8f6c719/status/update"
        #
        # payload = "Pending"
        # headers = {
        #     'x-api-key': 'd843ec7a50cf568b220e3ec6fb2bc795',
        #     'Content-Type': 'text/plain',
        # }
        #
        # response = requests.request("POST", updateURL, headers=headers, data=payload)

else:
    print("There are no new orders")
