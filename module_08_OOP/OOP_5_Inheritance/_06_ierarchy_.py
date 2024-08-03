import time


class Vehicle:
    def change_direction(self, on):
        pass

    def turn(self):
        self.change_direction(self, True)
        time.sleep()
        self.change_direction(self, False)


class TrackedVehicle(Vehicle):

    def control_track(self, stop):
        pass

    def change_direction(self, on):
        self.control_track(self, on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(self, on):
        pass

    def change_direction(self, on):
        self.turn_front_wheels(self, on)
