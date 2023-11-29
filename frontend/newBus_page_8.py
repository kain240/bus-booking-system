from tkinter import *
from backend import bus
from tkinter import messagebox

reopen_home = False

def page8():
    root = Tk()

    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    root.geometry(f'{screen_width}x{screen_height}')
    root.title('Add New Bus')

    Label(root,text="\t").grid(row=1,column=1)#right margin
    #busimage
    img = PhotoImage(file="frontend/starbus.png")
    Label(root, image=img).grid(row=1,column=2,columnspan=17)

    Label(root,text="\t").grid(row=8,column=14)#need some space

    #home
    def home():
        global reopen_home
        root.destroy()
        reopen_home = True

    homeimage=PhotoImage(file="frontend/homeicon.png")
    Button(root,image=homeimage,command=home,fg="blue2",bg="springgreen").grid(row=1,column=15)
    Label(root, text='\t\t\t\t').grid(row=1,column=0)
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
    Label(root, text="Bus Type").grid(row=8,column=4)
    options = ['AC 2X2', 'AC 3X2', 'Non AC 2X2', 'Non AC 3X2', 'AC-Sleeper 2X1', 'Non-AC Sleeper 2X1']
    clicked = StringVar()
    clicked.set('AC 2X2')
    drop = OptionMenu(root, clicked, *options)
    drop.grid(row=8, column=5)
    Label(root,text="\t").grid(row=8,column=6)

    #capacity
    Label(root,text="Capacity").grid(row=8,column=7)
    capacity=Entry()
    capacity.grid(row=8,column=8)
    Label(root,text="\t").grid(row=8,column=9)#need some space

    #Fare
    Label(root,text="Fare Rs").grid(row=8,column=10)
    Fare=Entry()
    Fare.grid(row=8,column=11)
    Label(root,text="\t").grid(row=8,column=12)#need some space

    #operator id
    Label(root,text="Operator Id").grid(row=8,column=13)
    operator=Entry()
    operator.grid(row=8,column=14)
    Label(root,text="\t").grid(row=8,column=15)#need some space

    def add_bus():
        Type = clicked.get()
        bus.Bus(bus_id.get(), Type, capacity.get(), Fare.get(), operator.get()).add()
        result = messagebox.showinfo('Bus entry', 'Bus details recorded successfully')
    def edit_bus():
        bus.Bus(bus_id.get(), 'ac', capacity.get(), Fare.get(), operator.get()).edit()
        result = messagebox.showinfo('Bus entry Update', 'Bus recorde updated successfully')

    Button(root,text="Add Bus",bg="Lightblue", command= add_bus).grid(row=10,column=2,columnspan=13)

    Label(root,text="\t").grid(row=9,column=3)#need some space

    Button(root,text="Edit Bus",bg="Lightblue", command= edit_bus).grid(row=10,column=4,columnspan=13)


    root.mainloop()
    return reopen_home


