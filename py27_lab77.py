class Foo:
    def __init__(self):
        self.counter = 0
        print 'init process'
        pass

    def __iter__(self):
        print 'start iterate'
        return self

    def next(self):
        if self.counter < 10:
            print ('generate something inside')
            self.counter += 1
            return self.counter
        else:
            print 'iterate through'
            raise StopIteration

f1 = Foo()
for i in f1:
    print 'counter:', i
print(type(f1))