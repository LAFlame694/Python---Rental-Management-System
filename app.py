from tkinter import ttk
import time
from tkinter import*
from tkinter import messagebox
import csv
import os

# ==== install rainbow csv later =======

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

    #===== Functions ========================================================================================================
    def clear_entries(self, *entries):
        for entry in entries:
            entry.delete(0, END)

    
    def calculate_total_and_balance(self, rent_entry, water_entry, garbage_entry, paid_entry, total_entry, balance_entry):
        try:
            rent = float(rent_entry.get() or 0)
            water = float(water_entry.get() or 0)
            garbage = float(garbage_entry.get() or 0)
            paid = float(paid_entry.get() or 0)

            total = rent + water + garbage
            balance = paid - total

            total_entry.delete(0, END)
            total_entry.insert(0, f"{total:.2f}")

            balance_entry.delete(0, END)
            balance_entry.insert(0, f"{balance:.2f}")

        except ValueError:
            messagebox.showerror("Invalid input", "Please enter numeric values only.")
        
    def save_record(self, house_number, paid_entry, rent_entry, water_entry, garbage_entry, balance_entry, total_entry):
        month = self.month_combobox.get()
        year = self.year_combobox.get()

        if not month or not year:
            messagebox.showwarning("Missing Date", "Please select both Month and Year.")
            return

        filename = f"{month}_{year}.csv"

        # Create file if not exists and add header
        file_exists = os.path.isfile(filename)

        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["House No.", "Amount Paid", "Rent", "Water Bill", "Garbage Fee", "Balance", "Total"])

            writer.writerow([
                house_number,
                paid_entry.get(),
                rent_entry.get(),
                water_entry.get(),
                garbage_entry.get(),
                balance_entry.get(),
                total_entry.get()
            ])

        messagebox.showinfo("Saved", f"Record for {house_number} saved to {filename}")

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

        #=== Frames =============================================================================================================
        self.frame = Frame(self.master)
        self.frame.pack(fill=X)

        self.month_year_frame = LabelFrame(self.frame, text="Month/Year", font=("Arial", 20, "bold"), bd=5, relief=GROOVE)
        self.month_year_frame.pack(side=TOP, fill=X, expand=False)

        # Set the width of the month_year_frame to accommodate all widgets
        self.month_year_frame.config(width=1500)

        # === Scrollable details_frame setup ==================================================================================
        self.details_frame_container = Frame(self.frame, bd=5, relief=GROOVE)
        self.details_frame_container.pack(side=TOP, fill=BOTH, expand=True)

        #====== Create canvas inside container ==================================================================================
        self.canvas = Canvas(self.details_frame_container)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        #==== Scrollbar for the canvas ==========================================================================================
        self.scrollbar = Scrollbar(self.details_frame_container, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        #==== Configure canvas ==================================================================================================
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        #==== Add a frame inside the canvas to hold the widgets =================================================================
        self.details_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.details_frame, anchor="nw")

        #==== Bind mouse wheel to canvas scroll =================================================================================
        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.canvas.bind_all("<MouseWheel>", _on_mousewheel)

        #=== Top_Labels ==============================================================================================================
        self.month_label = Label(self.month_year_frame, text="Select Month:", font=("Arial", 12, "bold"))
        self.month_label.grid(row=0, column=0)

        self.space = Label(self.month_year_frame, text=" ")
        self.space.grid(row=0, column=2)

        self.year_label = Label(self.month_year_frame, text="Select Year:", font=("Arial", 12, "bold"))
        self.year_label.grid(row=0, column=3)

        #=== Top_Entrys ==============================================================================================================
        self.month_combobox = ttk.Combobox(self.month_year_frame, values=months, font=("Arial", 12))
        self.month_combobox.grid(row=0, column=1)

        self.year_combobox = ttk.Combobox(self.month_year_frame, values=years, font=("Arial", 12))
        self.year_combobox.grid(row=0, column=4)

        #=== Details_Top_Labels ======================================================================================================
        self.bedsitter = Label(self.details_frame, text="House Number", font=("Arial", 12, "bold"))
        self.bedsitter.grid(row=0, column=0)

        self.space1 = Label(self.details_frame, text=" ")
        self.space1.grid(row=0, column=1)

        self.amount_paid = Label(self.details_frame, text="Amount Paid", font=("Arial", 12, "bold"))
        self.amount_paid.grid(row=0, column=2)

        self.space2 = Label(self.details_frame, text=" ")
        self.space2.grid(row=0, column=3)

        self.rent = Label(self.details_frame, text="Rent", font=("Arial", 12, "bold"))
        self.rent.grid(row=0, column=4)

        self.space2 = Label(self.details_frame, text=" ")
        self.space2.grid(row=0, column=5)

        self.water_bill = Label(self.details_frame, text="Water Bill", font=("Arial", 12, "bold"))
        self.water_bill.grid(row=0, column=6)

        self.space3 = Label(self.details_frame, text=" ")
        self.space3.grid(row=0, column=7)

        self.garbage_fee = Label(self.details_frame, text="Garbage Fee", font=("Arial", 12, "bold"))
        self.garbage_fee.grid(row=0, column=8)

        self.space4 = Label(self.details_frame, text=" ")
        self.space4.grid(row=0, column=9)

        self.extra = Label(self.details_frame, text="Balance", font=("Arial", 12, "bold"))
        self.extra.grid(row=0, column=10)

        self.space5 = Label(self.details_frame, text=" ")
        self.space5.grid(row=0, column=11)

        self.extra = Label(self.details_frame, text="Total", font=("Arial", 12, "bold"))
        self.extra.grid(row=0, column=12)

        self.space6 = Label(self.details_frame, text=" ")
        self.space6.grid(row=0, column=13)

        self.space7 = Label(self.details_frame, text=" ")
        self.space7.grid(row=0, column=15)

        self.space8 = Label(self.details_frame, text=" ")
        self.space8.grid(row=0, column=17)

        #=====House_Number_Labels============================================================================================
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

        self.c1 = Label(self.details_frame, text="C1", font=("Arial", 12, "bold"))
        self.c1.grid(row=22, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=23, column=0)

        self.c2 = Label(self.details_frame, text="C2", font=("Arial", 12, "bold"))
        self.c2.grid(row=24, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=25, column=0)

        self.c3 = Label(self.details_frame, text="C3", font=("Arial", 12, "bold"))
        self.c3.grid(row=26, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=27, column=0)

        self.c4 = Label(self.details_frame, text="C4", font=("Arial", 12, "bold"))
        self.c4.grid(row=28, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=29, column=0)

        self.c5 = Label(self.details_frame, text="C5", font=("Arial", 12, "bold"))
        self.c5.grid(row=30, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=31, column=0)

        self.d1 = Label(self.details_frame, text="D1", font=("Arial", 12, "bold"))
        self.d1.grid(row=32, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=33, column=0)

        self.d2 = Label(self.details_frame, text="D2", font=("Arial", 12, "bold"))
        self.d2.grid(row=34, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=35, column=0)

        self.d3 = Label(self.details_frame, text="D3", font=("Arial", 12, "bold"))
        self.d3.grid(row=36, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=37, column=0)

        self.d4 = Label(self.details_frame, text="D4", font=("Arial", 12, "bold"))
        self.d4.grid(row=38, column=0, sticky=W)

        self.space = Label(self.details_frame, text=" ")
        self.space.grid(row=39, column=0)

        self.d5 = Label(self.details_frame, text="D5", font=("Arial", 12, "bold"))
        self.d5.grid(row=40, column=0, sticky=W)

        #=== Amount_Paid_Entry_Fields ======================================================================================================
        self.a1_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a1_entry.grid(row=2, column=2)

        self.a2_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a2_entry.grid(row=4, column=2)

        self.a3_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a3_entry.grid(row=6, column=2)

        self.a4_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a4_entry.grid(row=8, column=2)

        self.a5_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a5_entry.grid(row=10, column=2)

        self.b1_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b1_entry.grid(row=12, column=2)

        self.b2_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b2_entry.grid(row=14, column=2)

        self.b3_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b3_entry.grid(row=16, column=2)

        self.b4_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b4_entry.grid(row=18, column=2)

        self.b5_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b5_entry.grid(row=20, column=2)

        self.c1_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c1_entry.grid(row=22, column=2)

        self.c2_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c2_entry.grid(row=24, column=2)

        self.c3_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c3_entry.grid(row=26, column=2)

        self.c4_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c4_entry.grid(row=28, column=2)

        self.c5_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c5_entry.grid(row=30, column=2)

        self.d1_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d1_entry.grid(row=32, column=2)

        self.d2_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d2_entry.grid(row=34, column=2)

        self.d3_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d3_entry.grid(row=36, column=2)

        self.d4_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d4_entry.grid(row=38, column=2)

        self.d5_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d5_entry.grid(row=40, column=2)

        #=== Rent_Entry_Fields ======================================================================================================
        self.a1_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a1_rent_entry.grid(row=2, column=4)

        self.a2_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a2_rent_entry.grid(row=4, column=4)

        self.a3_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a3_rent_entry.grid(row=6, column=4)

        self.a4_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a4_rent_entry.grid(row=8, column=4)

        self.a5_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a5_rent_entry.grid(row=10, column=4)

        self.b1_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b1_rent_entry.grid(row=12, column=4)

        self.b2_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b2_rent_entry.grid(row=14, column=4)

        self.b3_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b3_rent_entry.grid(row=16, column=4)

        self.b4_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b4_rent_entry.grid(row=18, column=4)

        self.b5_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b5_rent_entry.grid(row=20, column=4)

        self.c1_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c1_rent_entry.grid(row=22, column=4)

        self.c2_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c2_rent_entry.grid(row=24, column=4)

        self.c3_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c3_rent_entry.grid(row=26, column=4)

        self.c4_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c4_rent_entry.grid(row=28, column=4)

        self.c5_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c5_rent_entry.grid(row=30, column=4)

        self.d1_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d1_rent_entry.grid(row=32, column=4)

        self.d2_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d2_rent_entry.grid(row=34, column=4)

        self.d3_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d3_rent_entry.grid(row=36, column=4)

        self.d4_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d4_rent_entry.grid(row=38, column=4)

        self.d5_rent_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d5_rent_entry.grid(row=40, column=4)

        #===Water_Bill_Entry_Fields======================================================================================================
        self.a1_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a1_waterbill_entry.grid(row=2, column=6)

        self.a2_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a2_waterbill_entry.grid(row=4, column=6)

        self.a3_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a3_waterbill_entry.grid(row=6, column=6)

        self.a4_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a4_waterbill_entry.grid(row=8, column=6)

        self.a5_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a5_waterbill_entry.grid(row=10, column=6)

        self.b1_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b1_waterbill_entry.grid(row=12, column=6)

        self.b2_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b2_waterbill_entry.grid(row=14, column=6)

        self.b3_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b3_waterbill_entry.grid(row=16, column=6)

        self.b4_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b4_waterbill_entry.grid(row=18, column=6)

        self.b5_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b5_waterbill_entry.grid(row=20, column=6)

        self.c1_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c1_waterbill_entry.grid(row=22, column=6)

        self.c2_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c2_waterbill_entry.grid(row=24, column=6)

        self.c3_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c3_waterbill_entry.grid(row=26, column=6)

        self.c4_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c4_waterbill_entry.grid(row=28, column=6)

        self.c5_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")  
        self.c5_waterbill_entry.grid(row=30, column=6)

        self.d1_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d1_waterbill_entry.grid(row=32, column=6)

        self.d2_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d2_waterbill_entry.grid(row=34, column=6)

        self.d3_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d3_waterbill_entry.grid(row=36, column=6)

        self.d4_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d4_waterbill_entry.grid(row=38, column=6)

        self.d5_waterbill_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d5_waterbill_entry.grid(row=40, column=6)

        #=== Garbage_Fee_Entry_Fields ======================================================================================================
        self.a1_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a1_garbagefee_entry.grid(row=2, column=8)

        self.a2_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a2_garbagefee_entry.grid(row=4, column=8)

        self.a3_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a3_garbagefee_entry.grid(row=6, column=8)

        self.a4_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a4_garbagefee_entry.grid(row=8, column=8)

        self.a5_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a5_garbagefee_entry.grid(row=10, column=8)

        self.b1_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b1_garbagefee_entry.grid(row=12, column=8)

        self.b2_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b2_garbagefee_entry.grid(row=14, column=8)

        self.b3_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b3_garbagefee_entry.grid(row=16, column=8)

        self.b4_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b4_garbagefee_entry.grid(row=18, column=8)

        self.b5_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b5_garbagefee_entry.grid(row=20, column=8)

        self.c1_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c1_garbagefee_entry.grid(row=22, column=8)

        self.c2_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c2_garbagefee_entry.grid(row=24, column=8)

        self.c3_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c3_garbagefee_entry.grid(row=26, column=8)

        self.c4_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c4_garbagefee_entry.grid(row=28, column=8)

        self.c5_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c5_garbagefee_entry.grid(row=30, column=8)

        self.d1_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d1_garbagefee_entry.grid(row=32, column=8)

        self.d2_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d2_garbagefee_entry.grid(row=34, column=8)

        self.d3_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d3_garbagefee_entry.grid(row=36, column=8)

        self.d4_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d4_garbagefee_entry.grid(row=38, column=8)

        self.d5_garbagefee_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d5_garbagefee_entry.grid(row=40, column=8)

        #=== Balance_Entry_Fields ======================================================================================================
        self.a1_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a1_balance_entry.grid(row=2, column=10)

        self.a2_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a2_balance_entry.grid(row=4, column=10)

        self.a3_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a3_balance_entry.grid(row=6, column=10)

        self.a4_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a4_balance_entry.grid(row=8, column=10)

        self.a5_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a5_balance_entry.grid(row=10, column=10)

        self.b1_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b1_balance_entry.grid(row=12, column=10)

        self.b2_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b2_balance_entry.grid(row=14, column=10)

        self.b3_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b3_balance_entry.grid(row=16, column=10)

        self.b4_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b4_balance_entry.grid(row=18, column=10)

        self.b5_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b5_balance_entry.grid(row=20, column=10)

        self.c1_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c1_balance_entry.grid(row=22, column=10)

        self.c2_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c2_balance_entry.grid(row=24, column=10)

        self.c3_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c3_balance_entry.grid(row=26, column=10)

        self.c4_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c4_balance_entry.grid(row=28, column=10)

        self.c5_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c5_balance_entry.grid(row=30, column=10)

        self.d1_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d1_balance_entry.grid(row=32, column=10)

        self.d2_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d2_balance_entry.grid(row=34, column=10)

        self.d3_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d3_balance_entry.grid(row=36, column=10)

        self.d4_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d4_balance_entry.grid(row=38, column=10)

        self.d5_balance_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d5_balance_entry.grid(row=40, column=10)

        #=== Totals_Entry_Fields ======================================================================================================
        self.a1_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a1_total_entry.grid(row=2, column=12)

        self.a2_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a2_total_entry.grid(row=4, column=12)

        self.a3_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a3_total_entry.grid(row=6, column=12)

        self.a4_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a4_total_entry.grid(row=8, column=12)

        self.a5_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.a5_total_entry.grid(row=10, column=12)

        self.b1_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b1_total_entry.grid(row=12, column=12)

        self.b2_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b2_total_entry.grid(row=14, column=12)

        self.b3_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b3_total_entry.grid(row=16, column=12)

        self.b4_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b4_total_entry.grid(row=18, column=12)

        self.b5_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.b5_total_entry.grid(row=20, column=12)

        self.c1_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c1_total_entry.grid(row=22, column=12)

        self.c2_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c2_total_entry.grid(row=24, column=12)

        self.c3_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c3_total_entry.grid(row=26, column=12)

        self.c4_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c4_total_entry.grid(row=28, column=12)

        self.c5_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.c5_total_entry.grid(row=30, column=12)

        self.d1_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d1_total_entry.grid(row=32, column=12)

        self.d2_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d2_total_entry.grid(row=34, column=12)

        self.d3_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d3_total_entry.grid(row=36, column=12)

        self.d4_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d4_total_entry.grid(row=38, column=12)

        self.d5_total_entry = Entry(self.details_frame, font=("Arial", 12), bd=5, width=15, bg="aqua")
        self.d5_total_entry.grid(row=40, column=12)

        #===== totals buttons ===============================================================================================
        self.a1_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.a1_total_button.grid(row=2, column=14)

        self.a2_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.a2_total_button.grid(row=4, column=14)

        self.a3_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.a3_total_button.grid(row=6, column=14)

        self.a4_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.a4_total_button.grid(row=8, column=14)

        self.a5_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.a5_total_button.grid(row=10, column=14)

        self.b1_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.b1_total_button.grid(row=12, column=14)

        self.b2_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.b2_total_button.grid(row=14, column=14)

        self.b3_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.b3_total_button.grid(row=16, column=14)

        self.b4_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.b4_total_button.grid(row=18, column=14)

        self.b5_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.b5_total_button.grid(row=20, column=14)

        self.c1_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.c1_total_button.grid(row=22, column=14)

        self.c2_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.c2_total_button.grid(row=24, column=14)

        self.c3_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.c3_total_button.grid(row=26, column=14)

        self.c4_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.c4_total_button.grid(row=28, column=14)

        self.c5_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.c5_total_button.grid(row=30, column=14)

        self.d1_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.d1_total_button.grid(row=32, column=14)

        self.d2_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.d2_total_button.grid(row=34, column=14)

        self.d3_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.d3_total_button.grid(row=36, column=14)

        self.d4_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.d4_total_button.grid(row=38, column=14)

        self.d5_total_button = Button(self.details_frame, padx=10, pady=2, text="Total", font=("Arial", 10, "bold"), bg="light gray")
        self.d5_total_button.grid(row=40, column=14)

        #===== save record buttons ===============================================================================================
        self.a1_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.a1_saverecord_button.grid(row=2, column=16)

        self.a2_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.a2_saverecord_button.grid(row=4, column=16)

        self.a3_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.a3_saverecord_button.grid(row=6, column=16)

        self.a4_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.a4_saverecord_button.grid(row=8, column=16)

        self.a5_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.a5_saverecord_button.grid(row=10, column=16)

        self.b1_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.b1_saverecord_button.grid(row=12, column=16)

        self.b2_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.b2_saverecord_button.grid(row=14, column=16)

        self.b3_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.b3_saverecord_button.grid(row=16, column=16)

        self.b4_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.b4_saverecord_button.grid(row=18, column=16)

        self.b5_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.b5_saverecord_button.grid(row=20, column=16)

        self.c1_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.c1_saverecord_button.grid(row=22, column=16)

        self.c2_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.c2_saverecord_button.grid(row=24, column=16)

        self.c3_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.c3_saverecord_button.grid(row=26, column=16)

        self.c4_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.c4_saverecord_button.grid(row=28, column=16)

        self.c5_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.c5_saverecord_button.grid(row=30, column=16)

        self.d1_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.d1_saverecord_button.grid(row=32, column=16)

        self.d2_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.d2_saverecord_button.grid(row=34, column=16)

        self.d3_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.d3_saverecord_button.grid(row=36, column=16)

        self.d4_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.d4_saverecord_button.grid(row=38, column=16)

        self.d5_saverecord_button = Button(self.details_frame, padx=10, pady=2, text="Save Record", font=("Arial", 10, "bold"), bg="light gray")
        self.d5_saverecord_button.grid(row=40, column=16)

        # A Block
        self.a1_total_button.config(command=lambda: self.calculate_total_and_balance(self.a1_rent_entry, self.a1_waterbill_entry, self.a1_garbagefee_entry, self.a1_entry, self.a1_total_entry, self.a1_balance_entry))
        self.a2_total_button.config(command=lambda: self.calculate_total_and_balance(self.a2_rent_entry, self.a2_waterbill_entry, self.a2_garbagefee_entry, self.a2_entry, self.a2_total_entry, self.a2_balance_entry))
        self.a3_total_button.config(command=lambda: self.calculate_total_and_balance(self.a3_rent_entry, self.a3_waterbill_entry, self.a3_garbagefee_entry, self.a3_entry, self.a3_total_entry, self.a3_balance_entry))
        self.a4_total_button.config(command=lambda: self.calculate_total_and_balance(self.a4_rent_entry, self.a4_waterbill_entry, self.a4_garbagefee_entry, self.a4_entry, self.a4_total_entry, self.a4_balance_entry))
        self.a5_total_button.config(command=lambda: self.calculate_total_and_balance(self.a5_rent_entry, self.a5_waterbill_entry, self.a5_garbagefee_entry, self.a5_entry, self.a5_total_entry, self.a5_balance_entry))

        # B Block
        self.b1_total_button.config(command=lambda: self.calculate_total_and_balance(self.b1_rent_entry, self.b1_waterbill_entry, self.b1_garbagefee_entry, self.b1_entry, self.b1_total_entry, self.b1_balance_entry))
        self.b2_total_button.config(command=lambda: self.calculate_total_and_balance(self.b2_rent_entry, self.b2_waterbill_entry, self.b2_garbagefee_entry, self.b2_entry, self.b2_total_entry, self.b2_balance_entry))
        self.b3_total_button.config(command=lambda: self.calculate_total_and_balance(self.b3_rent_entry, self.b3_waterbill_entry, self.b3_garbagefee_entry, self.b3_entry, self.b3_total_entry, self.b3_balance_entry))
        self.b4_total_button.config(command=lambda: self.calculate_total_and_balance(self.b4_rent_entry, self.b4_waterbill_entry, self.b4_garbagefee_entry, self.b4_entry, self.b4_total_entry, self.b4_balance_entry))
        self.b5_total_button.config(command=lambda: self.calculate_total_and_balance(self.b5_rent_entry, self.b5_waterbill_entry, self.b5_garbagefee_entry, self.b5_entry, self.b5_total_entry, self.b5_balance_entry))

        # C Block
        self.c1_total_button.config(command=lambda: self.calculate_total_and_balance(self.c1_rent_entry, self.c1_waterbill_entry, self.c1_garbagefee_entry, self.c1_entry, self.c1_total_entry, self.c1_balance_entry))
        self.c2_total_button.config(command=lambda: self.calculate_total_and_balance(self.c2_rent_entry, self.c2_waterbill_entry, self.c2_garbagefee_entry, self.c2_entry, self.c2_total_entry, self.c2_balance_entry))
        self.c3_total_button.config(command=lambda: self.calculate_total_and_balance(self.c3_rent_entry, self.c3_waterbill_entry, self.c3_garbagefee_entry, self.c3_entry, self.c3_total_entry, self.c3_balance_entry))
        self.c4_total_button.config(command=lambda: self.calculate_total_and_balance(self.c4_rent_entry, self.c4_waterbill_entry, self.c4_garbagefee_entry, self.c4_entry, self.c4_total_entry, self.c4_balance_entry))
        self.c5_total_button.config(command=lambda: self.calculate_total_and_balance(self.c5_rent_entry, self.c5_waterbill_entry, self.c5_garbagefee_entry, self.c5_entry, self.c5_total_entry, self.c5_balance_entry))

        # D Block
        self.d1_total_button.config(command=lambda: self.calculate_total_and_balance(self.d1_rent_entry, self.d1_waterbill_entry, self.d1_garbagefee_entry, self.d1_entry, self.d1_total_entry, self.d1_balance_entry))
        self.d2_total_button.config(command=lambda: self.calculate_total_and_balance(self.d2_rent_entry, self.d2_waterbill_entry, self.d2_garbagefee_entry, self.d2_entry, self.d2_total_entry, self.d2_balance_entry))
        self.d3_total_button.config(command=lambda: self.calculate_total_and_balance(self.d3_rent_entry, self.d3_waterbill_entry, self.d3_garbagefee_entry, self.d3_entry, self.d3_total_entry, self.d3_balance_entry))
        self.d4_total_button.config(command=lambda: self.calculate_total_and_balance(self.d4_rent_entry, self.d4_waterbill_entry, self.d4_garbagefee_entry, self.d4_entry, self.d4_total_entry, self.d4_balance_entry))
        self.d5_total_button.config(command=lambda: self.calculate_total_and_balance(self.d5_rent_entry, self.d5_waterbill_entry, self.d5_garbagefee_entry, self.d5_entry, self.d5_total_entry, self.d5_balance_entry))

        # A Block
        self.a1_saverecord_button.config(command=lambda: self.save_record("A1", self.a1_entry, self.a1_rent_entry, self.a1_waterbill_entry, self.a1_garbagefee_entry, self.a1_balance_entry, self.a1_total_entry))
        self.a2_saverecord_button.config(command=lambda: self.save_record("A2", self.a2_entry, self.a2_rent_entry, self.a2_waterbill_entry, self.a2_garbagefee_entry, self.a2_balance_entry, self.a2_total_entry))
        self.a3_saverecord_button.config(command=lambda: self.save_record("A3", self.a3_entry, self.a3_rent_entry, self.a3_waterbill_entry, self.a3_garbagefee_entry, self.a3_balance_entry, self.a3_total_entry))
        self.a4_saverecord_button.config(command=lambda: self.save_record("A4", self.a4_entry, self.a4_rent_entry, self.a4_waterbill_entry, self.a4_garbagefee_entry, self.a4_balance_entry, self.a4_total_entry))
        self.a5_saverecord_button.config(command=lambda: self.save_record("A5", self.a5_entry, self.a5_rent_entry, self.a5_waterbill_entry, self.a5_garbagefee_entry, self.a5_balance_entry, self.a5_total_entry))

        # B Block
        self.b1_saverecord_button.config(command=lambda: self.save_record("B1", self.b1_entry, self.b1_rent_entry, self.b1_waterbill_entry, self.b1_garbagefee_entry, self.b1_balance_entry, self.b1_total_entry))
        self.b2_saverecord_button.config(command=lambda: self.save_record("B2", self.b2_entry, self.b2_rent_entry, self.b2_waterbill_entry, self.b2_garbagefee_entry, self.b2_balance_entry, self.b2_total_entry))
        self.b3_saverecord_button.config(command=lambda: self.save_record("B3", self.b3_entry, self.b3_rent_entry, self.b3_waterbill_entry, self.b3_garbagefee_entry, self.b3_balance_entry, self.b3_total_entry))
        self.b4_saverecord_button.config(command=lambda: self.save_record("B4", self.b4_entry, self.b4_rent_entry, self.b4_waterbill_entry, self.b4_garbagefee_entry, self.b4_balance_entry, self.b4_total_entry))
        self.b5_saverecord_button.config(command=lambda: self.save_record("B5", self.b5_entry, self.b5_rent_entry, self.b5_waterbill_entry, self.b5_garbagefee_entry, self.b5_balance_entry, self.b5_total_entry))

        # C Block
        self.c1_saverecord_button.config(command=lambda: self.save_record("C1", self.c1_entry, self.c1_rent_entry, self.c1_waterbill_entry, self.c1_garbagefee_entry, self.c1_balance_entry, self.c1_total_entry))
        self.c2_saverecord_button.config(command=lambda: self.save_record("C2", self.c2_entry, self.c2_rent_entry, self.c2_waterbill_entry, self.c2_garbagefee_entry, self.c2_balance_entry, self.c2_total_entry))
        self.c3_saverecord_button.config(command=lambda: self.save_record("C3", self.c3_entry, self.c3_rent_entry, self.c3_waterbill_entry, self.c3_garbagefee_entry, self.c3_balance_entry, self.c3_total_entry))
        self.c4_saverecord_button.config(command=lambda: self.save_record("C4", self.c4_entry, self.c4_rent_entry, self.c4_waterbill_entry, self.c4_garbagefee_entry, self.c4_balance_entry, self.c4_total_entry))
        self.c5_saverecord_button.config(command=lambda: self.save_record("C5", self.c5_entry, self.c5_rent_entry, self.c5_waterbill_entry, self.c5_garbagefee_entry, self.c5_balance_entry, self.c5_total_entry))

        # D Block
        self.d1_saverecord_button.config(command=lambda: self.save_record("D1", self.d1_entry, self.d1_rent_entry, self.d1_waterbill_entry, self.d1_garbagefee_entry, self.d1_balance_entry, self.d1_total_entry))
        self.d2_saverecord_button.config(command=lambda: self.save_record("D2", self.d2_entry, self.d2_rent_entry, self.d2_waterbill_entry, self.d2_garbagefee_entry, self.d2_balance_entry, self.d2_total_entry))
        self.d3_saverecord_button.config(command=lambda: self.save_record("D3", self.d3_entry, self.d3_rent_entry, self.d3_waterbill_entry, self.d3_garbagefee_entry, self.d3_balance_entry, self.d3_total_entry))
        self.d4_saverecord_button.config(command=lambda: self.save_record("D4", self.d4_entry, self.d4_rent_entry, self.d4_waterbill_entry, self.d4_garbagefee_entry, self.d4_balance_entry, self.d4_total_entry))
        self.d5_saverecord_button.config(command=lambda: self.save_record("D5", self.d5_entry, self.d5_rent_entry, self.d5_waterbill_entry, self.d5_garbagefee_entry, self.d5_balance_entry, self.d5_total_entry))

        # A Block
        self.a1_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.a1_clear_button.grid(row=2, column=18)

        self.a2_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.a2_clear_button.grid(row=4, column=18)

        self.a3_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.a3_clear_button.grid(row=6, column=18)

        self.a4_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.a4_clear_button.grid(row=8, column=18)

        self.a5_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.a5_clear_button.grid(row=10, column=18)

        # B Block
        self.b1_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.b1_clear_button.grid(row=12, column=18)

        self.b2_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.b2_clear_button.grid(row=14, column=18)

        self.b3_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.b3_clear_button.grid(row=16, column=18)

        self.b4_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.b4_clear_button.grid(row=18, column=18)

        self.b5_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.b5_clear_button.grid(row=20, column=18)

        # C Block
        self.c1_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.c1_clear_button.grid(row=22, column=18)

        self.c2_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.c2_clear_button.grid(row=24, column=18)

        self.c3_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.c3_clear_button.grid(row=26, column=18)

        self.c4_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.c4_clear_button.grid(row=28, column=18)

        self.c5_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.c5_clear_button.grid(row=30, column=18)

        # D Block
        self.d1_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.d1_clear_button.grid(row=32, column=18)

        self.d2_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.d2_clear_button.grid(row=34, column=18)

        self.d3_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.d3_clear_button.grid(row=36, column=18)

        self.d4_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.d4_clear_button.grid(row=38, column=18)

        self.d5_clear_button = Button(self.details_frame, padx=10, pady=2, text="Clear", font=("Arial", 10, "bold"), bg="orange")
        self.d5_clear_button.grid(row=40, column=18)

        # A Block
        self.a1_clear_button.config(command=lambda: self.clear_entries(self.a1_entry, self.a1_rent_entry, self.a1_waterbill_entry, self.a1_garbagefee_entry, self.a1_balance_entry, self.a1_total_entry))
        self.a2_clear_button.config(command=lambda: self.clear_entries(self.a2_entry, self.a2_rent_entry, self.a2_waterbill_entry, self.a2_garbagefee_entry, self.a2_balance_entry, self.a2_total_entry))
        self.a3_clear_button.config(command=lambda: self.clear_entries(self.a3_entry, self.a3_rent_entry, self.a3_waterbill_entry, self.a3_garbagefee_entry, self.a3_balance_entry, self.a3_total_entry))
        self.a4_clear_button.config(command=lambda: self.clear_entries(self.a4_entry, self.a4_rent_entry, self.a4_waterbill_entry, self.a4_garbagefee_entry, self.a4_balance_entry, self.a4_total_entry))
        self.a5_clear_button.config(command=lambda: self.clear_entries(self.a5_entry, self.a5_rent_entry, self.a5_waterbill_entry, self.a5_garbagefee_entry, self.a5_balance_entry, self.a5_total_entry))

        # B Block
        self.b1_clear_button.config(command=lambda: self.clear_entries(self.b1_entry, self.b1_rent_entry, self.b1_waterbill_entry, self.b1_garbagefee_entry, self.b1_balance_entry, self.b1_total_entry))
        self.b2_clear_button.config(command=lambda: self.clear_entries(self.b2_entry, self.b2_rent_entry, self.b2_waterbill_entry, self.b2_garbagefee_entry, self.b2_balance_entry, self.b2_total_entry))
        self.b3_clear_button.config(command=lambda: self.clear_entries(self.b3_entry, self.b3_rent_entry, self.b3_waterbill_entry, self.b3_garbagefee_entry, self.b3_balance_entry, self.b3_total_entry))
        self.b4_clear_button.config(command=lambda: self.clear_entries(self.b4_entry, self.b4_rent_entry, self.b4_waterbill_entry, self.b4_garbagefee_entry, self.b4_balance_entry, self.b4_total_entry))
        self.b5_clear_button.config(command=lambda: self.clear_entries(self.b5_entry, self.b5_rent_entry, self.b5_waterbill_entry, self.b5_garbagefee_entry, self.b5_balance_entry, self.b5_total_entry))

        # C Block
        self.c1_clear_button.config(command=lambda: self.clear_entries(self.c1_entry, self.c1_rent_entry, self.c1_waterbill_entry, self.c1_garbagefee_entry, self.c1_balance_entry, self.c1_total_entry))
        self.c2_clear_button.config(command=lambda: self.clear_entries(self.c2_entry, self.c2_rent_entry, self.c2_waterbill_entry, self.c2_garbagefee_entry, self.c2_balance_entry, self.c2_total_entry))
        self.c3_clear_button.config(command=lambda: self.clear_entries(self.c3_entry, self.c3_rent_entry, self.c3_waterbill_entry, self.c3_garbagefee_entry, self.c3_balance_entry, self.c3_total_entry))
        self.c4_clear_button.config(command=lambda: self.clear_entries(self.c4_entry, self.c4_rent_entry, self.c4_waterbill_entry, self.c4_garbagefee_entry, self.c4_balance_entry, self.c4_total_entry))
        self.c5_clear_button.config(command=lambda: self.clear_entries(self.c5_entry, self.c5_rent_entry, self.c5_waterbill_entry, self.c5_garbagefee_entry, self.c5_balance_entry, self.c5_total_entry))

        # D Block
        self.d1_clear_button.config(command=lambda: self.clear_entries(self.d1_entry, self.d1_rent_entry, self.d1_waterbill_entry, self.d1_garbagefee_entry, self.d1_balance_entry, self.d1_total_entry))
        self.d2_clear_button.config(command=lambda: self.clear_entries(self.d2_entry, self.d2_rent_entry, self.d2_waterbill_entry, self.d2_garbagefee_entry, self.d2_balance_entry, self.d2_total_entry))
        self.d3_clear_button.config(command=lambda: self.clear_entries(self.d3_entry, self.d3_rent_entry, self.d3_waterbill_entry, self.d3_garbagefee_entry, self.d3_balance_entry, self.d3_total_entry))
        self.d4_clear_button.config(command=lambda: self.clear_entries(self.d4_entry, self.d4_rent_entry, self.d4_waterbill_entry, self.d4_garbagefee_entry, self.d4_balance_entry, self.d4_total_entry))
        self.d5_clear_button.config(command=lambda: self.clear_entries(self.d5_entry, self.d5_rent_entry, self.d5_waterbill_entry, self.d5_garbagefee_entry, self.d5_balance_entry, self.d5_total_entry))


        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__== "__main__":
    main()