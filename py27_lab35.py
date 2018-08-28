set1 = {'A', 'P', 'P', 'L', 'E'}
set2 = {'B', 'A', 'N', 'A', 'N', 'A'}
set3 = {'P', 'I', 'N', 'E', 'A', 'P', 'P', 'L', 'E'}
print(set1)
print(set2)
print(set3)
print(set1 < set3, set3 < set1)
print(set1 < set2, set2 < set1)
print(set1 | set2)
print(set1 & set2)
print(set1 ^ set2)
print(len(set1), len(set2), len(set3))
for s1 in set1:
    print('iterate:', s1)

set1.add('X')
print(set1)
for e in set2:
    set1.add(e)
print(set1)