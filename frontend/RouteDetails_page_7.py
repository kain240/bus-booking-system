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

#Station_name
Label(root,text="Station_name").grid(row=6,column=5)
Station_name=Entry(root)
Station_name.grid(row=6,column=6)
Label(root,text="\t",).grid(row=6,column=7)

#Station_ID
Label(root,text="Station_ID").grid(row=6,column=8)
Station_ID=Entry(root)
Station_ID.grid(row=6,column=9)
Label(root,text="\t",).grid(row=6,column=10)


def add_route():
    route.Route(Route_ID.get(), Station_ID.get(), Station_name.get(), 'guna', 'indore').add()

#add route
Button(root,text="Add Route",bg="lawn green", command= add_route).grid(row=6,column=11)
Label(root,text="\t",).grid(row=6,column=12)

#delete route
Button(root,text="delete Route",bg="lawn green",fg="red").grid(row=6,column=13)




