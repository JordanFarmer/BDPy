# encoding=UTF-8
s1 = '中文輸入法'

print('{:_<30}==='.format(s1))
print('{:*>30}==='.format(s1))
print('{:@^30}==='.format(s1))
print('{:\'^30}==='.format(s1))

s2 = s1 * 5
s3 = u'中文輸入法' * 5
print('%s' % s2)
print('%.9s' % s2)
print('%.9s' % s3)
print('{:s}'.format(s2))
print('{:.12s}'.format(s2))
print(len(s1))
print(len(s3))
print(u'{:.7s}'.format(s3))