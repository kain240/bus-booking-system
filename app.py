from tkinter import *
from frontend.page_2 import Page2


class Page1:
    def page1(self):
        root = Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f'{screen_width}x{screen_height}')
        root.title('Online Bus Booking')
        img = PhotoImage(file='frontend/starbus.png')
        photo = Label(root, image=img)
        photo.pack()

        l1 = Label(root, text='Online Bus Booking System', font='Arial 35 ', fg='red', bg='powder blue')
        l1.pack()
        Label(root, text='\n\n').pack()
        name = Label(root, text='Name: Khushi Jain\n', fg='blue', font='Arial 15 bold')
        name.pack()
        er = Label(root, text='Er: 221b204\n', fg='blue', font='Arial 15 bold')
        er.pack()
        mobile = Label(root, text='Mobile: 9753640871\n\n', fg='blue', font='Arial 15 bold')
        mobile.pack()
        sumbitted = Label(root, text='Submitted to: Dr. Mahesh Kumar', font='Arial 25 ', fg='red', bg='powder blue')
        sumbitted.pack()
        l2 = Label(root, text='Project Based Learning', fg='red', font='Arial 10 bold')
        l2.pack()
        Label(root, text='\n\n\n').pack()
        Label(root, text='Press any key to continue...').pack()



        def page2(e):
            root.destroy()
            d1 = Page2()
            d1.page2()

        root.bind('<KeyPress>', page2)

        root.mainloop()


d = Page1()
d.page1()
