
from tkinter import *
import linecache
import mysql.connector as sq
from tkinter import *
from tkinter.ttk import Combobox, Treeview
from Loginclass import User
from test import test2
import tkinter as tk

mycon = sq.connect(host="localhost", user="root", passwd='Edgbaston@2019', database="billing",
                   auth_plugin='mysql_native_password')
if mycon.is_connected():
    print("hnksadk")
my = mycon.cursor()


class Mainpage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        billingpagebutton = Button(self, height=20, width=50,command=lambda: [billpagea()], bg='blue', text='billpage')
        billingpagebutton.place(x=100, y=100)
        transhistroybutton = Button(self, height=20, width=50, bg='blue', text='transpage',
                                    command=lambda: [transpagea()])
        transhistroybutton.place(x=300, y=100)
        settingsbutton = Button(self, height=20, width=50, bg='blue',command=lambda:[settingspagea()], text='settings')
        settingsbutton.place(x=600, y=100)

        def billpagea():
            from BIllpage_class import Billpage
            controller.show_frame(Billpage)

        def transpagea():
            a='Admin\n'
            particular_line = linecache.getline('test2.txt', 2)
            if particular_line == a:
                print("h")

                controller.show_frame(Transpage)
                print("admin")
            else:

                controller.show_frame(T2)

        def settingspagea():
            controller.show_frame(Settingpage)


class Transpage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        subframe = Frame(self, bd=10, bg='white')
        subframe.place(x=10, y=200, height=500, width=1500)

        scrollbar_order_x = Scrollbar(subframe, orient=HORIZONTAL)
        scrollbar_order_y = Scrollbar(subframe, orient=VERTICAL)

        order_tabel = Treeview(subframe,
                               columns=("BIll No", "AMOUNT", "DATE OF BILLING"),
                               xscrollcommand=scrollbar_order_x.set,
                               yscrollcommand=scrollbar_order_y.set)

        order_tabel.heading("BIll No", text="BIll No")
        order_tabel.heading("AMOUNT", text="Rate")
        order_tabel.heading("DATE OF BILLING", text="Quantity")

        order_tabel["displaycolumns"] = ("BIll No", "AMOUNT", "DATE OF BILLING")
        order_tabel["show"] = "headings"
        order_tabel.column("AMOUNT", width=200, anchor='center', stretch=NO)
        order_tabel.column("DATE OF BILLING", width=200, anchor='center', stretch=NO)

        scrollbar_order_x.pack(side=BOTTOM, fill=X)
        scrollbar_order_y.pack(side=RIGHT, fill=Y)

        scrollbar_order_x.configure(command=order_tabel.xview)
        scrollbar_order_y.configure(command=order_tabel.yview)

        order_tabel.pack(fill=BOTH, expand=1)

        def datatable():

            a = comboBox.get()

            query = "select * from {tab}".format(tab=a)
            my.execute(query)
            l = []
            c = my.fetchall()
            for i in c:
                l.append(i)
                print(l)
            for j in range(0, len(l)):
                order_tabel.insert("", 'end', text="L1", values=(l[j][0], l[j][1], l[j][2]))

        userquery = 'select username from logindetails'
        my.execute(userquery)
        userfetch = my.fetchall()
        print(userfetch)
        comboBox = Combobox(self, values=userfetch)
        comboBox.place(x=10, y=10)
        buttontoget = Button(self, text='GET', command=lambda: [datatable()])
        buttontoget.place(x=30, y=10)
        bakbuttontranspage = Button(self, text='Back', command=lambda: [transbackpagecm()])
        bakbuttontranspage.place(x=80, y=10)

        def transbackpagecm():
            controller.show_frame(Mainpage)



class T2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        subframe = Frame(self, bd=10, bg='white')
        subframe.place(x=10, y=200, height=500, width=1500)

        scrollbar_order_x = Scrollbar(subframe, orient=HORIZONTAL)
        scrollbar_order_y = Scrollbar(subframe, orient=VERTICAL)

        order_tabel = Treeview(subframe,
                               columns=("BIll No", "AMOUNT", "DATE OF BILLING"),
                               xscrollcommand=scrollbar_order_x.set,
                               yscrollcommand=scrollbar_order_y.set)

        order_tabel.heading("BIll No", text="BIll No")
        order_tabel.heading("AMOUNT", text="Rate")
        order_tabel.heading("DATE OF BILLING", text="Quantity")

        order_tabel["displaycolumns"] = ("BIll No", "AMOUNT", "DATE OF BILLING")
        order_tabel["show"] = "headings"
        order_tabel.column("AMOUNT", width=200, anchor='center', stretch=NO)
        order_tabel.column("DATE OF BILLING", width=200, anchor='center', stretch=NO)

        scrollbar_order_x.pack(side=BOTTOM, fill=X)
        scrollbar_order_y.pack(side=RIGHT, fill=Y)

        scrollbar_order_x.configure(command=order_tabel.xview)
        scrollbar_order_y.configure(command=order_tabel.yview)

        def table():

            sa = self.controller.get_page(User)
            ka = sa.username.get()

            query = "select * from {tab}".format(tab=ka)
            my.execute(query)
            l = []
            c = my.fetchall()
            for w in c:
                l.append(w)
                print(l)
                for j in range(0, len(l)):
                    order_tabel.insert("", 'end', text="L1", values=(l[j][0], l[j][1], l[j][2]))

        order_tabel.pack(fill=BOTH, expand=1)
        buttontoget = Button(self, text='GET', command=lambda: [table()])
        buttontoget.place(x=30, y=10)
        bakbuttontranspage = Button(self, text='Back', command=lambda: [transbackpagecm()])
        bakbuttontranspage.place(x=80, y=10)

        def transbackpagecm():
            controller.show_frame(Mainpage)





class Settingpage(Frame):

    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        testbutton=Button(self,text="Change",height=10, width=20,fg='black',bg='white',command=lambda: [lchange()],font=('Times new roman',22,"bold"))
        testbutton.place(x=60,y=60)
        sett=Button(self,text="BILL",height=10, width=20,fg='black',bg='white',command=lambda: [bill()],font=('Times new roman',22,"bold"))
        sett.place(x=60,y=400)

        window = tk.Frame(self, bg='white')
        window.place(x=500,y=30)

        window.grid_rowconfigure(0, minsize=600)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (Transpage,test2):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame1(Transpage)
        def lchange():
            self.show_frame1(Transpage)        
        def bill():
            a='Admin\n'
            particular_line = linecache.getline('test2.txt', 2)
            if particular_line == a:
                self.show_frame1(test2)
            else:
                print('m')
    def show_frame1(self, page):
        frame = self.frames[page]
        frame.tkraise()
       

 
