# encoding=UTF-8
import pandas

data1 = pandas.read_csv('.//data//data3_utf8.csv')
print data1.columns
data2 = data1[['處分字號', '違反勞動基準法條款', '違反法規內容']].groupby(['違反勞動基準法條款','違反法規內容']).count()
print data2
data3 = data2.sort_values('處分字號', ascending=False)
print data3
