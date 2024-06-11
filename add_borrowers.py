from customtkinter import *
from PIL import ImageTk, Image
from main_window import MainWindow
from tkinter import ttk
import sqlite3
import datetime
from datetime import date
import io


class AddBorrowers:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):

        self.left_frame = CTkFrame(self.display_window, fg_color='white', bg_color='gray95', corner_radius=15)
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=(20, 0))
        self.right_frame = CTkFrame(self.display_window, fg_color='white', bg_color='gray95', corner_radius=15)

        self.right_frame.pack(side=LEFT, fill=BOTH, expand=True, pady=(20,0), padx=(0, 20))
        CTkLabel(self.left_frame, text='').pack(padx=250)

        global date_frame
        date_frame = CTkFrame(self.left_frame, bg_color='white', fg_color='white', height=20)
        date_frame.pack(fill=X, padx=20, pady=(0, 10))
        CTkLabel(self.left_frame, bg_color='white', fg_color='white', text="Borrower's Access No",
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=20)
        self.access_entry = CTkEntry(self.left_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                       border_width=1, height=35, text_color='#0C2844', font=('roboto', 15, 'bold'),
                                     placeholder_text_color='gray60', placeholder_text='e.g. 24')
        self.access_entry.pack(fill=X, pady=(0, 10), padx=20)

        self.access_entry.bind('<FocusIn>', lambda event: self.access_entry.configure(border_color='#44aaee'))
        self.access_entry.bind('<FocusOut>', lambda event: self.access_entry.configure(border_color='#4CC053'))
        self.access_entry.bind('<KeyRelease>', self.showing_borrowers_info)

        two_frames_holder = CTkFrame(self.left_frame, fg_color='white', bg_color='white')
        two_frames_holder.pack(fill=BOTH, expand=True, pady=10)

        first_frame = CTkFrame(two_frames_holder, fg_color='white', bg_color='white')
        first_frame.pack(side=LEFT, fill=BOTH, padx=20, pady=(20, 0), expand=True)

        second_frame = CTkFrame(two_frames_holder, fg_color='white', bg_color='white')
        second_frame.pack(side=LEFT, fill=BOTH, padx=(0, 20), pady=(20, 0), expand=True)

        self.date = IntVar()
        self.date.set(1)

        self.date_check_button = CTkCheckBox(date_frame, text_color='black', width=150, text='Use system date',
                                             variable=self.date, font=('roboto', 15),
                                             command=lambda: self.getting_time(None))
        self.date_check_button.pack(side=LEFT)
        CTkLabel(first_frame, bg_color='white', fg_color='white', text='Amount',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.amount_entry = CTkEntry(first_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                       border_width=1, height=35, text_color='#0C2844', font=('roboto', 15, 'bold'))
        self.amount_entry.pack(fill=X, pady=(0, 10))
        self.amount_entry.bind('<FocusIn>', lambda event: self.amount_entry.configure(border_color='#44aaee'))
        self.amount_entry.bind('<FocusOut>', lambda event: self.amount_entry.configure(border_color='#4CC053'))
        self.amount_entry.bind('<KeyRelease>', self.amount_to_borrow)

        CTkLabel(first_frame, bg_color='white', fg_color='white', text='Processing fee',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.processing_entry = CTkEntry(first_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                       border_width=1, height=35, text_color='#0C2844', font=('roboto', 15),
                                       state=DISABLED)
        self.processing_entry.pack(fill=X, pady=(0, 10))

        CTkLabel(first_frame, bg_color='white', fg_color='white', text='Pay back',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.pay_back_entry = CTkEntry(first_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                       border_width=1, height=35, text_color='#0C2844', font=('roboto', 15),
                                       state=DISABLED)
        self.pay_back_entry.pack(fill=X, pady=(0, 10))

        """working on second frame from here"""

        CTkLabel(second_frame, bg_color='white', fg_color='white', text='Interest',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.interest_entry = CTkEntry(second_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                       border_width=1, height=35, text_color='#0C2844', font=('roboto', 15),
                                       state=DISABLED)
        self.interest_entry.pack(fill=X, pady=(0, 10))

        CTkLabel(second_frame, bg_color='white', fg_color='white', text='Daily payment',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.daily_pay_entry = CTkEntry(second_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                       border_width=1, height=35, text_color='#0C2844', font=('roboto', 15),
                                        state=DISABLED)
        self.daily_pay_entry.pack(fill=X, pady=(0, 10))

        CTkLabel(second_frame, bg_color='white', fg_color='white', text='Loan deadline',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.deadline_entry = CTkEntry(second_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                       border_width=1, height=35, text_color='#0C2844', font=('roboto', 15),
                                       )
        self.deadline_entry.pack(fill=X, pady=(0, 10))
        self.deadline_entry.configure(state=DISABLED)

        self.confirm_button = CTkButton(second_frame, bg_color='white', fg_color='#44aaee', hover_color='#2A9AE5',
                                     image=CTkImage(Image.open('icons/save.png'), size=(20, 20)), text_color='white',
                                     text='Confirm loan', font=('roboto', 15),
                                     command=self.submit_loan)
        self.confirm_button.pack(side=RIGHT)
        self.getting_time(None)

        """Working on the left frame with borrowers info"""
        global default_circular_image
        image = Image.open('images/default_photo.png')
        default_circular_image = MainWindow.__new__(MainWindow).make_circular_image(image)
        self.customer_photo_label = CTkLabel(self.right_frame, fg_color='white', bg_color='white', text='',
                                             image=CTkImage(default_circular_image, size=(150, 150)))
        self.customer_photo_label.pack(padx=80, pady=(80, 10))

        self.name = CTkLabel(self.right_frame, bg_color='white', fg_color='white', text="BORROWER'S NAME",
                             text_color='#085f00', font=('roboto', 15, 'bold'))
        self.name.pack(fill=X, padx=20, pady=(0, 5))

        CTkLabel(self.right_frame, bg_color='white', fg_color='white', text='ACCESS NO',
                 text_color='gray50', font=('roboto', 15), justify=LEFT, anchor='w'
                 ).pack(fill=X, padx=20, pady=(5, 0))
        self.access_no = CTkLabel(self.right_frame, bg_color='white', fg_color='white', text='None',
                                   text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w')
        self.access_no.pack(fill=X, padx=20)

        CTkLabel(self.right_frame, bg_color='white', fg_color='white', text='CONTACT',
                 text_color='gray50', font=('roboto', 15), justify=LEFT, anchor='w'
                 ).pack(fill=X, padx=20)

        self.phone = CTkLabel(self.right_frame, bg_color='white', fg_color='white', text='None',
                              text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w')
        self.phone.pack(fill=X, padx=20)

        CTkLabel(self.right_frame, bg_color='white', fg_color='white', text='EMAIL',
                 text_color='gray50', font=('roboto', 15), justify=LEFT, anchor='w'
                 ).pack(fill=X, padx=20)

        self.email = CTkLabel(self.right_frame, bg_color='white', fg_color='white', text='None',
                              text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w')
        self.email.pack(fill=X, padx=20)

    def getting_time(self, event):

        if self.date.get() == 0:
            self.deadline_entry.configure(state=NORMAL)
            self.deadline_entry.delete(0, END)
            self.deadline_entry.insert(0, 'Unknown')
            self.deadline_entry.configure(state=DISABLED)
            self.year_value = StringVar()
            self.year_value.set('2024')
            self.all_years = ['2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034',
                              '2035']
            self.year = CTkComboBox(date_frame, variable=self.year_value, text_color='gray20',
                                    border_color='#44aaee', button_color='#44aaee', width=80,
                                    fg_color='white', values=self.all_years, border_width=1, bg_color='white',
                                    dropdown_fg_color='white', dropdown_hover_color='#DBEAFF',
                                    dropdown_text_color='black', button_hover_color='#DBEAFF', )
            self.year.pack(side=RIGHT)
            self.year.configure(command=lambda event: self.get_loan_deadline(event))

            self.month_value = StringVar()
            self.month_value.set('Jan')
            self.all_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            self.month = CTkComboBox(date_frame, variable=self.month_value, text_color='gray20',
                                     border_color='#44aaee', button_color='#44aaee', width=70,
                                     fg_color='white', values=self.all_months, border_width=1, bg_color='white',
                                     dropdown_fg_color='white', dropdown_hover_color='#DBEAFF',
                                     dropdown_text_color='black', button_hover_color='#DBEAFF', )
            self.month.pack(side=RIGHT, padx=(0, 10))
            self.month.configure(command=lambda event: self.get_loan_deadline(event))

            self.day = CTkEntry(date_frame, bg_color='white', fg_color='white', border_color='#44aaee',
                                border_width=1, width=40, placeholder_text_color='gray20', text_color='black',
                                font=('roboto', 12), placeholder_text='Day')
            self.day.pack(side=RIGHT, padx=10)
            self.day.bind('<FocusIn>', lambda event: self.day.configure(border_color='#1379FF'))
            self.day.bind('<FocusOut>', lambda event: self.day.configure(border_color='#ACD0FF'))
            self.day.bind('<KeyRelease>', self.get_loan_deadline)

        else:
            current_date = datetime.date.today()
            delta = datetime.timedelta(days=30)
            last_date = current_date + delta

            day = last_date.strftime("%d")
            month = last_date.strftime("%b")
            year = last_date.strftime("%Y")

            self.deadline_entry.configure(state=NORMAL)
            self.deadline_entry.delete(0, END)
            self.deadline_entry.insert(0, f'{day}-{month}-{year}')
            self.deadline_entry.configure(state=DISABLED)
            for widget in date_frame.winfo_children()[1::]:
                widget.destroy()

    def get_loan_deadline(self, event):
        try:
            entered_date = f'{self.day.get()}-{self.month_value.get()}-{self.year_value.get()}'

            current_date = datetime.datetime.strptime(entered_date, '%d-%b-%Y')
            delta = datetime.timedelta(days=30)
            # Subtract 30 days from the current date
            new_date = current_date + delta
            # Format the new date
            day = new_date.strftime("%d")
            month = new_date.strftime("%b")
            year = new_date.strftime("%Y")

            self.deadline_entry.configure(state=NORMAL)
            self.deadline_entry.delete(0, END)
            self.deadline_entry.insert(0, f'{day}-{month}-{year}')
            self.deadline_entry.configure(state=DISABLED)

        except ValueError:
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid month day')
            self.day.delete(0, END)
            self.deadline_entry.configure(state=NORMAL)
            self.deadline_entry.delete(0, END)
            self.deadline_entry.insert(0, 'Unknown')
            self.deadline_entry.configure(state=DISABLED)

    def showing_borrowers_info(self, event):
        try:
            if not self.access_entry.get().strip():
                self.customer_photo_label.configure(image=CTkImage(default_circular_image, size=(150, 150)))
                self.name.configure(text="CUSTOMER'S NAME")
                self.access_no.configure(text='None')
                self.phone.configure(text='None')
                self.email.configure(text='None')
                return

            connection = sqlite3.connect('munange.db')
            cursor = connection.cursor()
            query = "SELECT photo, name, customer_id, phone, email FROM customers WHERE customer_id =?"
            customer_id = f'{self.access_entry.get().strip()}'
            cursor.execute(query, (customer_id, ))
            customer_info = cursor.fetchone()
            cursor.close()
            connection.close()

            image = Image.open(io.BytesIO(customer_info[0]))
            customer_image = MainWindow.__new__(MainWindow).make_circular_image(image)
            self.customer_photo_label.configure(image=CTkImage(customer_image, size=(150, 150)))

            self.name.configure(text=f'{customer_info[1]}')
            self.access_no.configure(text=f'{customer_info[2]}')
            self.phone.configure(text=f'{customer_info[3]}')
            self.email.configure(text=f'{customer_info[4]}')

        except TypeError:
            MainWindow.__new__(MainWindow).unsuccessful_information('No customer match this access number')
            self.customer_photo_label.configure(image=CTkImage(default_circular_image, size=(150, 150)))
            self.name.configure(text="CUSTOMER'S NAME")
            self.access_no.configure(text='None')
            self.phone.configure(text='None')
            self.email.configure(text='None')

    def amount_to_borrow(self, event):
        if not self.amount_entry.get().strip():
            interest = ''
            self.interest_entry.configure(state=NORMAL)
            self.interest_entry.delete(0, END)
            self.interest_entry.insert(0, f'{interest}')
            self.interest_entry.configure(state=DISABLED)

            processing_fee = ''
            self.processing_entry.configure(state=NORMAL)
            self.processing_entry.delete(0, END)
            self.processing_entry.insert(0, f'{processing_fee}')
            self.processing_entry.configure(state=DISABLED)

            daily_payment = ''
            self.daily_pay_entry.configure(state=NORMAL)
            self.daily_pay_entry.delete(0, END)
            self.daily_pay_entry.insert(0, f'{daily_payment}')
            self.daily_pay_entry.configure(state=DISABLED)

            pay_back_payment = ''
            self.pay_back_entry.configure(state=NORMAL)
            self.pay_back_entry.delete(0, END)
            self.pay_back_entry.insert(0, f'{pay_back_payment}')
            self.pay_back_entry.configure(state=DISABLED)
            return
        try:
            interest = int(self.amount_entry.get().strip()) * 0.2
            self.interest_entry.configure(state=NORMAL)
            self.interest_entry.delete(0, END)
            self.interest_entry.insert(0, f'{interest}')
            self.interest_entry.configure(state=DISABLED)

            processing_fee = int(self.amount_entry.get().strip()) * 0.05
            self.processing_entry.configure(state=NORMAL)
            self.processing_entry.delete(0, END)
            self.processing_entry.insert(0, f'{processing_fee}')
            self.processing_entry.configure(state=DISABLED)

            daily_payment = (int(self.amount_entry.get().strip()) + interest)/30
            self.daily_pay_entry.configure(state=NORMAL)
            self.daily_pay_entry.delete(0, END)
            self.daily_pay_entry.insert(0, f'{daily_payment}')
            self.daily_pay_entry.configure(state=DISABLED)

            pay_back_payment = int(self.amount_entry.get().strip()) + interest
            self.pay_back_entry.configure(state=NORMAL)
            self.pay_back_entry.delete(0, END)
            self.pay_back_entry.insert(0, f'{pay_back_payment}')
            self.pay_back_entry.configure(state=DISABLED)
        except ValueError:
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid amount')
            interest = ''
            self.interest_entry.configure(state=NORMAL)
            self.interest_entry.delete(0, END)
            self.interest_entry.insert(0, f'{interest}')
            self.interest_entry.configure(state=DISABLED)

            processing_fee = ''
            self.processing_entry.configure(state=NORMAL)
            self.processing_entry.delete(0, END)
            self.processing_entry.insert(0, f'{processing_fee}')
            self.processing_entry.configure(state=DISABLED)

            daily_payment = ''
            self.daily_pay_entry.configure(state=NORMAL)
            self.daily_pay_entry.delete(0, END)
            self.daily_pay_entry.insert(0, f'{daily_payment}')
            self.daily_pay_entry.configure(state=DISABLED)

            pay_back_payment = ''
            self.pay_back_entry.configure(state=NORMAL)
            self.pay_back_entry.delete(0, END)
            self.pay_back_entry.insert(0, f'{pay_back_payment}')
            self.pay_back_entry.configure(state=DISABLED)

    def submit_loan(self):
        if self.date.get() == 1:
            time_method = datetime.datetime(date.today().year, date.today().month, date.today().day)
            day = time_method.strftime("%d")
            month = time_method.strftime("%b")
            year = time_method.strftime("%Y")

            self.date_to_use = f'{day}-{month}-{year}'

        else:
            if self.day.get() == '':
                MainWindow.__new__(MainWindow).unsuccessful_information('Please enter day')
                return
            elif not self.day.get().isdigit():
                MainWindow.__new__(MainWindow).unsuccessful_information('Invalid month day')
                return
            elif int(self.day.get()) not in list(range(1, 32)):
                MainWindow.__new__(MainWindow).unsuccessful_information('Invalid month day')
                return
            elif self.month_value.get() not in self.all_months:
                MainWindow.__new__(MainWindow).unsuccessful_information('Invalid month selected')
                return
            elif not self.year_value.get().isdigit() or len(list(self.year_value.get())) != 4:
                MainWindow.__new__(MainWindow).unsuccessful_information('Invalid year')
                return
            else:
                self.date_to_use = f'{self.day.get()}-{self.month_value.get()}-{self.year_value.get()}'

        if not self.access_entry.get().strip() or not self.amount_entry.get().strip():
            MainWindow.__new__(MainWindow).unsuccessful_information('All fields are required')
            return
        elif not self.access_entry.get().strip().isdigit():
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid access number')
            return
        elif not self.amount_entry.get().strip().strip().isdigit():
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid amount')
            return
        else:
            connection = sqlite3.connect('munange.db')
            cursor = connection.cursor()
            cursor.execute("SELECT customer_id FROM customers")
            ids_of_customers = cursor.fetchall()
            if (int(self.access_entry.get().strip()),) not in ids_of_customers:
                MainWindow.__new__(MainWindow).unsuccessful_information('No customer match this access number')
                return

            cursor.execute("SELECT customer_no FROM loans WHERE status='on going'")
            ids_with_loans = cursor.fetchall()
            if (int(self.access_entry.get().strip()),) in ids_with_loans:
                MainWindow.__new__(MainWindow).unsuccessful_information('Borrower has unpaid debt')
                return

            query = "INSERT INTO loans(customer_no, amount, loan_date, loan_deadline) VALUES(?, ?, ?, ?)"
            cursor.execute(query, (self.access_entry.get(), self.amount_entry.get(), self.date_to_use,
                                   self.deadline_entry.get()))
            connection.commit()
            cursor.close()
            connection.close()
            MainWindow.__new__(MainWindow).success_information('Loan successfully processed')
            self.access_entry.delete(0, END)
            self.amount_entry.delete(0, END)
            self.access_entry.focus_set()
            self.showing_borrowers_info(None)
            self.amount_to_borrow(None)















