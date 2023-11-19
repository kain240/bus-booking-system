from tkinter import *
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

l1= Label(root, text='Online Bus Booking System', font='Arial 35 ', fg='red', bg='powder blue')
l1.grid(row=1,column=1, pady=50)

seat_Booking= Button(root, text='Seat Booking', font='Arial 15 ', bg='aquamarine')
seat_Booking.grid(row=2,column=0, padx=100)
check_booking= Button(root, text='Check Booked Seat', font='Arial 15 ', bg='spring green')
check_booking.grid(row=2,column=1)
add_bus= Button(root, text='Add Bus Details', font='Arial 15 ', bg='sea green')
add_bus.grid(row=2, column=2)
comment= Label(root, text='For Admin Only', font='Arial 12 bold', fg='red')
comment.grid(row=3, column=2,pady=10)

root.mainloop()
