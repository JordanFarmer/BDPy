# encoding=UTF-8
p = u'中文輸入'
print repr(p.encode('utf8'))
print repr(p.encode('big5'))
print repr(p.encode('ms950'))

new_string = '\xe5\xad\x97'
print new_string, repr(new_string)
print new_string.decode('latin-1'), new_string.decode('iso8859-1')
print new_string.decode('utf-8')