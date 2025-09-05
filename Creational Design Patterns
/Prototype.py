import copy

class Airplane:
    def __init__(self, wing_size = 11, max_speed = 260, range = 1000):
        self.wing_size = wing_size
        self.max_speed = max_speed
        self.range = range

    def clone(self, wing_size = None, max_speed = None, range = None):
        clone = Airplane(self.wing_size, self.max_speed, self.range)
        if wing_size is not None:
            clone.wing_size = wing_size
        elif max_speed is not None:
            clone.max_speed = max_speed
        elif range is not None:
            clone.range = range
        return clone

    def show_characteristics(self):
        print(f"Wing size: {self.wing_size}")
        print(f"Max speed: {self.max_speed}")
        print(f"Range: {self.range}\n")

if __name__ == "__main__":
    ap1 = Airplane()
    print("Original:")
    ap1.show_characteristics()
    print("Modified:")
    ap2 = Airplane(wing_size=9)
    ap2.show_characteristics()