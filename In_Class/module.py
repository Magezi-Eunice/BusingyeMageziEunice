import pandas

data = {
    "Name": ["John", "Agnes", "Peter"],
    "Age": [24, 21, 23]
}

print(data)
df = pandas.DataFrame(data)
print(df)

list1 = [1, 2, 3]
list2 =['a', 'b', 'c']

combined = list(zip(list1, list2))
print(combined)