from abc import ABC , abstractmethod

class State(ABC):
    @abstractmethod
    def press(self, button):
        pass

class OnState(State):
    def press(self, button):
        print("Light was turned on")
        button.state = OffState()
    

class OffState(State):
    def press(self, button):
        print("Light was turned off")
        button.state = OnState()

class Button:
    def __init__(self):
        self.state = OnState()

    def press(self):
        self.state.press(self)

if __name__ == "__main__":
    button = Button()

    button.press()
    button.press()
    button.press()