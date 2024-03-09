from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog


def home():
    home.destroy()
    import Home


def login():
    home.destroy()
    import Login


home = Tk()
home.title("Home")
home.geometry("900x600")
home.resizable(False, False)


logo = ImageTk.PhotoImage(file='dis_logo.jpg')
logoLabel = Label(home, image=logo)
logoLabel.place(x=0, y=0)

heading = Label(home, text="Disaster Relief Portal", font=('Protest Strike', 25, 'bold'))
heading.place(x=50, y=0)

logrsbutton = Button(home, text="Login/Register", font=('arial', 12), cursor="hand2", bg='yellow',activebackground='yellow', fg='black',
                     command=login)
logrsbutton.place(x=780, y=0)

hbutton = Button(home, text="Home", font=('arial', 12, 'bold'), cursor="hand2"
                 , bg='yellow', fg='black', activebackground='lightyellow', command=home)
hbutton.place(x=0, y=60)

abtusbutton = Button(home, text="About us", font=('arial', 12,'bold'), cursor="hand2", bg='yellow',activebackground='yellow', fg='black')
abtusbutton.place(x=60, y=60)

ctabutton = Button(home, text="CTA", font=('arial', 12,'bold'), cursor="hand2", bg='yellow',activebackground='yellow', fg='black')
ctabutton.place(x=144, y=60)

sftpbutton = Button(home, text="Safety Tips", font=('arial', 12,'bold'), cursor="hand2", bg='yellow',activebackground='yellow', fg='black')
sftpbutton.place(x=192, y=60)

atlsbutton = Button(home, text="Articles", font=('arial', 12,'bold'), cursor="hand2", bg='yellow',activebackground='yellow', fg='black')
atlsbutton.place(x=292, y=60)

cntsbutton = Button(home, text="Contact us", font=('arial', 12,'bold'), cursor="hand2", bg='yellow',activebackground='yellow', fg='black')
cntsbutton.place(x=364, y=60)

label=Label(home, text="   ",font=('arial',17,'bold'),width=460,height=1,bg="yellow")
label.place(x=462,y=60)

label1=Label(home,bg="yellow",height=23,width=60)
label1.place(x=250,y=110)

label2=Label(home, text="Welcome to our Disaster Management website!", font=('arial',12),bg='yellow',fg='black')
label2.place(relx=0.28, rely=0.21, anchor='w')

label3=Label(home, text="As the apex body for disaster management in World,",font=('arial',12),bg='yellow',fg='black')
label3.place(relx=0.28, rely=0.25,anchor='w')

label4=Label(home, text="we are committed to safeguarding lives, minimizing damage,",font=('arial',12),bg='yellow',fg='black')
label4.place(relx=0.28, rely=0.29,anchor='w')

label5=Label(home, text="and building a resilient world.",font=('arial',12),bg='yellow',fg='black')
label5.place(relx=0.28, rely=0.33,anchor='w')

label6=Label(home, text="Our Vision:",font=('arial',13,'bold'),bg='yellow',fg='black')
label6.place(relx=0.28, rely=0.40,anchor='w')

label7=Label(home, text="Prevention, Mitigation, Preparedness, and Response:",font=('arial',11,'bold'),bg='yellow',fg='black')
label7.place(relx=0.28, rely=0.44,anchor='w')

label8=Label(home, text="We envision an ethos where all stakeholders work ",font=('arial',12),bg='yellow',fg='black')
label8.place(relx=0.28, rely=0.48,anchor='w')

label9=Label(home, text="together to prevent, mitigate, prepare for and respond ",font=('arial',12),bg='yellow',fg='black')
label9.place(relx=0.28, rely=0.52,anchor='w')

label10=Label(home, text="effectively to disasters.",font=('arial',12),bg='yellow',fg='black')
label10.place(relx=0.28, rely=0.56,anchor='w')

label11=Label(home, text="Technology-Driven Approach:",font=('arial',11,'bold'),bg='yellow',fg='black')
label11.place(relx=0.28, rely=0.60,anchor='w')

label12=Label(home, text="We adopt a technology-driven, multi-hazard, and multi-",font=('arial',12),bg='yellow',fg='black')
label12.place(relx=0.28, rely=0.64,anchor='w')

label12=Label(home, text="sectoral strategy to create a safer and disaster-",font=('arial',12),bg='yellow',fg='black')
label12.place(relx=0.28, rely=0.68,anchor='w')

label13=Label(home, text="resilient World.",font=('arial',12),bg='yellow',fg='black')
label13.place(relx=0.28, rely=0.72,anchor='w')

home.mainloop()
