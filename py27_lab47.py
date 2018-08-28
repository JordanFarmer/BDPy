import requests
from bs4 import BeautifulSoup

url1 = 'https://www.uuu.com.tw/'
result1 = requests.get(url1)
soup = BeautifulSoup(result1.content, 'html.parser')
print(type(soup), soup.text)