class Person:
    firstName = ""
    lastName = ""

    def fullName(self):
        print(self.firstName + self.lastName)


obj1 = Person()
obj1.firstName = "anbu"
obj1.lastName = "arasan"
obj1.fullName()

obj2 = Person()
obj2.firstName = "vinoth"
obj2.lastName = "kumar"
obj2.fullName()


# print(obj1.firstName, obj1.lastName)
# print(obj2.firstName, obj2.lastName)
print(obj1)
print(obj2)
