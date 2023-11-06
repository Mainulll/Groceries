import requests
from bs4 import BeautifulSoup

url = 'https://www.coles.com.au/browse/fruit-vegetables?pid=homepage_cat_explorer_fruit_vege'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.findAll('div', class_='LinesEllipsis  product__title')

    for product in products:
        title = product.find('span', class_='LinesEllipsis  product__title').text
        price = product.find('span', class_='price__value').text
        print(title, price)
else:
        print('Failed to connect to the website')

    