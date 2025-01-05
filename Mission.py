import time
import datetime
import random
from Fuel import Fuel  # Import the Fuel class from the other file

class VehicleConditionCheck:
    def __init__(self, fuel_system):
        self.warnings = 0
        self.fuel_system = fuel_system

    def fuel(self):
        print(f"Fuel level: {self.fuel_system.check_fuel()}%")
        if self.fuel_system.check_fuel() < 20:  # Consider fuel low if less than 20%
            print("Warning: Low fuel. Please refuel soon!")
            self.warnings += 1

    def battery(self):
        battery = input("Is the battery charged? (yes/no): ").lower()
        if battery != 'yes':
            print("Warning: Battery may need to be charged !!!")
            self.warnings += 1

    def power(self):
        power = input("Is the Power System working properly? (yes/no): ").lower()
        if power != 'yes':
            print("Power System Failure !!!")
            self.warnings += 1

    def communication(self):
        communication = input("Is the Communication System working properly? (yes/no): ").lower()
        if communication != 'yes':
            print("Check Communication System...")
            self.warnings += 1

    def life_support(self):
        life_support = input("Is Life Support System working properly? (yes/no): ").lower()
        if life_support != 'yes':
            print("Check Life Support System...")
            self.warnings += 1

    def scientific(self):
        scientific = input("Are Scientific Instruments working properly? (yes/no): ").lower()
        if scientific != 'yes':
            print("Scientific instruments not working properly...")
            self.warnings += 1

    def backup(self):
        backup = input("Is the Backup System working properly? (yes/no): ").lower()
        if backup != 'yes':
            print("Check Backup Systems...")
            self.warnings += 1

    def vehicle_condition(self):
        print("\nVehicle Condition Summary: ")
        if self.warnings == 0:
            print("Your vehicle is in excellent condition!")
            print("It is Ready to launch")
            time.sleep(3)
            for i in range(10, 0, -1):
                print(i)
                time.sleep(1)
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"Titan has Launched Successfully at {current_time}....")
            return True
        else:
            print(f"Your vehicle has {self.warnings} issues. Please address them.")
            time.sleep(3)
            print("Mission Terminated due to some problems....")
            exit()
            return False


class SurvivalChallenge:
    def __init__(self, player_name, time_limit=60):
        self.player_name = player_name
        self.time_limit = time_limit
        self.time_left = time_limit
        self.level_started = False

    def welcome_page(self):
        print(f"\nWelcome {self.player_name} to the Survival Challenge!")
        print(f"Your task: Survive for {self.time_limit} seconds.")
        print("Random events will happen during this time. Get ready!")

    def random_event(self):
        events = ["An asteroid appears!", "A sudden meteor shower!", "You find a power-up!", "A monster spawns!"]
        return random.choice(events)

    def start(self):
        print(f"\nStarting the survival challenge... Time Limit: {self.time_limit} seconds")
        self.level_started = True
        start_time = time.time()

        while self.time_left > 0:
            current_time = time.time()
            self.time_left = self.time_limit - int(current_time - start_time)

            # Trigger a random event every 5 seconds
            if self.time_left % 5 == 0 and self.time_left != 0:
                print(f"Time left: {self.time_left} seconds. Event: {self.random_event()}")

            time.sleep(1)

        self.end()

    def end(self):
        print(f"\nTime's up! Well done {self.player_name}!")
        if self.time_left <= 0:
            print("You survived the challenge!")
            print("Congratulations!!! Titan Has Launched Successfully...")
        else:
            print("You didn't survive, try again!")


# Main Execution:
if __name__ == "__main__":
    player_name = input("Enter your name: ")

    # Initialize Fuel system
    print("\n--- Fuel System ---")
    capacity = int(input("Enter the total tank capacity: "))
    current_level = int(input("Enter the current fuel level: "))
    fuel_system = Fuel(capacity, current_level)

    # Vehicle Condition Check object
    print("\n--- Vehicle Condition Check ---")
    vehicle = VehicleConditionCheck(fuel_system)
    vehicle.fuel()  # Checking fuel
    vehicle.battery()
    vehicle.power()
    vehicle.communication()
    vehicle.life_support()
    vehicle.scientific()
    vehicle.backup()
    if not vehicle.vehicle_condition():
        exit()

    # Survival Challenge object
    survival = SurvivalChallenge(player_name)
    survival.welcome_page()
    survival.start()
