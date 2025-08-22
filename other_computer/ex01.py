sum = 0

for i in range(1,101):
    sum = sum + i

print(sum)
x=6
print((x==6))

x,y,z = "Orange", "Red", "Yellow"
print(x)

#in collection type: List, Tuple, Dictionary

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(1, "kiwi")
print(len(fruits))
 
students = ('Hayes', 99)
students


for x in fruits:
    print(x)
print("================================")

[print(x) for x in fruits]

newList = [x for x in fruits]
newList

newListA = [x for x in fruits if "a" in x]
print("For Newlist")
newListA


newListnum = [x for x in range(10,15)]
newListnum

newListup = [x.upper() for x in fruits]
newListup


