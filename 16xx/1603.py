class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.system = [big, medium, small]

    def addCar(self, carType):
        if self.system[carType - 1] != 0:
            self.system[carType - 1] -= 1
            return True
        return False        
        