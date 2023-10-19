class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, name, radius) -> None:
        self.radius=radius
        self.name=name
    
    def area(self):
        result= 3.1416*self.radius**2
        return result
    
class Rectangle(Shape):
    def __init__(self, name, height, width) -> None:
        self.height=height
        self.width=width
        self.name=name
        
    def area(self):
        result= self.height*self.width
        return result


circle=Circle('circle',4)
print(f'Here is area of {circle.name} {circle.area()}')

rectangle=Rectangle('Rectangle', 20, 4)
print(f'Here is area of {rectangle.name} {rectangle.area()}')
    