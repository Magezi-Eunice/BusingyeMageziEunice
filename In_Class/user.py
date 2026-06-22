class User:

    def __init__(self, first_name, last_name, age, nationality, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.gender = gender

    def describe_user(self):
        print(f"The user is called {self.first_name} {self.last_name}, aged {self.age}. The user is {self.nationality} and {self.gender} ")


    def greet_user(self):
        print(f"Welcome back {self.first_name}!")

user1 = User("Joy", "Namuli", 25, "Ugandan", "Female")
user2 = User("Mason", "Black", 30, "American", "Male")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()