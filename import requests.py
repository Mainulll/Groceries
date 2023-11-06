import requests
from bs4 import BeautifulSoup

url = 'https://www.woolworths.com.au/shop/browse/fruit-veg'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # txt
    