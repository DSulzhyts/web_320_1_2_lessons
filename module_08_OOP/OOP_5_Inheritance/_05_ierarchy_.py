import time


class TrackedVehicle:

    def control_track(self, stop):
        pass

    def turn(self):
        self.control_track(self, True)
        time.sleep(0.25)
        self.control_track(self, False)


class WheeledVehicle:
    def turn_front_wheels(self, on):
        pass

    def turn(self):
        self.turn_front_wheels(self, True)
        time.sleep(0.25)
        self.turn_front_wheels(self, False)
