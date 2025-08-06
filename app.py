from tkinter import ttk
import time
from tkinter import*
from tkinter import messagebox
import csv
import os

CREDENTIALS_FILE = "credentials.txt"

# Create the file with default credentials if it doesn't exist
if not os.path.exists(CREDENTIALS_FILE):
    with open(CREDENTIALS_FILE, "w") as f:
        f.write("admin,1234\n")


def main():
    root = Tk()
    LoginPage(root)
    root.mainloop()

class LoginPage:
    def change_password_window(self):
        self.pass_window = Toplevel(self.win)
        self.pass_window.title("Change Password")
        self.pass_window.geometry("600x200")
        self.pass_window.configure(bg="cyan4")

        Label(self.pass_window, text="Username:", font=("verdana", 12, "bold italic"), bg="cyan4", fg="white").grid(row=0, column=0, sticky=W)
        Label(self.pass_window, text=" ", bg="cyan4").grid(row=0, column=1)
        current_user = Entry(self.pass_window, highlightthickness=10)
        current_user.grid(row=0, column=2)

        Label(self.pass_window, text="Current Password:", font=("verdana", 12, "bold italic"), bg="cyan4", fg="white").grid(row=1, column=0, sticky=W)
        Label(self.pass_window, text=" ", bg="cyan4").grid(row=1, column=1)
        current_pass = Entry(self.pass_window, show="*", highlightthickness=10)
        current_pass.grid(row=1, column=2)

        Label(self.pass_window, text="New Password:", font=("verdana", 12, "bold italic"), bg="cyan4", fg="white").grid(row=2, column=0, sticky=W)
        Label(self.pass_window, text=" ", bg="cyan4").grid(row=2, column=1)
        new_pass = Entry(self.pass_window, show="*", highlightthickness=10)
        new_pass.grid(row=2, column=2)

        Label(self.pass_window, text="Confirm New Password:", font=("verdana", 12, "bold italic"), bg="cyan4", fg="white").grid(row=3, column=0, sticky=W)
        Label(self.pass_window, text=" ", bg="cyan4").grid(row=3, column=1)
        confirm_pass = Entry(self.pass_window, show="*", highlightthickness=10)
        confirm_pass.grid(row=3, column=2)

        def update_password():
            with open(CREDENTIALS_FILE, "r") as f:
                credentials = f.readline().strip().split(",")

            if current_user.get() != credentials[0] or current_pass.get() != credentials[1]:
                messagebox.showerror("Error", "Incorrect current username or password.")
                return

            if new_pass.get() != confirm_pass.get():
                messagebox.showerror("Error", "New passwords do not match.")
                return

            with open(CREDENTIALS_FILE, "w") as f:
                f.write(f"{current_user.get()},{new_pass.get()}")

            messagebox.showinfo("Success", "Password changed successfully.")
            self.pass_window.destroy()

        Button(self.pass_window, text="Update Password", font=("Arial", 12, "bold"), bg="dodgerblue", fg="white", bd= 5, width=15, command=update_password).grid(row=4, column=1)


    def __init__(self, win):
        self.win = win
        self.win.geometry("800x500+0+0")
        self.win.title("Rent Management System by George Mutinda")

        self.title_label = Label(self.win, text="GASHOKA APARTMENT", font=('Arial', 35, 'bold'),fg='snow',background="lightseagreen",borderwidth=15, relief=RIDGE)
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

            with open(CREDENTIALS_FILE, "r") as f:
                credentials = f.readline().strip().split(",")

            if username.get() == credentials[0] and password.get() == credentials[1]:

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

                    # remove all widgets from login window
                    for widget in self.win.winfo_children():
                        widget.destroy()    
                    
                    # initialize Window2
                    Window2(self.win)

                login_thread = threading.Thread(target=simulate_login_progress)
                login_thread.start()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

        def reset():
            username.set("")
            password.set("")

        self.button_frame=LabelFrame(self.entry_frame, text="Options", font=("Arial", 15), bg="lightgrey", bd=7, relief=GROOVE)
        self.button_frame.place(x=20, y=188, width=700,height=100)

        self.login_btn=Button(self.button_frame, text="Login", font=("Arial", 15),bg="dodgerblue", bd= 5, width=15,command=check_login)
        self.login_btn.grid(row=0, column=0, padx=20, pady=2)

        self.reset_btn=Button(self.button_frame, text="Reset", font=("Arial", 15), bd =5, bg="red", width = 15,command=reset)
        self.reset_btn.grid(row=0, column=2, padx=20, pady=2)

        self.change_pass_btn = Button(self.button_frame, text="Change Password", bd =5, font=("Arial", 15), bg="green", fg="white", command=self.change_password_window, width = 15)
        self.change_pass_btn.grid(row=0, column=1, padx=20)

