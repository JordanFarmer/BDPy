class Emp:
    pass


class Engineer(Emp):
    pass


class PM(Emp):
    pass


class HR(Emp):
    pass


emp1 = Emp()
engineer1 = Engineer()
pm1 = PM()
hr1 = HR()
staffs = [(emp1, "generic employee"),
          (engineer1, "engineer 1"),
          (pm1, "project management1"),
          (hr1, "human resource1")]
classes = [Emp, Engineer, PM, HR]

for staff, name in staffs:
    for emp_class in classes:
        isA = isinstance(staff, emp_class)
        message1 = 'is a' if isA else 'is not a'
        print name, message1, emp_class.__name__

print '**for subclass practice**'
for class1 in classes:
    for class2 in classes:
        isSub = issubclass(class1, class2)
        message1 = '{0} a suclass of'.format('is' if isSub else 'is not')
        print class1.__name__, message1, class2.__name__
