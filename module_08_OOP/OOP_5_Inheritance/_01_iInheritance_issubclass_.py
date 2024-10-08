class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        if cls1.__name__ == cls2.__name__:
            print("Same", end="\t")
            continue
        print(issubclass(cls1, cls2), end="\t")

    print()
