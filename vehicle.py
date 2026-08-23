class Vehicle:
    def __init__(self, vehicle_number, brand, price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price

    def categorize(self):
        if self.price >= 1000000:
            return "Luxury"
        else:
            return "Economy"

    def display(self):
        print("Vehicle Number:", self.vehicle_number)
        print("Brand:", self.brand)
        print("Price: ₹", self.price)
        print("Category:", self.categorize())
        print("-" * 35)


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        print("\nVehicle Details")
        print("=" * 40)

        for vehicle in self.vehicles:
            vehicle.display()


# Main Program
showroom = Showroom()

v1 = Vehicle("MH12AB1234", "BMW", 1500000)
v2 = Vehicle("MH14CD5678", "Maruti", 700000)
v3 = Vehicle("MH12EF9012", "Toyota", 1200000)

showroom.add_vehicle(v1)
showroom.add_vehicle(v2)
showroom.add_vehicle(v3)

showroom.display_vehicles()