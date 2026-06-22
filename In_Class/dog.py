class dog:
    name = "Rex"
    breed = "German Shepherd"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def sit(self):
        print(f"{self.name} is sitting")

    def eat(self):
        print(f"{self.name} is eating.")


dog1 = dog("Max", "Poodle")
print(dog1.name)

dog1.sit()
dog1.eat()