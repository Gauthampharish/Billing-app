import mysql.connector as sq

from tkinter import *
import datetime
from mainpage_class import Mainpage
from tkinter.ttk import Combobox, Treeview
from tkinter import ttk
import datetime
mycon = sq.connect(host="localhost", user="root", passwd='Edgbaston@2019', database="billing",
                   auth_plugin='mysql_native_password')
if mycon.is_connected():
    print("billl")
my = mycon.cursor()
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def __str__(self):
        return self.items

class Billpage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.billnumbervar=IntVar()
        self.productname=StringVar()
        self.mrpvalue=IntVar()
        self.quantity=IntVar()
        self.totalamt=IntVar()
    
        details=Stack()




        promrpframe=Frame(self,bg="white")
        promrpframe.place(x=1, y=1, height=250, width=1000)
        Bill = Label(self, text='Bill Number', fg='Black', bg="white", font=('Times new roman', 22, "bold")).place(
            x=400, y=30)
        date = Label(self, text="hhh", fg='black', bg="white", font=('Times new roman', 20, "bold")).place(x=180, y=30)
        date1 = Label(self, text='Date and Time:', fg='black', bg="white", font=('Times new roman', 22, "bold")).place(
            x=12, y=30)
        billnumber = Entry(self, width=15, textvariable=self.billnumbervar, bg="white", font=('arial', 16)).place(x=600,y=30)


        userquery='select productname from productdetails'
        my.execute(userquery)
        userfetch = my.fetchall()


        nameofpro = Label(self, text='Product', fg='black', bg="white", font=('Times new roman', 30, "bold"))
        nameofpro.place(x=12, y=75)

        quantiylabel = Label(self, text='Quantity', fg='black', bg="white", font=('Times new roman', 30, "bold"))
        quantiylabel.place(x=500, y=75)
        
        comboBox = Combobox(self, values=userfetch)
        comboBox.place(x=5, y=150 , height=30)

        quantityentry = Entry(self, width=15, bg="white", textvariable=self.quantity, font=('arial', 16)).place(x=485, y=150,
                                                                                                           height=30)
        testb = Button(self, text="Add", command=lambda: [tableadd()]).place(x=900, y=30)
        testc=Button(self, text="Delete", command=lambda: [treeviewdelete()]).place(x=900, y=60)
        pay=Button(self,text='Pay',command=lambda:[payfn()]).place(x=900,y=100)
        def payfn():
             if len(details.__str__())>1:
                print("jkggg")
                
                for i in details.__str__():
                   print (i[0], i[1], i[2], i[3])

        def treeviewadd():
          print(len(details.__str__()),"kkl")
          if len(details.__str__())>1:
                print("jkggg")
                order_tabel.delete(*order_tabel.get_children())
                for i in details.__str__():
                    order_tabel.insert("", 'end', values=(i[0], i[1], i[2], i[3]))



          else:
              if len(details.__str__()) ==0:
                  order_tabel.delete(*order_tabel.get_children())
              else:
                for i in details.__str__():

                     print(i,"nj")
                     order_tabel.insert("", 'end', values=(i[0], i[1], i[2], i[3]))

        def treeviewdelete():
            print(len(details.__str__()),"jh")
            print(details.pop())
            print(len(details.__str__()),"jk")
            if len(details.__str__())!=1:
                treeviewadd()
            else:
                order_tabel.delete(*order_tabel.get_children())
                for i in details.__str__():
                    print(i, "nj")
                    order_tabel.insert("", 'end', values=(i[0], i[1], i[2], i[3]))

        def tableadd():
            a = comboBox.get()
            b = self.quantity.get()
            mrpquery = "select mrp from productdetails where productname='{}'".format(a)
            my.execute(mrpquery)
            userfetch = my.fetchone()
            for i in userfetch:
                c=i
            tot = int(b) * int(c)
            l1 = [a, c, b,tot]
            details.push(l1)
            treeviewadd()




        order_frame = Frame(self, bd=8, bg="white")
        order_frame.place(x=12, y=300, height=500, width=1000)




        # Order Tabel

        order_tabel_frame = Frame(order_frame)
        order_tabel_frame.place(x=0, y=0, height=500, width=1000)

        scrollbar_order_x = Scrollbar(order_tabel_frame, orient=HORIZONTAL)
        scrollbar_order_y = Scrollbar(order_tabel_frame, orient=VERTICAL)

        order_tabel = ttk.Treeview(order_tabel_frame,
                                   columns=("name", "rate", "quantity", "Total"), xscrollcommand=scrollbar_order_x.set,
                                   yscrollcommand=scrollbar_order_y.set)

        order_tabel.heading("name", text="Name")
        order_tabel.heading("rate", text="Rate")
        order_tabel.heading("quantity", text="Quantity")
        order_tabel.heading("Total", text="Total")
        order_tabel["displaycolumns"] = ("name", "rate", "quantity", "Total")
        order_tabel["show"] = "headings"
        order_tabel.column("rate", width=200, anchor='center', stretch=NO)
        order_tabel.column("quantity", width=200, anchor='center', stretch=NO)
        order_tabel.column("Total", width=200, anchor='center', stretch=NO)

        scrollbar_order_x.pack(side=BOTTOM, fill=X)
        scrollbar_order_y.pack(side=RIGHT, fill=Y)

        scrollbar_order_x.configure(command=order_tabel.xview)
        scrollbar_order_y.configure(command=order_tabel.yview)

        order_tabel.pack(fill=BOTH, expand=1)




