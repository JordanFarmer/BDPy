sales = {'iphone6': 490, 'iphone6+': 670, 'iphone8': 400, 'iphone8+': 300, 'watch3': 200}
print sales['iphone6'], sales['iphone8']
# print sales['ucom']
print sales.get('ucom'), sales.get('iphone8')
for i in sales:
    print('key=%s, value=%s' % (i, str(sales[i])))
print('ucom' in sales, 'iphone6' in sales, 500 in sales)

for i in sales.keys():
    print('get key=', i)

summation = 0
for i in sales.values():
    summation += i
    print(type(i), i)

print('total sales=%d' % (summation))

for i in sales.items():
    print(type(i), i)
for i in sales.items():
    print('key=%s, value=%s' % (i[0], i[1]))
for key, value in sales.items():
    print('***key=%s, value=%s' % (key, value))

sales['iPad'] = 500
print(sales)
sales.update({'iPad': 700, 'iphone6+': 300, 'mighty': 200})
print(sales)
del sales['iphone6']
print(sales)