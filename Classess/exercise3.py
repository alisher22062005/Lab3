class Shape:
    def area(self):
        print(0)


class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print(self.length*self.width)



p=Shape()
p.area()
p=Rectangle(5,10)
p.area()