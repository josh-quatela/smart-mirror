#Imports all necesarry libraries for the project
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time
import webbrowser
import imp

import json
import requests

#Sets each sensor to specific pin on the pi
Sensor1 = 23
Sensor2 = 24
Sensor3 = 25
Sensor4 = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(Sensor1, GPIO.IN)
GPIO.setup(Sensor2, GPIO.IN)
GPIO.setup(Sensor3, GPIO.IN)
GPIO.setup(Sensor4, GPIO.IN)
var = True

#Function that creates html for the date and time
def date():
    #Makes api call for date and time
    api_key = "a95770827a9048f6a3cc3b236ee1b6db"

    base_url = "https://api.ipgeolocation.io/timezone"
    complete_url = base_url + '?apiKey=' + api_key + '&tz=America/New_York'

    response = requests.get(complete_url);

    x = response.json()

    y = x["date_time_txt"]


    f = open("date_and_time","w")

    m = """
    <html>
    <head><meta http-equiv="refresh" content="30"></meta></head>
    <body style="background:black; position:relative; left:400px; top:0px;">
    <h1 style = "color:white; opacity:10;"><b>"""+ str(y) +"""</b></h1>
    </body>
    </html>
    """

    f.write(m)
    f.close()

#Creates html for calendar of the month of December 2019
def calendar():
    f = open('calendar','w')

    message = """
    <html>
    <body style="background-color:black; position:relative; top:300px;">

    <h2 style = "color:white; opacity:10; "><b>December</b></h2>

    <pre><p style="color:white; opacity:10;"><b>Sun   Mon   Tue   Wed   Thu   Fri   Sat</b></p></pre>
    <pre><p style="color:white; opacity:10;"><b>1     2    (3)    4     5     6     7  </b></p></pre>
    <pre><p style="color:white; opacity:10;"><b>8     9     10    11    12    13    14 </b></p></pre>
    <pre><p style="color:white; opacity:10;"><b>15    16    17    18    19    20    21 </b></p></pre>
    <pre><p style="color:white; opacity:10;"><b>22    23    24    25    26    27    28 </b></p></pre>
    <pre><p style="color:white; opacity:10;"><b>29    30    31                         </b></p></pre>

    </body>
    </html>
    """
    f.write(message)
    f.close()

#Creates html for the current weather
def weather():
    #Makes api call to get current weather
    api_key = "62faff5a06b54b08f3993c0e0ff08fa9"

    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    complete_url = base_url + 'id=524901&APPID=' + api_key + '&q=' + 'New York'

    response = requests.get(complete_url);

    x= response.json();

    y = x["list"]
    temp = y[0]['main']['temp'];
    condition = y[0]['weather'][0]['description']

    temp = temp-273.15
    temp = temp * (9.0/5)
    temp += 32
    temp =round(temp,1)

    f = open('weather','w')

    message = """<html>
    <head><meta http-equiv="refresh"content="30"></meta></head>
    <body style="background:black; position:relative; left:800px; top:10px;">
    <h1 style="color:white; opacity:10;"><b>"""+"Weather"+"""</b></h1>
    <h1 style="color:white; opacity:10;"><b>"""+str(temp)+"""</b></h1>
    <h1 style="color:white; opacity:10;"><b>"""+condition+"""</b></h1>
    </body>
    </html>
    """


    f.write(message)
    f.close()

#Creates html for to-do list
def todo():
    f = open('todo','w')

    message = """
    <html>
    <body style="background-color:black; position:relative; left:820px; top:400px;">

    <h2 style = "color:white; opacity:10; "><b>To-Do List</b></h2>

    <ul style = "list-style-type:circle;">
        <li style="color:white; opacity:10;"><b>Feed the dog</b></li>
        <li style="color:white; opacity:10;"><b>Take out the trash</b></li>
        <li style="color:white; opacity:10;"><b>Text Karen</b></li>
    </ul>

    </body>
    </html>
    """
    f.write(message)
    f.close()

#Creates html for an all black screen that represents the display being off
def screen_off():
    f = open('screen_off','w')

    message = """
    <html>
    <body style="background-color:black; position:relative; top:300px;">
    </body>
    </html>
    """
    f.write(message)
    f.close()

#Reads input from sensors    
while var:
    time.sleep(5) #delays loop for every 5 seconds
    if GPIO.input(24): #if the specific sensor reads high, a unique html is opened
        date()
        imp.reload(webbrowser)
        webbrowser.open('file:///home/pi/Desktop/smart-mirror/date_and_time')
    elif GPIO.input(25):
        calendar()
        imp.reload(webbrowser)
        webbrowser.open('file:///home/pi/Desktop/smart-mirror/calendar')
    elif GPIO.input(23):
        weather()
        imp.reload(webbrowser)
        webbrowser.open('file:///home/pi/Desktop/smart-mirror/weather')
    elif GPIO.input(23) and GPIO.input(24): #both sensors need to read high for display to show
        todo()
        imp.reload(webbrowser)
        webbrowser.open('file:///home/pi/Desktop/smart-mirror/todo')
    elif GPIO.input(12):
        screen_off()
        imp.reload(webbrowser)
        webbrowser.open('file:///home/pi/Desktop/smart-mirror/screen_off')
