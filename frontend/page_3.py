from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import backend.journey_booking
from backend import journey_booking
from backend import passenger


reopen_home = False

def page3():
    root=Tk()

    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    root.geometry(f'{screen_width}x{screen_height}')
    root.title('Seat Booking')
    #maxwidth is storing the maximum column wise expansion of root page-1
    maxwidth=16
    Label(root,text="\t        \t").grid(row=1,column=1)


    #image
    img=PhotoImage(file="frontend/starbus.png")
    Label(root, image=img).grid(row=1,column=4,columnspan=maxwidth-4)
    #homeicon
    def home():
        global reopen_home
        root.destroy()
        reopen_home = True


    homeimage=PhotoImage(file="frontend/homeicon.png")
    Button(root,image=homeimage,command=home,fg="blue2",bg="springgreen").grid(row=1,column=maxwidth-2, rowspan=2)
    Label(root,text='\t').grid(row=6,column=4)#want some margin

    def get_runs():
        new_booking = journey_booking.Booking( From.get().lower(), To.get().lower(), JourneyDate.get())
        runs = new_booking.find_runs()
        l11 = Label(root, text='                                      ', fg='red')
        l11.grid(row=90, column=2, columnspan=maxwidth)
        if len(runs)>0:
            Show_Bus(runs)

        else:
            l11.config(text='no buses found!!')


        # update_runs_on_UI(runs)



    #label1 online bus booking system
    Label(root,text="Online Bus Booking System",font="arial 20 bold",bg="light blue",fg="red").grid(row=2,column=2,columnspan=maxwidth)
    Label(root,text="\n").grid(row=3,column=1,columnspan=3)#leaving an empty line

    #journey details
    Label(root,text="Enter Journey Details",font="Arial 12 bold",bg='spring green',fg="green4").grid(row=4,column=2,columnspan=maxwidth)
    Label(root,text="\n").grid(row=5,column=1,columnspan=maxwidth)#leaving an empty line
     #destination
    Label(root,text='To').grid(row=6,column=2)
    To=Entry(root)
    To.grid(row=6,column=3)
    Label(root,text='\t').grid(row=6,column=4)#want some space in between
     #from
    Label(root,text='From').grid(row=6,column=5)
    From=Entry(root)
    From.grid(row=6,column=6)
    Label(root,text='\t').grid(row=6,column=7)#want some space in between
     #date
    Label(root,text='JourneyDate').grid(row=6,column=8)
    JourneyDate=Entry(root)
    JourneyDate.grid(row=6,column=9)
    Label(root,text='\t').grid(row=6,column=10)#want some space in between

    #show bus
    def Show_Bus(runs):
        Label(root, text='Select Bus').grid(row=8, column=2, columnspan=2)
        Label(root, text='Operator').grid(row=8, column=4, columnspan=2)
        Label(root, text='Bus Type').grid(row=8, column=6, columnspan=2)
        Label(root, text='Availablity').grid(row=8, column=8, columnspan=2)
        Label(root, text='Fare').grid(row=8, column=10, columnspan=2)

        def select_bus():
            selected_bus_no=selected_bus.get()
            print(selected_bus_no)
            choice_is= list(runs[selected_bus_no])
            print(choice_is)
            return(choice_is[0])

        def fare_is():
            selected_bus_no = selected_bus.get()
            choice_is = list(runs[selected_bus_no])
            return (choice_is[4])

        def bus_booking_details():
            selected_bus_no = selected_bus.get()
            choice_is = list(runs[selected_bus_no])
            return (choice_is)

        style = ttk.Style()
        style.configure('TRadiobutton', background='light green', relief='raised')

        counter = 8
        selected_bus = IntVar()


        for index, run in enumerate(runs):
            counter += 1
            ttk.Radiobutton(root, text='Select ', variable=selected_bus, value=index,
                        command=select_bus, style= 'TRadiobutton').grid(row=counter, column=2, columnspan=2, padx=5, pady=3)
            Label(root, text=run[1]).grid(row=counter, column=4, columnspan=2)
            Label(root, text=run[2]).grid(row=counter, column=6, columnspan=2)
            Label(root, text=run[3]).grid(row=counter, column=8, columnspan=2)
            Label(root, text=run[4]).grid(row=counter, column=10, columnspan=2)


        #Label(root,text="").grid(row=109,column=1,columnspan=3)#leaving an empty line
        #fill passenger details
        def fill_passenger_details():
            Label(root,text="Fill Passenger Details to book the bus ticket",bg="turquoise1",fg="red", font='15').grid(row=100,column=2,columnspan=maxwidth)
            Label(root, text="\n").grid(row=111, column=1, columnspan=3)
            Label(root,text="Name").grid(row=112,column=2)
            Name=Entry(root)
            Name.grid(row=112,column=3)
            Label(root,text='\t').grid(row=112,column=4)#want some space in between
            #radio button for gender
            def show_gender():
                return selected_option.get()

            Label(root,text="Gender").grid(row=112,column=5)
            gender_list=['Male', 'Female', 'Third Gender']
            selected_option= StringVar()
            selected_option.set('--select--')
            drop= OptionMenu(root, selected_option, *gender_list)
            drop.grid(row=112, column=6)

            Label(root,text='\t').grid(row=112,column=7)#want some space in between
            #number of seats
            Label(root,text="No. of seats").grid(row=112,column=8)
            No_of_seats=Entry(root)
            No_of_seats.grid(row=112,column=9)
            Label(root,text='\t').grid(row=112,column=10)#want some space in between
            #mobile number
            Label(root,text="mobile number").grid(row=112,column=11)
            Mobile_Number=Entry(root)
            Mobile_Number.grid(row=112,column=12)
            Label(root,text='\t').grid(row=112,column=13)#want some space in between
            #age
            Label(root,text="Age").grid(row=112,column=14)
            Age=Entry(root)
            Age.grid(row=112,column=15)
            Label(root, text='\t').grid(row=112, column=16)  # want some space in between
            def make_booking():
                journey_booking.BookingTicket(Mobile_Number.get(), select_bus()).set_booking()
                print('done')
            def Book_Seat():
                l22=Label(root, text='                                                                                     ', fg='red')
                l22.grid(row=200, column=2, columnspan=maxwidth)
                l33=Label(root, text='                                                                        ', fg='red')
                l33.grid(row=201, column=2,columnspan=maxwidth)
                l44=Label(root, text='                                                                        ', fg='red')
                l44.grid(row=202, column=2, columnspan=maxwidth)
                redFlag = True
                seats= bus_booking_details()
                if(Name.get() == ''):
                    l22.config(text='please enter your name!!')
                    redFlag = False
                if (No_of_seats.get()==''):
                    l33.config(text='please enter the number of seats needed!!')
                    redFlag = False
                elif (int(No_of_seats.get())> int(seats[3])):
                    l33.config(text='                  seats not available!!                    ')
                    redFlag = False
                if(len(Mobile_Number.get())>10 or  len(Mobile_Number.get())<10):
                    l44.config(text='invalid Mobile Number!!')
                    redFlag = False
                if(redFlag == True):
                    passenger.Passenger(Name.get(), show_gender(), No_of_seats.get(), Mobile_Number.get(), Age.get(), select_bus()).add()
                #Label(root, text="Booked successfully").grid(row=115, column=2, columnspan=maxwidth)
                    amount= int(No_of_seats.get()) * int(fare_is())
                    result = messagebox.askyesno('Fare Confirm', 'total amount to paid Rs. ' + str(amount))

                def view_ticket():
                    result = messagebox.showinfo('Booking Confirmation', 'Booking confirmed')
                    new_window = Toplevel(root)
                    new_window.title("Bus Ticket")
                    screen_width = new_window.winfo_screenwidth()
                    screen_height = new_window.winfo_screenheight()
                    new_window.geometry(f'{screen_width}x{screen_height}')

                    img = PhotoImage(file='frontend/starbus.png')
                    photo = Label(new_window, image=img)
                    photo.image = img  # Keeping a reference to avoid garbage collection
                    photo.grid(row=0, column=2, padx=550)


                    l1 = Label(new_window, text='Online Bus Booking System', font='Arial 20 ', fg='red', bg='powder blue')
                    l1.grid(row=1, column=2, pady=20)

                    Label(new_window, text='Bus Ticket', font='Arial 20 ').grid(row=2, column=2)
                    Label(new_window, text='').grid(row=3, column=2)

                    fr = Frame(new_window, relief="raised", bd=4)
                    Label(fr, text="passengers", font= 'bold').grid(row=1, column=1)
                    Label(fr, text=Name.get(), font= 'bold').grid(row=1, column=2)

                    Label(fr, text="No. Of Seat", font= 'bold').grid(row=2, column=1)
                    Label(fr, text=No_of_seats.get(), font= 'bold').grid(row=2, column=2)

                    Label(fr, text="Age", font= 'bold').grid(row=3, column=1)
                    Label(fr, text=Age.get(), font= 'bold').grid(row=3, column=2)

                    Label(fr, text="Booking Ref.", font= 'bold').grid(row=4, column=1)
                    Label(fr, text="Booking", font= 'bold').grid(row=4, column=2)

                    bus_details = bus_booking_details()

                    Label(fr, text="Travel on", font= 'bold').grid(row=5, column=1)
                    Label(fr, text=JourneyDate.get(), font= 'bold').grid(row=5, column=2)
                    Label(fr, text="\n").grid(row=6, column=1)  # leaving an empty line

                    Label(fr, text="Boarding Point :", font= 'bold').grid(row=7, column=2, columnspan=2)
                    Label(fr, text="Destination :", font= 'bold').grid(row=8, column=2, columnspan=2)
                    Label(fr, text=To.get(), font= 'bold').grid(row=7, column=4)
                    Label(fr, text=From.get(), font= 'bold').grid(row=8, column=4)
                    Label(fr, text="\t").grid(row=1, column=3)  # want some space
                    # second column
                    amount = int(No_of_seats.get()) * int(fare_is())

                    Label(fr, text="Gender", font= 'bold').grid(row=1, column=4)
                    Label(fr, text="Phone", font= 'bold').grid(row=2, column=4)
                    Label(fr, text="Fare", font= 'bold').grid(row=3, column=4)
                    Label(fr, text="Bus Detail", font= 'bold').grid(row=4,column=4)

                    Label(fr, text=show_gender(), font= 'bold').grid(row=1, column=5)
                    Label(fr, text=Mobile_Number.get(), font= 'bold').grid(row=2, column=5)
                    Label(fr, text=str(amount), font= 'bold').grid(row=3, column=5)
                    Label(fr, text=bus_details[1], font= 'bold').grid(row=4, column=5)

                    Label(fr, text="\t").grid(row=1, column=55)  # want some space
                    Label(fr, text='\n').grid(row=8, column=1)
                    Label(fr, text="\tTotal amount " + str(amount) + " to be paid at the time of boarding", font= 'bold').grid(row=9, column=1, columnspan=5)

                    fr.grid(row=6, column=2, columnspan=5)



                if result==True:
                    make_booking()
                    view_ticket()
            #Book_Seat
            Button(root,text="Book Seat",command=Book_Seat, bg='light green').grid(row=112,column=17)
            Label(root,text='\t').grid(row=12,column=17)#want some space in between
            Label(root,text="\n").grid(row=13,column=1,columnspan=3)#leaving an empty line

        Button(root, text='Proceed To Book', bg='light green', command=fill_passenger_details).grid(row=counter, column=12)

    Button(root,text="show bus",command=get_runs,fg="blue2",bg="springgreen").grid(row=6,column=12)

    Label(root,text="\n").grid(row=7,column=1,columnspan=3)#leaving an empty line

    root.mainloop()
    return reopen_home
