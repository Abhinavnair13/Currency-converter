from requests import get
from pprint import PrettyPrinter
API_KEY ="fca_live_EdUJv18QnIEPQsiy7m6mWZt41QFNtsLsmxcTYKNo"
BASE_URL=f"https://api.freecurrencyapi.com/"

printer = PrettyPrinter()
def get_currencies():
    endpoint =f"v1/currencies?apikey={API_KEY}"
    url = BASE_URL+endpoint
    data = get(url).json()['data']

    data = list(data.items())
    data.sort()
    return data

def print_currency(currencies):
    #currencies is a tuple(str,list)
    for name,currency in currencies:

        name = currency['name']
        code = currency['code']
        symbol = currency.get('symbol_native',"")
        print(f"{code} - {name} - {symbol}")

def exchange_rates(currency1,currency2):
    if len(currency1)!=0 and len(currency2)!=0:
        endpoint = f"v1/latest?apikey={API_KEY}&currencies={currency1}&base_currency={currency2}"
        url = BASE_URL+endpoint
        response= get(url)
        if response.status_code==200:
            data = get(url).json()['data']


            data = list(data.values())[0]
            print(f"The currency conversion rate between {currency1} and {currency2} is {data}")
            return data
        else:
            print("Bad response.")
    else:
        print("Enter valid values for conversion")

def convert_currency(currency1,currency2,amount):
    conversion_rate = exchange_rates(currency1,currency2)
    conversion_rate = float(conversion_rate)
    amount =float(amount)
    amount2 = amount*conversion_rate
    print(f"{currency1}-{amount2}=> {currency2}-{amount}")

data = get_currencies()
print_currency(data)
currency1= input("Enter the first currency : ").upper()
currency2= input("Enter the second currency : ").upper()
exchange_rates(currency1,currency2)
while True:
    amount = input("Enter the amount you want to exchange : ")
    if amount.isdigit():
        convert_currency(currency1,currency2,amount)
        break
    else:
        print("Enter valid amount")
        continue
