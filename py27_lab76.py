class Foo:
    def __init__(self):
        print 'init process'
        pass

    def __iter__(self):
        print 'start iterate'
        return self

    def next(self):
        print 'iterate through'
        raise StopIteration


f1 = Foo()
for i in f1:
    print i
print(type(f1))