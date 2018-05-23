class Rectangle:
    def __init__(self, c, w, h):
        self.color = c
        self.width = w
        self.height = h

    def square(self):
        return self.width*self.height


rect1 = Rectangle(w=10, c="brown", h=20)
print(rect1.square())

rect2 = Rectangle("", 30, 40)
print(rect2.square())
rect2.height = 50
print(rect2.square())