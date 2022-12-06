##Arbitrary Arguments

##def add(*a):
##    z = 0
##    for i in a:
##        z += i
##    print(z)

##add()
##add(1,6)
##add(1,6,6)
##add(1,6,46,8)
##add(1,6,6,5,6,8)


##keyword aruguments

##def person(name, location, age):
##    print(name,location,age)

##person(age= 15,name="ragava", location="pondy")

##Arbitrary Keyword Arguments, **kwargs

##def person(**a):
##    print(a)


##person(age= 15,name="ragava", location="pondy", address= "saram")


##Default Parameter Value

def person(name="", location="", age=""):
    print(name,location,age)

person("ragava",  "pondy")
person("ragava",  "pondy", 20)
person()
