from customtkinter import *
from PIL import Image
from main_window import MainWindow
from tkinter import ttk
import sqlite3
import datetime
from datetime import date, datetime, timedelta

import os
import sys


# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class ViewBorrowers:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        self.buttons_frame = CTkFrame(self.display_window, bg_color='gray95', fg_color='white')
        self.buttons_frame.pack(fill=X, pady=20, padx=20)

        self.title_frame = CTkFrame(self.display_window, fg_color='white', bg_color='gray95',
                                                   )
        self.title_frame.pack(fill=BOTH, expand=True, padx=20)

        CTkLabel(self.buttons_frame, text='Borrowers', text_color='#0C2844', fg_color='white', bg_color='white',
                 font=('roboto', 16), height=50).pack(side=LEFT, padx=20)

        self.download_button = CTkButton(self.buttons_frame, fg_color='#0C2844', bg_color='white', text='Download',
                                         text_color='white', font=('roboto', 15), compound=LEFT, width=100,
                                         image=CTkImage(Image.open(resource_path('icons/download.png')), size=(20, 20)),
                                         command=lambda: self.print_or_download_borrowers(True))
        self.download_button.pack(side=RIGHT, padx=10)

        self.print_button = CTkButton(self.buttons_frame, fg_color='#0C2844', bg_color='white', text='Print',
                                         text_color='white', font=('roboto', 15), compound=LEFT, width=100,
                                         image=CTkImage(Image.open(resource_path('icons/print.png')), size=(15, 15)),
                                      command=lambda: self.print_or_download_borrowers(False))
        self.print_button.pack(side=RIGHT, padx=(5, 0))

        self.search_borrowers_entry = CTkEntry(self.buttons_frame, bg_color='white',
                                               fg_color='gray95', border_width=0, placeholder_text='Search',
                                               placeholder_text_color='gray50', font=('roboto', 15),
                                               text_color='#0C2844', corner_radius=20, width=150)
        self.search_borrowers_entry.pack(side=RIGHT, padx=20)
        self.search_borrowers_entry.bind('<KeyRelease>', self.searching_for_borrowers)

        CTkLabel(self.search_borrowers_entry, bg_color='gray95', fg_color='gray95', text='', width=10,
                 image=CTkImage(Image.open(resource_path('icons/search2.png')), size=(15, 15))).place(relx=0.8, rely=0.01)
        self.working_on_treeview(self.title_frame)

    def working_on_treeview(self, tree_frame):

        style = ttk.Style()
        # Modify the font of the body
        global customers_tree

        style.configure("mystyle.Treeview", font=('arial', 17), foreground='gray30', rowheight=40)

        # Modify the font of the headings
        style.configure("mystyle.Treeview.Heading", font='arial 18', foreground='black')

        # Apply the layout to the Treeview
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
        customers_tree = ttk.Treeview(tree_frame, style="mystyle.Treeview")

        # customers_tree.
        customers_tree['columns'] = ['customer_id', 'name', 'gender', 'days', 'amount', 'balance']
        # format columns
        customers_tree.column('#0', width=0, stretch=NO)
        customers_tree.column('customer_id', width=150, minwidth=150, anchor=CENTER)
        customers_tree.column('name', width=300, minwidth=200, anchor='w')
        customers_tree.column('gender', width=150, minwidth=100, anchor='w')
        customers_tree.column('days', width=150, minwidth=120, anchor='w')
        customers_tree.column('amount', width=150, minwidth=120, anchor='w')
        customers_tree.column('balance', width=150, minwidth=120, anchor='w')

        # creating headings
        customers_tree.heading('#0', text='')
        customers_tree.heading('customer_id', text='ACCESS NO', anchor=CENTER)
        customers_tree.heading('name', text='NAME', anchor='w')
        customers_tree.heading('gender', text='GENDER', anchor='w')
        customers_tree.heading('days', text='DAYS LEFT', anchor='w')
        customers_tree.heading('amount', text='AMOUNT', anchor='w')
        customers_tree.heading('balance', text='BALANCE', anchor='w')

        customers_tree.pack(fill=BOTH, expand=True, pady=5, padx=5)
        query = ("SELECT customers.customer_id, customers.name, customers.gender, loans.loan_id, loans.amount, loans.loan_date, "
                 "loans.loan_deadline, loans.balance FROM customers JOIN loans ON customers.customer_id = loans.customer_no WHERE "
                 "loans.status='on going' ORDER BY name ASC")
        self.showing_borrowers_in_tree(query)
        customers_tree.bind('<Double-1>', lambda event: self.double_click(event))

    def showing_borrowers_in_tree(self, query):
        customers_tree.delete(*customers_tree.get_children())
        customers_tree.tag_configure('color1', background='gray98')
        customers_tree.tag_configure('color2', background='white')
        customers_tree.tag_configure('color3', foreground='red')
        my_tag = 'color2'
        # Getting data from database
        connection = sqlite3.connect(resource_path('munange.db'))
        cursor = connection.cursor()

        cursor.execute(query)
        self.borrowers = cursor.fetchall()
        # print(self.borrowers)

        count = 0
        for borrower in self.borrowers:
            # cursor.execute(query, (customer_id, ))
            # global customer_info, deadline_date
            # customer_info = cursor.fetchone()

            cursor.execute("SELECT amount, date FROM payments WHERE payment_id=?", (borrower[3], ))
            payments_info = cursor.fetchall()
            # print(payments_info)
            # working on the days remaining to deadline
            time_method = datetime(date.today().year, date.today().month, date.today().day)
            day = time_method.strftime("%d")
            month = time_method.strftime("%b")
            year = time_method.strftime("%Y")

            current = f'{day}-{month}-{year}'
            deadline = borrower[6]
            current_date = datetime.strptime(current, '%d-%b-%Y')
            deadline_date = datetime.strptime(deadline, '%d-%b-%Y')
            if current_date >= deadline_date:
                remaining_days = '0'
            else:
                remaining_days = str(deadline_date - current_date).split(',')[0]

            # working_with_getting_missed_days
            loan_date = borrower[5]

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
            # current_amount = 0
            try:
                for payment in payments_info:
                    # current_amount += int(payment[0])
                    self.paid_days.append(payment[1])
            except IndexError:
                pass

            # missed_days = list(days for days in days_list if days not in self.paid_days)
            outstanding_balance = int(borrower[7])
            if current_date > deadline_date:
                remaining_days = 'Passed deadline'
                if outstanding_balance == 0:
                    remaining_days = 'CLOSED'
                else:
                    pass

            my_tag = 'color1' if my_tag == 'color2' else 'color2'
            if remaining_days == 'Passed deadline':
                my_tag = 'color3'

            customers_tree.insert(parent='', index='end', iid=count, values=(borrower[0], borrower[1], borrower[2],
                                  remaining_days, borrower[4], outstanding_balance), tags=my_tag)
            count += 1

        cursor.close()
        connection.close()
        return len(self.borrowers)

    def searching_for_borrowers(self, event):
        query = (f"SELECT customers.customer_id, customers.name, customers.gender, loans.loan_id, loans.amount, loans.loan_date, "
                 "loans.loan_deadline, loans.balance FROM customers JOIN loans ON customers.customer_id = loans.customer_no WHERE "
                 f"loans.status='on going' AND customers.name LIKE '%{self.search_borrowers_entry.get().strip()}%'"
                 f" ORDER BY name ASC")
        borrowers_no = self.showing_borrowers_in_tree(query)
        if borrowers_no == 0:
            MainWindow.__new__(MainWindow).unsuccessful_information('No borrowers match your search')

    def print_or_download_borrowers(self, isdirectory):
        from borrowers_excel import BorrowerExcel
        if isdirectory:
            directory = filedialog.askdirectory(title='Select folder to save this file')
            if directory:
                BorrowerExcel(directory)
                MainWindow.__new__(MainWindow).success_information('Borrowers file successfully saved.')
        else:
            MainWindow.__new__(MainWindow).success_information('Loading....')
            BorrowerExcel(False)

    def double_click(self, event):
        global row_double_click
        row_double_click = customers_tree.identify_row(event.y)
        borrower_data = customers_tree.item(row_double_click, 'values')

        # print(customers_data)
        if row_double_click:
            from borrower_details import BorrowerDetails
            BorrowerDetails(self.display_window, borrower_data)
        else:
            pass

    def back_to_view_borrowers(self, display_frame):
        ViewBorrowers(display_frame)




