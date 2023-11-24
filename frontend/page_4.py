from tkinter import *

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f'{screen_width}x{screen_height}')
root.title('Online Bus Booking')
# image
img = PhotoImage(file="frontend/starbus.png")
Label(root, image=img).grid(row=1, column=2, columnspan=7)
Label(root, text="\t").grid(row=1, column=9)  # want some space


# home icon
def home():
    root.destroy()
    import frontend.page_2

homeimage = PhotoImage(file="frontend/homeicon.png")
Button(root, image=homeimage, command=home, fg="blue2", bg="springgreen").grid(row=1, column=10)

# label1 online bus booking system
Label(root, text="Online Bus Booking System", font="arial 20 bold", bg="light blue", fg="red").grid(row=2, column=2,
                                                                                                    columnspan=7)
Label(root, text="\n").grid(row=3, column=1, columnspan=3)  # leaving an empty line

# check your booking
Label(root, text="Check Your Booking", font="Arial 15 bold", fg="green4", bg="lawngreen").grid(row=4, column=2,
                                                                                               columnspan=7)
Label(root, text="\n").grid(row=5, column=2)  # leaving an empty line
Label(root, text="Enter your Mobile Number:").grid(row=5, column=3)
mob = Entry()
mob.grid(row=5, column=4)


def check():
    fr = Frame(root, relief="raised", bd=4)
    Label(fr, text="passengers").grid(row=1, column=1)
    Label(fr, text="namequery").grid(row=1, column=2)

    Label(fr, text="No. Of Seat").grid(row=2, column=1)
    Label(fr, text="No. of seat query").grid(row=2, column=2)

    Label(fr, text="Age").grid(row=3, column=1)
    Label(fr, text="Age query").grid(row=3, column=2)

    Label(fr, text="Booking Ref.").grid(row=4, column=1)
    Label(fr, text="Booking Ref query").grid(row=4, column=2)

    Label(fr, text="Travel on").grid(row=5, column=1)
    Label(fr, text="\n").grid(row=6, column=1)  # leaving an empty line

    Label(fr, text="Boarding Point").grid(row=7, column=1)
    Label(fr, text="Destination").grid(row=8, column=1)
    Label(fr, text="\t").grid(row=1, column=3)  # want some space
    # second column
    Label(fr, text="Gender").grid(row=1, column=4)
    Label(fr, text="Phone").grid(row=2, column=4)
    Label(fr, text="Fare").grid(row=3, column=4)
    Label(fr, text="\t").grid(row=1, column=55)  # want some space

    Label(fr, text="\ttotal amount<query>to be paid at the time of boarding").grid(row=9, column=1, columnspan=5)

    fr.grid(row=6, column=2, columnspan=5)


Button(root, text="Check Booking", command=check).grid(row=5, column=6)
root.mainloop()