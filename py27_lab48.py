import requests
from bs4 import BeautifulSoup

url1 = 'https://www.mobile01.com/'
url2 = 'https://www.mobile01.com/category.php?id=4'
url3 = 'https://www.mobile01.com/category.php?id=15'
url4 = 'https://www.mobile01.com/category.php?id=6'
urls = (url1, url2, url3, url4)
for url in urls:
    result1 = requests.get(url)
    soup = BeautifulSoup(result1.content, 'html.parser')
    # print(type(soup), soup.text)

    print soup.title.name, soup.title.string
    hot_topics = soup.find('div', {'id': 'hot-posts'})
    hot_topics.find_all('a')
    for hot_topic in hot_topics:
        print hot_topic