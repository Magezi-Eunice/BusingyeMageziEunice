#creating a set
drinkList = ["Mocha", "Mirinda Orange", "Mango Booster"]
favorites = set(drinkList)
print(favorites)

#adding items to a set
favorites.add("Minute Maid")
favorites.add("Nojito")
print(favorites)

#checking membership
mySet = {"oven", "kettle", "microwave", "refrigerator"}

if "microwave" in mySet:
    print("Item is present")
else:
    print("Item is absent")


# removing a member
mySet.remove("kettle")
print(mySet)

#looping through a set
for item in mySet:
    print(item)

#adding a list to a set
food = {"fries", "pizza", "burger", "strawberry"}
food_list = ["mango", "apple"]

food.update(food_list)
print(food)

#joining two sets
age = {18}
name = {"Jane"}
combinedSet = age | name
print(combinedSet)



####STRINGS

#concatenating two variables
age = 18
name = "Mary is "
sentence = name + str(age)
print(sentence)

#removing space
txt = "  Hello,  Uganda!  "
print(txt.replace(" ", ""))

#making uppercase
print(txt.upper())

#replacing characters
print(txt.replace("U", "V"))

#returning a range of characters
y = "I am proudly Ugandan"
print(y[1:4])

#correcting an error
#x = "All "Data Scientists" are cool!" [code with error]

x = "All Data Scientists are cool!" # fixed
print(x)