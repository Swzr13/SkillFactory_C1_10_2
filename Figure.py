class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height


rectangle_1 = Rectangle(width=50, height=100)
print(rectangle_1.get_square())