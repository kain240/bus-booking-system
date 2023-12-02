from tkinter import *
from backend import operator
from tkinter import messagebox

reopen_home = False
def page6():
    root=Tk()

    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    root.geometry(f'{screen_width}x{screen_height}')
    root.title('Add New Operator')

    Label(root,text="\t        \t").grid(row=1,column=1)#image should be centre aligned

    def home():
        global reopen_home
        root.destroy()
        reopen_home = True

    #image
    img=PhotoImage(file="frontend/starbus.png")
    Label(root,image=img).grid(row=1,column=2,columnspan=17)


    #home icon
    homeimage=PhotoImage(file="frontend/homeicon.png")
    Button(root, image=homeimage, command=home, fg="blue2", bg="springgreen").grid(row=1, column=17)

    #label1 online bus booking system
    Label(root,text="Online Bus Booking System",font="arial 20 bold",bg="light blue",fg="red").grid(row=2,column=2,columnspan=21)
    Label(root,text="\n").grid(row=3,column=1,columnspan=3)#leaving an empty line

    #Add Bus Operator Details
    Label(root,text="Add Bus Operator Details",font="Arial 15 bold",fg="green4").grid(row=4,column=2,columnspan=21)
    Label(root,text="\n").grid(row=5,column=1,columnspan=3)#leaving an empty line
     #Operator Id
    Label(root,text='Operator Id').grid(row=6,column=2)
    Operator_Id=Entry()
    Operator_Id.grid(row=6,column=3)
    Label(root,text='\t').grid(row=6,column=4)#want some space in between
     #Operator Name
    Label(root,text='Operator Name').grid(row=6,column=5)
    Operator_Name=Entry()
    Operator_Name.grid(row=6,column=6)
    Label(root,text='\t').grid(row=6,column=7)#want some space in between
     #Address
    Label(root,text='Address').grid(row=6,column=8)
    Address=Entry()
    Address.grid(row=6,column=9)
    Label(root,text='\t').grid(row=6,column=10)#want some space in between

     #Phone
    Label(root,text='Phone').grid(row=6,column=11)
    Phone=Entry()
    Phone.grid(row=6,column=12)
    Label(root,text='\t').grid(row=6,column=13)#want some space in between

     #Email
    Label(root,text='Email').grid(row=6,column=14)
    Email=Entry()
    Email.grid(row=6,column=15)
    Label(root,text='\t').grid(row=6,column=16)#want some space in between

    #Add
    def add_operator():
        redflag = True
        l1 = Label(root, text='                                                             ', fg='red')
        l1.grid(row=8, column=1, columnspan=17)
        l2 = Label(root, text='                                                             ', fg='red')
        l2.grid(row=9, column=1, columnspan=17)
        l3 = Label(root, text='                                                             ', fg='red')
        l3.grid(row=10, column=1, columnspan=17)
        if Operator_Id.get() == '':
            l1.config(text='Operator Id is a Mandatory field')
            redflag = False

        if Operator_Name.get() == '':
            l2.config(text='Name is a Mandatory field')
            redflag = False

        if len(Phone.get())>10 or len(Phone.get())<10:
            l3.config(text='Invalid mobile number')
            redflag = False

        if (redflag == True):
            operator.Operator(Operator_Id.get(), Operator_Name.get(), Address.get(), Phone.get(), Email.get()).add()
            result = messagebox.showinfo('Operator entry', 'operator recorded successfully')

    Button(root,text="Add",command= add_operator,fg="blue2",bg="springgreen").grid(row=6,column=17)
    #Edit
    def edit_operator():
        redflag = True
        l1 = Label(root, text='                                                             ', fg='red')
        l1.grid(row=8, column=1, columnspan=17)
        if (Operator_Id.get()==''or Operator_Name.get()==''or Phone.get()==''):
            l1.config(text='operatoe Id, name and phone number are mendatory fields')
            redflag = False
        if redflag == True:
            operator.Operator(Operator_Id.get(), Operator_Name.get(), Address.get(), Phone.get(), Email.get()).edit()
            result = messagebox.showinfo('Operator entry update', 'operator recorde updated successfully')

    Button(root,text="Edit",fg="blue2",bg="springgreen", command= edit_operator).grid(row=6,column=19)


    Label(root,text="\n").grid(row=7,column=1,columnspan=3)#leaving an empty line

    root.mainloop()
    return reopen_home
