class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_slots = big
        self.medium_slots = medium
        self.small_slots = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big_slots > 0:
                self.big_slots -= 1
                return True
            else:
                return False
        
        if carType == 2:
            if self.medium_slots > 0:
                self.medium_slots -= 1
                return True
            else:
                return False

        if carType == 3:
            if self.small_slots > 0:
                self.small_slots -= 1
                return True
            else:
                return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
