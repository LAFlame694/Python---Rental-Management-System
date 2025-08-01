from tkinter import ttk
import time
import tkinter as tk
from tkinter import*
from tkinter import messagebox

def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()

class LoginPage:

    def __init__(self, win):
        self.win = win
        self.win.geometry("800x500+0+0")
        self.win.title("Rent Management System by George Mutinda")

        self.title_label = Label(self.win, text="GASHOKA APARTMENT", font=('Arial', 35, 'bold'),fg='yellow',background="purple",borderwidth=15, relief=RIDGE)
        self.title_label.pack(side=TOP, fill=X)

        self.main_frame=Frame(self.win, background="black", borderwidth=6, relief=GROOVE)
        self.main_frame.place(x =1, y=90, width=800, height=410)

        self.login_lbl=Label(self.main_frame, text="Login", bd=6, relief=GROOVE, anchor=CENTER, bg="lightgrey", font=('sans - serif',25, 'bold'))
        self.login_lbl.pack(side=TOP, fill=X)

        self.entry_frame=LabelFrame(self.main_frame, text="Enter Details", bd=6, relief=GROOVE, bg="lightgrey", font=('sans - serif',18))
        self.entry_frame.pack(fill=BOTH, expand=TRUE)

        self.entus_lbl=Label(self.entry_frame, text="Enter Username: ", font=("sans-serif", 15))
        self.entus_lbl.grid(row= 0, column=0,padx=2,pady=2)

        username = StringVar()
        password = StringVar()

        self.entus_ent = Entry(self.entry_frame, font=('sans-serif',15),bd=6, bg="aqua",textvariable=username,show="")
        self.entus_ent.grid(row=0,column=1,padx=2, pady=2)

        self.entpass_lbl = Label(self.entry_frame, text="Enter Password: ", bg="lightgrey", font=("sans- serif", 15))
        self.entpass_lbl.grid(row=1,column=0,padx=2, pady=2)

        self.entpass_ent = Entry(self.entry_frame, font=('sans-serif', 15), bd=6, bg="aqua",textvariable=password,show="*")
        self.entpass_ent.grid(row = 1, column= 1, padx=2, pady=2)

        def check_login():

            if username.get() == "flame" and password.get() == "1234":
                self.progress_window = Toplevel(self.win)
                self.progress_window.title("Logging In...")
                self.progress_window.geometry("300x100")
                self.progress_bar = ttk.Progressbar(self.progress_window, orient="horizontal", length=200,mode="determinate")
                self.progress_bar.pack(pady=20)

                import threading

                def simulate_login_progress():
                    for i in range(101):
                        self.progress_bar['value'] = i
                        self.progress_window.update_idletasks()
                        time.sleep(0.01)
                    self.progress_window.destroy()
                    self.newwindow = Toplevel(self.win)
                    self.app = Window2(self.newwindow)

                login_thread = threading.Thread(target=simulate_login_progress)
                login_thread.start()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

        def reset():
            username.set("")
            password.set("")

        self.button_frame=LabelFrame(self.entry_frame, text="Options", font=("Arial", 15), bg="lightgrey", bd=7, relief=GROOVE)
        self.button_frame.place(x=20, y=188, width=500,height=100)

        self.login_btn=Button(self.button_frame, text="Login", font=("Arial", 15),bg="blue", bd= 5, width=15,command=check_login)
        self.login_btn.grid(row=0, column=0, padx=20, pady=2)

        self.reset_btn=Button(self.button_frame, text="Reset", font=("Arial", 15), bd =5, bg="red", width = 15,command=reset)
        self.reset_btn.grid(row=0, column=2, padx=20, pady=2)

