pi = 22/7

def circleArea(r):
    area = pi * r * r

    print(f"The area of the circle is {area:.2f}cm")


radius = float(input("Enter the circle of the radius(cm): "))

circleArea(radius)