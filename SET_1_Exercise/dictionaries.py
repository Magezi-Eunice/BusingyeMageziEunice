#printing a value
Shoes = {
	"brand" : "Nick",
	"color" : "black",
	"size" : 40
}

print(Shoes["size"])

#changing a value
Shoes["brand"] = "Adidas"
print(Shoes)

#adding a key/value pair
Shoes["type"] = "sneakers"
print(Shoes)

#returing all keys
print(Shoes.keys())

#returning all values
print(Shoes.values())

#checking if key "size" exists

#looping through dictionary
for item, value in Shoes.items():
    print(item, value)

#removing item from dictionary
del Shoes["color"]
print(Shoes)

#emptying dictionary
Shoes.clear()
print(Shoes)

#creating a dictionary and making a copy
student = {
    "name": "Moses Bukenya",
    "age": 20,
    "course": "Software Engineering"
}

clone = student.copy()
print(clone)

#nested dictionaries
student = {
    "name": "Moses Bukenya",
    "age": 20,
    "course": "Software Engineering",
    "address" : {
        "phone" : "0774789302",
        "home address" : "Kololo"
    },
    "year" : "II"    
}

print(student)