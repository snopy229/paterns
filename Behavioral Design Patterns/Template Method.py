from abc import ABC, abstractmethod

class BeverageTemplate(ABC):
    def prepare_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boil water")

    @abstractmethod
    def brew(self):
        pass

    def pour_in_cup(self):
        print("Pour in cup")

    @abstractmethod
    def add_condiments(self):
        pass

class Tea(BeverageTemplate):
    def brew(self):
        print("Brew tea leaves")

    def add_condiments(self):
        print("Add lemon and sugar")

class Coffee(BeverageTemplate):
    def brew(self):
        print("Brew coffee")

    def add_condiments(self):
        print("Add milk and sugar")

if __name__ == "__main__":
    tea = Tea()
    tea.prepare_beverage()
    print("")
    coffee = Coffee()
    coffee.prepare_beverage()