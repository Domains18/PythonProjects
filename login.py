from cProfile import label
from importlib.metadata import entry_points
from tkinter import *
from tkinter import messagebox
import pymysql


window= Tk ()



#################################################################functions

def reset_password():
    if mailentry == '':
        messagebox.showerror('Error', 'enter the email to reset password')
    else:
        con=pymysql.connect(host='localhost',user='root', password='@rootuser', database='register')
        cur=con.cursor()
        cur.execute('select * from students where email = %s', mailentry.get())
        row=cur.fetchone()

        if row== None:
            messagebox.showerror('Error', 'Please enter a valid email')

        else:
            con.close()
            root2=Toplevel()
            root2.title('forget password')
            root2.geometry('470x560+400+60')
            root2.config(bg='white')
            root2.focus_force()
            root2.grab_set()
            forgetlabel= Label(root2, text='Forgot')
            forgetlabel.place(x=128, y=18)
            root2.mainloop()
            

def register():
    window.destroy()
    import registration


def sign_in():
    if mailentry.get()== '' or passwordentry == '':
        messagebox.showerror('error', 'All fields are required')
    else:
        try:
            con=pymysql.connect(host='localhost', user='root', password='@rootuser', database='register')
            cur=con.cursor()
            cur.execute('select * from students where email=%s', mailentry.get(), passwordentry.get())
            row=cur.fetchone()

            if row == None:
                messagebox.showerror('error', 'Invalid email or password')
            else:
                messagebox.showinfo('succes', 'Access Granted')
            con.close()
        except Exception as e:
            messagebox.showerror('error', f'Due to error in {e}')






#############################################################################

window.geometry('900x600+50+50')
window.title('login Page')


#bgloginimage=PhotoImage(file='loginbg.png')
#bgloginlabel= Label(window, image=bgloginimage)
#bgloginlabel.place(y=0, x=0)

frame= Frame(window, width=568, height=320, bg='white')
frame.place(x=180, y=140)


#userimage=PhotoImage(file='user.png')
#userimagelabel= label(Frame, Image=userimage, bg='white')
#userimagelabel.place(x=10, y=50)


maillabel=Label(frame, text='Email', bg='white')
maillabel.place(x=220, y=32)
mailentry= Entry(frame, bg='white')
mailentry.place(x=220, y=70)

passwordlabel = Label(frame, text='Password' , bg='white')
passwordlabel.place(x=220, y=120)
passwordentry= Entry(frame, bg='white',show='*')
passwordentry.place(x=220, y=160)


regButton=Button(frame, text='Register New Account', bg='white', cursor='hand2', activebackground='white', bd=0, command=register)
regButton.place(x=220, y=200)

forgetbutton=Button(frame, text='forgot password?', bd=0, bg='white',activebackground='white', fg='red', activeforeground='red', cursor='hand2', command=reset_password)
forgetbutton.place(x=410, y=200)

loginbutton=Button(frame, text='Login', fg='white', bg='gray20', cursor='hand2',)
loginbutton.place(x=450, y=240)




window.mainloop()