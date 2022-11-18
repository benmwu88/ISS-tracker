#ISS location with methods to define significance of location
class Location():
    #initialization function that takes in a user input for position
    def __init__(self,user_position):
        self.userposition = user_position
    #function that finds current position of ISS
    def iss_position(self):
        pass
    #function that finds distance from ISS to user input
    def distance_from_user(self):
        pass
    #function that finds distance from ISS to various famous landmarks
    def distance_from_landmarks(self):
        pass

#ISS movement attributes at a certain location 
class Movement(Location):
    #velocity of ISS at a certain location
    def velocity(self):
        pass
    #acceleration of ISS at a certain location
    def acceleration(self):
        pass
    #direction of ISS at a certain location
    def direction(self):
        pass

#displays ISS position and updates it
class Display():
    #draws ISS positions on a map using a line to connect the dots
    def map():
        pass
