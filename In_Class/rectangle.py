def rect_area():
    length = int(input("Enter rectangle lenth(cm): "))
    width = int(input("Enter rectangle width(cm): "))
    area = length * width
    print(f"The area of the rectangle is {area:.,}cm")


rect_area()