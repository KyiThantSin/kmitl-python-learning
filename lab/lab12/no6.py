from abc import ABC, abstractmethod

class Transportation(ABC):
    def __init__(self, start_place, end_place, distance) -> None:
        super().__init__()
        self.start_place = start_place
        self.end_place = end_place
        self.distance = distance

    @abstractmethod
    def find_cost(self):
        pass


class Walk(Transportation):
    def __init__(self, start_place, end_place, distance) -> None:
        super().__init__(start_place, end_place, distance)

    def find_cost(self):
        return 0

class Taxi(Transportation):
    def __init__(self, start_place, end_place, distance) -> None:
        super().__init__(start_place, end_place, distance)
    
    def find_cost(self):
        return self.distance * 40

class Train(Transportation):
    def __init__(self, start_place, end_place, distance, station) -> None:
        super().__init__(start_place, end_place, distance)
        self.station = station

    def find_cost(self):
        return self.distance * 5 * self.station

def main():
    walk = Walk("KMITL", "Lawson at KMITL", 0.6)
    taxi = Taxi("Lawson at KMITL", "Ladkrabang Station", 5)
    train = Train("Ladkrabang Station", "Phayathai Station", 40, 6)
    taxi1 = Taxi("Phayathai Station", "The British Council", 3)

    print(f"Total Cost from {walk.start_place} to {walk.end_place}: {walk.find_cost()} Baht")
    print(f"Total Cost from {taxi.start_place} to {taxi.end_place}: {taxi.find_cost()} Baht")
    print(f"Total Cost from {train.start_place} to {train.end_place}: {train.find_cost()} Baht")
    print(f"Total Cost from {taxi1.start_place} to {taxi1.end_place}: {taxi1.find_cost()} Baht")
main()