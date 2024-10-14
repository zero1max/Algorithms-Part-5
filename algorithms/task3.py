class Car:
    def __init__(self, name, year, engine: bool, petrol: int):
        self.name = name
        self.year = year
        self.engine = engine
        self.petrol = petrol

    def moving(self):
        if self.engine:
            print("Mashina xarakatda")
        elif self.engine:
            print("mashina xarakatda emas")



class Bmw(Car):
    def __init__(self, name, year, engine, petrol, color, speed, price, model):
        super().__init__(name, year, engine, petrol)
        self.color = color
        self.speed = speed
        self.price = price
        self.model = model


    def display(self):
        return f"Color:{self.color}, Speed:{self.speed}, Price:{self.price}, Model:{self.model}"

    def check(self):
        if self.petrol > 0 and self.engine:
            print("car started")
        else:
            print("car stopped")

    def show(self):
        if self.petrol:
            return f"Benzin {self.petrol // 10 * 100}kmga yetadi"
        else:
            return "notogri"


obj = Bmw("Bmw", 2023, True, 20, "Black", 320, 192.000, "m5 cs")
print(obj.show())
