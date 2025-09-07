class Fruits:
    def __init__(self):
        self.fruits = []

    def add(self, fruit):
        self.fruits.append(fruit)

    def __iter__(self):
        return Iterator(self.fruits)
    
class Iterator:
    def __init__(self, fruits):
        self.fruits = fruits
        self.index = 0
        
    def __next__(self):
        if self.index >= len(self.fruits):
            raise StopIteration
        fruit = self.fruits[self.index]  
        self.index += 1          
        return fruit      


if __name__ == "__main__":
    fruits = Fruits()
    fruits.add("Apple")
    fruits.add("Banana")
    fruits.add("Pineapple")
    for fruit in fruits:
        print(fruit)