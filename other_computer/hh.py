
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(1, "kiwi")
print(len(fruits))
 
fruits.sort()
print("Sort Fruits: ", fruits)
fruits.sort(reverse = True)
print(fruits)

#dictionary use curly braces
thisDict = {
    "brand" : "ford",
    "model" : "Mustang",
    "year"  : 19023

}
print(thisDict["brand"])
print(thisDict)

secondDict = dict(name = "Benjie ", age = 18)
print(secondDict["name"])