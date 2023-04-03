import mysql.connector as sq
import tkinter as tk
from tkinter import *

from Loginclass import User , Register

from mainpage_class import *

from BIllpage_class import Billpage
mycon = sq.connect(host="localhost", user="root", passwd='Edgbaston@2019', database="billing",
                   auth_plugin='mysql_native_password')
if mycon.is_connected():
    print("hnksadk")
my = mycon.cursor()



class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self, bg='white')
        window.pack()

        window.grid_rowconfigure(0, minsize=600)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (User, Register, Mainpage, Billpage, Transpage, Settingpage, T2 ):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(User)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("BIllZ")

    def get_page(self, page_class):
        return self.frames[page_class]


app = Application()
app.maxsize(1530, 800)

app.mainloop()
