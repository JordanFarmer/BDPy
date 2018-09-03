class Car:
    vendor = 'Lexus'
    valid = True


print Car.vendor, Car.valid
c1 = Car()
c1.color = 'RED'
c2 = Car()
print c1.vendor, c2.vendor, Car.vendor
print c1.color
c2.capacity=70
print c2.capacity
Car.maxSpeed = 140
print Car.maxSpeed, c1.maxSpeed, c2.maxSpeed