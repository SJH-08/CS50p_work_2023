# Import library to use
import sys
import requests
import json

# User has to specify the number of bitcoin to buy
# 0 < input < 2
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# If argument cannot be converted into a float --> exit + error message
try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line is not a number")


try:
# Send a web request
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# Catch exceptions
except requests.RequestException:
    sys.exit("error in getting the cost of bitcoin")

else:
# Get a JSON object
# Find the USD rate in the dict
# Calcultate the bitcoin rate
    data = response.json()
    price = data["bpi"]["USD"]["rate_float"]
    amount = bitcoin * price
# Output the current cost of bitcoin in USD (4 dec , sep=",")
    print(f"${amount:,.4f}")
