import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

mu = 80
sigma = 8
x = mu + sigma * np.random.randn(1000000)
print len(x)
num_bins = 50
# normed ==> density
n, bins, patches = plt.hist(x, num_bins, density=1, facecolor='blue', alpha=0.5)
# install scipy, from scipy.stats import norm
y = norm.pdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('sample data')
plt.ylabel('frequency')
plt.title('demo1 for histogram')
plt.show()
# pip install scipy