# pip install numpy
# pip list --format=columns
import numpy

a1 = numpy.arange(20)
print(type(a1), len(a1), a1)
a2 = numpy.arange(5, 20)
print(len(a2), a2)
a3 = numpy.arange(5, 20, 2)
print(len(a3), a3)
a4 = numpy.arange(0, 1, 0.1)
print(len(a4), a4)
a5 = numpy.linspace(0, 1)
print(len(a5), a5)
a6 = numpy.linspace(0, 1, 10)
print(len(a6), a6)

# pip install matplotlib
import matplotlib.pyplot as plt

plt.plot(a6, a6 ** 2, 'ro')
plt.show()
r7 = range(1, 10)
plt.plot(r7, r7 ** 2, 'gs')
plt.show()
