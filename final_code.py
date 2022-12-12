import json
import turtle
import urllib.request
from math import radians, cos, sin, asin, sqrt
from geopy.geocoders import Nominatim
import time as time_module
 
 
#ISS location with methods to define significance of location
class Location():
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
 
    #function that calculates circle distance between 2 points
    def globecalc(self,lon1, lat1, lon2, lat2):
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
 
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
        return c * r
 
    #function that displays significance of location of ISS 
    def display_location(self,lon, lat):
        geolocator = Nominatim(user_agent="http") # initialize Nominatim API
        location = geolocator.reverse(f'{lat},{lon}')
        if location==None:
            return 'Ocean'
        return location.raw['address'].get('country', '')
 
#ISS movement attributes at a certain location
class Movement(Location):
    #function that initializes location object to use globecalc function
    def __init__(self):
        self.d = Location()
    #velocity of ISS at a certain location
    def velocity(self,lon1, lat1, time1, lon2, lat2, time2):
        x = self.d.globecalc(lon1, lat1, lon2, lat2)
        t = time2-time1 or 1 # incase of 0 time difference change to 1 to handle ZeroDivisionError
        return round(((x/t)*3600)/1.60934, 2) # returns speed in kilometers per hour rounded upto 2nd decimal place
    #moves ISS to new location
    def go(self,lon,lat):
        turtle.goto(lon,lat)
 
#Siaplays Map and ISS position, updating every refresh time
class Display(Movement):
    #display a rectangular map (use library)
    def setup(self):
        turtle.title('ISS Tracker')
 
        # Setup the world map
        screen = turtle.Screen()
        screen.setup(1189, 848)
        screen.setworldcoordinates(-180,-90,180,90)
        screen.bgpic("map.gif")
 
        
    #shows which astronauts are on the ISS right now
    def astronaut_details(self):
        # load the current status of astronauts on ISS in real-time
        response = urllib.request.urlopen("http://api.open-notify.org/astros.json")
        result = json.loads(response.read())
 
        # Extract and print the astronaut's details
        print(f"There are currently {result['number']} astronauts on the ISS: ")
        for p in result["people"]:
            print(p['name'])
 

def main(trail=True): 
    ISS = Display()
    ISS.setup()
    ISS.astronaut_details()#sets up map and prints astronaut list
    ISS.iss_position()
 
    prevlon, prevlan, prevtime = ISS.iss_position() # initialize reference values
 
    while trail == True:
        lon, lat, time = ISS.iss_position()
        speed = ISS.velocity(prevlon, prevlan, prevtime, lon, lat, time) #calculates speed
    
        # Update the ISS location on the map
        ISS.go(lon, lat) #moves the icon

        # Output speed and country to terminal
        print(f'Speed: {speed} mph')
        print(f'Above {ISS.display_location(lon, lat)}')
 
        prevlon, prevlan, prevtime = lon, lat, time # update reference values
        time_module.sleep(5) # Update every 5 seconds

main()