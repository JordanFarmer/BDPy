# encoding=UTF-8
import requests

# change this when you copy my file
URL = 'https://fbdemo2017-169c4.firebaseio.com/%s.json'

url1 = URL % 'sample1_string'
json1 = 'hello world_829_9:57'
r1 = requests.put(url1, json=json1)
print r1.status_code, r1.content

url2 = URL % 'sample2_ch_string'
json2 = '寫入'
r2 = requests.put(url2, json=json2)
print r2.status_code, r2.content

url3 = URL % 'sample3_ch_utf'
json3 = u'寫入'
r3 = requests.put(url3, json=json3)
print r3.status_code, r3.content

url4 = URL % 'sample4_lists'
json4 = ['key1', 200, 3.14, None, u'寫入']
r4 = requests.put(url4, json=json4)
print r4.status_code, r4.content

url5 = URL % 'sample4_dict'
json5 = {'name': 'bdpy', 'duration': 35}
r5 = requests.put(url5, json=json5)
print r5.status_code, r5.content