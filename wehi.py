class Vehicle:

# create init method

    def __init__(self, max_speed, mileage):

# bind the arguments

        self.max_speed = max_speed

        self.mileage = mileage

# Object creation

MGHector= Vehicle(240, 12)

# access the variables inside init method

print("Model Max Speed:",MGHector.max_speed)

print("Model Mileage:", MGHector.mileage)

