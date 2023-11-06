import requests
from bs4 import BeautifulSoup

url = 'https://www.woolworths.com.au/shop/browse/fruit-veg'

# It's a good practice to include headers with your requests to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all <a> tags with the class 'product-title-link'
    data_elements = soup.find_all('a', class_='product-title-link')
    
    for element in data_elements:
        # The text of the <a> tag is the product name
        product_name = element.text.strip()  # .strip() removes any leading/trailing whitespace
        
        # The href attribute of the <a> tag contains the URL suffix for the product details
        product_url_suffix = element['href']
        product_url = f'https://www.woolworths.com.au/{product_url_suffix}'  # Assuming the base URL is required
        
        print(product_name, product_url)
else:
    print(f"Failed to retrieve content, status code: {response.status_code}")
