import csv
sampleFile = open('.\\data\\data.csv')
sampleReader = csv.reader(sampleFile)
sampleData = list(sampleReader)
sampleFile.close()

print sampleData

for row in sampleData:
    for col in row:
        print 'now process %s'%str(col)