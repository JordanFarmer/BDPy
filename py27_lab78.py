class Foo:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
        pass

    def __iter__(self):
        return self

    def next(self):
        if self.counter < self.limit:
            self.counter += 1
            return 'result=%d' % self.counter
        else:
            raise StopIteration


f1 = Foo(5)
for i in f1:
    print 'this line is printing::', i
f2 = Foo(7)
for i in f2:
    print i