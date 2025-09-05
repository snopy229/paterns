class VideoSettings:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, resolution = 720, volume = 75, speed = 2):
        self.resolution = resolution
        self.volume = volume
        self.speed = speed 

    def output(self):
        print(f"Resolution: {self.resolution}p, Volume: {self.volume}%, Speed: {self.speed}x")

if __name__ == "__main__":
    a = VideoSettings(360, 25, 1.5)
    b = VideoSettings(1080, 50, 1.75)
    a.output() #output b
    b.output() #output b
    print(a is b)