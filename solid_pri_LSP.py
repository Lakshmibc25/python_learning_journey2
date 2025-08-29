class Vehicle:
    def stop(self):
        pass
class bike(Vehicle):
    def stop(self):
        print("bike engine stoped..")
class boat(Vehicle):
    def stop(self):
        print("boat engine stoped..")
def stop_vehicle(Vehicle):
    Vehicle.stop_engine()

stop_vehicle(bike())
stop_vehicle(boat())