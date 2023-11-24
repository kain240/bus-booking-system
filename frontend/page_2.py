from tkinter import *
from frontend.page_3 import Page3

class Page2:
    def page2(self):
        root=Tk()
        screen_width=root.winfo_screenwidth()
        screen_height=root.winfo_screenheight()
        root.geometry(f'{screen_width}x{screen_height}')
        root.title('Online Bus Booking')

        frame= Frame(root)
        frame.grid(row=0, column=1)

        img=PhotoImage(file='frontend/starbus.png')
        photo=Label(root,image=img)
        photo.grid(row=0, column=1, padx=250)

        def seatBooking():
            root.destroy()
            d2 = Page3()
            d2.page3()

        def checkBooking():
            root.destroy()
            import frontend.page_4

        def addBus():
            root.destroy()
            import frontend.page_5

        l1= Label(root, text='Online Bus Booking System', font='Arial 35 ', fg='red', bg='powder blue')
        l1.grid(row=1,column=1, pady=50)

        seat_Booking= Button(root, text='Seat Booking', font='Arial 15 ', bg='aquamarine', command= seatBooking)
        seat_Booking.grid(row=2,column=0, padx=100)
        check_booking= Button(root, text='Check Booked Seat', font='Arial 15 ', bg='spring green', command= checkBooking)
        check_booking.grid(row=2,column=1)
        add_bus= Button(root, text='Add Bus Details', font='Arial 15 ', bg='sea green', command= addBus)
        add_bus.grid(row=2, column=2)
        comment= Label(root, text='For Admin Only', font='Arial 12 bold', fg='red')
        comment.grid(row=3, column=2,pady=10)

        root.mainloop()
