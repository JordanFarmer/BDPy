class Emp():
    gradeLevel = 6

    def startWork(self):
        pass

    def endWork(self):
        pass


class RD(Emp):
    pass


class PM(Emp):
    pass


print RD.gradeLevel, PM.gradeLevel, Emp.gradeLevel
PM.gradeLevel = 8
print RD.gradeLevel, PM.gradeLevel, Emp.gradeLevel
Emp.gradeLevel = 7
print RD.gradeLevel, PM.gradeLevel, Emp.gradeLevel