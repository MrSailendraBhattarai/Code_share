import time
import random


class VehicleConditionCheck:
    def __init__(self):
        self.warnings = 0

    def fuel(self):
        fuel = input("Is the engine oil level high? (yes/no): ").lower()
        if fuel != 'yes':
            print("Warning: Low engine oil. Check or replace the oil !!!")
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
            return True
        elif self.warnings > 0:
            print(f"Your vehicle has {self.warnings} issues. Please address them.")
            time.sleep(3)
            print("Mission Terminate due to Some Problem....")
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
        else:
            print("You didn't survive, try again!")


# Main Execution:
if __name__ == "__main__":
    player_name = input("Enter your name: ")

    # Vehicle Condition Check object
    print("\n--- Vehicle Condition Check ---")
    vehicle = VehicleConditionCheck()
    vehicle.fuel()
    vehicle.battery()
    vehicle.power()
    vehicle.communication()
    vehicle.life_support()
    vehicle.scientific()
    vehicle.backup()
    vehicle.vehicle_condition()

    # Survival Challenge object
    survival = SurvivalChallenge(player_name)
    survival.welcome_page()
    survival.start()
