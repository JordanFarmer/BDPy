# pip install requests
# pip install bs4
import requests

url1 = 'https://bugzilla.mozilla.org/rest/bug/35'
result1 = requests.get(url1)
print result1.status_code, result1.headers['content-type']
print type(result1.content), result1.content[:50]
print type(result1.json())
bugs = result1.json()['bugs']
for bug in bugs:
    for k, v in bug.items():
        print 'k=%s,v=%s' % (k, str(v))

firstBug = bugs[0]
ccDetails = firstBug['cc_detail']
for detail in ccDetails:
    print type(detail), detail