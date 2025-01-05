

class Fuel:
    def __init__(self, capacity=100, current_level=100):
        self.capacity = capacity  # Total fuel capacity
        self.current_level = current_level  # Current fuel level

    def check_fuel(self):
        fuel_percentage = (self.current_level / self.capacity) * 100
        return round(fuel_percentage)

    def refuel(self, amount):
        if amount + self.current_level > self.capacity:
            return "overflow"
        self.current_level += amount
        return "refueled"

    def use_fuel(self, amount):
        if amount > self.current_level:
            return "insufficient"
        self.current_level -= amount
        return "successful"
