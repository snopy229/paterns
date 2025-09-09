from abc import ABC, abstractmethod

class Flashlight:
    def turn_off(self):
        print("Flashlight is turned off")

    def turn_on(self):
        print("Flashlight is turned on")

class ICommand(ABC):
    def action(self):
        pass

class CommandTurnOff(ICommand):
    def __init__(self):
        self.flashlight = Flashlight()

    def action(self):
        self.flashlight.turn_off()

class CommandTurnOn(ICommand):
    def __init__(self):
        self.flashlight = Flashlight()

    def action(self):
        self.flashlight.turn_on()

class Button:
    def __init__(self, command):
        self.command = command

    def press(self):
        self.command.action()

if __name__ == "__main__":
    turn_off = CommandTurnOff()
    button_turn_off = Button(turn_off)
    button_turn_off.press()

    turn_on = CommandTurnOn()
    button_turn_on = Button(turn_on)
    button_turn_on.press()
