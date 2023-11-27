from tkinter import *
from backend import run
from tkinter import messagebox
root=Tk()
Label(root,text="\t\t").grid(row=1,column=1)#right margin
root.geometry("1200x650")

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
root.geometry(f'{screen_width}x{screen_height}')
root.title('Add New Run')
#bus image
img=PhotoImage(file="frontend/starbus.png")
Label(root,image=img).grid(row=1,column=2,columnspan=17)

Label(root,text="\t").grid(row=1,column=15)

#homeicon
def home():
    Label(root,text="please link home button to the root window").grid(row=100,column=2,columnspan=13)

homeimage=PhotoImage(file="frontend/homeicon.png")
Button(root,image=homeimage,command=home,fg="blue2",bg="springgreen",bd=4).grid(row=1,column=16)
Label(root,text="\t").grid(row=1,column=12)#some space
Label(root,text="Online Bus Booking System",font="arial 20 bold",bg="light blue",fg="red").grid(row=2,column=2,columnspan=17)
Label(root,text="\n").grid(row=3,column=2)#leaving a blank line
Label(root,text="Add Bus Running Details",font="Arial 15 bold",fg="green").grid(row=4,column=2,columnspan=17)
Label(root,text="\n").grid(row=5,column=2,columnspan=3)#leaving a blank line

#Bus_Id
Label(root,text="Bus Id").grid(row=6,column=2)
Bus_Id=Entry()
Bus_Id.grid(row=6,column=3)
Label(root,text="\t").grid(row=6,column=4)#some space

#running date
Label(root,text="Running Date").grid(row=6,column=5)
Running_Date=Entry()
Running_Date.grid(row=6,column=7)
Label(root,text="\t").grid(row=6,column=8)#some space

#seat availablity
Label(root,text="Seat Available").grid(row=6,column=9)
Seat_Available=Entry()
Seat_Available.grid(row=6,column=10)
Label(root,text="\t").grid(row=7,column=11)#some space

#route_id
Label(root,text="Route Id").grid(row=6,column=12)
route_id=Entry()
route_id.grid(row=6,column=13)
Label(root,text="\t").grid(row=7,column=14)#some space

def add_run():
    run.Run(Bus_Id.get(), route_id.get(), Running_Date.get(), Seat_Available.get()).add()
    result = messagebox.showinfo('Add New Run', 'New run added successfully')

def delete_run():
    run.Run(Bus_Id.get(), route_id.get(), Running_Date.get(), Seat_Available.get()).delete()
    result = messagebox.showinfo('delete Run', 'Run deleted successfully')

Button(root,text="Add Bus",bg="lawngreen", command= add_run).grid(row=6,column=15)
Label(root,text="\t").grid(row=7,column=13)#some space
Button(root,text="Delete Bus",bg="lawngreen", command= delete_run).grid(row=6,column=16)
root.mainloop()

