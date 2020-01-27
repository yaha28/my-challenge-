class Horse():
    def __init__ (self, name, rider):
        self.name = name
        self.rider = rider

class Rider():
    def __init__ (self, name):
        self.name = name

the_rider = Rider("Sally")
the_horse = Horse("Harry", the_rider)

print(the_horse.rider.name)


