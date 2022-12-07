import json
import turtle
import urllib.request
from math import radians, cos, sin, asin, sqrt
from geopy.geocoders import Nominatim
import time as time_module


#ISS location with methods to define significance of location
class Location():
    #initialization function that takes in a user input for position
    def __init__(self,user_position):
        self.userposition = user_position
    #function that finds current position of ISS
    def iss_position(self):
        # load the current status of the ISS in real-time
        response = urllib.request.urlopen("http://api.open-notify.org/iss-now.json")
        result = json.loads(response.read())   

        # Extract the ISS location and time
        location = result["iss_position"]
        lat = float(location['latitude'])
        lon = float(location['longitude'])
        time = result["timestamp"]

        return lon, lat, time


    def golbeclac(lon1, lat1, lon2, lat2):
        """
        Calculate the great circle distance in kilometers between two points 
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
        return c * r

    def display_location(lon, lat):
        geolocator = Nominatim(user_agent="http") # initialize Nominatim API
        location = geolocator.reverse(f'{lat},{lon}')
        if location==None:
            return 'Ocean'
        return location.raw['address'].get('country', '')
    def distance_from_user(self):
        pass
    #function that finds distance from ISS to various famous landmarks
    def distance_from_landmarks(self):
        pass

#ISS movement attributes at a certain location 
class Movement(Location):
    #velocity of ISS at a certain location
    def velocity(lon1, lat1, time1, lon2, lat2, time2):
        d = globecalc(lon1, lat1, lon2, lat2)
        t = time2-time1 or 1 # incase of 0 time difference change to 1 to handle ZeroDivisionError
        return round(((d/t)*3600)/1.60934, 2) # returns speed in kilometers per hour rounded upto 2nd decimal place
    #acceleration of ISS at a certain location
    def acceleration(self):
        pass
    #direction of ISS at a certain location
    def direction(self):
        pass

#Siaplays Map and ISS position, updating every refresh time
class Display():
    #display a rectangular map (use library)
    def setup():
        turtle.title('ISS Tracker')

        # Setup the world map
        screen = turtle.Screen()
        screen.setup(1189, 848)
        screen.setworldcoordinates(-180,-90,180,90)
        screen.bgpic("map.gif") 

        # Setup ISS object
        screen.register_shape("iss.gif")
        iss = turtle.Turtle()
        iss.shape("iss.gif")
        iss.penup()

        return iss # return ISS object

def main(trail=True):
    iss = Display()