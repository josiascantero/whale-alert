import requests
from datetime import datetime
from bs4 import BeautifulSoup



url = "https://whale-alert.io/whales.html"
response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")
response.encoding = 'utf-8'

soup = BeautifulSoup(response.content, 'html.parser')
table_rows = soup.select('table.table tbody tr')

for row in table_rows:
    print(type(row.find))

crypto_data: list = []
