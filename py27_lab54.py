import requests

URL = 'https://fbdemo2017-169c4.firebaseio.com/%s.json'
url1 = URL % 'sample1_string'
url2 = URL % 'sample2_ch_string'

url3 = URL % 'sample3_ch_utf'
url4 = URL % 'sample4_lists'
url5 = URL % 'sample4_dict'
url6 = URL % 'data6_records'

r1 = requests.delete(url1)
print r1.status_code, r1.content
requests.delete(url2)
requests.delete(url3)
requests.delete(url4)
requests.delete(url5)
requests.delete(url6)
