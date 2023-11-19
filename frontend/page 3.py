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
photo.grid(row=0, column=3, padx=250)

l1= Label(root, text='Online Bus Booking System', font='Arial 30 ', fg='red', bg='powder blue')
l1.grid(row=1,column=3)

def show_bus():
    Label(root, text='Select Bus', fg='green').grid(row=4, column=0)
    Label(root, text='Operator', fg='green').grid(row=4, column=1)
    Label(root, text='Bus Type', fg='green').grid(row=4, column=2)
    Label(root, text='Available Capacity', fg='green').grid(row=4, column=3)
    Label(root, text='Fare', fg='green').grid(row=4, column=4)
    proceed= Button(root, text='Proceed to book')

label = Label(root, text='Enter Journey Details', font='Arial 15 ', bg='light green')
label.grid(row=2, column=3, pady=20)
to= Label(root, text='To')
From= Label(root, text='From')
date= Label(root, text='Journey Date')
show= Button(root, text='Show Bus', command=show_bus)

to.grid(row=3,column=0, padx=100)
From.grid(row=3,column=2)
date.grid(row=3,column=4)
show.grid(row=3,column=6)

to_e= Entry(root)
from_e= Entry(root)
date_e= Entry(root)

to_e.grid(row=3, column=1)
from_e.grid(row=3, column=3)
date_e.grid(row=3, column=5)

root.mainloop()
