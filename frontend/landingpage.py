from tkinter import *

def SeatBooking():
    seat = Toplevel(root)
    seat.title("Seat Booking")

    def fun():
        Label(seat, text='Select Bus').grid(row=8, column=2)
        Label(seat, text='Operator').grid(row=8, column=4)
        Label(seat, text='Bus Type').grid(row=8, column=6)
        Label(seat, text='Availability').grid(row=8, column=8)
        Label(seat, text='Fare').grid(row=8, column=10)

    Label(seat, image=img).grid(row=1, column=2, columnspan=8)
    Label(seat, text='\t').grid(row=1, column=9)  # want some space in between

    def go_back():
        seat.destroy()  # Close the Seat Booking window
        new1 = Toplevel(root)
        new1.title("Option Window")

        # Add widgets to the new window
        label = Label(new1, image=img)
        label.grid(row=0, column=1, columnspan=3, rowspan=3, padx=10, pady=10, sticky="nsew")  # "nsew" for center alignment

        frame = Frame(new1, bg="lightblue", padx=1, pady=1)
        frame.grid(row=3, column=0, columnspan=5, pady=10, sticky="nsew")

        Label(frame, text='Online Bus Booking System', font='times 20 bold italic', fg='red', bg='lightblue').grid(row=0, column=0, pady=10, sticky="nsew")

        # Add buttons with background color
        Button(new1, text="Seat Booking", bg="blue", fg="white", command=SeatBooking).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        Button(new1, text="Checked Booked Seat", bg="green", fg="white", command=Checked).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        Button(new1, text="Add Bus Details", bg="orange", fg="white", command=Details).grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

        for i in range(21):
            new1.grid_rowconfigure(i, weight=1)
        for i in range(5):
            new1.grid_columnconfigure(i, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)

    home_button = Button(seat, image=homeimage, command=go_back, fg="blue2", bg="springgreen")
    home_button.grid(row=1, column=10)

    # label1 online bus booking system
    Label(seat, text="Online Bus Booking System", font="arial 20 bold", bg="light blue", fg="red").grid(row=2, column=2, columnspan=10)
    Label(seat, text="\n").grid(row=3, column=1, columnspan=3)  # leaving an empty line

    # journey details
    Label(seat, text="Enter Journey Details", font="Arial 10 bold", bg='spring green', fg="green4").grid(row=4, column=2, columnspan=10)
    Label(seat, text="\n").grid(row=5, column=1, columnspan=3)  # leaving an empty line
    # destination
    Label(seat, text='Destination').grid(row=6, column=2)
    To = Entry(seat)
    To.grid(row=6, column=3)
    Label(seat, text='\t').grid(row=6, column=4)  # want some space in between
    # from
    Label(seat, text='From').grid(row=6, column=5)
    From = Entry(seat)
    From.grid(row=6, column=6)
    Label(seat, text='\t').grid(row=6, column=7)  # want some space in between
    # date
    Label(seat, text='JourneyDate').grid(row=6, column=8)
    JourneyDate = Entry(seat)
    JourneyDate.grid(row=6, column=9)
    Label(seat, text='\t').grid(row=6, column=10)  # want some space in between

    Button(seat, text="show bus", command=fun, fg="blue2", bg="springgreen").grid(row=6, column=11)
    Label(seat, text="\n").grid(row=7, column=1, columnspan=3)  # leaving an empty line

def Checked():
    print("Checked Function")

