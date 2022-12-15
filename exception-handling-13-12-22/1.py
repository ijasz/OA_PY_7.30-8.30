# Name Error
# print(a)


# ZeroDivisionError
# print(5 / 0)

# try:
#     # a = 5
#     print(a)
# except:
#     print("something went wrong")

# try:
#     # print(5 / 0)
#     print("hi")
# except NameError:
#     print("something went wrong")

# except ZeroDivisionError:
#     print("Sorry, can't able to divide with 0")

# finally:
#     print("finally am working")


a = -2

if(a < 0):
    raise Exception("sorry")
else:
    print(a)