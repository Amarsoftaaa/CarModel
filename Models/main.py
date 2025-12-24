from datetime import datetime

from Models.Car import Car
from Models.User import User


print("Opcije : "
      "\n1. Add new user "
      "\n2. View users "
      "\n3. View available cars"
      "\n4. View renal cars"
      "\n5. I want to rent a car")


available_options = [1, 2, 3, 4, 5]

option = None

while option is None:

    options = int(input("Enter the option you want. "))
    print(options)

    if options not in available_options:
        raise ValueError("Unknown option")

    if options == 1:
        user = User()
        user.name = input("Enter users name")
        user.age = int(input("Enter users age"))
        user.create()
        option = None

    elif options == 2:
        print(User.ALL_USERS)
        option = None

    elif options == 3 or options == 4:

        for brand in Car.VALID_CARS:
            for car in Car.VALID_CARS[brand]:
                if not car["rented"] and options == 3:
                    print(car)
                    print("\n If you want to rent a vehicle, click 5")
                elif car["rented"] and options == 4:
                    rented_until_date = datetime.strptime(car["rented_until"], "%d.%m.%Y")
                    today = datetime.today()
                    remaining_days = (rented_until_date - today).days
                    print(f" {brand}{car}"There are {remaining_days} days left until the end of the rent.")
                    option = None
    elif options == 5:
        car_rented = input("Which car do you want to rent?")
        car_until = input("How long do you want to rent the car for? \n(dd.mm.yyyy)\n")
        car_until_gultig= datetime.strptime(car_until,"%d.%m.%Y")
        today_rent=datetime.today()
        total_rent_days = car_until_gultig-today_rent
        print(f"You have successfully rented {car_rented} until {car_until}.")


