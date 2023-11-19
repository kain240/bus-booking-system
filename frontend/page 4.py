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
l1.grid(row=1,column=1)
label = Label(root, text='Check Your Booking', font='Arial 15 ', bg='light green')
label.grid(row=2, column=1, pady=10)
mob= Label(root, text='Enter Your Mobile No: ')
mob.grid(row=3, column=1, sticky=W)
mob_e= Entry(root)
mob_e.grid(row=3,column=1)
check= Button(root, text='Check Booking')
check.grid(row=3, column=1, sticky=E)

root.mainloop()
