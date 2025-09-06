class USACar:
    def get_distance_miles(self):
        return 200

class MilesToKm:
    def __init__(self):
        self.USA_dist = USACar()
    
    def convert_miles_to_km(self):
        miles = self.USA_dist.get_distance_miles()
        km = miles * 1.609
        return km
    
class EuropeanCar:
    def  show_distance(self, km):
        print(f"Passed: {km}km")

if __name__ == "__main__":
    mtk = MilesToKm()
    km = mtk.convert_miles_to_km()

    ec = EuropeanCar()
    ec.show_distance(km)


