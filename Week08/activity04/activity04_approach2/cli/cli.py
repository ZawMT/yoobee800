import subprocess  # To call the database service
import subprocess   # To call the database service
import json


class CarCLI:

    MENU = (
        "\nCar Rental System"
        "\n1. Add Car"
        "\n2. List Cars"
        "\n3. Remove Car"
        "\n4. Exit"
        "\nChoose: "
    )

    # Calling the database service through subprocess
    def run_db(self, args):
        result = subprocess.run(
            ["python", "/db/db_service.py"] + args,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()

    # Menu loop - 1 to add a car / 2 to list all the cars / 3 to remove a car - until the input is 4 (which means to exit)
    def start(self):
        while True:
            choice = input(self.MENU).strip()

            if choice == "1":  # To add a car
                self.add_car()

            elif choice == "2":  # To list all the cars
                self.list_cars()

            elif choice == "3":  # To remove a car
                self.remove_car()

            elif choice == "4":  # To exit
                break

    def add_car(self):
        plate = input("Plate: ").strip().upper()
        car_type = input("Type: ").strip()
        year = input("Year: ").strip()
        print(self.run_db(["add", plate, car_type, year]))

    def list_cars(self):
        output = self.run_db(["list"])
        rows = json.loads(output or "[]")
        print("\n\nList of cars:")
        for r in rows:
            print(r)

    def remove_car(self):
        plate = input("Plate: ").strip().upper()
        print(self.run_db(["remove", plate]))


if __name__ == "__main__":
    app = CarCLI()
    app.start()
