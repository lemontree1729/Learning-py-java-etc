class Car:
    speed = 0

    def upSpeed(self, value):
        self.speed += value

        print("current speed(super class) :", self.speed)


class Sedan(Car):
    def upSpeed(self, value):
        self.speed += value

        if self.speed > 150:
            self.speed = 150

        print("current speed(sub class) :", self.speed)


class Truck(Car):
    pass


sedan1, truck1 = None, None
truck1 = Truck()
sedan1 = Sedan()
print("truck --> ", end="")
truck1.upSpeed(200)
print("sedan --> ", end="")
sedan1.upSpeed(200)
