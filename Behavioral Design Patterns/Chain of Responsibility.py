
class Check():
    def __init__(self, successor = None):
        self.successor = successor
        

    def check(self, number):
        if self.successor:
            return self.successor.check(number)
        return None

class CheckLowerNumber(Check): 
    def check(self, number):
        if number <= 10:
            print(f"Number {number} is small")
        return super().check(number)

class CheckMiddleNumber(Check): 
    def check(self, number):
        if 10 < number <= 99:
            print(f"Number {number} is middle")
        return super().check(number)

class CheckHighNumber(Check): 
    def check(self, number):
        if 99 < number:
            print(f"Too {number} is high")
        return super().check(number)

if __name__ == "__main__":
    check = CheckHighNumber(
            CheckMiddleNumber(
            CheckLowerNumber()
            )
        )
    check.check(5)
    check.check(15)
    check.check(115)
