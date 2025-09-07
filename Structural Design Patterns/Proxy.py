class Toy:
    def play(self):
        pass

class RealToy(Toy):
    def play(self):
        return "Play with toy"
    
class ToyProxy(Toy):
    def __init__(self):
        self.real_toy = RealToy()
        self.is_allowed = False

    def allowed_access(self):
        self.is_allowed = True

    def play(self):
        if self.is_allowed:
            print(self.real_toy.play())
        else:
            print("Don't play with toy")

if __name__ == "__main__":
    play = ToyProxy()
    play.allowed_access()
    play.play()

    dont_play = ToyProxy()
    dont_play.play()