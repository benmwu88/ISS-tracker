import turtle

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

#Siaplays Map and ISS position, updating every refresh time
class Display():
    #display a rectangular map (use library)
    def map():
        # Setup the world map
        screen = turtle.Screen()
        screen.setup(1189, 848)
        screen.setworldcoordinates(-180,-90,180,90)
        screen.bgpic("map.gif") 
        screen.register_shape("iss.gif")
    #draws ISS positions on a map and lines between points every x miles
    def point():
        
        iss = turtle.Turtle()
        iss.shape("iss.gif")
        iss.penup()

        return iss # return ISS object

def main(trail=True):
    iss = Display()