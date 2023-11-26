from tkinter import *
root=Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f'{screen_width}x{screen_height}')
img=PhotoImage(file="frontend/starbus.png")
Label(root,text="\t").grid(row=1,column=1, padx=200)#want some space
Label(root,image=img).grid(row=1,column=2,columnspan=9)


#homeicon
def home():
    root.destroy()
    import frontend.page_2

def newOperator():
    root.destroy()
    import frontend.Operator_page_6

def newBus():
    root.destroy()
    import frontend.newBus_page_8

def newRoute():
    root.destroy()
    import frontend.RouteDetails_page_7

def newRun():
    root.destroy()
    import frontend.run_page_9

Label(root, text='\t\t\t\t').grid(row=1,column=12)
homeimage=PhotoImage(file="frontend/homeicon.png")
Button(root,image=homeimage,command=home,fg="blue2",bg="springgreen").grid(row=1,column=13)
Label(root,text="Online Bus Booking System",font="arial 25 bold",bg="light blue",fg="red").grid(row=2,column=2,columnspan=9)
Label(root,text="\n").grid(row=3,column=2)#leaving a blank line
Label(root,text="Add New Details to Database",font="Arial 15 bold",fg="green").grid(row=4,column=2,columnspan=9)
Label(root,text="\n",font="Arial 10 bold",fg="red").grid(row=5,column=2,columnspan=3)

Button(root,text="New Operator",command= newOperator,bg="SeaGreen1", font='10').grid(row=6,column=3, pady=30)
Label(root,text="\t").grid(row=6,column=4)#want some space
Button(root,text="New Bus",command=newBus,bg="coral", font='10').grid(row=6,column=5)
Label(root,text="\t").grid(row=6,column=6)#want some space
Button(root,text="New Route",command=newRoute,bg="steel blue", font='10').grid(row=6,column=7)
Label(root,text="\t").grid(row=6,column=8)#want some space
Button(root,text="New Run",command=newRun,bg="LightPink3", font='10').grid(row=6,column=9)
Label(root,text="\t").grid(row=6,column=10)#want some space
root.mainloop()