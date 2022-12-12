# ISS-tracker


## Table of contents
* [Summary](#summary)
* [Overview of Code](#overview-of-code)
* [Instructions to use](#instructions-to-use)
* [Suggested future directions](#suggested-future-directions)

## Summary
The program we wrote is an International Space Station (ISS) tracker. It tracks the current location of the ISS and displays it on a world map created by the turtle library. Within the terminal, the program displays quantitative data. This data includes the names of the astronauts onboard as well as the velocity the ISS is traveling at in miles per hour. The main inner functionality of the program includes using the NASA API to extract the latitude and longitude of the ISS, then finding  those coordinates on the world map. These coordinates are taken from NASA’s website and are updated in the script every five seconds. Due to this, relevant data such as the velocity as well as the position of the ISS icon are changed constantly. We also wanted to display the ISS icon compared to the center of the globe, which is why there is a line connecting it to there. 

## Overview of Code
Within our code, we have three separate classes. The first class, named Location, has no attributes, but several methods. The first method is the iss_position method which tracks the ISS’s location at a set interval, which we set at five seconds. The second method is the globecalc method which calculates the circle distance on the globe between two points. This is used later to calculate the velocity of the ISS at a certain time. The final method is the display_location method which shows what location the ISS is currently over, either the country or the ocean, which is printed in the terminal. 
The second class, called Movement, inherits from the Location class in order to move the ISS on the map and track velocity. A Location object is initialized as an attribute so that the globecalc function can be used within the velocity method to divide the distance difference between two time points by the difference in the times. The speed will be printed in the terminal. The go method moves the ISS to the new location.
The third and final class, Display, has two methods. The setup method sets up the background of the world map. The astronaut_details method shows what astronauts are currently on the ISS. Display inherits from movement in order to use the go method so that the icon will move to the next location. 

## Instructions to Use
Clone the repository:
```
$ git clone https://github.com/benmwu88/ISS-tracker.git
```
Change current directory to ISS-tracker repository:
```
$ cd ISS-tracker
```
Install the geopy library:
```
pip install geopy
```
Run the program:
```
python final_code.py
```
## Suggested future directions

Someone that wants to develop the project further could allow the user to input their own location and compare their distance to the ISS. Another feature that can be implemented is determining the direction the ISS is traveling using azimuth and bearing angles. Finally, there could be direction and acceleration as further features. 



##Final Project Proposal

Partners: Kevin Zhou and Ben Wu

We will distribute work evenly 50/50 and help each other with tasks if needed.

Project Overview: We will create a bot that tracks the position of the International Space Station and map it out on a world map. The position will be tracked in real
time in terms of longitude and latitude and show how far it is from your current location. The speed and direction of the ISS can also be recorded. Furthermore, the
significance of the position will be displayed, such as which ocean/continent it is over, and if it is near any landmarks (e.g. Great Wall, Eiffel Tower, etc.)’

**Project Class and Methods**

Class: Location 

Method 1: Extract longitude and latitude

Method 2: Compare it to your position and find exact distance

Method 3: Check how far it is from list of defined landmark positions (TBD)

Class: Movement

Method 1: Find magnitude of velocity and acceleration

Method 2: Determine direction

Class: Display

Method 1: Initialize data from other 2 classes

Method 2: Display movement on world map/graph (TBD)


**Libraries**

Turtle Library: Creates Designs and Images

Urllib3 Library: Fetches URLs

Pycopy-webbrowser: Allows users to view Web-based documents

**Priority of Features**

High Priority: Longitude Latitude and display on some sort of map/graph

Medium Priority: Speed/acceleration and distance from you

Low Priority: Distance from landmarks

Clone the repository:
Git clone https://github.com/benmwu88/ISS-tracker.git

Change current directory to ISS-tracker repository:
cd ISS-tracker

Install the geopy library:
pip install geopy

Run the program:
python final_code.py

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is simple Lorem ipsum dolor generator.
	
## Technologies
Project is created with:
* Lorem version: 12.3
* Ipsum version: 2.33
* Ament library version: 999
	
## Setup
To run this project, install it locally using npm:

```
$ cd ../lorem
$ npm install
$ npm start
