# Python Supports Three access modifiers
'''
Python Supports Three access modifiers
- Public, accessible everywhere
- Protected, accessible within the class and subclass
-Private , accessible only inside the class

'''

# Employee Example, name, salary, age
# Public Name
class Employee:
    def __init__(self):
        self.name = 'Peter'

emp = Employee()

print(emp.name)


# Protect Salary (single underscore before variable name)
class Employee:
    def __init__(self):
        self._salary = 600000

emp = Employee()

#print(emp._salary)

# Private Salary (double underscore before variable name)
class Employee:
    def __init__(self):
        self.__salary = 600000

emp = Employee()

#print(emp._Employee__salary)


#Exercise : Create a class called car with, brand, model, price then make brand public, 
# model protected, price private, Display all values appropriately

class Car:
    def __init__(self):
        self.brand = "Toyota"
        self._model = "Mini Pajero"
        self.__price = 200000000

car1 = Car()
print(car1.brand)
print(car1._model)
print(car1._Car__price)