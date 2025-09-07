class Mediator:
    def __init__(self):
        self.airplane1 = None
        self.airplane2 = None

    def register_airplanes(self, airplane1, airplane2):
        self.airplane1 = airplane1
        self.airplane2 = airplane2
        airplane1.set_mediator(self)
        airplane2.set_mediator(self)

    def notify(self, sender, event):
        if sender == self.airplane1 and event == "fly":
            print("Mediator: Airplane1 is flying to USA.")
            self.airplane1.fly_to_USA()
        elif sender == self.airplane2 and event == "fly":
            print("Mediator: Airplane2 is flying to Germany.")
            self.airplane2.fly_to_Germany()


class Airplane1:
    def set_mediator(self, mediator):
        self.mediator = mediator

    def fly(self):
        self.mediator.notify(self, "fly")

    def fly_to_USA(self):
        print("Airplane1: Flying to USA")


class Airplane2:
    def set_mediator(self, mediator):
        self.mediator = mediator

    def fly(self):
        self.mediator.notify(self, "fly")

    def fly_to_Germany(self):
        print("Airplane2: Flying to Germany")


if __name__ == "__main__":
    mediator = Mediator()
    airplane1 = Airplane1()
    airplane2 = Airplane2()

    mediator.register_airplanes(airplane1, airplane2)

    airplane1.fly()
    airplane2.fly()
