class Car():
    WHEELS = "4 Wheels"

    def __init__(self,make,model,year,color,fuel):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel = fuel

    def __str__(self):
        return (f"\nmake   : {self.make}"
                f"\nyear   : {self.year}"
                f"\nmodel  : {self.model}"
                f"\ncolor  : {self.color}"
                f"\nfuel   : {self.fuel}"
                f"\nwheels : {self.WHEELS}")

class Electric_Car(Car):

    def __init__(self,make,model,year,colors,fuel,range):
        super().__init__(make,model,year,colors,fuel)
        self.range = range

    def __str__(self):
        return (f"\nmake   : {self.make}"
                f"\nyear   : {self.year}"
                f"\nmodel  : {self.model}"
                f"\ncolor  : {self.color}"
                f"\nfuel   : {self.fuel}"
                f"\nRange  : {self.range} miles "
                f"\nwheels : {self.WHEELS}")

class Hydrogen_Car(Electric_Car):

    def __init__(self,make,model,year,color,fuel,range):
        super().__init__(make,model,year,color,fuel,range)

    def __str__(self):
        return (f"\nmake   : {self.make}"
                f"\nyear   : {self.year}"
                f"\nmodel  : {self.model}"
                f"\ncolor  : {self.color}"
                f"\nfuel   : {self.fuel}"
                f"\nRange  : {self.range} miles "
                f"\nwheels : {self.WHEELS}")

car1 = Car("Honda","Accord",2023,"Black","Petrol")
car2 = Electric_Car("Tesla","S",2024,"GREY","Electric","250")
car3 = Hydrogen_Car("HydroCar","H2ONE",2025,"AQUA","Hydrogen",500)
print(car1)
print(car2)
print(car3)