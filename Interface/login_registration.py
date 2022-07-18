from tkinter import *
from PIL import ImageTk
# import ast
import mysql.connector
import tkinter.messagebox as msg

class User:
    def __init__(self, root):
        self.root=root
        self.root.title("Homepage")
        self.root.geometry("900x750+100+50")
        self.root.configure(bg='#fff')
        self.root.resizable(False, False)
        # self.img = PhotoImage(file="Interface/Images/sign.png", master= self.root)
        self.bg = ImageTk.PhotoImage(file="Interface/Images/ltts.jpg")
        Label(self.root, image=self.bg, border=0, bg='white').place(x=0, y=0)


        # self.bg = ImageTk.PhotoImage(file="Interface/Images/ltts.jpg")
        # Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        title = Label(self.root, text="Welcome to L&T Technology Services Field test tool", bd='5', width="60", fg="#63666A", bg='white', font=("Arial", 18, 'italic','bold'))
        title.pack()

        About_button = Button(self.root, text="About", cursor='hand2', bd="3", height="2", width="10",font=("Microdoft Yahei UI Light", 11), command=self.about)
        About_button.place(x=550, y=60)

        register_button = Button(self.root, text= "Register", cursor='hand2', bd="3", height="2", width="10",font=("Microdoft Yahei UI Light", 11),command=self.register)
        register_button.place(x=670, y=60)

        login_button = Button(self.root, text="Login", cursor='hand2', bd="3", height="2", width="10",font=("Microdoft Yahei UI Light", 11),command=self.login)
        login_button.place(x=790, y=60)


    def register(self):
        window = Tk()
        window.title("SignUp")
        window.geometry("900x750+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)
        self.img = PhotoImage(file="Interface/Images/register.png",master=window)
        Label(window, image=self.img, border=0, bg='white').place(x=70, y=200)

        self.img1 = ImageTk.PhotoImage(file="Interface/Images/LT.jpg",master =window)
        Label(window, image=self.img1, border=0, bg='white').pack()

        frame = Frame(window, width=350, height=390, bg='#fff')
        frame.place(x=480, y=180)

        heading = Label(frame, text="Register", fg="#57a1f8", bg="white", font=("Microdoft Yahei UI Light", 23, 'bold'))
        heading.place(x=100, y=5)

        def on_enter(e):
            self.user.delete(0, 'end')

        def on_leave(e):
            if self.user.get() == '':
                self.user.insert(0, 'Username')

        self.user = Entry(frame, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
        self.user.place(x=80, y=80)
        self.user.insert(0, 'Username')
        self.user.bind("<FocusIn>", on_enter)
        self.user.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=75, y=107)

        ##################################################################
        def on_enter(e):
            self.password.delete(0, 'end')
            self.password.config(show='*')

        def on_leave(e):
            if self.password.get() == '':
                self.password.insert(0, 'Password')

        self.password = Entry(frame,fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
        self.password.place(x=80, y=150)
        self.password.insert(0, 'Password')
        self.password.bind("<FocusIn>", on_enter)
        self.password.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=75, y=177)

        ##############################################################################
        def on_enter(e):
            self.email.delete(0, 'end')

        def on_leave(e):
            if self.email.get() == '':
                self.email.insert(0, 'Email')

        self.email = Entry(frame, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
        self.email.place(x=80, y=220)
        self.email.insert(0, 'Email')
        self.email.bind("<FocusIn>", on_enter)
        self.email.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=75, y=247)

        Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', cursor="hand2", fg='white', border=0, command=self.register_user).place(x=75, y=280)

    def login(self):
        window = Tk()
        window.title("SignIn")
        window.geometry("900x750+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)
        window.img = PhotoImage(file="Interface/Images/login.png", master=window)
        Label(window, image=window.img, border=0, bg='white').place(x=50, y=200)

        self.img1 = ImageTk.PhotoImage(file="Interface/Images/LT.jpg", master=window)
        Label(window, image=self.img1, border=0, bg='white').pack()

        frame = Frame(window, width=350, height=390, bg='#fff')
        frame.place(x=480, y=180)

        heading = Label(frame, text="Login", fg="#57a1f8", bg="white", font=("Microdoft Yahei UI Light", 23, 'bold'))
        heading.place(x=100, y=5)

        def on_enter(e):
            self.user_login.delete(0, 'end')

        def on_leave(e):
            if self.user_login.get() == '':
                self.user_login.insert(0, 'Username')

        self.user_login = Entry(frame, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
        self.user_login.place(x=80, y=80)
        self.user_login.insert(0, 'Username')
        self.user_login.bind("<FocusIn>", on_enter)
        self.user_login.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=75, y=107)

        ##################################################################
        def on_enter(e):
            self.login_password.delete(0, 'end')
            self.login_password.config(show='*')

        def on_leave(e):
            if self.login_password.get() == '':
                self.login_password.insert(0, 'Password')

        self.login_password = Entry(frame, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
        self.login_password.place(x=80, y=150)
        self.login_password.insert(0, 'Password')
        self.login_password.bind("<FocusIn>", on_enter)
        self.login_password.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=75, y=177)

        Button(frame, width=39, pady=7, text='Sign In', bg='#57a1f8', cursor="hand2", fg='white',command=self.login_user, border=0).place(x=75, y=207)

        Button(frame, text="Forget Password?", cursor="hand2", bg="white", fg="#d77337", bd=0,font=("times new roman", 10),command=self.forget_password).place(x=160, y=250)

    def forget_password(self):
        window = Tk()
        window.title("Forget Password")
        window.geometry("900x750+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)
        window.img = PhotoImage(file="Interface/Images/sign.png", master=window)
        Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)

        frame = Frame(window, width=350, height=390, bg='#fff')
        frame.place(x=480, y=70)

        heading = Label(frame, text="Change Password", fg="#57a1f8", bg="white", font=("Microdoft Yahei UI Light", 20, 'bold','italic'))
        heading.place(x=90, y=5)

        def on_enter(e):
            self.email.delete(0, 'end')

        def on_leave(e):
            if self.email.get() == '':
                self.email.insert(0, 'Email')

        self.email = Entry(frame, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
        self.email.place(x=80, y=80)
        self.email.insert(0, 'Email')
        self.email.bind("<FocusIn>", on_enter)
        self.email.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=75, y=107)

        ##################################################################
        def on_enter(e):
            self.New_password.delete(0, 'end')

        def on_leave(e):
            if self.New_password.get() == '':
                self.New_password.insert(0, 'New Password')

        self.New_password = Entry(frame, fg='black', border=0, bg='white', font=("Microdoft Yahei UI Light", 11))
        self.New_password.place(x=80, y=150)
        self.New_password.insert(0, 'New Password')
        self.New_password.bind("<FocusIn>", on_enter)
        self.New_password.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=75, y=177)

        Button(frame, width=39, pady=7, text='Reset Password', bg='#57a1f8', cursor="hand2", fg='white', border=0).place(x=75, y=207)


    def register_user(self):
        mydb = mysql.connector.connect(host='localhost', port='3306',user='root',password='anupbasu1421.',database='register_login')
        mycursor = mydb.cursor()

        username = self.user.get()
        password = self.password.get()
        email = self.email.get()

        mycursor.execute("insert into register values(%s,%s,%s)",(username,password,email))
        mydb.commit()

        msg.showinfo("Registration details","Registered successfully")

    def login_user(self):
        mydb = mysql.connector.connect(host='localhost', port='3306', user='root', password='anupbasu1421.',database='register_login')
        mycursor = mydb.cursor()

        username1 = self.user_login.get()
        password1 = self.login_password.get()

        mycursor.execute("select * from register where username=%s and password=%s",(username1,password1))

        c = 0
        for i in mycursor:
            c=c+1

        if c>=1:
            mycursor.execute("insert into login values(%s,%s)",(username1,password1))
            mydb.commit()
            mycursor.execute(self.field_page())

        else:
            msg.showinfo("login details","Invalid credentials")

    def forget_user(self):
        mydb = mysql.connector.connect(host='localhost', port='3306', user='root', password='anupbasu1421.',database='register_login')
        mycursor = mydb.cursor()

        username2 = self.email.get()
        new_password = self.New_password.get()


    def about(self):
        about = Tk()
        about.title("About")
        about.geometry("900x750+100+50")

    def field_page(self):
        window = Tk()
        window.title("Field Page")
        window.geometry("900x750+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)
        window.img = PhotoImage(file="Interface/Images/sign.png", master=window)
        Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)

        frame = Frame(window, width=350, height=390, bg='#fff')
        frame.place(x=480, y=70)

        heading = Label(frame, text="Field Test Tool", fg="#57a1f8", bg="white", font=("Microdoft Yahei UI Light", 23, 'italic','bold'))
        heading.place(x=100, y=5)

        bt1 = Button(frame, text="Field Test", bg="white", fg='black', bd='5', height="2", width="25", cursor='hand2',font=("Microdoft Yahei UI Light", 11, 'bold'),command=self.field_test)
        bt1.place(x=100, y=90)

        bt2 = Button(frame, text="Check Connected Devices", bg="white", fg='black', bd='5', height="2", width="25", cursor='hand2',font=("Microdoft Yahei UI Light", 11,'bold'))
        bt2.place(x=100, y=160)

        bt3 = Button(frame, text="Reports", bg="white", fg='black', bd='5', height="2", width="25", cursor='hand2',font=("Microdoft Yahei UI Light", 11,'bold'))
        bt3.place(x=100, y=230)

        bt3 = Button(frame, text="Exit", bg="white", fg='black', bd='5', height="2", width="25", cursor='hand2',font=("Microdoft Yahei UI Light", 11,'bold'))
        bt3.place(x=100, y=300)

    def field_test(self):
        window = Tk()
        window.title("Field Page")
        window.geometry("900x750+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)
        window.img = PhotoImage(file="Interface/Images/sign.png", master=window)
        Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)

        frame = Frame(window, width=350, height=390, bg='#fff')
        frame.place(x=480, y=70)

        heading = Label(frame, text="Field Test", fg="#57a1f8", bg="white",font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
        heading.place(x=100, y=5)

        bt1 = Button(frame, text="Create New Field", bg="white", fg='black', bd='3', height="2", width="25", cursor='hand2',font=("Microdoft Yahei UI Light", 11, 'bold'), command=self.field_test)
        bt1.place(x=80, y=90)

        bt2 = Button(frame, text="Check Existing Field", bg="white", fg='black', bd='3', height="2", width="25",cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold'))
        bt2.place(x=80, y=180)

        bt3= Button(frame, text="Back", bg="white", fg='black', bd='3', height="2", width="25",cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold'), command=self.field_page)
        bt3.place(x=80, y=270)


root =Tk()
obj = User(root)
root.mainloop()