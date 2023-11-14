import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime




def scrape_flipkart(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

#     response = requests.get(url, headers=headers)

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data from {url}: {e}")
        return []
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        product_name = soup.find_all('span', class_='B_NuCI')
        price = soup.find_all('div', class_='_30jeq3 _16Jk6d')
        Mrp = soup.find_all('div', class_='_3I9_wc')
#         tot=soup.find_all('div',class_='_3XINqE')

        data = []

        for product, price, Mrp in zip(product_name, price, Mrp):
            data.append({
                'product_name': product.text.strip(),
                'price': price.text.strip(),
                'Mrp': Mrp.text.strip()
#                 'tot':tot.text.strip()
            })

        return data
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return []

# Read URLs from Excel file
excel_file_path = r"/content/sample_data/url/FLIPKART_URLs.xlsx"
df = pd.read_excel(excel_file_path)

url_column = 'URL'
url_list = df[url_column]
print(url_list)