import demoModule as d

s1 = d.foo(1, 2)
s2 = d.bar(3, 4)
print('inside lab37, s1=%s' % s1)
print('inside lab37, s2=%s' % s2)

from demoModule import foo, bar

s3 = foo(5, 6)
print('again, s3=%s' % s3)
s4 = bar(7, 8)
print('again, s4=%s' % s4)

from demoModule import foo as f, bar as b

s5 = f(9, 10)
s6 = b(11, 12)
print('once again, s5=%s' % s5)
print('once again, s6=%s' % s6)

import sys

print(sys.path)