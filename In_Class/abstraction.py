from abc import ABC, abstractmethod
import math

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print('Car Started')
    def stop(self):
        print('Car stopped')
#car = Car()
#car.start()
#car.stop()


# Exercise 3 : Using Multiple abstract method
# Create an abstract class for shapes, should have method area(), perimeter()
#Create a Rectangle and Circle to implement both methods

class Shapes(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass

class Circle(Shapes):
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        perimeter = 2 * math.pi * self.r 
        print(f"Perimeter of the circle = {perimeter:.2f}cm")

    def area(self):
        area = math.pi * (self.r ** 2)
        print(f"Area of the circle = {area:.2f} sqcm")

circle1 = Circle(20)
circle1.perimeter()
circle1.area()
print("\n")

class Rectangle(Shapes):
    def __init__(self, L, W):
        self.L = L
        self.W = W

    def perimeter(self):
        perimeter = 2 * (self.L + self.W) 
        print(f"Perimeter of the rectangle = {perimeter:.2f}cm")

    def area(self):
        area = self.L * self.W
        print(f"Area of the rectangle = {area:.2f} sqcm")

rectangle1 = Rectangle(50, 20)
rectangle1.perimeter()
rectangle1.area()
print("\n")