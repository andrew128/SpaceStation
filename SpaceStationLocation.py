# Code is in Python 3 

import json
import turtle
import urllib.request

"""put web address into variable"""
url = 'http://api.open-notify.org/astros.json'
"""call the web service"""
response = urllib.request.urlopen(url)
"""load JSON response into python data structure"""
result = json.loads(response.read())
"""-----------------------------"""
print('People in Space: ', result['number'])

people = result['people']

for p in people:
  print(p['name'], ' in ', p['craft'])
"""-----------------------------"""
"""Get current location of ISS"""
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latutide: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.jpg')

screen.register_shape('iss.png')
iss = turtle.Turtle()
iss.shape('iss.png')
iss.setheading(90)

"""Move ISS to correct location from center of map"""
iss.penup()
iss.goto(lon, lat)
