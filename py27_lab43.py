# encoding=UTF-8
import itertools

x = ['a', 'b', 'c']
y = [1, 2, 3]
z = [u'甲', u'乙', u'丙', u'丁']
result = itertools.chain(x, y, z)
print type(result)
for i in result:
    print 'first time', i
for i in result:
    print 'second time', i
result2 = itertools.chain(x, y, z)
list2 = list(result2)
for i in list2:
    print '[2]first time', i
for i in list2:
    print '[2]second time', i