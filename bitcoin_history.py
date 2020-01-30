########################################################################################
# Purpose: Obtain historic bitcoin values based on date
# Author: Gary Hooks
# Email: garyhooks@gmail.com
# Date: 7th February 2019
########################################################################################

import requests
import sys
import datetime

def dateFormat(rawDate):
    ## Convert date YYYY-MM-DD
    myDate = datetime.datetime.strptime(rawDate, "%Y-%m-%d")
    return myDate.strftime("%d %B %Y")

def main():

    ## Obtain required information from user

    quantity = input("Insert amount of bitcoin: ")
    date = input("Enter date required (YYYY-MM-DD): ")
    currency = input("Enter currency to convert to (Default: GBP): ")
    if len(currency) < 1:
        currency = "GBP"

    ## Build URL for API lookup and then use requests to obtain response from Coindesk API 
    url = "https://api.coindesk.com/v1/bpi/historical/close.json&?start=" + date + "&end=" + date + "&currency=" + currency
    print("\nObtaining Values from: " + url + " ... ")
    try:
        data = requests.get(url).json()
    except:
        sys.exit("[*] ERROR: Issue with obtaining information online, check input values or internet connection")

    ## Pull value from json string returned from Coindesk API 
    value = data["bpi"][date]
    print ("[*] Value of a single Bitcoin for date: " + str(dateFormat(date)) + " is " + str(value) + " " + currency)

    ## calculate total by multiplying the quantity by the single BTC value at the time 
    total = round(float(quantity) * float(value), 2)
    print ("[*] Your selected amount of Bitcoin (" + str(quantity) + ") on this date is " + str(total) + " " + currency)

    print ("\n-End")
if __name__ == "__main__":
    main()
