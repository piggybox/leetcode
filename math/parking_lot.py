# 1603 design parking system

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_slots = big
        self.medium_slots = medium
        self.small_slots = small
        
    def addCar(self, carType: int) -> bool:
        if carType == 1: # big
            if self.big_slots >= 1:
                self.big_slots -= 1
                return True
            else:
                return False
        elif carType == 2: # medium
            if self.medium_slots >= 1:
                self.medium_slots -= 1
                return True
            else:
                return False
        elif carType == 3: # medium
            if self.small_slots >= 1:
                self.small_slots -= 1
                return True
            else:
                return False
        else:
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)