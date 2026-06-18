#list of five people, outputing 2nd item
people = ["James", "Mary", "John", "Eileen", "Luna"]
print(people[1])

#changing value of first item
people[0] = "Jonathan"
print(people)

#adding sixth item
people.append("Henry")
print(people)

#adding "Bathel" as third item
people.insert(2, "Bathel")
print(people)

#removing 4th item
del people[3]
print(people)

#negative indexing to print the last item
print(people[-1])

#printing range of indexes
food = ["rice", "matooke", "irish", "beans", "yams", "cassava", "beef"]
print(food[2:5])

#copy of a list
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"]
countries_clone = countries.copy()
print(countries)
print(countries_clone)

#looping through list
for item in countries:
    print(item)

#sorting a list
animals = ["dog", "cat", "elephant", "tiger", "lion", "armadillo"]
print(animals)

animals.sort() #ascending order
print(animals)

animals.reverse() #descending order
print(animals)

#printing animals with 'a'
letter = "a"

for item in animals:
    if letter in item:
        print(item)

#joining lists
firstName = ["Magezi", "Eunice"]
secondName = ["Busingye"]

secondName.extend(firstName)
print(secondName)