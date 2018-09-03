import pandas_datareader.wb as wb

# fred.py
# change first line to
# from pandas.api.types import is_list_like
# string <-- comes from data.worldbank.org
data = wb.search(string='SE.PRM.TENR', field='id')
# type(data)
# data.iloc[:,2:]
# data.iloc[:,1]
# data.iloc[0,1]
