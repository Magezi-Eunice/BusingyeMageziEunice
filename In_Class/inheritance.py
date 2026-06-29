class Person:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print('Name: ', self.name)


class Student(Person):
    def study(self):
        print(' I am studying python')

student = Student('Eunice')

student.display()
student.study()