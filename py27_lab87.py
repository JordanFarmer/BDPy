import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

randomSequence = pd.DataFrame(np.random.normal(1.0, 0.08, (100, 8)))
accumulates = randomSequence.cumprod()
accumulates.plot()
plt.title('random plot')
plt.xlabel('time')
plt.ylabel('value')
plt.show()
