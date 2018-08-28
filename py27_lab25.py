# encoding=UTF-8
string1 = '0123456789' * 3
print '%30s' % string1
print '%30s' % string1[:15]
print '%30s' % string1 * 2
print '%30s' % '中文測試驗'
print '%30s' % u'中文測試驗'
print '{:>30}'.format(string1[:15])
print '{:>30}'.format('中文測試驗')
print u'{:>30}'.format(u'中文測試驗')
print '{:>30}'.format(string1 * 2)