def Details():
    admin = Toplevel(root)
    admin.title("Seat Booking")
    Label(admin, text="\t").grid(row=1, column=1)  # want some space
    Label(admin, image=img).grid(row=1, column=2, columnspan=9)
    Label(admin, text="Online Bus Booking System", font="arial 20 bold", bg="light blue", fg="red").grid(row=2, column=2, columnspan=9)
    Label(admin, text="\n").grid(row=3, column=2)  # leaving a blank line
    Label(admin, text="Add New Details to Database", font="Arial 15 bold", fg="green").grid(row=4, column=2, columnspan=9)
    Label(admin, text="\n", font="Arial 10 bold", fg="red").grid(row=5, column=2, columnspan=3)

    def linkme():
        Label(admin, text="I think you are supposed to do the rest").grid(row=5, column=2, columnspan=6)

    def operate():
        oper = Toplevel(root)  # create a new Toplevel window
        oper.title("Operate Window")

        def fun():
            Label(oper, text='Select Bus').grid(row=8, column=2)
            Label(oper, text='Operator').grid(row=8, column=4)
            Label(oper, text='Bus Type').grid(row=8, column=6)
            Label(oper, text='Availablity').grid(row=8, column=8)
            Label(oper, text='Fare').grid(row=8, column=10)

        # image
        
        Label(oper, image=img).grid(row=1, column=2, columnspan=17)

        # home icon
        homeimage = PhotoImage(file="homeicon.png")
        Button(oper, image=homeimage, command=fun, fg="blue2", bg="springgreen").grid(row=1, column=17)

        # label1 online bus booking system
        Label(oper, text="Online Bus Booking System", font="arial 20 bold", bg="light blue", fg="red").grid(row=2, column=2, columnspan=21)
        Label(oper, text="\n").grid(row=3, column=1, columnspan=3)  # leaving an empty line

        # Add Bus Operator Details
        Label(oper, text="Add Bus Operator Details", font="Arial 15 bold", fg="green4").grid(row=4, column=2,
                                                                                                columnspan=21)
        Label(oper, text="\n").grid(row=5, column=1, columnspan=3)  # leaving an empty line
        # Operator Id
        Label(oper, text='Operator Id').grid(row=6, column=2)
        Operator_Id = Entry(oper)
        Operator_Id.grid(row=6, column=3)
        Label(oper, text='\t').grid(row=6, column=4)  # want some space in between
        # Operator Name
        Label(oper, text='Operator Name').grid(row=6, column=5)
        Operator_Name = Entry(oper)
        Operator_Name.grid(row=6, column=6)
        Label(oper, text='\t').grid(row=6, column=7)  # want some space in between
        # Address
        Label(oper, text='Address').grid(row=6, column=8)
        Address = Entry(oper)
        Address.grid(row=6, column=9)
        Label(oper, text='\t').grid(row=6, column=10)  # want some space in between

        # Phone
        Label(oper, text='Phone').grid(row=6, column=11)
        Phone = Entry(oper)
        Phone.grid(row=6, column=12)
        Label(oper, text='\t').grid(row=6, column=13)  # want some space in between

        # Email
        Label(oper, text='Email').grid(row=6, column=14)
        Email = Entry(oper)
        Email.grid(row=6, column=15)
        Label(oper, text='\t').grid(row=6, column=16)  # want some space in between

        # Add
        def Add():
            Label(oper, text="operator added to the database").grid(row=8, column=2, columnspan=21)

        Button(oper, text="Add", command=Add, fg="blue2", bg="springgreen").grid(row=6, column=17)
        # Edit
        def Edit():
            Label(oper, text="operator edited in the database").grid(row=8, column=2, columnspan=21)

        Button(oper, text="Edit", command=Edit, fg="blue2", bg="springgreen").grid(row=6, column=19)
        Label(oper, text="\n").grid(row=7, column=1, columnspan=3)  # leaving an empty line

    Button(admin, text="New Operator", command=operate, bg="SeaGreen1").grid(row=6, column=2)
    Label(admin, text="\t").grid(row=6, column=3)  # want some space
    Button(admin, text="New Bus", command=linkme, bg="coral").grid(row=6, column=4)
    Label(admin, text="\t").grid(row=6, column=5)  # want some space
    Button(admin, text="New Route", command=linkme, bg="steel blue").grid(row=6, column=6)
    Label(admin, text="\t").grid(row=6, column=7)  # want some space

root = Tk()
root.geometry('510x510')
root.config()

def open_new_window(event):
    # Create a new window
    new = Toplevel(root)
    new.title("Option Window")

    # Add widgets to the new window
    label = Label(new, image=img)
    label.grid(row=0, column=1, columnspan=3, rowspan=3, padx=10, pady=10, sticky="nsew")  # "nsew" for center alignment

    frame = Frame(new, bg="lightblue", padx=1, pady=1)
    frame.grid(row=3, column=0, columnspan=5, pady=10, sticky="nsew")

    Label(frame, text='Online Bus Booking System', font='times 20 bold italic', fg='red', bg='lightblue').grid(row=0, column=0, pady=10, sticky="nsew")

    # Add buttons with background color
    Button(new, text="Seat Booking", bg="blue", fg="white", command=SeatBooking).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
    Button(new, text="Checked Booked Seat", bg="green", fg="white", command=Checked).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
    Button(new, text="Add Bus Details", bg="orange", fg="white", command=Details).grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

    for i in range(21):
        new.grid_rowconfigure(i, weight=1)
    for i in range(5):
        new.grid_columnconfigure(i, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)


homeimage = PhotoImage(file="/Users/shivanshmahajan/Desktop/Ds lab/holiday/project mahesh/homeicon.png")
img = PhotoImage(file="/Users/shivanshmahajan/Desktop/Ds lab/holiday/project mahesh/starbus.png")
Label(root, image=img).pack()
Label(root, text="Online Bus Booking System", font="arial 20 bold", bg="light blue", fg="red").pack()
Label(root, text="\n\nName: Ishu Jain\n\nER :221B185\n\nMobile: 9983302501\n\n", fg="blue2").pack()
Label(root, text="Submitted to: Mahesh Kumar", font="arial 15 bold", bg="light blue", fg="red").pack()
Label(root, text="Project Based Learning", fg="red").pack()
root.bind("<Button-1>", open_new_window)
root.mainloop()
