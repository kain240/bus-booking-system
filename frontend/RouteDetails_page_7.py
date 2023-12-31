from tkinter import *
from backend import route
from tkinter import messagebox

reopen_home = False

def page7():
    root=Tk()

    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    root.geometry(f'{screen_width}x{screen_height}')
    root.title('Add New Route')

    img=PhotoImage(file="frontend/starbus.png")
    Label(root,text="\t").grid(row=1,column=1)#want some space
    Label(root,image=img).grid(row=1,column=2,columnspan=17)


    #homeicon
    def home():
        global reopen_home
        root.destroy()
        reopen_home = True

    homeimage=PhotoImage(file="frontend/homeicon.png")

    Button(root,image=homeimage,command=home,fg="blue2",bg="springgreen").grid(row=1,column=14)
    Label(root, text='\t\t\t\t').grid(row=1, column=0)
    Label(root,text="Online Bus Booking System",font='arial 20 bold',bg="light blue",fg="red").grid(row=2,column=2,columnspan=17)
    Label(root,text="\n").grid(row=3,column=2)#leaving a blank line
    Label(root,text="Add Bus Route Details", font='arial 15 bold', fg='green').grid(row=4,column=2,columnspan=17)
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
        redflag = True
        l1 = Label(root, text='                                                            ', font='10', fg='red')
        l1.grid(row=15, column=2, columnspan=17)
        if (Route_ID.get() == '' or start.get() == '' or stop.get() == ''):
            l1.config(text='Fill all the fields')
            redflag = False
        if redflag == True:
            route.Route(Route_ID.get(), start.get(), stop.get()).add()
            result = messagebox.showinfo('Add Bus Route', 'New Bus route added successfully')

    def delete_route():
        redflag = True
        l1 = Label(root, text='                                                            ', font='10', fg='red')
        l1.grid(row=15, column=2, columnspan=17)
        if (Route_ID.get() == '' or start.get() == '' or stop.get() == ''):
            l1.config(text='Fill all the fields')
            redflag = False
        if redflag == True:
            route.Route(Route_ID.get(), start.get(), stop.get()).delete()
            result = messagebox.showinfo('Delete Bus Route', 'Bus route deleted successfully')

    #add route
    Button(root,text="Add Route",bg="lawn green", command= add_route).grid(row=6,column=11)
    Label(root,text="\t",).grid(row=6,column=12)

    #delete route
    Button(root,text="delete Route",bg="lawn green",fg="red", command= delete_route).grid(row=6,column=13)
    root.mainloop()
    return reopen_home




