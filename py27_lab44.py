import itertools

l1 = list('PQRSTUV')
print l1

p1 = itertools.permutations(l1, 2)
result1 = list(p1)
print(len(result1), result1)
c1 = itertools.combinations(l1, 2)
result2 = list(c1)
print(len(result2), result2)