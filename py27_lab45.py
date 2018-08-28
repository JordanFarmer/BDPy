# encoding=UTF-8
import json

course1 = {'name': 'bdpy', 'duration': 35, 'schedule': ['Mon', 'Tue', 'Wed']}
string1 = json.dumps(course1)
print string1

waiting_list1 = ['Mark','John',u'阿福老師']
string2 = json.dumps(waiting_list1)
print string2

obj1 = json.loads(string1)
print type(obj1), obj1['schedule'], obj1['duration'],obj1['schedule'][1]

obj2 = json.loads(string2)
print type(obj2), obj2[2], obj2[1]