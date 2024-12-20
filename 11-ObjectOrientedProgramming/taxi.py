class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    def print_recipt(self):
        return self.fare
        


def main():
    ride1 = TaxiRide(7)
    ride2 = TaxiRide(3.5)
    ride1.calculate_fare(7)
    ride2.calculate_fare(4)
    print(f'{ride1.print_recipt()}')
    print(f'{ride2.print_recipt()}')



if __name__ == "__main__":
    main()
