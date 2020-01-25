
class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Square(Shape):
    square_list = []
    def __init__ (self, s1):
        self.s1 = s1
        self.square_list.append(self.s1)

    def calculate_perimeter(self):
        return self.s1 * 4
    
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

a_square = Square(15)
print (Square.square_list)
print (a_square)

b_square = Square(20)
print (Square.square_list)
print (b_square)

def compare (a, b):
    return a is b
print(compare("x", "x"))
