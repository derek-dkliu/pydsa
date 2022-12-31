from enum import Enum

class ParkingLot:
    def __init__(self, levels_num):
        self.levels = [ParkingLevel(i, 30) for i in range(levels_num)]

    def park(self, vehicle):
        for level in self.levels:
            if level.park(vehicle):
                return True
        return False

    def remove(self, vehicle):
        for level in self.levels:
            if level.remove(vehicle):
                return True
        return False

    def __str__(self):
        return '\n'.join(map(str, self.levels))

class ParkingLevel:
    SPOTS_PER_ROW = 10

    def __init__(self, floor, spots_num):
        self.floor = floor
        self.spots = []
        large_spots = spots_num // 4
        small_spots = spots_num // 4
        medium_spots = spots_num - large_spots - small_spots
        self.spots.extend([ParkingSpot(VehicleSize.Large) for _ in range(large_spots)])
        self.spots.extend([ParkingSpot(VehicleSize.Medium) for _ in range(medium_spots)])
        self.spots.extend([ParkingSpot(VehicleSize.Small) for _ in range(small_spots)])

    def park(self, vehicle):
        start = self.find_available_spots(vehicle)
        if start != -1:
            for i in range(vehicle.spots_num):
                self.spots[start + i].park(vehicle)
            return True
        else:
            return False

    def remove(self, vehicle):
        start = 0
        while start < len(self.spots):
            spot = self.spots[start]
            if spot.vehicle is vehicle:
                for i in range(vehicle.spots_num):
                    self.spots[start + i].remove()
                return True
            start += 1
        return False

    def find_available_spots(self, vehicle):
        start = 0
        while start < len(self.spots):
            spot = self.spots[start]
            if spot.is_available() and spot.fits(vehicle):
                found = True
                for i in range(1, vehicle.spots_num - 1):
                    nextspot = self.spots[start + i]
                    if not nextspot.is_available() or not nextspot.fits(vehicle) or not self.same_row(start, start+i):
                        start += i
                        found = False
                        break
                if found:
                    return start
            start += 1
        return -1

    def same_row(self, i, j):
        return self.get_row(i) == self.get_row(j)

    def get_row(self, index):
        return index // ParkingLevel.SPOTS_PER_ROW

    def __str__(self):
        rows = []
        for i, spot in enumerate(self.spots):
            if i % ParkingLevel.SPOTS_PER_ROW == 0:
                rows.append([f'Row {self.get_row(i)}:'])
            rows[-1].append(str(spot))
        result = "\n".join(" | ".join(row) for row in rows)
        return f"Floor {self.floor}\n{result}"  
        
class ParkingSpot:
    def __init__(self, size):
        self.vehicle = None
        self.size = size

    def is_available(self):
        return self.vehicle is None

    def fits(self, vehicle):
        return self.size.value >= vehicle.size.value

    def park(self, vehicle):
        self.vehicle = vehicle

    def remove(self):
        self.vehicle = None

    def __str__(self):
        return f" -- {self.size.name[0]} -- " if self.is_available() else str(self.vehicle)

class VehicleSize(Enum):
    Small = 1
    Medium = 2
    Large = 3

class Vehicle:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"{type(self).__name__[0:5]:5}({self.id:02})"

class Motorbike(Vehicle):
    def __init__(self, id):
        super().__init__(id)
        self.spots_num = 1
        self.size = VehicleSize.Small

class Car(Vehicle):
    def __init__(self, id):
        super().__init__(id)
        self.spots_num = 1
        self.size = VehicleSize.Medium

class Bus(Vehicle):
    def __init__(self, id):
        super().__init__(id)
        self.spots_num = 5
        self.size = VehicleSize.Large

import random
vehicles = []
for i in range(50):
    vehicle_cls = random.choice([Motorbike, Car, Bus])
    vehicles.append(vehicle_cls(i + 1))

parkinglot = ParkingLot(5)
print(parkinglot)
print()
for vehicle in vehicles:
    if parkinglot.park(vehicle):
        print(f"{vehicle} is parked")
    else:
        print(f"{vehicle} cannot be parked")
print()
print(parkinglot)
print()
for _ in range(5):
    v = random.choice(vehicles)
    if parkinglot.remove(v):
        print(f"{v} is removed")
    else:
        print(f"{v} already removed")
print()
print(parkinglot)