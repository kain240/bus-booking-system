from tkinter import *
from backend import bus
root = Tk()

Label(root,text="\t").grid(row=1,column=1)#right margin
#busimage
img = PhotoImage(file="frontend/starbus.png")
Label(root, image=img).grid(row=1,column=2,columnspan=12)

Label(root,text="\t").grid(row=8,column=14)#need some space

#home
def home():
    Label(root,text="please link home button to the root window").grid(row=100,column=2,columnspan=15)
homeimage=PhotoImage(file="frontend/homeicon.png")
Button(root,image=homeimage,command=home,fg="blue2",bg="springgreen").grid(row=1,column=15)

#online bus booking system
Label(root, text="Online Bus Booking System", font="arial 20 bold", bg="light blue", fg="red").grid(row=4,column=2,columnspan=15)
Label(root,text="\n").grid(row=5,column=1)#NewLine

Label(root, text="Add Bus Details", font="arial 20 bold", bg="lawngreen", fg="green").grid(row=6,column=2,columnspan=15)
Label(root,text="\n").grid(row=7,column=1)

#bus id
Label(root, text="Bus ID").grid(row=8,column=1)
bus_id=Entry()
bus_id.grid(row=8,column=2)
Label(root,text="\t").grid(row=8,column=3)

#OptionMenu(root,text="Bus Type").grid(row=8,column=4)

Label(root,text="\t").grid(row=8,column=5)

#capacity
Label(root,text="Capacity").grid(row=8,column=6)
capacity=Entry()
capacity.grid(row=8,column=7)
Label(root,text="\t").grid(row=8,column=8)#need some space

#Fare
Label(root,text="Fare Rs").grid(row=8,column=9)
Fare=Entry()
Fare.grid(row=8,column=10)
Label(root,text="\t").grid(row=8,column=11)#need some space

#operator id
Label(root,text="Operator Id").grid(row=8,column=12)
operator=Entry()
operator.grid(row=8,column=13)
Label(root,text="\t").grid(row=8,column=14)#need some space

#Route id
Label(root,text="Route Id").grid(row=8,column=15)
route=Entry()
route.grid(row=8,column=16)
Label(root,text="\n").grid(row=9,column=1)#NewLine

def add_bus():
    bus.Bus(bus_id.get(), 'ac', capacity.get(), Fare.get(), operator.get(), route.get()).add()

Button(root,text="Add Bus",bg="Lightblue", command= add_bus).grid(row=10,column=2,columnspan=13)

Label(root,text="\t").grid(row=9,column=3)#need some space

Button(root,text="Edit Bus",bg="Lightblue").grid(row=10,column=4,columnspan=13)


root.mainloop()


