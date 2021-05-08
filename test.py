# Example of replacing URLs with IDs
IDs = input("Enter up to 3 IDs, seperated by commas: ").split(',')
URL = f'https://url.com/orders/orderID/status'

for x in IDs:
    updatedURL = URL.replace("orderID", x)
    print(updatedURL)
