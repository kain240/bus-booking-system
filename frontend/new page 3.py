from tkinter import *
from backend import booking

root=Tk()

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
root.geometry(f'{screen_width}x{screen_height}')
root.title('Online Bus Booking')
#maxwidth is storing the maximum column wise expansion of root page-1
maxwidth=16
Label(root,text="\t        \t").grid(row=1,column=1)


#image
img=PhotoImage(file="frontend/starbus.png")
Label(root,image=img).grid(row=1,column=2,columnspan=maxwidth-4)
#homeicon
def home():
    Label(root,text="please link home button to the root window").grid(row=100,column=2,columnspan=maxwidth)
homeimage=PhotoImage(file="frontend/homeicon.png")
Button(root,image=homeimage,command=home,fg="blue2",bg="springgreen").grid(row=1,column=maxwidth-4)
Label(root,text='\t').grid(row=6,column=4)#want some margin

def get_details():
    booking.Booking(To.get(), From.get(), JourneyDate.get()).make_booking()
def Book_Seat():
    Label(root,text="please add functionality to book seat function").grid(row=90,column=2,columnspan=maxwidth)

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
def Show_Bus():
    Label(root,text='Select Bus').grid(row=8,column=2)
    Label(root,text='Operator').grid(row=8,column=4)
    Label(root,text='Bus Type').grid(row=8,column=6)
    Label(root,text='Availablity').grid(row=8,column=8)
    Label(root,text='Fare').grid(row=8,column=10)
    #here i would add a frame on row 9 to display available buses
    Label(root,text="\n").grid(row=10,column=1,columnspan=3)#leaving an empty line    
    #fill passenger details
    Label(root,text="Fill Passenger Details to book the bus ticket",bg="turquoise1",fg="red").grid(row=11,column=2,columnspan=maxwidth)
    Label(root,text="Name").grid(row=12,column=2)
    Name=Entry()
    Name.grid(row=12,column=3)
    Label(root,text='\t').grid(row=12,column=4)#want some space in between
    #radio button for gender
    Label(root,text='\t').grid(row=12,column=7)#want some space in between
    #number of seats
    Label(root,text="No. of seats").grid(row=12,column=8)
    No_of_seats=Entry()
    No_of_seats.grid(row=12,column=9)
    Label(root,text='\t').grid(row=12,column=10)#want some space in between
    #mobile number
    Label(root,text="mobile number").grid(row=12,column=11)
    Mobile_Number=Entry()
    Mobile_Number.grid(row=12,column=12)
    Label(root,text='\t').grid(row=12,column=13)#want some space in between
    #age
    Label(root,text="Age").grid(row=12,column=14)
    Age=Entry()
    Age.grid(row=12,column=15)
    #Book_Seat
    Button(root,text="Book Seat",command=Book_Seat).grid(row=12,column=16)
    Label(root,text='\t').grid(row=12,column=17)#want some space in between
    Label(root,text="\n").grid(row=13,column=1,columnspan=3)#leaving an empty line
Button(root,text="show bus",command=Show_Bus,fg="blue2",bg="springgreen").grid(row=6,column=14)

Label(root,text="\n").grid(row=7,column=1,columnspan=3)#leaving an empty line

root.mainloop()
