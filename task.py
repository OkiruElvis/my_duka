# Create a small vehicle management system using inheritance. Start by creating a parent class called Vehicle. The Vehicle class should have three attributes: brand, model, and year. 
# It should have a display_info() method that prints the vehicle's basic information. 
# Add a start() method that prints a simple message saying the vehicle has started, and a stop() method that prints a simple message saying the vehicle has stopped.


# Next, create a child class called Car that inherits from Vehicle. A Car should have an additional attribute called number_of_doors. 
# Add a simple drive() method that prints a message saying the car is driving. Override the display_info() method so that it also displays the number of doors. 
# Inside the overridden method, use super() to call the parent's display_info() method.


# Then create another child class called Motorcycle that also inherits from Vehicle. 
# A Motorcycle should have an additional attribute called engine_cc, representing the engine size. Add a simple ride() method that prints a message saying the motorcycle is being ridden. 
# Override display_info() so that it also displays the engine size. Again, use super() to call the parent's display_info() method.


class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def display_info(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Year : {self.year}")

    def start(self):
        print("The vehicle has started.")

    def stop(self):
        print("The vehicle has stopped.")

#Child Inheritance = Car
class Car(Vehicle):
    def __init__(self, brand, model, year,number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors=number_of_doors

    def drive(self):
        print("The car is driving")

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.number_of_doors}")



#Child Inheritance =Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year,engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc=engine_cc

    def ride(self):
        print("The motorcycle is being ridden.")

    def display_info(self):
        super().display_info()
        print(f"Engine Size: {self.engine_cc} cc")

#Car Object
car=Car("Toyota","Fortuner",2023,4)

print("CAR INFORMATION")
car.display_info()
car.start()
car.drive()
car.stop()

print("\n-------------------------")

#Motorcycle Object
motorcycle=Motorcycle("Yamaha","Bajaj",2022,210)

print("MOTORCYCLE INFORMATION")
motorcycle.display_info()
motorcycle.start()
motorcycle.ride()
motorcycle.stop()
