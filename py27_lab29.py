l1 = list('abcde')
l2 = l1
l3 = l1[:]
l4 = list(l1)
l5 = [item for item in l1]
print(hex(id(l1)), hex(id(l2)), hex(id(l3)), hex(id(l4)), hex(id(l5)))
l1[0] = 'A'
l2[2] = 'C'
l1[4] = 'E'
print(l1, l2, l3, l4, l5)