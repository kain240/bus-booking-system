from tkinter import *
root=Tk()

img=PhotoImage(file="frontend/starbus.png")
Label(root,text="\t").grid(row=1,column=1)#want some space
Label(root,image=img).grid(row=1,column=2,columnspan=7)


#homeicon
def home():
    Label(root,text="please link home button to the root window").grid(row=7,column=2,columnspan=8)

homeimage=PhotoImage(file="frontend/homeicon.png")
Button(root,image=homeimage,command=home,fg="blue2",bg="springgreen").grid(row=1,column=9)
Label(root,text="Online Bus Booking System",font="arial 20 bold",bg="light blue",fg="red").grid(row=2,column=2,columnspan=9)
Label(root,text="\n").grid(row=3,column=2)#leaving a blank line
Label(root,text="Add New Details to Database",font="Arial 15 bold",fg="green").grid(row=4,column=2,columnspan=9)
Label(root,text="\n",font="Arial 10 bold",fg="red").grid(row=5,column=2,columnspan=3)

def linkme():
    Label(root,text="I think you are supposed to do the rest").grid(row=8,column=2,columnspan=8)

Button(root,text="New Operator",command=linkme,bg="SeaGreen1").grid(row=6,column=2)
Label(root,text="\t").grid(row=6,column=3)#want some space
Button(root,text="New Bus",command=linkme,bg="coral").grid(row=6,column=4)
Label(root,text="\t").grid(row=6,column=5)#want some space
Button(root,text="New Route",command=linkme,bg="steel blue").grid(row=6,column=6)
Label(root,text="\t").grid(row=6,column=7)#want some space
Button(root,text="New Run",command=linkme,bg="LightPink3").grid(row=6,column=8)
Label(root,text="\t").grid(row=6,column=9)#want some space
