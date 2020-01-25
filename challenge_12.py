class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def triangle_area(self):
        return self.base*self.height*1/2
    
    def change_triangle(self, base, height):
        self.base = base
        self.height = height

a_triangle = Triangle(20, 30)
print(a_triangle.triangle_area())

a_triangle.change_triangle(50, 20)
print(a_triangle.triangle_area())

b_triangle =Triangle(50, 20)
b_triangle.change_triangle(40, 60)
print(b_triangle.triangle_area())
