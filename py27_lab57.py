# encoding=UTF-8
p = u'中文輸入'
print repr(p.encode('utf8'))
print repr(p.encode('big5'))
print repr(p.encode('ms950'))