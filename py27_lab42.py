import math
import random

print math.pi, math.e, math.sqrt(5)
myRandom = []
for i in range(1000):
    myRandom.append(random.randint(1, 500))

print myRandom[:10]

pokers = ['A', 'Joker', 'J', 'Q', 'K']
print 'choose', random.choice(pokers)
random.shuffle(pokers)
print pokers