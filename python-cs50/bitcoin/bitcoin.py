import requests
import sys
import json

if len(sys.argv) == 2:
    try:
        entry = float(sys.argv[1])
    except:
        sys.exit('Command-line argument is not a number')

else:
    sys.exit('Missing command-line argument')

try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    btc = response.json()['bpi']['USD']['rate_float']
    result = entry * btc
    print(f'${result:,.4f}')

except requests.RequestException:
    sys.exit('RequestException')