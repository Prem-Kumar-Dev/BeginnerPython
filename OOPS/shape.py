class shape:
    def __init__(self,color):
        self.color = color
        

class rectangle(shape):
    def __init__(self, length, breadth,color):
        self.length = length
        self.breadth = breadth
        super().__init__(color)

    def area(self):
        return self.length * self.breadth
    
    def rectangle_display(self):
        print("Length:{} Breadth:{} Area:{} Color:{}".format(self.length, self.breadth, self.area(), self.color))

class triangle(shape):
    def __init__(self, base, height,color):
        self.base = base
        self.height = height
        super().__init__(color)

    def area(self):
        return 0.5 * self.base * self.height

    
    def traingle_details(self):
        print("Base:{} Height:{} Area:{} Color:{}".format(self.base, self.height, self.area(), self.color))

r = rectangle(10, 20, "Red")
r.rectangle_display()
t = triangle(10, 20, "Green")
t.traingle_details()


