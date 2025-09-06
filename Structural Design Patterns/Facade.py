class Customer:
    def order(self):
        print("Ordered steak")

class Waiter:
    def accepted_the_order(self):
        print("Accepted the order")

class Cook:
    def cook(self):
        print("Cook")

class Facade:
    def __init__(self):
        self.customer = Customer()
        self.waiter = Waiter()
        self.cook = Cook()

    def restaurant(self):
        for i in range(10):
            self.customer.order()
        for i in range(10):
            self.waiter.accepted_the_order()
        for i in range(10):
            self.cook.cook()

if __name__ == "__main__":
    facade = Facade()
    facade.restaurant()
        