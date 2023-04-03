from passlib.hash import sha256_crypt
from tkinter import *
import mysql.connector as sq
#
#from PIL import ImageTk, Image

mycon = sq.connect(host="localhost", user="root", passwd='Edgbaston@2019', database="billing",
                   auth_plugin='mysql_native_password')
if mycon.is_connected():
    print("user")
my = mycon.cursor()


class User(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        self.username = StringVar()
        self.password = StringVar()

        Frame.__init__(self, parent)
        canvas_for_image = Canvas(self, height=1500, width=1800, borderwidth=0, highlightthickness=0)
        canvas_for_image.grid(row=0, column=0, sticky='nesw', padx=0, pady=0)


        loginframe = Frame(self, bg='white', bd=10, height=400, width=400)
        loginframe.place(x=500, y=200)

        titleLabel = Label(loginframe, text='BILLzz', fg='black', font=('comic sans', 30))
        titleLabel.place(x=350, y=100)
        usernamelabel = Label(loginframe, text="Username", font=("Arial Bold", 15), bg='ivory')
        usernamelabel.place(x=10, y=10)
        usernameentry = Entry(loginframe, textvariable=self.username, width=30, bd=5)
        usernameentry.place(x=120, y=10)
        passwordlabel = Label(loginframe, text="Password", font=("Arial Bold", 15), bg='ivory')
        passwordlabel.place(x=10, y=60)
        passwordentry = Entry(loginframe, textvariable=self.password, width=30, show='*', bd=5)
        passwordentry.place(x=120, y=60)
        signinbutton = Button(loginframe, text="Signin", command=lambda: [loginfn()], bd=0,
                              font=('arial', 14))
        signinbutton.place(x=100, y=200)
        signupbutton = Button(loginframe, text="Sign Up", command=lambda: [registerfn()], bd=0,
                              font=('arial', 14))
        signupbutton.place(x=180, y=200)

        def loginfn():

            a = self.username.get()
            b = self.password.get()

            encryptenetrdpass = sha256_crypt.hash(b)

            y = 'select password,type from logindetails where username="{}"'.format(a)
            my.execute(y)

            fetchingdata = my.fetchone()
            l = list(fetchingdata)
            print(l)
            for i in fetchingdata:

                if sha256_crypt.verify(i, encryptenetrdpass):
                    print('true')
                    f = open("test2.txt", "w")
                    f.write(a)
                    f.write('\n')
                    for j in l:
                        f.writelines(j)
                        f.write('\n')

                    f.close()
                    from mainpage_class import Mainpage
                    controller.show_frame(Mainpage)


                else:
                    pass

        def registerfn():
            print('a')
            controller.show_frame(Register)


class Register(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        registerframe = Frame(self, bd=10, bg='white', height=1500, width=400)
        registerframe.place(x=200, y=200)
        rusername = StringVar()
        rpassword = StringVar()
        adminon = IntVar()

        usernamelabel = Label(registerframe, text="Username", font=("Arial Bold", 15), bg='ivory')
        usernamelabel.place(x=10, y=10)
        usernameentry = Entry(registerframe, textvariable=rusername, width=30, bd=5)
        usernameentry.place(x=120, y=10)
        passwordlabel = Label(registerframe, text="Password", font=("Arial Bold", 15), bg='ivory')
        passwordlabel.place(x=10, y=60)
        passwordentry = Entry(registerframe, textvariable=rpassword, width=30, show='*', bd=5)
        passwordentry.place(x=120, y=60)
        createbutton = Button(registerframe, text="Create", command=lambda: [createaccount()], bd=0, font=('arial', 14))
        createbutton.place(x=180, y=200)
        adminonbutton = Checkbutton(registerframe, text='Admin', variable=adminon, onvalue=1, offvalue=0, bg='white')
        adminonbutton.place(x=10, y=200)

        def createaccount():
            type1 = 'Standard'
            if adminon.get() == 1:
                type1 = 'Admin'
            sqlinsert = "insert into logindetails values('{}','{}','{}')".format(rusername.get(), rpassword.get(),
                                                                                 type1)
            my.execute(sqlinsert)
            mycon.commit()
            print('ínserted')
            controller.show_frame(User)
