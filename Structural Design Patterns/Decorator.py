class Coffee:
    def cost(self):
        return 100
    
    def description(self):
        return "Coffee"
    
class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 20
    
    def description(self):
        return f"{self._coffee.description()}, milk"
    
class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 10
    
    def description(self):
        return f"{self._coffee.description()}, sugar"
    
class ChocolateDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 30
    
    def description(self):
        return f"{self._coffee.description()}, chocolate"
    
if __name__ == "__main__":
    coffee = Coffee()
    print(f"{coffee.description()}: {coffee.cost()}")

    coffee_with_milk = MilkDecorator(coffee)
    print(f"{coffee_with_milk.description()}: {coffee_with_milk.cost()}")

    coffee_with_milk_sugar = SugarDecorator(coffee_with_milk)
    print(f"{coffee_with_milk_sugar.description()}: {coffee_with_milk_sugar.cost()}")
    
    coffee_with_sugar = SugarDecorator(coffee)
    print(f"{coffee_with_sugar.description()}: {coffee_with_sugar.cost()}")

    coffee_with_chocolate = ChocolateDecorator(coffee)
    print(f"{coffee_with_chocolate.description()}: {coffee_with_chocolate.cost()}")
