# Define a class
class Car:
    # Constructor to initialize the attributes of the class
    def __init__(self, make, model, year):
        self.make = make    # Manufacturer of the car
        self.model = model  # Model of the car
        self.year = year    # Year of manufacture

    # Method to describe the car
    def car_details(self):
        return f"{self.year} {self.make} {self.model}"

    # Method to simulate starting the car
    def start_engine(self):
        return f"The engine of the {self.model} is now running!"

    # Method to simulate stopping the car
    def stop_engine(self):
        return f"The engine of the {self.model} is now off!"

# Create objects (instances) of the Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)

# Access attributes and call methods
print(car1.car_details())  # Output: 2020 Toyota Camry
print(car1.start_engine()) # Output: The engine of the Camry is now running!
print(car1.stop_engine())  # Output: The engine of the Camry is now off!

print(car2.car_details())  # Output: 2022 Honda Civic
print(car2.start_engine()) # Output: The engine of the Civic is now running!
print(car2.stop_engine())  # Output: The engine of the Civic is now off!
