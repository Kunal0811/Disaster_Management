from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import streamlit as st

def user_enter(event):
    if username.get()=='Username':
        username.delete(0,END)

def password_enter(event):
    if password.get()=='Password':
        password.delete(0,END)

def hide():
    openeye.config(file='closeye.png')
    password.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    password.config(show='')
    eyeButton.config(command=hide)

def signup_page():
    login.destroy()
    import Signup

def home():
    if username.get()=='' and password.get()=='':
        messagebox.showerror('Error','Please fill the all fields.')
    else:
        login.destroy()
        import Home



login=Tk()
login.title("Login")
login.geometry("1000x772")
login.resizable(False,False)
bgImage=ImageTk.PhotoImage(file='disa_bg.jpg')

bgLabel=Label(login,image=bgImage)
bgLabel.place(x=0,y=0)
frame=Frame(login,bg='lightyellow')
frame.place(x=400,y=350)

heading=Label(frame,text='USER LOGIN',font=('Franklin Gothic Medium',23,
                                           'bold'),bg='lightyellow',fg='black')

heading.grid(row=0,column=0,padx=10,pady=10)
username=Entry(frame,width=30,font=('keyboard',11),bg='lightyellow')
username.grid(row=1,column=0,padx=10,pady=10)
username.insert(0,'Username')
username.bind('<FocusIn>',user_enter)

password=Entry(frame,width=30,font=('keyboard',11),bg='lightyellow')
password.grid(row=2,column=0,padx=0,pady=0)
password.insert(0,'Password')
password.bind('<FocusIn>',password_enter)



openeye=PhotoImage(file='openeye.png')
eyeButton=Button(frame,image=openeye,bd=0,bg='lightyellow',activebackground='white'
                 ,cursor='hand2',command=hide)
eyeButton.grid(row=2,column=1,padx=0)

forgetButton=Button(frame,text='Forgot Password?',fg='blue',bg='lightyellow',activebackground='white'
                 ,cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'))
forgetButton.grid(row=3,column=0)

loginButton=Button(frame,text='Login',font=('Open Sans',16,'bold'),
                   bg='firebrick1',fg='white',activebackground='yellow',cursor='hand2'
                   ,bd=0,width=19,command=home)
loginButton.grid(row=4,column=0,padx=10,pady=10)

signupLabel=Label(frame,text="Don't have an account?",font=('Open Sans',9,'bold'),bg='white')
signupLabel.grid(row=5,column=0,padx=50)

signupButton=Button(frame,text='Create new one',font=('Open Sans',9,'bold underline'),
                   bg='white',fg='blue',activebackground='white',cursor='hand2'
                   ,bd=0,command=signup_page)
signupButton.grid(row=6,column=0)

login.mainloop()
