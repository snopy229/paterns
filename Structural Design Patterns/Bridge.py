from abc import ABC, abstractmethod

class IDevice(ABC):
    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def set_volume(self):
        pass

class TV(IDevice):
    def turn_off(self):
        print(f"TV is turned off")

    def turn_on(self):
        print(f"TV is turned on")

    def set_volume(self):
        print(f"Volume is set")

class Radio(IDevice):
    def turn_off(self):
        print(f"Radio is turned off")

    def turn_on(self):
        print(f"Radio is turned on")

    def set_volume(self):
        print(f"Volume is set")

class RemoteDevice:
    def __init__(self, device):
        self.device = device

    def turn_off(self):
        self.device.turn_off() 

    def turn_on(self):
        self.device.turn_on()

    def set_volume(self):
        self.device.set_volume()  

if __name__ == "__main__":
    TV = RemoteDevice(TV())
    TV.turn_off()
    TV.turn_on()
    TV.set_volume()
    print("")
    Radio = RemoteDevice(Radio())
    Radio.turn_off()
    Radio.turn_on()
    Radio.set_volume()
