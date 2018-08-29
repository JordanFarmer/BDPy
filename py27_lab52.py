# encoding=UTF-8
import requests

# change this when you copy my file
URL = 'https://fbdemo2017-169c4.firebaseio.com/%s.json'
url1 = URL % 'sample1_string'
url2 = URL % 'sample2_ch_string'

url3 = URL % 'sample3_ch_utf'
url4 = URL % 'sample4_lists'
url5 = URL % 'sample4_dict'
url6 = URL % 'data6_records'

r1 = requests.get(url1)
print r1.content
r2 = requests.get(url2)
print r2.content
r3 = requests.get(url3)
print r3.content
r4 = requests.get(url4)
print r4.content
r5 = requests.get(url5)
print r5.content
r6 = requests.get(url6)
print r6.content
biddings = r6.json()
print type(biddings)
for values in biddings.values():
    for k, v in values.items():
        print 'key=%s, value=%s' % (k, v)