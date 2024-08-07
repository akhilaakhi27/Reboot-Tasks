import math
def area_calculator():
    shape = input("Choose shape (circle, square, rectangle, triangle): ").lower()
    
    if shape == "circle":
        radius = float(input("Enter radius: "))
        area = math.pi* (radius ** 2)
        print(f"The area of the circle is: {area}")
    elif shape == "square":
        side = float(input("Enter side length: "))
        area = side ** 2
        print(f"The area of the square is: {area}")
    elif shape == "rectangle":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print(f"The area of the rectangle is: {area}")
    elif shape == "triangle":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is: {area}")
    else:
        print("Invalid shape.")
area_calculator()
