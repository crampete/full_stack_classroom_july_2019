from our_math.geometry import square, circle


print(f"Area of a circle with radius 3 is {circle.area(3)}")
print(
    f"Circumference of a circle with radius 5 units is {circle.perimeter(5)}")


print(f"Area of a square of side 3.33 units is {round(square.area(3.33), 2)}")
print(f"Perimeter of a square of side 5 units is {square.perimeter(5)}")