SAVED_RECORDS_DIR = "Saved Records"
if not os.path.exists(SAVED_RECORDS_DIR):
    os.makedirs(SAVED_RECORDS_DIR)


class Window2:

    #===== Functions ========================================================================================================
    def calculate_month_summary(self):
        month = self.month_combobox.get()
        year = self.year_combobox.get()

        if not month or not year:
            messagebox.showwarning("Missing Date", "Please select both Month and Year.")
            return

        filename = os.path.join(SAVED_RECORDS_DIR, f"{month}_{year}.csv")
        if not os.path.exists(filename):
            messagebox.showerror("File Not Found", f"No data found for {month} {year}.")
            return

        try:
            total_rent = 0.0
            total_water = 0.0
            total_garbage = 0.0

            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    rent = float(row.get("Rent", 0) or 0)
                    water = float(row.get("Water Bill", 0) or 0)
                    garbage = float(row.get("Garbage Fee", 0) or 0)

                    total_rent += rent
                    total_water += water
                    total_garbage += garbage

            grand_total = total_rent + total_water + total_garbage

            # Set values to labels
            self.total_rent_var.set(f"{total_rent:,.2f}")
            self.total_water_var.set(f"{total_water:,.2f}")
            self.total_garbage_var.set(f"{total_garbage:,.2f}")
            self.grand_total_var.set(f"{grand_total:,.2f}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def key_pressed(self, event):
        focused_widget = self.master.focus_get()
        
        # If the focused widget is an Entry but not the calculator display, ignore keypress
        if isinstance(focused_widget, Entry) and focused_widget != self.txtDisplay:
            return

        key = event.char
        if key in '0123456789+-*/':
            self.clickbutton(key)
        elif key == '\r':  # Enter
            self.equals()
        elif key.lower() == 'c':
            self.clearvalue()
        elif event.keysym == 'BackSpace':
            self.operator = self.operator[:-1]
            self.value.set(self.operator)
            self.txtDisplay.delete(0, END)
            self.txtDisplay.insert(END, self.operator)

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

        # Check for empty fields
        entries = [paid_entry, rent_entry, water_entry, garbage_entry, balance_entry, total_entry]
        if any(not entry.get().strip() for entry in entries):
            messagebox.showwarning("Missing Data", "Please fill in all fields before saving.")
            return

        filename = os.path.join(SAVED_RECORDS_DIR, f"{month}_{year}.csv")

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

    def clickbutton(self, value):
        self.operator += str(value)
        self.value.set(self.operator)
        self.txtDisplay.delete(0, END)
        self.txtDisplay.insert(END, self.operator)

    def clearvalue(self):
        self.operator = ""
        self.value.set("")
        self.txtDisplay.delete(0, END)

    def equals(self):
        try:
            expression = self.operator.replace('÷', '/').replace('x', '*')
            result = str(eval(expression))
            self.value.set(result)
            self.txtDisplay.delete(0, END)
            self.txtDisplay.insert(END, result)
            self.operator = result
        except Exception:
            self.value.set("Error")
            self.txtDisplay.delete(0, END)
            self.txtDisplay.insert(END, "Error")
            self.operator = ""


    def __init__(self, master):

        self.master = master
        self.master.bind("<Key>", self.key_pressed)
        self.master.title("Welcome to Gashoka Apartment")
        self.master.geometry("1500x1000+0+0")

        self.operator = ""
        self.value = StringVar()


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
        self.frame.pack(fill=BOTH, expand=True)

        self.title_label = Label(self.frame, text="WELCOME TO GASHOKA APARTMENT", font=('Arial', 30, 'bold'), fg='snow', background="lightseagreen", borderwidth=15, relief=RIDGE)
        self.title_label.pack(side=TOP, fill=X)

        self.month_year_frame = LabelFrame(self.frame, text="Month/Year", font=("Arial", 20, "bold"), bd=5, relief=GROOVE)
        self.month_year_frame.pack(side=TOP, fill=X, expand=True)

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

        # Bottom: Bottom Frame (holds calculator on the right)
        self.bottom_frame = Frame(self.frame)
        self.bottom_frame.pack(side=TOP, fill=BOTH, expand=True)

        #=== Calculator Frame ===================================================================================================
        self.calculator_frame = Frame(self.frame, bd=5, relief=GROOVE, bg="cyan")
        self.calculator_frame.pack(side=RIGHT, fill=Y)

        #=== monthly summery frame ===================================================================================================
        self.monthly_summery_frame = LabelFrame(self.frame, text="Monthly Summary", font=("Arial", 20, "bold"), bd=5, relief=GROOVE, bg="lightSteelBlue2")
        self.monthly_summery_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.total_rent_var = StringVar(value="0.00")
        self.total_water_var = StringVar(value="0.00")
        self.total_garbage_var = StringVar(value="0.00")
        self.grand_total_var = StringVar(value="0.00")

        self.summary_button = Button(self.monthly_summery_frame, text="Monthly Totals", font=("Arial", 12, "bold"), bg="gold", command=self.calculate_month_summary)
        self.summary_button.grid(row=0, column=8, padx=10)

        Label(self.monthly_summery_frame, text="Total Rent:", font=("Arial", 14, "bold")).grid(row=0, column=0, sticky=W, padx=10, pady=5)
        Label(self.monthly_summery_frame, textvariable=self.total_rent_var, font=("Arial", 14)).grid(row=0, column=1, sticky=W)

        Label(self.monthly_summery_frame, text="Total Water Bill:", font=("Arial", 14, "bold")).grid(row=1, column=0, sticky=W, padx=10, pady=5)
        Label(self.monthly_summery_frame, textvariable=self.total_water_var, font=("Arial", 14)).grid(row=1, column=1, sticky=W)

        Label(self.monthly_summery_frame, text="Total Garbage Fee:", font=("Arial", 14, "bold")).grid(row=2, column=0, sticky=W, padx=10, pady=5)
        Label(self.monthly_summery_frame, textvariable=self.total_garbage_var, font=("Arial", 14)).grid(row=2, column=1, sticky=W)

        Label(self.monthly_summery_frame, text="Grand Total:", font=("Arial", 16, "bold"), fg="green").grid(row=3, column=0, sticky=W, padx=10, pady=10)
        Label(self.monthly_summery_frame, textvariable=self.grand_total_var, font=("Arial", 16, "bold"), fg="green").grid(row=3, column=1, sticky=W)

        #==== Bind mouse wheel to canvas scroll =================================================================================
        """def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.canvas.bind_all("<MouseWheel>", _on_mousewheel)"""

        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta / 120)), "units")

        def _bind_to_mousewheel(event):
            self.canvas.bind_all("<MouseWheel>", _on_mousewheel)

        def _unbind_from_mousewheel(event):
            self.canvas.unbind_all("<MouseWheel>")

        # Bind/unbind when cursor enters or leaves the canvas
        self.canvas.bind("<Enter>", _bind_to_mousewheel)
        self.canvas.bind("<Leave>", _unbind_from_mousewheel)


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

        self.calculator_frame.pack(side=RIGHT, fill=Y, expand=False, anchor='n')
        self.calculator_frame.config(width=320)  # or whatever width fits your buttons

        #===== calculator entry =========================================================================================================
        self.txtDisplay = Entry(self.calculator_frame, font="arial 20 bold", justify="right", bd=5, bg="powder blue", textvariable=self.value)
        self.txtDisplay.grid(columnspan=4, sticky="nsew")

        #===== calculator buttons =========================================================================================================
        # 1. Configure grid weights for uniform expansion
        for i in range(5):  # 5 rows (0 to 4)
            self.calculator_frame.grid_columnconfigure(i, weight=1)
        for j in range(4):  # 4 columns (0 to 3)
            self.calculator_frame.grid_rowconfigure(j, weight=1)
        

        # Button Layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
        ]

        for (text, row, col) in buttons:
            if text == "=":
                Button(self.calculator_frame, text=text, padx=30, pady=5, bd=10,
                    font=('arial', 15, 'bold'), bg="green", command=self.equals).grid(row=row, column=col, sticky="nsew")
            elif text == "C":
                Button(self.calculator_frame, text=text, padx=30, pady=5, bd=10,
                    font=('arial', 15, 'bold'), bg="red", command=self.clearvalue).grid(row=row, column=col, sticky="nsew")
            else:
                Button(self.calculator_frame, text=text, padx=30, pady=5, bd=10,
                    font=('arial', 15, 'bold'), command=lambda txt=text: self.clickbutton(txt)).grid(row=row, column=col, sticky="nsew")


if __name__== "__main__":
    main()