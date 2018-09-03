# pip list --format=columns
# pip install ipython matplotlib pyreadline pandas numpy
# pip install ipython[notebook]
# remember to install this!!
# pip install pandas-datareader

import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6, 7), index=list(range(0, 12, 2)),
                   columns=list(range(0, 7, 1)))
print df1
print df1[0], df1[3], df1[4]
# ipython
# who
# df1[:2], df1[2:], df1.iloc[:2], df1.iloc[2:]
# df1[0] ==> first col
# df1.iloc[:,:3], df1.iloc[:,3:]
# df1.iloc[2:4, 3:5]
