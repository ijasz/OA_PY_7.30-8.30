import length
import addition


# user = input("Check words length : ")
num = int(input("how many numbers to add : "))

list = []

for i in range(1,num+1):
    list.append(int(input(f"Enter {i} number : ")))


print(length.l(list), "length")

# print(length.l(int(user)))

print(addition.addList(list), "sum")

