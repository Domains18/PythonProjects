from cProfile import label
from os import access
import tkinter
from tkinter import *
import cryptography
from tkinter.ttk import Combobox
from tkinter import messagebox
import pymysql

from setuptools import Command

### functions

def login():
    print ("succesful")


def clear():
    entryfirstName.delete(0, END)
    entryLastName.delete(0, END)
    entrycontact.delete(0, END)
    entryEmail.delete(0, END)
    entrypassword.delete(0, END)
    entryconfirmpassword.delete(0, END)
    entryanswer.delete(0, END)
    comboquestion.current(0)
    check.set(0)


def register():
    if entryfirstName.get()=='' or entryLastName.get() == '' or entryEmail.get() == '' or entrycontact.get() == ''\
        or entrypassword.get() == '' or entryconfirmpassword.get() == '' or comboquestion.get()== 'select':
            messagebox.showerror('Error', 'Access denied, please fill out everything')

    elif entrypassword.get()!=entryconfirmpassword.get():
        messagebox.showerror('Error', 'access denied, password mismatch')
    
    elif check.get==0:
        messagebox.showerror('Error' 'Please agree to our terms and conditions')

    else:
        try:
            con=pymysql.connect(host='localhost', user='root', password='@rootuser', database='register')
            cur=con.cursor()
            cur.execute('select * from students where email = %s', entryEmail.get())
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror('Error', 'User already exists')

            else:
                cur.execute('insert into students(f_name, l_name, contact, email, question, answer, password) values=(%s, %s, %s,%s, %s, %s, %s)',
                (entryfirstName.get(), entryLastName.get(), entrycontact.get(), 
                entryEmail.get(), comboquestion.get(), entryanswer.get(), entrypassword.get()))
                con.commit()
                con.close()

                messagebox.showerror('Success', 'Registration succesful')
                clear()
        except Exception as e:
            messagebox.showerror('error', f'error due to {e}')
            clear()
            root.destroy()
            import login 




#############################end of functions
root = Tk ()
root.geometry('675x355')

root.geometry('675x355+10+10')
root.title('REGISTRATION FORM')
registerFrame=Frame(root, width=325, height=325,)
registerFrame.place(x=315, y=15)
titleLabel = Label(registerFrame, text="REGISTRATION FORM")
titleLabel.place(x=10, y=2)

firstNamelabel = Label (registerFrame, text="FirstName")
firstNamelabel.place(x=10, y=40)
entryfirstName = Entry(registerFrame , bg='lightgray')
entryfirstName.place(x=10, y=57.5)

lastNameLabel = Label (registerFrame , text="LastName")
lastNameLabel.place(x=185, y=40)
entryLastName = Entry(registerFrame , bg='lightgray')
entryLastName.place(x=185, y=57.5)


contactLabel = Label (registerFrame , text="Contact")
contactLabel.place(x=185, y=100)
entrycontact = Entry(registerFrame)
entrycontact.place(x=185, y=117.5)


EmailLabel = Label (registerFrame , text="Email")
EmailLabel.place(x=10, y=100)
entryEmail = Entry(registerFrame)
entryEmail.place(x=10, y=117.5)


questionLabel = Label (registerFrame , text="SECURITY QUESTION")
questionLabel.place(x=10, y=160)
entryanswer= Entry(registerFrame)
entryanswer.place(x=185, y=177.5)

comboquestion = Combobox(registerFrame,state='readonly')
comboquestion.config(values = ('select', 'Your First Name', 'your best friend', 'your pet'))
comboquestion.place(x=10, y=177.5)
comboquestion.current(0)

answerLabel= Label (registerFrame, text='Answer')
answerLabel.place (x=185, y=160)

passwordLabel = Label (registerFrame , text="Enter your password")
passwordLabel.place(x=10, y=220)
entrypassword = Entry(registerFrame,show='')
entrypassword.place(x=10, y=237.5)

confirmpasswordLabel = Label (registerFrame , text="confirm your password")
confirmpasswordLabel.place(x=185, y=220)
entryconfirmpassword = Entry(registerFrame,show='*')
entryconfirmpassword.place(x=185, y=237.5)

check=IntVar()
checkbutton=Checkbutton( registerFrame , text='I agree to all terms and conditions', onvalue=1, offvalue=0, variable=check)
checkbutton.place(x=10, y=265)

registerButton = Button (registerFrame, text='Register', bg='white', cursor='hand2', activebackground='white', bd=0, command=register)
registerButton.place(x=125, y=290)

loginButton = Button(text='LOGIN', bg='white', cursor='hand2', activebackground='white', bd=0, command=login)
loginButton.place(x=120, y=165)
root.mainloop()