from tkinter import *
from backend import route
root=Tk()

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
root.geometry(f'{screen_width}x{screen_height}')
root.title('Online Bus Booking')

img=PhotoImage(file="frontend/starbus.png")
Label(root,text="\t").grid(row=1,column=1)#want some space
Label(root,image=img).grid(row=1,column=2,columnspan=7)


#homeicon
def home():
    Label(root,text="please link home button to the root window").grid(row=100,column=2,columnspan=8)

homeimage=PhotoImage(file="frontend/homeicon.png")
Button(root,image=homeimage,command=home,fg="blue2",bg="springgreen").grid(row=1,column=9)
Label(root,text="Online Bus Booking System",font='arial 20 bold',bg="light blue",fg="red").grid(row=2,column=2,columnspan=9)
Label(root,text="\n").grid(row=3,column=2)#leaving a blank line
Label(root,text="Add New Details to Database").grid(row=4,column=2,columnspan=9)
Label(root,text="\n",).grid(row=5,column=2,columnspan=3)#leaving an empty line


#route id
Label(root,text="Route Id").grid(row=6,column=2)
Route_ID=Entry(root)
Route_ID.grid(row=6,column=3)
Label(root,text="\t",).grid(row=6,column=4)

#Start
Label(root,text="Start").grid(row=6,column=5)
start=Entry(root)
start.grid(row=6,column=6)
Label(root,text="\t",).grid(row=6,column=7)

#Stop
Label(root,text="Stop").grid(row=6,column=8)
stop=Entry(root)
stop.grid(row=6,column=9)
Label(root,text="\t",).grid(row=6,column=10)


def add_route():
    route.Route(Route_ID.get(), start.get(), stop.get()).add()

def delete_route():
    route.Route(Route_ID.get(), start.get(), stop.get()).delete()

#add route
Button(root,text="Add Route",bg="lawn green", command= add_route).grid(row=6,column=11)
Label(root,text="\t",).grid(row=6,column=12)

#delete route
Button(root,text="delete Route",bg="lawn green",fg="red", command= delete_route).grid(row=6,column=13)




