import requests
import sys
import json  # for presenting the API in JSON format


try:  # checks that input is a number or decimal
    if len(sys.argv) == 2 and sys.argv[1].isalpha() == False:
        # request API and output of it
        bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        # converts to 2nd argument or the number to a float
        t = float(sys.argv[1])

        # finds the rate of a float and converts it to an integer
        b = bitcoin.json()
        b = float(b["bpi"]["USD"]["rate_float"])

    # exception if the request is not successful or if the index for commandline argument is out of range
except (requests.RequestException, IndexError):
    print("Missing command-line argument")
    sys.exit()

    # if the command line argument is not a number or decimal
except ValueError:
    print("command-line argument is not a number")
    sys.exit()
    # formatting for the number to have commas for each thousandth and up and also to display up to the 4th decimal place
else:
    print(f"${t * b:,.4f}")
