import tkinter as tk
from tkinter import ttk
import requests
def info_get():
    city = city_name.get()
    
    API_key = "0be9f763fdb57ab3c875f166d794c6d9"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    response = requests.get(url)
    info = response.json()
    
    we_label1.config(text=info["weather"][0]["main"])
    weat_label1.config(text=info["weather"][0]["description"])
    temp_label1.config(text=str(int(info["main"]["temp"]-273.15)))
    per_label1.config(text=info["main"]["pressure"])

root = tk.Tk()
root.title("WEATHER APP")
root.config(bg="sky blue")
root.geometry("500x570")

name_label = tk.Label(root, text = "SkyGazer Weather" ,
                   font=("Times New Roman", 30 , "bold"))
name_label.place(x = 25,y=50, height = 50, width = 450)

list_name = [
    "Karachi","Lahore" ,"Kotla" ,"Qasim Khan" ,"Faisalabad","Rawalpindi","Gujranwala","Peshawar","Multan",
             "Hyderabad City","Islamabad","Quetta","Cantonment","Eminabad"
             ]
city_name = tk.StringVar()
com =ttk.Combobox(root,values=list_name,
                   font=("Times New Roman", 20 , "bold"),textvariable=city_name)
com.place(x =25,y=120,height=50,width=450)

we_label = tk.Label(root,text="Weather Climate",
                   font=("Times New Roman", 17 ))
we_label.place(x =25,y=260,height=50,width=210)
we_label1 = tk.Label(root,text="",
                   font=("Times New Roman", 17 ))
we_label1.place(x =250,y=260,height=50,width=210)
 

weat_label = tk.Label(root,text = "Weather Description",
                   font=("Times New Roman", 17 ))
weat_label.place(x =25,y=330,height=50,width=210)
weat_label1 = tk.Label(root,text="",
                   font=("Times New Roman", 17 ))
weat_label1.place(x =250,y=330,height=50,width=210)

temp_label = tk.Label(root,text="Temperature",
                   font=("Times New Roman", 20 ))
temp_label.place(x =25,y=400,height=50,width=210)
temp_label1 = tk.Label(root,text="",
                   font=("Times New Roman", 20 ))
temp_label1.place(x =250,y=400,height=50,width=210)
 
per_label = tk.Label(root,text="Pressure",
                   font=("Times New Roman", 20 ))
per_label.place(x =25,y=470,height=50,width=210)
per_label1 = tk.Label(root,text="",
                   font=("Times New Roman", 20 ))
per_label1.place(x =250,y=470,height=50,width=210)


click_button =tk.Button(root,text="DONE",
                   font=("Times New Roman", 20 , "bold"),command=info_get)

click_button.place(x =200,y=190,height=50,width=100)
 

root.mainloop()





