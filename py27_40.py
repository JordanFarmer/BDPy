from datetime import datetime

now = datetime.now()

print '(repr)' + repr(now)
print '(str)' + str(now)
print(now)
# from console, use now directly

print (now,)
print[now, ]
print{now, }
print{'k1': now}
print[str(now), ]