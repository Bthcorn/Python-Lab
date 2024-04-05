# import abc

class Transportation():
    def __init__(self, start_place, end_place, distance):
        self.start_place = start_place
        self.end_place = end_place
        self.distance = distance
        
    # @abc.abstractclassmethod
    def find_cost(self):
        pass
    
class Walk(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)
    
    def find_cost(self):
        return 0
        
class Taxi(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)
    
    def find_cost(self):
        return self.distance * 40

class Train(Transportation):
    def __init__(self, start_place, end_place, distance, station):
        super().__init__(start_place, end_place, distance)
        self.station = station
        
    def find_cost(self):
        return self.station * 5
        
walk = Walk("KMITL", "Lawson at KMITL", 0.6).find_cost()
taxi1 = Taxi("Lawson at KMITL", "Ladkrabang Station", 5).find_cost()
train = Train("Ladkrabang Station", "Payathai Station", 40, 6).find_cost()
taxi2 = Taxi("Payathai Station", "The British Council", 3).find_cost()

# def find_cost(list)

print(walk + taxi1 + taxi2 + train)
    