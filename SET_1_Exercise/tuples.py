#outputting favorite phone brand
x = ("samsung", "iphone", "tecno", "redmi")
print(x[0])

#outputting second last item
print(x[-2])

# changing "iphone" to "itel"
temp = list(x)
temp[1] = "itel"
x = tuple(temp)

print(x)

#adding "Huawei" to tuple
temp2 = list(x)
temp2.append("Huawei")
x = tuple(temp2)

print(x)

#looping through tuple
for item in x:
    print(item)

#deleting first item
temp3 = list(x)
del temp3[0]
x = tuple(temp3)

print(x)

#using the tuple constructor
cities_list = ["Kampala","Jinja", "Masaka", "Entebbe"]
cities_tuple = tuple(cities_list)
print(cities_tuple)

#unpacking a tuple
Capital, Eastern, Western, Central = cities_tuple

print(Capital)
print(Central)
print(Eastern)
print(Western)

#printing range of indexes
print(cities_tuple[1:5])

#joining tuples
firstNames = ("Eunice", "Jasmine")
secondName = ("Busingye", "Magezi")
name = secondName + firstNames

print(name)

#multiply a tuple
colors = ("red", "pink", "blue", "purple")
new_colors = colors * 3
print(new_colors)

#counting how many times 8 appears
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))