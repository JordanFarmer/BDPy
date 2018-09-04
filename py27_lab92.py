import pandas
from matplotlib import pyplot, rc

# https://data.worldbank.org/indicator/SP.POP.TOTL
data1 = pandas.read_csv('.\\data\\data2.csv', skiprows=4, index_col='Country Name')
print data1.shape
print data1.columns
print data1.head()
print data1['1960'].mean(), data1['1960'].median(), data1['1960'].max(), data1['1960'].min()
data1['important'] = data1['1970'] + data1['1971'] + data1['1972']
print data1.columns
# pip install openpyxl
data1.to_excel('.\\data\\new.xlsx', sheet_name='population_total')
print data1['Country Code'].unique()
ausData = data1[data1['Country Code'] == 'AUS']
print ausData.shape
print ausData['1960'], ausData['1970'], ausData['1980']
font = {'family': 'Courier New'}
rc('font', **font)
pyplot.style.use('seaborn-notebook')
selected_years = ['1960', '1970', '1980', '1990', '2000']
ausData.plot(kind='bar', figsize=(14, 6), y=selected_years, fontsize=17)
for style in pyplot.style.available:
    print style,
pyplot.show()
