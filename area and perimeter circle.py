import math



class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_radius(cls, radius):
        return cls(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius



radius = float(input("Enter the radius of the circle: "))

c = Circle.from_radius(radius)

print("Area of circle:", c.area())
print("Perimeter of circle:", c.perimeter())
