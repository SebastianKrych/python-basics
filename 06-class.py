class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(self.brand + " drives nicely!")


car = Car("Mazda")
print(car.brand)
car.drive()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)

