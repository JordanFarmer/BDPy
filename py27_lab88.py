import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 1, 0.05)
plt.figure(1)
plt.subplot(311)
plt.plot(t, t, '-')
plt.subplot(312)
plt.plot(t, t ** 2, '-')
plt.subplot(3, 1, 3)
plt.plot(t, t ** 3, '-')
plt.show()
