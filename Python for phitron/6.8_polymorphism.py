import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Function to calculate and print the area of a shape
def print_area(shape):
    print(f"Area: {shape.area()}")

# Create instances of different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 7)

# Call the function to calculate and print the area of different shapes
print_area(circle)     # Outputs: Area: 78.53981633974483
print_area(rectangle)  # Outputs: Area: 24
print_area(triangle)   # Outputs: Area: 10.5
