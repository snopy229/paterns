class Computer:
    def __init__(self):
        self.processor = None
        self.video_card = None
        self.RAM = 0
        self.SSD = 0
        self.HDD = 0

    def __str__(self):
        return (f"Processor: {self.processor}\n"
            f"Video card: {self.video_card}\n"
            f"RAM: {self.RAM} GB\n"
            f"SSD: {self.SSD} GB\n"
            f"HDD: {self.HDD} GB")

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def build_processor(self, name):
        self.computer.processor = name
        return self
    
    def build_video_card(self, name):
        self.computer.video_card = name
        return self
    
    def build_RAM(self, count):
        self.computer.RAM = count
        return self

    def build_SSD(self, count):
        self.computer.SSD = count
        return self

    def build_HDD(self, count):
        self.computer.HDD = count
        return self
    
    def get_result(self):  
        return self.computer

if __name__ == "__main__":
    builder  = ComputerBuilder()
    computer = (builder
                .build_processor("AMD")
                .build_video_card("Nvidia")
                .build_RAM(16)
                .build_SSD(512)
                .build_HDD(1024)
                .get_result())
    
    print(computer)
