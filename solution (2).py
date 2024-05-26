class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def calculate_area(self):
        return self.a * self.b
class PerimeterMixin:
    def calculate_perimeter(self):
        return 2 * (self.a + self.b)
class Square(Rectangle, PerimeterMixin):
    def __init__(self, a):
        super().__init__(a, a)
    def __eq__(self, other):
        return self.a == other.a
    def __gt__(self, other):
        return self.calculate_area() > other.calculate_area()
    def __add__(self, other):
        return self.calculate_area() + other.calculate_area()
square1 = Square(3)
square2 = Square(2)
print(square1.calculate_area())
print(square1.calculate_perimeter())  # Вызываем метод для вычисления периметра
print(square1 == square1)
print(square1 == square2)
print(square1 > square2)
print(square1 > square1)
print(square1 + square1)