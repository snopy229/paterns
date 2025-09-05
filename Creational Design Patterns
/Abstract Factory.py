from abc import ABC, abstractmethod

class IEngine(ABC):
    @abstractmethod
    def create_engine(self):
        pass

class GermanEngine(IEngine):
    def create_engine(self):
        print("German engine")

class USAEngine(IEngine):
    def create_engine(self):
        print("USA engine")

class ICar(ABC):
    @abstractmethod
    def create_car(self, engine):
        pass

class GermanCar(ICar):
    def create_car(self, engine):
        print("German car with ", end='')
        engine.create_engine()

class USACar(ICar):
    def create_car(self, engine):
        print("USA car with ", end='')
        engine.create_engine()

class IFactory(ABC):
    @abstractmethod
    def make_engine(self):
        pass
    
    @abstractmethod
    def make_car(self):
        pass

class GermanFactory(IFactory):
    def make_engine(self):
        return GermanEngine()
    
    def make_car(self):
        return GermanCar()

class USAFactory(IFactory):
    def make_engine(self):
        return USAEngine()
    
    def make_car(self):
        return USACar()

if __name__ == "__main__":
    g_factory = GermanFactory()
    g_car = g_factory.make_car()
    g_engine = g_factory.make_engine()

    g_car.create_car(g_engine)

    usa_factory = USAFactory()
    usa_car = usa_factory.make_car()
    usa_engine = usa_factory.make_engine()

    usa_car.create_car(usa_engine)