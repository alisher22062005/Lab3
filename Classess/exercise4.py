class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print(self.x,self.y)

    def show(self):
        print(self.x-5,self.y-5)

    def move(self):
        self.x=self.x-5
        self.x=self.x-5
        print(self.x,self.y)

    def dist(self):
        if self.x>self.y:
            print(self.x-self.y)
        elif self.x==self.y:
            print(0)
        else:
            print(self.y-self.x)


x=int(input())
y=int(input())
points=Point(x,y)
points.show()
points.move()
points.dist()