from tkinter import *
from tkinter import ttk
import backend.journey_booking
from backend import journey_booking
from backend import passenger


class Page3:
    def page3(self):
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
        Label(root, image=img).grid(row=1,column=2,columnspan=maxwidth-4)
        #homeicon
        def home():
            root.destroy()



        homeimage=PhotoImage(file="frontend/homeicon.png")
        Button(root,image=homeimage,command=home,fg="blue2",bg="springgreen").grid(row=1,column=maxwidth-4)
        Label(root,text='\t').grid(row=6,column=4)#want some margin

        def get_runs():
            new_booking = journey_booking.Booking( From.get(), To.get(), JourneyDate.get())
            runs = new_booking.find_runs()
            print(runs)
            Show_Bus(runs)

            # update_runs_on_UI(runs)



        #label1 online bus booking system
        Label(root,text="Online Bus Booking System",font="arial 20 bold",bg="light blue",fg="red").grid(row=2,column=2,columnspan=maxwidth)
        Label(root,text="\n").grid(row=3,column=1,columnspan=3)#leaving an empty line

        #journey details
        Label(root,text="Enter Journey Details",font="Arial 10 bold",bg='spring green',fg="green4").grid(row=4,column=2,columnspan=maxwidth)
        Label(root,text="\n").grid(row=5,column=1,columnspan=maxwidth)#leaving an empty line
         #destination
        Label(root,text='To').grid(row=6,column=2)
        To=Entry()
        To.grid(row=6,column=3)
        Label(root,text='\t').grid(row=6,column=4)#want some space in between
         #from
        Label(root,text='From').grid(row=6,column=5)
        From=Entry()
        From.grid(row=6,column=6)
        Label(root,text='\t').grid(row=6,column=7)#want some space in between
         #date
        Label(root,text='JourneyDate').grid(row=6,column=8)
        JourneyDate=Entry()
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

            style = ttk.Style()
            style.configure('TRadiobutton', background='light green', relief='raised')

            counter = 8
            selected_bus = IntVar()


            for index, run in enumerate(runs):
                counter += 1
                ttk.Radiobutton(root, text='Select ' + str(index), variable=selected_bus, value=index,
                            command=select_bus, style= 'TRadiobutton').grid(row=counter, column=2, columnspan=2, padx=5, pady=5)
                Label(root, text=run[1]).grid(row=counter, column=4, columnspan=2)
                Label(root, text=run[2]).grid(row=counter, column=6, columnspan=2)
                Label(root, text=run[3]).grid(row=counter, column=8, columnspan=2)
                Label(root, text=run[4]).grid(row=counter, column=10, columnspan=2)


            Label(root,text="\n").grid(row=110,column=1,columnspan=3)#leaving an empty line
            #fill passenger details
            Label(root,text="Fill Passenger Details to book the bus ticket",bg="turquoise1",fg="red", font='15').grid(row=111,column=2,columnspan=maxwidth)
            Label(root,text="Name").grid(row=112,column=2)
            Name=Entry(root)
            Name.grid(row=112,column=3)
            Label(root,text='\t').grid(row=112,column=4)#want some space in between
            #radio button for gender
            gender='male'
            def show_gender(e):
                global gender
                gender=combobox.get()


            Label(root,text="Gender").grid(row=112,column=5)
            gender_list=['Male', 'Female', 'Third Gender']
            selected_option= StringVar()
            selected_option.set(gender_list[0])
            combobox= ttk.Combobox(root, textvariable=selected_option, value=gender_list)
            combobox.grid(row=112, column=6)
            combobox.bind("<<ComboboxSelected>>", show_gender)

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

            def make_booking():
                journey_booking.BookingTicket(Mobile_Number.get(), select_bus()).set_booking()
                print('done')
            def Book_Seat():
                passenger.Passenger(Name.get(), gender, No_of_seats.get(), Mobile_Number.get(), Age.get(), select_bus()).add()
                Label(root, text="Booked successfully").grid(row=115, column=2, columnspan=maxwidth)

                make_booking()

            #Book_Seat
            Button(root,text="Book Seat",command=Book_Seat).grid(row=12,column=16)
            Label(root,text='\t').grid(row=12,column=17)#want some space in between
            Label(root,text="\n").grid(row=13,column=1,columnspan=3)#leaving an empty line
        Button(root,text="show bus",command=get_runs,fg="blue2",bg="springgreen").grid(row=6,column=14)

        Label(root,text="\n").grid(row=7,column=1,columnspan=3)#leaving an empty line

        root.mainloop()
