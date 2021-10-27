class Car:
    speed = 0

    def upSpeed(self, value):
        self.speed = self.speed + value

    def downSpeed(self, value):
        self.speed = self.speed - value


class Sedan(Car):
    seatNum = 0

    def getSeatNum(self):
        return self.seatNum


class Truck(Car):
    capacity = 0

    def getCapacity(self):
        return self.capacity


sedan1, truck1 = None, None

sedan1 = Sedan()
truck1 = Truck()
sedan1.upSpeed(100)
truck1.upSpeed(80)
sedan1.seatNum = 5
truck1.capacity = 50
print(f"sedan1's speed is {sedan1.speed}, seatnumber is {sedan1.getSeatNum()}")
print(f"truck1's speed is {truck1.speed}, capacity is {truck1.getCapacity()}")
