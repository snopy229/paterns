from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def accept(self, visitor):
        visitor.visit_circle(self)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def accept(self, visitor):
        visitor.visit_square(self)

class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass
    
    @abstractmethod
    def visit_square(self, square):
        pass


class AreaCalculator(Visitor):
    def visit_circle(self, circle):
        area = 3.14 * circle.radius ** 2
        print(f"Area of the circle: {area}")
    
    def visit_square(self, square):
        area = square.side ** 2
        print(f"Area of the square: {area}")

class PerimeterCalculator(Visitor):
    def visit_circle(self, circle):
        perimeter = 2 * 3.14 * circle.radius
        print(f"Perimeter of the circle: {perimeter}")
    
    def visit_square(self, square):
        perimeter = 4 * square.side
        print(f"Perimeter of the square: {perimeter}")


if __name__ == "__main__":
    shapes = [Circle(5), Square(3)]
    
    area_calculator = AreaCalculator()
    perimeter_calculator = PerimeterCalculator()
    
    for shape in shapes:
        shape.accept(area_calculator)

    for shape in shapes:
        shape.accept(perimeter_calculator)