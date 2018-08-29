# encoding=UTF-8
import requests

# change this when you copy my file
URL = 'https://fbdemo2017-169c4.firebaseio.com/%s.json'

for i in range(20):
    url6 = URL % 'data6_records'
    json6 = {'item': 'battery', 'quantity': i + 20, 'id': i}
    r6 = requests.post(url6, json=json6)
    print r6.status_code, r6.content