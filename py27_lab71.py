import PIL

print PIL.__version__


class MyClass:
    pass


i1 = MyClass()


class MyClass2(object):
    pass


i2 = MyClass2()

print 'class type=', type(MyClass), type(i1)
print 'class2 type=%s,i2 type=%s' % (type(MyClass2), type(i2))
print 'for i1 the legacy way', i1.__class__, i1.__class__.__bases__
print 'for i2, the new way', i2.__class__, i2.__class__.__bases__
print 'i1 type is MyClass type?', type(i1) == MyClass
print 'i2 type is MyClass2 type?', type(i2) == MyClass2