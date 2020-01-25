
class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__ (self, w, l):
        self.width = w
        self.len = l
    def calculate_perimeter(self):
       return (self.width + self.len) * 2

class Square(Shape):
    def __init__ (self, s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1 * 4
    def change_size (self, new_size):
        self.s1 += new_size 

a_rectangle = Rectangle(300, 400)

a_square = Square(100)
print(a_square.calculate_perimeter())
a_square.change_size(200)
print(a_square.calculate_perimeter())

a_square.what_am_i()
a_rectangle.what_am_i()


