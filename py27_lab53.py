# encoding=UTF-8
import requests

# change this when you copy my file
URL = 'https://andbiz1222.firebaseio.com/%s.json'

url4 = URL % 'sample4_lists'
url5 = URL % 'sample4_dict'

patchJson5 = {'name': 'BDPY Python跟bigdata實戰演練', 'schedule': ['M', 'Tu', 'W']}
r5 = requests.patch(url5, json=patchJson5)
print r5.status_code, r5.content

patchJson4 = {'2':3.14159268,'7':'add something from patch'}
r4 = requests.patch(url4, json=patchJson4)
print r4.status_code, r4.content