class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Welcome to Gashoka Apartment")
        self.master.geometry("1500x1200+0+0")

        months = [
            "January", 
            "February", 
            "March", 
            "April", 
            "May", 
            "June", 
            "July", 
            "August", 
            "September",
            "October", 
            "November", 
            "December",
        ]

        years = [
            "2025", 
            "2026", 
            "2027", 
            "2028", 
            "2029", 
            "2030", 
            "2031", 
            "2032", 
            "2033", 
            "2034", 
            "2035", 
            "2036", 
            "2037", 
            "2038", 
            "2039", 
            "2040",
        ]

        #===Frames==============================================================================================================
        self.frame = Frame(self.master)
        self.frame.pack(anchor=W)

        self.month_year_frame = LabelFrame(self.frame, text="Month/Year", font=("Arial", 20, "bold"), bd=5, relief=GROOVE)
        self.month_year_frame.pack(side=TOP, fill=X)

        self.details_frame = Frame(self.frame, bd=5, relief=GROOVE)
        self.details_frame.pack(side=TOP, fill=X)

        #===Top_Labels==============================================================================================================
        self.month_label = Label(self.month_year_frame, text="Select Month:", font=("Arial", 12, "bold"))
        self.month_label.grid(row=0, column=0)

        self.space = Label(self.month_year_frame, text=" ")
        self.space.grid(row=0, column=2)

        self.year_label = Label(self.month_year_frame, text="Select Year:", font=("Arial", 12, "bold"))
        self.year_label.grid(row=0, column=3)

        #===Top_Entrys==============================================================================================================
        self.month_combobox = ttk.Combobox(self.month_year_frame, values=months, font=("Arial", 12))
        self.month_combobox.grid(row=0, column=1)

        self.year_combobox = ttk.Combobox(self.month_year_frame, values=years, font=("Arial", 12))
        self.year_combobox.grid(row=0, column=4)

        #===Details_Top_Labels==============================================================================================================
        self.bedsitter = Label(self.details_frame, text="Bedsitter", font=("Arial", 12, "bold"))
        self.bedsitter.grid(row=0, column=0)

        self.space1 = Label(self.details_frame, text=" ")
        self.space1.grid(row=0, column=1)

        self.rent_paid = Label(self.details_frame, text="Rent Paid", font=("Arial", 12, "bold"))
        self.rent_paid.grid(row=0, column=2)

        self.space2 = Label(self.details_frame, text=" ")
        self.space2.grid(row=0, column=3)

        self.water_bill = Label(self.details_frame, text="Water Bill", font=("Arial", 12, "bold"))
        self.water_bill.grid(row=0, column=4)

        self.space3 = Label(self.details_frame, text=" ")
        self.space3.grid(row=0, column=5)

        self.garbage_fee = Label(self.details_frame, text="Garbage Fee", font=("Arial", 12, "bold"))
        self.garbage_fee.grid(row=0, column=6)

        self.space4 = Label(self.details_frame, text=" ")
        self.space4.grid(row=0, column=7)

        self.extra = Label(self.details_frame, text="Extra", font=("Arial", 12, "bold"))
        self.extra.grid(row=0, column=8)
        
        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=1, column=0)

        self.a1 = Label(self.details_frame, text="A1", font=("Arial", 12, "bold"))
        self.a1.grid(row=2, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=3, column=0)

        self.a2 = Label(self.details_frame, text="A2", font=("Arial", 12, "bold"))
        self.a2.grid(row=4, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=5, column=0)

        self.a3 = Label(self.details_frame, text="A3", font=("Arial", 12, "bold"))
        self.a3.grid(row=6, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=7, column=0)

        self.a4 = Label(self.details_frame, text="A4", font=("Arial", 12, "bold"))
        self.a4.grid(row=8, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=9, column=0)

        self.a5 = Label(self.details_frame, text="A5", font=("Arial", 12, "bold"))
        self.a5.grid(row=10, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=11, column=0)

        self.b1 = Label(self.details_frame, text="B1", font=("Arial", 12, "bold"))
        self.b1.grid(row=12, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=13, column=0)

        self.b2 = Label(self.details_frame, text="B2", font=("Arial", 12, "bold"))
        self.b2.grid(row=14, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=15, column=0)

        self.b3 = Label(self.details_frame, text="B3", font=("Arial", 12, "bold"))
        self.b3.grid(row=16, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=17, column=0)

        self.b4 = Label(self.details_frame, text="B4", font=("Arial", 12, "bold"))
        self.b4.grid(row=18, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=19, column=0)

        self.b5 = Label(self.details_frame, text="B5", font=("Arial", 12, "bold"))
        self.b5.grid(row=20, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=21, column=0)

        self.b5 = Label(self.details_frame, text="C1", font=("Arial", 12, "bold"))
        self.b5.grid(row=22, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=23, column=0)

        self.b5 = Label(self.details_frame, text="C2", font=("Arial", 12, "bold"))
        self.b5.grid(row=24, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=25, column=0)

        self.b5 = Label(self.details_frame, text="C3", font=("Arial", 12, "bold"))
        self.b5.grid(row=26, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=27, column=0)

        self.b5 = Label(self.details_frame, text="C4", font=("Arial", 12, "bold"))
        self.b5.grid(row=28, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=29, column=0)

        self.b5 = Label(self.details_frame, text="C5", font=("Arial", 12, "bold"))
        self.b5.grid(row=30, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=31, column=0)

        self.b5 = Label(self.details_frame, text="D1", font=("Arial", 12, "bold"))
        self.b5.grid(row=32, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=33, column=0)

        self.b5 = Label(self.details_frame, text="D2", font=("Arial", 12, "bold"))
        self.b5.grid(row=34, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=35, column=0)

        self.b5 = Label(self.details_frame, text="D3", font=("Arial", 12, "bold"))
        self.b5.grid(row=36, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=37, column=0)

        self.b5 = Label(self.details_frame, text="D4", font=("Arial", 12, "bold"))
        self.b5.grid(row=38, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=39, column=0)

        self.b5 = Label(self.details_frame, text="D5", font=("Arial", 12, "bold"))
        self.b5.grid(row=40, column=0, sticky=W)

if __name__== "__main__":
    main()