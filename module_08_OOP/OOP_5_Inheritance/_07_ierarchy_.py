import time


class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())
wheeled.turn(True)
wheeled.turn(False)

# class Vehicle:
#     def change_direction(self, on):
#         pass
#
#     def turn(self):
#         self.change_direction(self, True)
#         time.sleep()
#         self.change_direction(self, False)
#
#
# class TrackedVehicle(Vehicle):
#
#     def control_track(self, stop):
#         pass
#
#     def change_direction(self, on):
#         self.control_track(self, on)
#
#
# class WheeledVehicle(Vehicle):
#     def turn_front_wheels(self, on):
#         pass
#
#     def change_direction(self, on):
#         self.turn_front_wheels(self, on)
