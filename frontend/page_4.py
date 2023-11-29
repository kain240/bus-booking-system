from tkinter import *
from backend import journey_booking

reopen_home = False
def page4():
    root = Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f'{screen_width}x{screen_height}')
    root.title('Online Bus Booking')


    # image
    img = PhotoImage(file="frontend/starbus.png")
    Label(root, image=img).grid(row=1, column=2)
    Label(root, text="\t").grid(row=1, column=9)  # want some space


    # home icon
    def home():
        global reopen_home
        root.destroy()
        reopen_home = True

    homeimage = PhotoImage(file="frontend/homeicon.png")
    Button(root, image=homeimage, command=home, fg="blue2", bg="springgreen").grid(row=1, column=10)

    # label1 online bus booking system
    Label(root, text="Online Bus Booking System", font="arial 20 bold", bg="light blue", fg="red").grid(row=2, column=2)

    Label(root, text="\n").grid(row=3, column=1)  # leaving an empty line

    # check your booking
    Label(root, text="Check Your Booking", font="Arial 15 bold", fg="green4", bg="lawngreen").grid(row=4, column=2)
    Label(root, text='\t\t\t\t\t\t\t\t').grid(row=0, column=0)
    Label(root, text="\n").grid(row=5, column=2)  # leaving an empty line
    Label(root, text="Enter your Mobile Number:").grid(row=5, column=1)
    mob = Entry(root)
    mob.grid(row=5, column=2)


    def fill_ticket_details(data, i):

        reg_leb = Label(root, text='                                                                      ', font='15')
        reg_leb.grid(row=7, column=2)
        try:
            ticket_data = data[i]
        except IndexError:
            reg_leb.config(text='No Ticket is registered with this Mobile Number', font='arial 15', fg='red')

        date_list = journey_booking.get_running_date(ticket_data[5])
        date = date_list[2]

        ToFrom = journey_booking.get_to_from(date_list[1])
        From = ToFrom[0]
        To = ToFrom[1]

        fareAndType = journey_booking.get_fare_type(date_list[0])
        fare = fareAndType[0]
        Type = fareAndType[1]

        name = journey_booking.get_bus_name(fareAndType[2])

        fr = Frame(root, relief="raised", bd=4)
        Label(fr, text="passengers").grid(row=1, column=1)
        Label(fr, text=ticket_data[0]).grid(row=1, column=2)

        Label(fr, text="No. Of Seat").grid(row=2, column=1)
        Label(fr, text=ticket_data[2]).grid(row=2, column=2)

        Label(fr, text="Age").grid(row=3, column=1)
        Label(fr, text=ticket_data[4]).grid(row=3, column=2)

        Label(fr, text="Booking Ref.").grid(row=4, column=1)
        Label(fr, text="Booking").grid(row=4, column=2)

        Label(fr, text="Travel on").grid(row=5, column=1)
        Label(fr, text=date).grid(row=5, column=2)
        Label(fr, text="\n").grid(row=6, column=1)  # leaving an empty line

        Label(fr, text="Boarding Point :").grid(row=7, column=2, columnspan=2)
        Label(fr, text="Destination :").grid(row=8, column=2, columnspan=2)
        Label(fr, text=From).grid(row=7, column=4)
        Label(fr, text=To).grid(row=8, column=4)
        Label(fr, text="\t").grid(row=1, column=3)  # want some space
        # second column
        amount = int(fare) * int(ticket_data[2])
        Label(fr, text="Gender").grid(row=1, column=4)
        Label(fr, text="Phone").grid(row=2, column=4)
        Label(fr, text="Fare").grid(row=3, column=4)
        Label(fr, text="Bus Detail").grid(row=4, column=4)
        Label(fr, text='Type').grid(row=5, column=4)

        Label(fr, text=ticket_data[1]).grid(row=1, column=5)
        Label(fr, text=ticket_data[3]).grid(row=2, column=5)
        Label(fr, text=str(amount)).grid(row=3, column=5)
        Label(fr, text=name).grid(row=4, column=5)
        Label(fr, text=Type).grid(row=5, column=5)

        Label(fr, text="\t").grid(row=1, column=55)  # want some space
        Label(fr, text='\n').grid(row=8, column=1)
        Label(fr, text="\tTotal amount " + str(amount) + " to be paid at the time of boarding").grid(row=9, column=1,
                                                                                                     columnspan=5)
        fr.grid(row=6, column=2)

        # adding ticket change panel
        def show_prev():
            fill_ticket_details(data, i-1)

        def show_next():
            fill_ticket_details(data, i+1)

        Button(root, text="<", command=show_prev).grid(row=7, column=1)
        Label(root, text=f"{i+1} of {len(data)}").grid(row=7, column=2)
        Button(root, text=">", command=show_next).grid(row=7 , column=3)


    def check():
        final_ticket = get_ticket()
        i=0
        fill_ticket_details(final_ticket, i)


    def get_ticket():
        mobile_num = mob.get()
        ticket = journey_booking.get_booking(mobile_num)
        return ticket

    Button(root, text="Check Booking", command=check).grid(row=5, column=3)
    root.mainloop()
    return reopen_home