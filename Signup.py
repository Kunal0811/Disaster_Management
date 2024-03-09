from tkinter import *
from tkinter import messagebox


from PIL import ImageTk

def login_page():
    signup_window.destroy()
    import Login


def required():
    if emailEntry.get() == "" or passwordEntry.get() == "" or usernameEntry.get() == "" or comfirmEntry.get() == "":
        messagebox.showerror("Error", "Please fill all the fields")

    elif passwordEntry.get() != comfirmEntry.get():
        messagebox.showerror("Error", "Passwords do not match")

    else:
        messagebox.showinfo("Congratulations", "Your account has been successfully registered. \nNow click on login button to login")


signup_window = Tk()
signup_window.title('SignUp Page')
signup_window.resizable(True,True)
background=ImageTk.PhotoImage(file='disbg.png')

bgLabel = Label(signup_window, image=background)
bgLabel.grid()

heading=Label(signup_window,text='CREATE AN ACCOUNT',font=('Franklin Gothic Medium',18,
                                           'bold'),bg='lightyellow')
heading.place(x=650,y=260)

emailLabel=Label(signup_window,text='Email',font=('Microsoft Yahei UI Light',10,
                                           'bold'),bg='lightyellow')
emailLabel.place(x=650,y=320)

emailEntry=Entry(signup_window,width=25,font=('Microsoft Yahei UI Light',10,
                                           'bold'),bg='lightyellow',fg='black')
emailEntry.place(x=650,y=340)

usernameLabel=Label(signup_window,text='Username',font=('Microsoft Yahei UI Light',10,
                                           'bold'),bg='lightyellow')
usernameLabel.place(x=650,y=370)

usernameEntry=Entry(signup_window,width=25,font=('Microsoft Yahei UI Light',10,
                                           'bold'),bg='lightyellow',fg='black')
usernameEntry.place(x=650,y=390)

passwordLabel=Label(signup_window,text='Password',font=('Microsoft Yahei UI Light',10,
                                           'bold'),bg='lightyellow')
passwordLabel.place(x=650,y=420)

passwordEntry=Entry(signup_window,width=25,font=('Microsoft Yahei UI Light',10,
                                           'bold'),bg='lightyellow',fg='black')
passwordEntry.place(x=650,y=440)

comfirmLabel=Label(signup_window,text='Comfirm Password',font=('Microsoft Yahei UI Light',10,
                                           'bold'),bg='lightyellow')
comfirmLabel.place(x=650,y=470)

comfirmEntry=Entry(signup_window,width=25,font=('Microsoft Yahei UI Light',10,
                                           'bold'),bg='lightyellow',fg='black')
comfirmEntry.place(x=650,y=490)

check=IntVar()
tnc=Checkbutton(signup_window,text='I agree to the terms and conditions'
     ,font=('Microsoft Yahei UI',9,'bold'),bg='lightyellow',cursor='hand2',variable=check)
tnc.place(x=650,y=520)

btn=Button(signup_window,text='SignUp',font=('Microsoft Yahei UI Light',9,'bold')
           ,bg='lightyellow',fg='black',activebackground='lightyellow'
           ,cursor='hand2',bd=0,width=19,command=required)
btn.place(x=650,y=550)

loginLabel=Label(signup_window,text="Already have an account?",font=('Open Sans',9,'bold'),bg='lightyellow')
loginLabel.place(x=650,y=590)

LoginButton=Button(signup_window,text='Login',font=('Open Sans',9,'bold underline'),
                   bg='lightyellow',fg='blue',activebackground='white',cursor='hand2'
                   ,bd=0,command=login_page)
LoginButton.place(x=800,y=590)

signup_window.mainloop()
