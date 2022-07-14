from tkinter import *

root = Tk()
root.geometry('500x300')


def checkvals():
    print("Accepted")


Label(root, text="Registration form", font='ar 15 bold').grid(row=0, column=3)
Name = Label(root, text="Name")
Phone = Label(root, text="Phone")
Email = Label(root, text="Email")
Gender = Label(root, text="Gender")
Payment = Label(root, text="Payment mode")
Name.grid(row=1, column=2)
Phone.grid(row=2, column=2)
Email.grid(row=3, column=3)
Gender.grid(row=4, column=2)
Payment.grid(row=5, column=2)

Namevalue = StringVar
Phonevalue = StringVar
EmailValue = StringVar
Gendervalue = StringVar
Paymentvalue = StringVar
CheckValue = IntVar

Nameentry = Entry(root, textvariable=Namevalue)
phoneentry = Entry(root, textvariable=Phonevalue)
emailentry = Entry(root, textvariable=EmailValue)
Genderentry = Entry(root, textvariable=Gendervalue)
Paymententry = Entry(root, textvariable=Paymentvalue)

Nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
emailentry.grid(row=3, column=3)
Genderentry.grid(row=4, column=3)
Paymententry.grid(row=5, column=3)

clickButton = Checkbutton(text="Remember Me", variable=CheckValue)

clickButton.grid(row=6, column=3)

Button(text="Submit", command=checkvals).grid(row=7, column=3)

root.mainloop()