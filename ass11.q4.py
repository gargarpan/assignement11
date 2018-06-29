class Shape:
    def __init__(self):
        self.length=10
        self.breadth=20

    def squarearea(self):
        return self.length*self.length

    def rectanglearea(self):
        return self.length*self.breadth

class rectangle(Shape):
    def rectangle(self):
        print("Area Of Rectangle:",super().rectanglearea())

class square(Shape):
    def square(self):
        print("Area Of Square:",super().squarearea())

obj=Shape()
obj1=rectangle()
obj2=square()

obj1.rectangle()
obj2.square()
