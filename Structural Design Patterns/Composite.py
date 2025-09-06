from abc import ABC, abstractmethod

class IArt(ABC):
    @abstractmethod
    def draw_by(self):
        pass

class MonaLisa(IArt):
    def draw_by(self):
        return "Leonardo da Vinci"

class Scream(IArt):
    def draw_by(self):
        return "Edward Munch"

class Gallery(IArt):
    def __init__(self, name):
        self.name = name 
        self.arts = []

    def add(self, art):
        self.arts.append(art)

    def draw_by(self):
        for art in self.arts:
            print(art.draw_by())  

if __name__ == "__main__":
    mona_lisa = MonaLisa()
    scream = Scream()
    
    renaissance_collection = Gallery("Renaissance")
    expressio_collection = Gallery("Expressio")

    renaissance_collection.add(mona_lisa)  
    expressio_collection.add(scream)       

    museum = Gallery("Museum")
    museum.add(renaissance_collection)
    museum.add(expressio_collection)


    museum.draw_by()