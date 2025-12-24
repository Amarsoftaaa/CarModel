from datetime import datetime

from Models.Car import Car
from Models.User import User


print("Opcije : "
      "\n1. Dodaj korisnika "
      "\n2. Prikazi korisnika "
      "\n3. Prikazi raspoloziva vozila"
      "\n4. Prikazi rentana vozila"
      "\n5. Zelim rentati vozilo")

available_options = [1, 2, 3, 4, 5]

option = None

while option is None:

    options = int(input("Unesite opciju koju zelite "))
    print(options)

    if options not in available_options:
        raise ValueError("Nepoznata opcija")

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
                    print("\nAko zelite rentati vozilo pritisnite 5")
                elif car["rented"] and options == 4:
                    rented_until_date = datetime.strptime(car["rented_until"], "%d.%m.%Y")
                    today = datetime.today()
                    remaining_days = (rented_until_date - today).days
                    print(f" {brand}{car} ostalo je jos {remaining_days} dana do kraja rente")
                    option = None
    elif options == 5:
        car_rented = input("Koje auto zelite rentati")
        car_until = input("Do kada zelite rentati auto \n(dd.mm.yyyy)\n")
        car_until_gultig= datetime.strptime(car_until,"%d.%m.%Y")
        today_rent=datetime.today()
        total_rent_days = car_until_gultig-today_rent
        print(f"Uspjesno ste rentali {car_rented} do {car_until} godine.")


