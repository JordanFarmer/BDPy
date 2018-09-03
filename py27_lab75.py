class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def __str__(self):
        return 'dim=[%d,%d]' % (self.width, self.height)


r1 = Rectangle(3, 5)
print r1
print 'area=%d' % r1.calculate_area()
r2 = Rectangle(4, 6)
print r2, 'area=%d' % r2.calculate_area()