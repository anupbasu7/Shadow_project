from tkinter import *
from PIL import ImageTk
import mysql.connector
import tkinter.messagebox as msg
import ast
from  tkinter import messagebox
import os
import subprocess
import robot
import webbrowser
from tkinter import filedialog
from datetime import date
import shutil

Dict = {1: 'Message_automation_suite.robot', 2: 'Call_suite.robot', 3: 'Calculator_Automate.robot', 4: 'check_IPV6_case.robot', 5:'TC_1_HTTP_Downlink_in_LTE_3G.robot', 6:'TC_6_Message_Automate.robot', 7:'TC_15&16_connection_check.robot'}
list1 = ['1']
today = date.today()
test_run_no = 0
initial_path='E:/LT_Technology_Services/INTERNSHIP/Shadow_project/TestSuite/'
test_sel_by_num=False

###########################################################################
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


##########################################################################

    def second_page(self):
        def op1():
            window.destroy()
            self.field_page()

        def op2():
            window.destroy()
            self.devices_check()

        def op3():
            window.destroy()
            self.login()


        def op4():
            window.destroy()


        def op5():
            window.destroy()

        def reports_check():
            #   window.destroy()
                filename = filedialog.askopenfilename(
                initialdir="E:/LT_Technology_Services/INTERNSHIP/Shadow_project/Reports/",
                title="Select the report file",
                filetypes=(("Text files",
                            "*.txt*"),
                           ("all files",
                            "*.*")))
                webbrowser.open_new_tab(filename)

        window = Tk()
        window.title("Second Page")
        window.geometry("1000x750+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)
        window.img = PhotoImage(file="Interface/Images/sign.png", master=window)
        Label(window, image=window.img, border=0, bg='white').place(x=50, y=60)
        window.img2 = PhotoImage(file="Interface/Images/test_l.png", master=window)
        Label(window, image=window.img2, border=0, bg='white').place(x=50, y=460)
        Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)

        frame = Frame(window, width=350, height=390, bg='#fff')
        frame.place(x=550, y=70)

        heading = Label(frame, text="Field Test Tool", fg="#57a1f8", bg="white",
                        font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
        heading.place(x=40, y=5)

        bt1 = Button(frame, text="Field Test", bg="#014b88", fg='black', bd='5', height="2", width="25", cursor='hand2',
                     font=("Microdoft Yahei UI Light", 11, 'bold'), command=op1)
        bt1.place(x=40, y=90)

        bt2 = Button(frame, text="Check Connected Devices", bg="#014b88", fg='black', bd='5', height="2", width="25",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=op2)
        bt2.place(x=40, y=160)

        bt3 = Button(frame, text="Reports", bg="#014b88", fg='black', bd='5', height="2", width="25", cursor='hand2',
                     font=("Microdoft Yahei UI Light", 11, 'bold'),command=reports_check)
        bt3.place(x=40, y=230)
        bt4 = Button(frame, text="Back", bg="#014b88", fg='black', bd='5', height="2", width="25", cursor='hand2',
                     font=("Microdoft Yahei UI Light", 11, 'bold'), command=op3)
        bt4.place(x=40, y=300)
        # window.mainloop()

    #########



    def field_page(self):
        def op1():
            window.destroy()
            self.create_field()

        def op2():
            window.destroy()
            self.exist_field()


        def op3():
            window.destroy()
            self.second_page()

        window = Tk()
        window.title("Field Page")
        window.geometry("1000x750+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)
        window.img = PhotoImage(file="Interface/Images/sign.png", master=window)
        Label(window, image=window.img, border=0, bg='white').place(x=50, y=60)
        window.img2 = PhotoImage(file="Interface/Images/test_l.png", master=window)
        Label(window, image=window.img2, border=0, bg='white').place(x=50, y=460)
        Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)

        frame = Frame(window, width=350, height=390, bg='#fff')
        frame.place(x=480, y=70)

        heading = Label(frame, text="Field Test Tool", fg="#57a1f8", bg="white",
                        font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
        heading.place(x=40, y=5)

        bt1 = Button(frame, text="Create test run", bg="white", fg='black', bd='5', height="2", width="25", cursor='hand2',
                     font=("Microdoft Yahei UI Light", 11, 'bold'), command=op1)
        bt1.place(x=40, y=90)

        bt2 = Button(frame, text="Check Existing run", bg="#014b88", fg='black', bd='5', height="2", width="25",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=op2)
        bt2.place(x=40, y=160)

        bt3 = Button(frame, text="Back", bg="#014b88", fg='black', bd='5', height="2", width="25")
        bt2 = Button(frame, text="Check Existing run", bg="white", fg='black', bd='5', height="2", width="25",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=op2)
        bt2.place(x=40, y=160)

        bt3 = Button(frame, text="Back", bg="white", fg='black', bd='5', height="2", width="25",cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold'), command=op3)
        bt3.place(x=40, y=230)



    def create_field(self):
        def op1():
            window.destroy()
            self.test_plan()

        def op2():
            window.destroy()
            self.field_page()

        window = Tk()
        window.title("Create Field Page")
        window.geometry("1000x750+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)
        window.img = PhotoImage(file="Interface/Images/sign.png", master=window)
        Label(window, image=window.img, border=0, bg='white').place(x=50, y=60)
        window.img2 = PhotoImage(file="Interface/Images/test_l.png", master=window)
        Label(window, image=window.img2, border=0, bg='white').place(x=50, y=460)
        Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)
        frame = Frame(window, width=350, height=390, bg='#fff')
        frame.place(x=480, y=70)

        heading = Label(frame, text="Enter the details", fg="#57a1f8", bg="white",
                        font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
        heading.place(x=40, y=5)

        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            if user.get() == '':
                user.insert(0, 'Product Version')

        user = Entry(frame, fg='black', width=30, border=0, bg='#57a1f8', font=("Microdoft Yahei UI Light", 11), bd=5, relief='raised')
        user = Entry(frame, fg='black', width=25, border=0, bg='#57a1f8', font=("Microdoft Yahei UI Light", 11))
        user.place(x=40, y=80)
        user.insert(0, 'Product Version')
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)

        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            if user.get() == '':
                user.insert(0, 'OS Type')
        user = Entry(frame, fg='black', width=30, border=0, bg='#57a1f8', font=("Microdoft Yahei UI Light", 11),bd=5, relief='raised')
        user = Entry(frame, fg='black', width=25, border=0, bg='#57a1f8', font=("Microdoft Yahei UI Light", 11))
        user.place(x=40, y=120)
        user.insert(0, 'OS Type')
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)

        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            if user.get() == '':
                user.insert(0, 'Android Version')
        user = Entry(frame, fg='black', border=0, width=30, bg='#57a1f8', font=("Microdoft Yahei UI Light", 11),bd=5, relief='raised')
        user = Entry(frame, fg='black', border=0, width=25, bg='#57a1f8', font=("Microdoft Yahei UI Light", 11))
        user.place(x=40, y=160)
        user.insert(0, 'Android Version')
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)

        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            if user.get() == '':
                user.insert(0, 'H/w type')
        user = Entry(frame, fg='black', border=0, width=30,  bg='#57a1f8', font=("Microdoft Yahei UI Light", 11), bd=5, relief='raised')
        user = Entry(frame, fg='black', border=0, width=25,  bg='#57a1f8', font=("Microdoft Yahei UI Light", 11))
        user.place(x=40, y=200)
        user.insert(0, 'H/W type')
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)
        bt1 = Button(frame, text="Test selector", bg="#014b88", fg='black', bd='5', height="2", width="25", cursor='hand2',
                     font=("Microdoft Yahei UI Light", 11, 'bold'), command=op1)
        bt1.place(x=40, y=240)
        bt2 = Button(frame, text="Back", bg="#014b88", fg='black', bd='5', height="2", width="25", cursor='hand2')
        bt1 = Button(frame, text="Test selector", bg="white", fg='black', bd='5', height="2", width="25", cursor='hand2',
                     font=("Microdoft Yahei UI Light", 11, 'bold'), command=op1)
        bt1.place(x=40, y=240)
        bt2 = Button(frame, text="Back", bg="white", fg='black', bd='5', height="2", width="25", cursor='hand2',
                     font=("Microdoft Yahei UI Light", 11, 'bold'), command=op2)
        bt2.place(x=40, y=320)

        window.mainloop()

    def test_plan(self):

        def test_plan_selector():
            global test_run_no
            test_run_no = test_run_no + 1
            path = filedialog.askdirectory()
            print(path)
            files = os.listdir(path)
            print(files)
            i = 0
            length = len(files)
            while i < length:
                list1.append(files[i])
                i = i + 1


        def select_single_file():
            global test_run_no
            test_run_no = test_run_no + 1
            filename = filedialog.askopenfilename(initialdir="E:/LT_Technology_Services/INTERNSHIP/Shadow_project/TestSuite/",
                                                  title="Select a File",
                                                  filetypes=(("Text files",
                                                              "*.txt*"),
                                                             ("all files",
                                                              "*.*")))

            print(filename)
            list1.append(filename)

        def select_multiple_file():
            global test_run_no
            test_run_no = test_run_no + 1
            messagebox.showinfo("showinfo", "Please press Control to select multiple files")
            filename = filedialog.askopenfilenames(initialdir="E:/LT_Technology_Services/INTERNSHIP/Shadow_project/TestSuite/",
                                                   title="Select a File",
                                                   filetypes=(("Text files",
                                                               "*.txt*"),
                                                              ("all files",
                                                               "*.*")))

            print(filename)
            i = 0
            length = len(filename)
            print(length)
            while i < length:
                print(filename[i])
                list1.append(filename[i])
                i = i + 1

        def test_run():
            if(test_run_no==0):
               messagebox.showinfo("showinfo", "Please select atleast one test file before clicking on run")
               return
            length = len(list1)
            print(length)
            i = 1

            # Iterating using while loop
            while i < length:
                file_exec = list1[i]
                print(file_exec)
                i = i + 1
                messagebox.showinfo("showinfo", "Your selected test case run started")
                logFile = open('mylog.txt', 'w')
                robot.run(file_exec)

                messagebox.showinfo("showinfo", "Your selected test case run has successfully ended")
                # file_exec = file_exec[::-1]
                file_exec = file_exec.split('/')
                print(file_exec)
                report_file = file_exec[-1] + str(today)
                report_file = report_file + '.html'
                print(report_file)
                path = 'E:/LT_Technology_Services/INTERNSHIP/Shadow_project/Reports/TC77_4G LTE Lab_' + str(today)
                isdir = os.path.isdir(path)
                if isdir == False:
                    os.mkdir(path)
                with open('E:/LT_Technology_Services/INTERNSHIP/Shadow_project/report.html', 'r') as firstfile,open(path + '/' + report_file, 'w') as secondfile:
                    for line in firstfile:
                        # write content to second file
                        secondfile.write(line)

        def op1():
            window.destroy()
            self.field_page()

        def test_by_num():
            window.destroy()
            self.test_select_num()

        window = Tk()
        window.title("Create run field Page")
        window.title("Exist Field Page")
        window.geometry("1000x900+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)
        window.img = PhotoImage(file="Interface/Images/sign.png", master=window)
        Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)
        window.img2 = PhotoImage(file="Interface/Images/test2l.png", master=window)
        Label(window, image=window.img2, border=0, bg='white').place(x=80, y=660)
        window.img3 = PhotoImage(file="Interface/Images/test2l.png", master=window)
        Label(window, image=window.img3, border=0, bg='white').place(x=500, y=660)
        frame = Frame(window, width=350, height=550, bg='#fff')
        frame.place(x=480, y=40)
        frame = Frame(window, width=350, height=550, bg='#fff')
        frame.place(x=480, y=70)
        heading = Label(frame, text="Field Test Tool", fg="#57a1f8", bg="white",
                        font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
        heading.place(x=40, y=5)
        bt1 = Button(frame, text="Select single test file run", bg="#014b88", fg='black', bd='5', height="2", width="25", cursor='hand2',
                     font=("Microdoft Yahei UI Light", 11, 'bold'), command=select_single_file)
        bt1.place(x=40, y=90)

        bt2 = Button(frame, text="Select multiple file run", bg="#014b88", fg='black', bd='5', height="2", width="25",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=select_multiple_file)
        bt2.place(x=40, y=160)

        bt3 = Button(frame, text="Select test plan folder", bg="#014b88", fg='black', bd='5', height="2", width="25",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=test_plan_selector)
        bt3.place(x=40, y=240)
        bt3 = Button(frame, text="Select test by number", bg="#014b88", fg='black', bd='5', height="2", width="25")
        bt1 = Button(frame, text="Select single test file run", bg="white", fg='black', bd='5', height="2", width="25", cursor='hand2',
                     font=("Microdoft Yahei UI Light", 11, 'bold'), command=select_single_file)
        bt1.place(x=40, y=90)

        bt2 = Button(frame, text="Select multiple file run", bg="white", fg='black', bd='5', height="2", width="25",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=select_multiple_file)
        bt2.place(x=40, y=160)

        bt3 = Button(frame, text="Select test plan folder", bg="white", fg='black', bd='5', height="2", width="25",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=test_plan_selector)
        bt3.place(x=40, y=240)
        bt3 = Button(frame, text="Select test by number", bg="white", fg='black', bd='5', height="2", width="25",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=test_by_num)
        bt3.place(x=40, y=300)
        bt3 = Button(frame, text="Run", bg="#57a1f8", fg='black', bd='5', height="2", width="25",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=test_run)
        bt3.place(x=40, y=360)
        bt3 = Button(frame, text="Back", bg="#57a1f8", fg='black', bd='5', height="2", width="25",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold'), command=op1)
        bt3.place(x=40, y=420)
        window.mainloop()



    def exist_field(self):
        def status_open():
            window.destroy()
            self.status()
            #os.system('scrcpy')

        def progress():
            subprocess.call(['gnome-terminal'])

        def ret():
            window.destroy()
            self.field_page()

        window = Tk()
        window.title("existing run page")
        window.geometry("1000x800+100+50")
        window.configure(bg='white')
        window.resizable(False, False)

        img = PhotoImage(file="Interface/Images/sign.png",master=window)
        Label(window, image=img, border=0, bg='white').place(x=10, y=80)
        window.img2 = PhotoImage(file='Interface/Images/lt4_2.png', master=window)
        Label(window, image=window.img2, border=0, bg='white').place(x=5, y=550)


        frame = Frame(window, width=800, height=500, bg='white')
        frame.place(x=550, y=70)


        b1 = Button(frame, width=39, height=1, pady=7, text='Completion status', bg='#57a1f8', fg='white', border=2, bd=5,
                    relief='raised', command=progress).place(x=75,y=70)
        b1 = Button(frame, width=39, height=1, pady=7, text='Status', bg='#57a1f8', fg='white', border=2, bd=5,
                    relief='raised', command=status_open).place(x=75, y=150)
        # b3 = Button(frame, width=39, pady=7, text='Reports', bg='#57a1f8', fg='white', border=0).place(x=75, y=250)
        b1 = Button(frame, width=39, pady=2, height=1,  text='Back', bg='#57a1f8', fg='white', border=2, bd=5,
                    relief='raised', command=ret).place(x=75, y=230)

        window.title("Existing")
        window.geometry("1200x900+100+50")
        window.configure(bg='#014b88')
        window.resizable(False, False)

        img = PhotoImage(file="Interface/Images/L&T_Technology_Services_logo.v1.png",master=window)
        Label(window, image=img, border=0, bg='#014b88').place(x=10, y=80)

        frame = Frame(window, width=800, height=500, bg='#014b88')
        frame.place(x=550, y=70)

        heading = Label(frame, text="LTTS Field test tool status", fg="#57a1f8", bg="white", relief='raised',
                        font=("Microdoft Yahei UI Light", 23, 'bold'))
        heading.place(x=60, y=5)
        b1 = Button(frame, width=39, pady=7, text='Completion status', bg='#57a1f8', fg='white', border=2,
                    relief='raised', command=progress).place(x=75,y=70)
        b1 = Button(frame, width=39, pady=7, text='Status', bg='#57a1f8', fg='white', border=2,
                    relief='raised', command=status_open).place(x=75, y=150)
       # b3 = Button(frame, width=39, pady=7, text='Reports', bg='#57a1f8', fg='white', border=0).place(x=75, y=250)
        b1 = Button(frame, width=39, pady=7, text='Back', bg='#57a1f8', fg='white', border=2,
                    relief='raised', command=ret).place(x=75, y=350)

        window.mainloop()


    def devices_check(self):
        def op2():
            t = subprocess.check_output("adb devices", shell=True)
            t = t.decode('utf-8')
            window.destroy()
            op3(t)


        def op3(t):
            def ret_here():
                window.destroy()
                self.devices_check()
            window= Tk()
            window.title("Devices check Page")
            window.geometry("900x600+100+50")
            window.configure(bg='#fff')
            window.resizable(False, False)

            img = PhotoImage(file="Interface/Images/sign.png")
            Label(window, image=img, border=0, bg='#0000CD').place(x=10, y=80)
            l2 = Label(window, text=t, bg="#fff", fg='black', bd='5', relief='raised', borderwidth='5', width="40",
                       height="15", font=("Times New Roman", 13))

            l2.place(x=450,y=80)
            b1 = Button(frame, width=10, pady=7, text='Back', bg='#57a1f8', fg='white', border=0,
                        relief='raised', command=ret_here)
            b1.place(x=300, y=100)
            window.mainloop()

        def ret():
            window.destroy()
            self.second_page()

        window = Tk()
        window.title("Devices Options page")
        window.geometry("900x900+100+50")
        window.geometry("1200x600+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)

        img = PhotoImage(file="Interface/Images/sign.png")
        Label(window, image=img, border=0, bg='#0000CD').place(x=10, y=80)
        window.img2 = PhotoImage(file='Interface/Images/lt4_2.png', master=window)
        Label(window, image=window.img2, border=0, bg='white').place(x=1, y=550)
        frame = Frame(window, width=500, height=500, bg='#fff')
        frame.place(x=400, y=70)

        heading = Label(frame, text="Devices page", fg="#57a1f8", bg="white", relief='raised',
                        font=("Microdoft Yahei UI Light", 23, 'bold'))
        heading.place(x=80, y=5)
        b1 = Button(frame, width=39,height=2, pady=7, text='Check Connected devices', bg='#57a1f8', fg='white', border=0,bd=5, relief='raised', command=op2).place(
            x=75, y=70)
        b1 = Button(frame, width=39, height=2, pady=7, text='Assign new device', bg='#57a1f8', fg='white', border=0,
                    bd=5, relief='raised', command=op2).place(
            x=75, y=150)
        b1 = Button(frame, width=39, height=2, pady=7, text='Back', bg='#57a1f8', fg='white', border=0,
                    bd=5, relief='raised', command=op2).place( x=75, y=250)


        frame = Frame(window, width=500, height=500, bg='#fff')
        frame.place(x=400, y=70)

        heading = Label(frame, text="LTTS Field test tool", fg="#57a1f8", bg="white", relief='raised',
                        font=("Microdoft Yahei UI Light", 23, 'bold'))
        heading.place(x=80, y=5)
        b1 = Button(frame, width=39, pady=7, text='Check Connected devices', bg='#57a1f8', fg='white', border=0, relief='raised', command=op2).place(
            x=75, y=70)
        b2 = Button(frame, width=39, pady=7, text='Assign more devices', bg='#57a1f8', fg='white', border=0).place(x=75, y=150)
        b2 = Button(frame, width=39, pady=7, text='Back', bg='#57a1f8', fg='white', border=0, command=ret).place(x=75,y=250)
        window.mainloop()

    def test_select_num(self):
        def one():
            global test_sel_by_num
            test_sel_by_num=True
            global test_run_no
            test_run_no = test_run_no + 1
            test_var=Dict.get(1)
            test_var = initial_path + test_var
            list1.append(test_var)
        def two():
            global test_sel_by_num
            test_sel_by_num = True
            global test_run_no
            test_run_no = test_run_no + 1
            test_var=Dict.get(2)
            test_var=initial_path+test_var
            list1.append(test_var)
        def three():
            global test_sel_by_num
            test_sel_by_num = True
            global test_run_no
            test_run_no = test_run_no + 1
            test_var=Dict.get(3)
            test_var = initial_path + test_var
            list1.append(test_var)
        def four():
            global test_sel_by_num
            test_sel_by_num = True
            global test_run_no
            test_run_no = test_run_no + 1
            test_var=Dict.get(4)
            test_var = initial_path + test_var
            list1.append(test_var)
        def five():
            global test_sel_by_num
            test_sel_by_num = True
            global test_run_no
            test_run_no = test_run_no + 1
            test_var=Dict.get(5)
            test_var = initial_path + test_var
            list1.append(test_var)
        def six():
            global test_sel_by_num
            test_sel_by_num = True
            global test_run_no
            test_run_no = test_run_no + 1
            test_var = Dict.get(6)
            test_var = initial_path + test_var
            list1.append(test_var)
        def seven():
            global test_sel_by_num
            test_sel_by_num = True
            global test_run_no
            test_run_no = test_run_no + 1
            test_var = Dict.get(7)
            test_var = initial_path + test_var
            list1.append(test_var)
        def op1():
            window.destroy()
            self.test_plan()
        window = Tk()
        window.title("test_run Page")
        window.geometry("1000x900+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)
        window.img = PhotoImage(file="Interface/Images/sign.png", master=window)
        Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)

        frame = Frame(window, width=350, height=550, bg='#fff')
        frame.place(x=480, y=70)

        heading = Label(frame, text="Field Test Tool", fg="#57a1f8", bg="white",
                        font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
        heading.place(x=40, y=5)
        bt1 = Button(frame, text="ONE", bg="white", fg='black', bd='5', height="1", width="10",
                     cursor='hand2',
                     font=("Microdoft Yahei UI Light", 11, 'bold'), command=one)
        bt1.place(x=40, y=90)

        bt2 = Button(frame, text="TWO", bg="white", fg='black', bd='5', height="1", width="10",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=two)
        bt2.place(x=40, y=130)

        bt3 = Button(frame, text="THREE", bg="white", fg='black', bd='5', height="1", width="10",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=three)
        bt3.place(x=40, y=170)
        bt3 = Button(frame, text="FOUR", bg="white", fg='black', bd='5', height="1", width="10",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=four)
        bt3.place(x=40, y=220)
        bt3 = Button(frame, text="FIVE", bg="white", fg='black', bd='5', height="1", width="10",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=five)
        bt3.place(x=40, y=270)
        bt3 = Button(frame, text="SIX", bg="white", fg='black', bd='5', height="1", width="10",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=six)
        bt3.place(x=40, y=320)
        bt3 = Button(frame, text="SEVEN", bg="white", fg='black', bd='5', height="1", width="10",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=seven)
        bt3.place(x=40, y=370)
        bt3 = Button(frame, text="Back", bg="#57a1f8", fg='black', bd='5', height="2", width="25",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold',), command=op1)
        bt3.place(x=40, y=420)
        window.mainloop()

    def status(self):
        def op1():
            window.destroy()
            subprocess.call('scrcpy')
        def op2():
            window.destroy()
            subprocess.call('scrcpy')

        def op3():
            window.destroy()
            subprocess.call('scrcpy')

        def back(self):
            window.destroy()
            self.exist_field()

        window = Tk()
        window.title("Status Page")
        window.geometry("1000x900+100+50")
        window.configure(bg='#fff')
        window.resizable(False, False)
        window.img = PhotoImage(file="Interface/Images/sign.png", master=window)
        Label(window, image=window.img, border=0, bg='white').place(x=50, y=80)
    # <<<<<<< HEAD
        window.img2 = PhotoImage(file='Interface/Images/lt4_2.png', master=window)
        Label(window, image=window.img2, border=0, bg='white').place(x=5, y=650)

        frame = Frame(window, width=450, height=550, bg='#fff')
        frame.place(x=480, y=70)

        heading = Label(frame, text="Ongoing Test runs are:", fg="#57a1f8", bg="white",
                        font=("Microdoft Yahei UI Light", 23, 'italic', 'bold'))
        heading.place(x=40, y=5)
        length=len(list1)
        i=1
        vary=60
        while(i<length):
            str=list1[i].split('/')
            str1=str[-1]
            bt3 = Button(frame, text=str1, bg="#57a1f8", fg='black', bd='5', height="2", width="25",
                         cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold'), command=op1)
            bt3.place(x=40, y=vary)
            i=i+1
            vary=vary+70
        bt3 = Button(frame, text="Back", bg="#57a1f8", fg='black', bd='5', height="2", width="25",
                     cursor='hand2', font=("Microdoft Yahei UI Light", 11, 'bold'), command=back)
        bt3.place(x=40, y=vary)
        window.mainloop()

root =Tk()
obj = User(root)
root.mainloop()