from abc import ABC, abstractmethod

class SoundStrategy(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class DogSound(SoundStrategy):
    def make_sound(self):
        return "Wool-woof"
    
class CatSound(SoundStrategy):
    def make_sound(self):
        return "Meow-meow"
    
class DuckSound(SoundStrategy):
    def make_sound(self):
        return "Quack-quack"
    
class Animal:
    def __init__(self, sound_strategy):
        self.sound_strategy = sound_strategy

    def set_sound_strategy(self, sound_strategy):
        self.sound_strategy = sound_strategy

    def make_sound(self):
        return self.sound_strategy.make_sound()
    
if __name__ == "__main__":
    animal = Animal(DogSound())
    print(animal.make_sound())
    animal.set_sound_strategy(CatSound())
    print(animal.make_sound())
    animal.set_sound_strategy(DuckSound())
    print(animal.make_sound())