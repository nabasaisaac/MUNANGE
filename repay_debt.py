from customtkinter import *
from PIL import Image
from main_window import MainWindow
import sqlite3
import datetime
from datetime import date, datetime, timedelta
import io
import os
import sys

# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class RepayDebt:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        self.scrollable_frame = CTkScrollableFrame(self.display_window, bg_color='gray95', fg_color='gray95',
                                                   scrollbar_button_color='gray80', scrollbar_button_hover_color='gray85',
                                                   )
        self.scrollable_frame.pack(fill=BOTH, padx=10, expand=True)
        self.repay_frame = CTkFrame(self.scrollable_frame, fg_color='white', bg_color='gray95', corner_radius=15)
        self.repay_frame.pack(pady=(20, 0), fill=Y, expand=True)
        CTkLabel(self.repay_frame, text='').pack(padx=300)

        global date_frame
        date_frame = CTkFrame(self.repay_frame, bg_color='white', fg_color='white', height=20)
        date_frame.pack(fill=X, padx=20, pady=(0, 10))

        self.date = IntVar()
        self.date.set(1)

        self.date_check_button = CTkCheckBox(date_frame, text_color='black', width=150, text='Use system date',
                                             variable=self.date, font=('roboto', 15),
                                             command=lambda: self.getting_time(None))
        self.date_check_button.pack(side=LEFT)

        CTkLabel(self.repay_frame, bg_color='white', fg_color='white', text="Borrower's Access No",
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=20, pady=(10, 0))
        self.access_entry = CTkEntry(self.repay_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                       border_width=1, height=35, text_color='#0C2844', font=('roboto', 15, 'bold'),
                                     placeholder_text_color='gray60', placeholder_text='e.g. 24')
        self.access_entry.pack(fill=X, pady=(0, 10), padx=20)

        self.access_entry.bind('<FocusIn>', lambda event: self.access_entry.configure(border_color='#44aaee'))
        self.access_entry.bind('<FocusOut>', lambda event: self.access_entry.configure(border_color='#4CC053'))
        self.access_entry.bind('<KeyRelease>', self.showing_borrowers_info)

        self.borrower_frame = CTkFrame(self.repay_frame, bg_color='white', fg_color='white', height=20)
        self.borrower_frame.pack(fill=X, padx=20, pady=10)

        CTkLabel(self.borrower_frame, bg_color='white', fg_color='white', text="Borrower's basic information",
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w'
                 ).pack(fill=X, pady=(0, 5))

        photo_frame = CTkFrame(self.borrower_frame, bg_color='white', fg_color='white')
        photo_frame.pack(side=LEFT)

        info_frame = CTkFrame(self.borrower_frame, bg_color='white', fg_color='white')
        info_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(30, 0))

        left_frame = CTkFrame(info_frame, bg_color='white', fg_color='white')
        left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 20))
        right_frame = CTkFrame(info_frame, bg_color='white', fg_color='white')
        right_frame.pack(side=LEFT, fill=BOTH, expand=True)

        global default_circular_image
        image = Image.open(resource_path('images/default_photo.png'))
        default_circular_image = MainWindow.__new__(MainWindow).make_circular_image(image)
        self.customer_photo_label = CTkLabel(photo_frame, fg_color='white', bg_color='white', text='',
                                             image=CTkImage(default_circular_image, size=(120, 120)))
        self.customer_photo_label.pack()

        self.name = CTkLabel(photo_frame, bg_color='white', fg_color='white', text="BORROWER'S NAME",
                        text_color='#085f00', font=('roboto', 15, 'bold'))
        self.name.pack()

        CTkLabel(left_frame, bg_color='white', fg_color='white', text='Loan Date',
                 text_color='#7b809a', font=('roboto', 15), justify=LEFT, anchor='w'
                 ).pack(fill=X)
        self.date_label = CTkLabel(left_frame, bg_color='white', fg_color='white', text='None',
                 text_color='#344767', font=('roboto', 15), justify=LEFT, anchor='w'
                 )
        self.date_label.pack(fill=X, pady=(0, 5))

        CTkLabel(left_frame, bg_color='white', fg_color='white', text='Loan Amount',
                 text_color='#7b809a', font=('roboto', 15), justify=LEFT, anchor='w'
                 ).pack(fill=X)
        self.loan_amount_label = CTkLabel(left_frame, bg_color='white', fg_color='white', text='None',
                 text_color='#344767', font=('roboto', 15), justify=LEFT, anchor='w'
                 )
        self.loan_amount_label.pack(fill=X, pady=(0, 5))

        CTkLabel(left_frame, bg_color='white', fg_color='white', text='Outstanding Balance',
                 text_color='#7b809a', font=('roboto', 15), justify=LEFT, anchor='w'
                 ).pack(fill=X)
        self.balance_label = CTkLabel(left_frame, bg_color='white', fg_color='white', text='None',
                 text_color='red', font=('roboto', 15), justify=LEFT, anchor='w'
                 )
        self.balance_label.pack(fill=X, pady=(0, 5))

        # working on the right widgets
        CTkLabel(right_frame, bg_color='white', fg_color='white', text='Days to Deadline',
                 text_color='#7b809a', font=('roboto', 15), justify=LEFT, anchor='w'
                 ).pack(fill=X)
        self.days_deadline_label = CTkLabel(right_frame, bg_color='white', fg_color='white', text='None',
                 text_color='#344767', font=('roboto', 15), justify=LEFT, anchor='w'
                 )
        self.days_deadline_label.pack(fill=X, pady=(0, 5))

        CTkLabel(right_frame, bg_color='white', fg_color='white', text='Daily Payment',
                 text_color='#7b809a', font=('roboto', 15), justify=LEFT, anchor='w'
                 ).pack(fill=X)
        self.daily_payment_label = CTkLabel(right_frame, bg_color='white', fg_color='white', text='None',
                 text_color='#344767', font=('roboto', 15), justify=LEFT, anchor='w'
                 )
        self.daily_payment_label.pack(fill=X, pady=(0, 5))

        CTkLabel(right_frame, bg_color='white', fg_color='white', text='Missed Days',
                 text_color='#7b809a', font=('roboto', 15), justify=LEFT, anchor='w'
                 ).pack(fill=X)
        self.missed_days_label = CTkLabel(right_frame, bg_color='white', fg_color='white', text='None',
                 text_color='red', font=('roboto', 15), justify=LEFT, anchor='w'
                 )
        self.missed_days_label.pack(fill=X, pady=(0, 5))

        CTkLabel(self.repay_frame, bg_color='white', fg_color='white', text="Amount",
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=20, pady=(10, 0))
        self.amount_entry = CTkEntry(self.repay_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                       border_width=1, height=35, text_color='#0C2844', font=('roboto', 15, 'bold'),
                                     placeholder_text_color='gray60')
        self.amount_entry.pack(fill=X, pady=(0, 10), padx=20)

        self.amount_entry.bind('<FocusIn>', lambda event: self.amount_entry.configure(border_color='#44aaee'))
        self.amount_entry.bind('<FocusOut>', lambda event: self.amount_entry.configure(border_color='#4CC053'))
        self.amount_entry.bind('<Return>', self.confirm_repayment)

        self.confirm_button = CTkButton(self.repay_frame, bg_color='white', fg_color='#44aaee', hover_color='#2A9AE5',
                                     image=CTkImage(Image.open(resource_path('icons/save.png')), size=(20, 20)), text_color='white',
                                     text='Confirm Payment', font=('roboto', 15),
                                     command=lambda: self.confirm_repayment(None))
        self.confirm_button.pack(side=RIGHT, padx=20, pady=(15, 40))

    def getting_time(self, event):

        if self.date.get() == 0:
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

            self.month_value = StringVar()
            self.month_value.set('Jan')
            self.all_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            self.month = CTkComboBox(date_frame, variable=self.month_value, text_color='gray20',
                                     border_color='#44aaee', button_color='#44aaee', width=70,
                                     fg_color='white', values=self.all_months, border_width=1, bg_color='white',
                                     dropdown_fg_color='white', dropdown_hover_color='#DBEAFF',
                                     dropdown_text_color='black', button_hover_color='#DBEAFF', )
            self.month.pack(side=RIGHT, padx=(0, 10))

            self.day = CTkEntry(date_frame, bg_color='white', fg_color='white', border_color='#44aaee',
                                border_width=1, width=40, placeholder_text_color='gray20', text_color='black',
                                font=('roboto', 12), placeholder_text='Day')
            self.day.pack(side=RIGHT, padx=10)
            self.day.bind('<FocusIn>', lambda event: self.day.configure(border_color='#1379FF'))
            self.day.bind('<FocusOut>', lambda event: self.day.configure(border_color='#ACD0FF'))

        else:
            for widget in date_frame.winfo_children()[1::]:
                widget.destroy()

    def showing_borrowers_info(self, event):
        def setting_to_default():
            self.customer_photo_label.configure(image=CTkImage(default_circular_image, size=(120, 120)))
            self.name.configure(text="CUSTOMER'S NAME")
            self.date_label.configure(text="None")
            self.loan_amount_label.configure(text="None")
            self.balance_label.configure(text="None")
            self.days_deadline_label.configure(text="None")
            self.daily_payment_label.configure(text="None")
            self.missed_days_label.configure(text="None")
        try:
            if not self.access_entry.get().strip():
                setting_to_default()
                return

            connection = sqlite3.connect(resource_path('munange.db'))
            cursor = connection.cursor()
            query = ("SELECT customers.photo, customers.name, loans.loan_id, loans.loan_date, loans.amount, "
                     "loans.loan_deadline, loans.balance FROM customers JOIN loans ON customers.customer_id="
                     "loans.customer_no WHERE customer_id=? AND loans.status='on going'")
            customer_id = f'{self.access_entry.get().strip()}'
            cursor.execute(query, (customer_id, ))
            global customer_info, deadline_date
            customer_info = cursor.fetchone()

            cursor.execute("SELECT amount, date FROM payments WHERE payment_id=?", (customer_info[2], ))
            payments_info = cursor.fetchall()
            # working on the days remaining to deadline
            time_method = datetime(date.today().year, date.today().month, date.today().day)
            day = time_method.strftime("%d")
            month = time_method.strftime("%b")
            year = time_method.strftime("%Y")

            current = f'{day}-{month}-{year}'
            deadline = customer_info[5]
            current_date = datetime.strptime(current, '%d-%b-%Y')
            deadline_date = datetime.strptime(deadline, '%d-%b-%Y')
            if current_date >= deadline_date:
                remaining_days = '0'
            else:
                remaining_days = str(deadline_date - current_date).split(',')[0]

            # working_with_getting_missed_days
            loan_date = customer_info[3]

            days_list = []
            if current_date >= deadline_date:
                for day in range(30 - int(remaining_days.split()[0])):
                    loan_taken_date = datetime.strptime(loan_date, '%d-%b-%Y')
                    delta = timedelta(days=1)
                    date_ = loan_taken_date + delta
                    day = date_.strftime("%d")
                    month = date_.strftime("%b")
                    year = date_.strftime("%Y")
                    days_list.append(f'{day}-{month}-{year}')
                    loan_date = f'{day}-{month}-{year}'
            else:
                for day in range(30 - int(remaining_days.split()[0]) - 1):
                    loan_taken_date = datetime.strptime(loan_date, '%d-%b-%Y')
                    delta = timedelta(days=1)
                    date_ = loan_taken_date + delta
                    day = date_.strftime("%d")
                    month = date_.strftime("%b")
                    year = date_.strftime("%Y")
                    days_list.append(f'{day}-{month}-{year}')
                    loan_date = f'{day}-{month}-{year}'

            # print(days_list)
            self.paid_days = []

            try:
                for payment in payments_info:
                    self.paid_days.append(payment[1])
            except IndexError:
                pass

            missed_days = list(days for days in days_list if days not in self.paid_days)

            outstanding_balance = int(customer_info[6])

            self.daily_payment = (int(customer_info[4]) + int(customer_info[4]) * 0.2) / 30
            image = Image.open(io.BytesIO(customer_info[0]))
            customer_image = MainWindow.__new__(MainWindow).make_circular_image(image)
            self.customer_photo_label.configure(image=CTkImage(customer_image, size=(120, 120)))
            self.name.configure(text=f'{customer_info[1]}')
            self.date_label.configure(text=f'{customer_info[3]}')
            self.loan_amount_label.configure(text=f'{customer_info[4]}')
            self.balance_label.configure(text=f'{outstanding_balance}')
            self.daily_payment_label.configure(text=f'{self.daily_payment}')
            if current_date > deadline_date:
                self.days_deadline_label.configure(text=f'Passed deadline')
            else:
                self.days_deadline_label.configure(text=f'{remaining_days}')
            if len(missed_days) == 0:
                self.missed_days_label.configure(text=f'{len(missed_days)}', text_color='#344767')
            else:
                self.missed_days_label.configure(text=f'{len(missed_days)}')
            cursor.close()
            connection.close()

        except TypeError:
            MainWindow.__new__(MainWindow).unsuccessful_information('No borrower match this Access number')
            setting_to_default()

    def confirm_repayment(self, event):
        if self.date.get() == 1:
            time_method = datetime(date.today().year, date.today().month, date.today().day)
            day = time_method.strftime("%d")
            month = time_method.strftime("%b")
            year = time_method.strftime("%Y")

            self.repay_date = f'{day}-{month}-{year}'

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
                self.repay_date = f'{int(self.day.get()):02d}-{self.month_value.get()}-{self.year_value.get()}'
                # print(self.repay_date)
        if not self.access_entry.get().strip() or not self.amount_entry.get().strip():
            MainWindow.__new__(MainWindow).unsuccessful_information('All fields are required')
            return
        elif self.loan_amount_label.cget('text') == 'None':
            MainWindow.__new__(MainWindow).unsuccessful_information('No borrower match this Access number')
            return
        elif not self.amount_entry.get().strip().isdigit():
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid amount')
            return
        elif int(self.amount_entry.get().strip()) > self.daily_payment:
            MainWindow.__new__(MainWindow).unsuccessful_information('Amount exceeds daily payment')
            return
        elif datetime.strptime(self.repay_date, '%d-%b-%Y') > deadline_date:
            MainWindow.__new__(MainWindow).unsuccessful_information('Date is out of loan period')
            return
        elif datetime.strptime(self.repay_date, '%d-%b-%Y') <= datetime.strptime(customer_info[3], '%d-%b-%Y'):
            MainWindow.__new__(MainWindow).unsuccessful_information('Date is out of loan period')
            return
        else:
            connection = sqlite3.connect(resource_path('munange.db'))
            cursor = connection.cursor()

            new_balance = int(customer_info[6]) - int(self.amount_entry.get().strip())
            if self.repay_date in self.paid_days:
                cursor.execute('SELECT amount FROM payments WHERE payment_id=? AND date=?',
                               (customer_info[2], self.repay_date))
                amount_that_day = int(cursor.fetchone()[0])

                new_amount_that_day = amount_that_day + int(self.amount_entry.get().strip())
                if new_amount_that_day > self.daily_payment:
                    MainWindow.__new__(MainWindow).unsuccessful_information('New amount exceeds daily payment')
                else:
                    print('am seeing it')
                    cursor.execute('UPDATE payments SET amount=? WHERE payment_id=? AND date=?',
                                   (new_amount_that_day, customer_info[2], self.repay_date))
                    cursor.execute("UPDATE loans SET balance=? WHERE loan_id=?", (new_balance, customer_info[2]))
                    connection.commit()
                    MainWindow.__new__(MainWindow).success_information('Payment successfully updated')
                    self.showing_borrowers_info(None)
                    cursor.close()
                    connection.close()
                    # self.amount_entry.delete(0, END)
                    return
                return

            if int(self.amount_entry.get()) > self.daily_payment:
                MainWindow.__new__(MainWindow).unsuccessful_information('Amount exceeds daily payment')
                return
        cursor.execute('INSERT INTO payments VALUES(?, ?, ?)',
                       (customer_info[2], self.amount_entry.get().strip(), self.repay_date))
        cursor.execute("UPDATE loans SET balance=? WHERE loan_id=?", (new_balance, customer_info[2]))
        connection.commit()
        MainWindow.__new__(MainWindow).success_information('Payment successfully received')
        self.showing_borrowers_info(None)
        cursor.close()
        connection.close()

