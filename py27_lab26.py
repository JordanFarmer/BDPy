# encoding=UTF-8
string1 = '0123456789' * 3
print '%-30s||||||' % string1
print '%-30s||||||' % string1[:15]
print '%*s||||||' % (-30, string1[:15]) # extract formatter as a parameter
print '%-30s||||||' % string1 * 2
print '%-30s||||||' % '中文測試驗'
print '%-30s||||||' % u'中文測試驗'
print '{:<{}s}||||||'.format(string1[:15], 30)
print '{:>{}s}||||||'.format(string1[:15], 30)
print '{:<{}s}||||||'.format('中文測試驗', 30)
print '{:>{}s}||||||'.format('中文測試驗', 30)
# print '{:<{}s}||||||'.format(u'中文測試驗', 30)
# print '{:>{}s}||||||'.format(u'中文測試驗', 30)