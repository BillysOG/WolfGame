class Shape:
    def __init__(self,colour,is_filled):
        self.colour = colour
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.is_filled else 'is not filled'}")
        
class Circle(Shape):
    def __init__(self,colour,is_filled, radius):
        super().__init__(colour,is_filled)
        self.radius = radius
    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {self.radius * 3.14 * self.radius}cm2\n")
        
    def area(self):
        return self.radius * 3.14 * self.radius
        
class Square(Shape):
    def __init__(self,colour,is_filled, side):
        super().__init__(colour,is_filled)
        self.side = side
    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.side * self.side}cm2\n")
        
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self,colour,is_filled,  base, height):
        super().__init__(colour,is_filled)
        self.base = base
        self.height = height
    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {0.5 * self.base * self.height}cm2\n")
        
    def area(self):
        return self.base * 0.5 * self.height

class Paper(Square):
    def __init__(self,colour,is_filled, side):
        super().__init__(colour,is_filled, side)
        self.colour = colour
        self.is_filled = is_filled
        self.side = side

circle = Circle("blue",False,8)
square = Square("red",True,5)
triangle = Triangle("green", True,4,5)
paper = Paper("white",True,9)

shapes = [circle, square, triangle, paper]

print()

circle.describe()
square.describe()
triangle.describe()
for shape in shapes:
    print(f"{shape.__class__.__name__} : {shape.area()}cm2")

print()