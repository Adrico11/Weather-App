# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:39:03 2020

@author: snice
"""

"""CREATE EXECUTABLE APP
Use pyinstaller and type in the conda envt :
    pyinstaller.exe --onefile --icon=icon_name.ico pythonfile.py
Place images in the same directory as the executable app
 """   


"""
GUI WITH TKINTER

Nested structure from the root downwards
root (canvas,frame) --> frame (button,entry,label)

Initialiser la fenêtre:
    1. tk.Canvas(root,height,width) = affiche la fenêtre d'une certaine taille 
    2. tk.Frame(root,background,border) = partie de la fenêtre

Ajouts esthétiques:
    1. tk.PhotoImage(file)

Plusieurs éléments dispo :
    1. button(frame,text,bg,fg,command=function call, font) = bouton
    2. entry(frame,bg,font) = searchbar
    3. label(frame,text,bg,image,font,anchor,justify,bd) = tout le reste (titre,image...)

Différentes méthodes pour placer nos éléments sur l'écran:
    1. elt.pack(side,fill,expand) basic (fill pour agrandir le bouton dans certaines directions et expand pour l'agrandir encore plus)
    2. elt.place(anchor,elx,rely,relwidth,relheight) adapts very well to the screen size (position par rapport au 'nw' = anchor)
    3. elt.grid(row,column) very useful to stack many elts on the screen

Remarques importantes:
    Font : import font from tkinter and font=('font_name',size in pixels)
    Place the background image in the same directory as our python file
    Use caps for global variables (variables with values that remain the sema throughout the programm)
"""

"""API (Application Programming Interface)
Way for developpers to access and communicate with a server to get some info (web-based API)

In the button, use lambda: test_function(entry.get()) instead of just test_function(entry.get()) to have it rerun every time we push the button
(otherwise it just runs once and since nothing is inserted in the entry at the start, it returns nothing)
Use the % notation to print complex strings
"""

import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600


"""Get the weather info with a weather API"""

def format_response(weather):
    """Formats the weather response in our window"""
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        
        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name,description,temp)
    
    except:
        final_str='There was a problem retrieving the weather info'
    
    return final_str

def get_weather(city):
    """Get the weather info with Weather API"""
    weather_key = '255be8a35b0b05acc37983ffd2be22a6'
    url = 'https://api.openweathermap.org/data/2.5/weather' 
    params = {'APPID':weather_key,'q':city,'units':'metric'}
    response = requests.get(url,params=params)
    weather = response.json() #converts the response to a json file (easy to use dictionnary)
    
    label['text'] = format_response(weather) #use our same label defined below and add some text
    
# 255be8a35b0b05acc37983ffd2be22a6
# api.openweathermap.org/data/2.5/forecast?q={city name},{state},{country code}&appid={your api key}

"""Create GUI"""

root = tk.Tk() #initialiser l'appli au début

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH) #window size
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)


"""Main frame"""
frame =tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n') #on place la frame en haut de l'app
entry = tk.Entry(frame, font=('Courier',18)) #Searchbar
entry.place(relwidth=0.65,relheight=1)
button = tk.Button(frame, text='Get Weather', font=('Courier',12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7,rely=0,relwidth=0.3,relheight=1)

"""Lower Frame"""
lower_frame=tk.Frame(root,bg="#80c1ff",bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')
label = tk.Label(lower_frame,font=('Courier',18),anchor='nw', justify='left', bd=4)#Title (plain text)
label.place(relwidth=1,relheight=1) #relx>position du boutton pour éviter l'overlap (sinon il passe dessus)

root.mainloop() #lancer l'appli à la fin

"""
NEXT STEPS:
    Add icon to illustrate the weather (Keith's git)
    View 5 days 3h forecast instead of just the current weather (weather->forecast in url)
"""    