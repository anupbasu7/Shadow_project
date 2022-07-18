from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import robot
# from tkinter import filedialog



class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("900x600+100+50")
        self.root.resizable(False, False)
        # Background_Image
        self.bg = ImageTk.PhotoImage(file="Interface/Images/ltts.jpg")
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Login_Frame

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=120, y=120,height=340, width=500)

        Label(Frame_login, text="Login Here", font=("Impact", 30, "bold"), fg="#d77337", bg="white").place(x=90, y=30)
        Label(Frame_login, text="Employee User Login Here", font=("Goudy", 10, "bold"), fg="#d25d17", bg="white").place(x=90, y=100)

        Label(Frame_login, text="Username", font=("Goudy", 10, "bold"), fg="gray", bg="white").place(x=90, y=140)
        self.txt_user = Entry(Frame_login, font=("times new roman", 10), bg="lightgray")
        self.txt_user.place(x=90, y=170, width=350, height=35)

        Label(Frame_login, text="Password", font=("Goudy", 10, "bold"), fg="gray", bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 10), bg="lightgray", show="*")
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        Button(Frame_login, text="Forget Password?", cursor="hand2", bg="white", fg="#d77337", bd=0, font=("times new roman", 10)).place(x=90, y=280)
        Button(self.root, command=self.login_function, cursor="hand2", text="Login", fg="white", bg="#d77337", font=("times new roman", 20)).place(x=310, y=440,width=140,height=40)
    def login_function(self):
        if self.txt_pass.get() == "" or self.txt_user.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_pass.get() != "12345678" or self.txt_user.get() != "shadow project":
            messagebox.showerror("Error", "Invalid Username/Password", parent=self.root)
        else:
            # messagebox.showinfo("Welcome", "Login Successful")
            root.title("Automation Test Cases")
            root.geometry("1000x600+100+50")
            root.resizable(True, True)
            # root.state("zoomed")
            root.bg = ImageTk.PhotoImage(file="Interface/Images/background.png")
            Label(root, image=root.bg).place(x=0, y=0, relwidth=1, relheight=1)

            Button(root, text="Test Case1", command=self.Test_Case1, cursor="hand2", bg="white", activebackground='#00ff00', font=("times new roman", 12, "bold")).place(x=120, y=120)
            Button(root, text="Test Case2", command=self.Test_Case2, cursor="hand2", bg="white", activebackground='#00ff00', font=("times new roman", 12, "bold")).place(x=120, y=200)
            Button(root, text="Test Case3", command=self.Test_Case3, cursor="hand2", bg="white", activebackground='#00ff00', font=("times new roman", 12, "bold")).place(x=120, y=280)
    def Test_Case1(self):
        logFile = open('mylog1.txt', 'w')
        robot.run("TestSuite\\Call_suite.robot", stdout=logFile)
        file = open("mylog1.txt")
        read_file = file.read()
        messagebox.showinfo(title="Output_Log",parent=self, message=str(read_file))
    def Test_Case2(self):
        logFile = open('mylog2.txt', 'w')
        robot.run("TestSuite\\Message_automation_suite.robot", stdout=logFile)
        file = open("mylog2.txt")
        read_file = file.read()
        messagebox.showinfo(title="Output_Log",parent=root, message=str(read_file))
    def Test_Case3(self):
        logFile = open('mylog3.txt', 'w')
        robot.run("TestSuite\\Message_automation_suite.robot", stdout=logFile)
        file = open("mylog3.txt")
        read_file = file.read()
        messagebox.showinfo(title="Output_Log",parent=root, message=str(read_file))
root = Tk()
obj = Login(root)
root.mainloop()