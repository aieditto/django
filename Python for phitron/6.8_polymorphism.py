class Figure:
    def size(self, height, width):
        self.height=height
        self.width=width

class Square(Figure):
    def __init__(self, height) -> None:
        self.height=height
        pass
    
    def calculation(height):
        result = height*height
        return result
    

Squaree=Square()
Squaree.calculation(5)