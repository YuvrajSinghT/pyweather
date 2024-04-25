from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


root=Tk()
root.title("Weather app")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M:%p")
    clock.config(text=current_time)
    name.config(text="Current Time")

    #weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c6e51db51bacddc0ed11e93ce96b18b5"

    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","feels","like",temp,"°"))
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)


#search box
Search_image=PhotoImage(file=("images/search.png"))
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")

textfield.place(x=50,y=40)
textfield.focus()
Search_icon=PhotoImage(file="images/search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

#logo
logo_image=PhotoImage(file="images/logo.png")
logo=Label(image=logo_image)
logo.place(x=150,y=100)

#bottom box
Frame_image=PhotoImage(file="images/box.png")
frame_img=Label(image=Frame_image)
frame_img.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=630,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=645,y=150)

#label
label1=Label(root,text="Wind",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label1=Label(root,text="Humidity",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=250,y=400)

label1=Label(root,text="Description",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=430,y=400)

label1=Label(root,text="Pressure",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)

d=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=460,y=430)

p=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=660,y=430)





root.mainloop()