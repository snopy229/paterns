from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def calculate(self):
        pass

class Sum(ICalculator):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def calculate(self):
        print(f"{self.first}+{self.second}={self.first+self.second}")
    
class Difference(ICalculator):
    
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def calculate(self):
        print(f"{self.first}-{self.second}={self.first-self.second}")
    
class Product(ICalculator):
    
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def calculate(self):
        print(f"{self.first}*{self.second}={self.first*self.second}")


class Quotient(ICalculator):
    
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def calculate(self):
        print(f"{self.first}/{self.second}={self.first/self.second}")  

class CalculatorFactory:
    def create_calculator(operation:str, first:int, second:int):
        if operation == "+":
            return Sum(first, second)
        elif operation == "-":
            return Difference(first, second)
        elif operation == "*":
            return Product(first, second)
        elif operation == "/":
            return Quotient(first, second)
        else:
            raise ValueError("Неизвестный оператор")

    


if __name__=="__main__":
    sum = CalculatorFactory.create_calculator("+", 2, 4)
    sum.calculate()
    dif = CalculatorFactory.create_calculator("-", 2, 4)
    dif.calculate()
    prod = CalculatorFactory.create_calculator("*", 2, 4)
    prod.calculate()
    quo = CalculatorFactory.create_calculator("/", 2, 4)
    quo.calculate()