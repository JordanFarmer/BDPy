class Emp():
    gradeLevel = 6

    def startWork(self):
        pass

    def endWork(self):
        pass


class RD(Emp):
    def __init__(self):
        self.currentGrade = self.gradeLevel

    def startWork(self):
        print 'rd start to work with gradle level%d' % self.currentGrade

    def endWork(self):
        print 'finish work with level%d' % self.currentGrade

class PM(Emp):
    def __init__(self):
        self.currentGrade = self.gradeLevel

    def startWork(self):
        print 'pm start to work with gradle level%d' % self.currentGrade

    def endWork(self):
        print 'pm finish work with level%d' % self.currentGrade

rd1 = RD()
pm1 = PM()
rd1.currentGrade = 9
pm1.currentGrade = 8
print Emp.gradeLevel, rd1.currentGrade, pm1.currentGrade
print rd1.gradeLevel, pm1.gradeLevel

pm1.startWork()
pm1.endWork()
rd1.startWork()
rd1.endWork()