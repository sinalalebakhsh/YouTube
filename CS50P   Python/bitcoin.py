import sys
import requests

api_key = 'https://api.coindesk.com/v1/bpi/currentprice.json'
data = requests.get(api_key)
data = data.json()

price_bitcoin = data['bpi']['USD']['rate_float']

try:
    if len(sys.argv) != 2:
        sys.exit('Missing command-line argument')
    elif len(sys.argv) == 2:
        if float(sys.argv[1]):
            get_number_user = float(sys.argv[1])
            print(f'${price_bitcoin*get_number_user:,.4f}')
except ValueError:
    sys.exit('Command-line argument is not a number')
