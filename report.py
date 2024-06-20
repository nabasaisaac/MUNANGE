import sqlite3
from customtkinter import *
from PIL import Image
from datetime import date, datetime
import os
import sys


# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Report:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):

        self.designing_window()

    def designing_window(self):
        self.upper_buttons_frame = CTkFrame(self.display_window, bg_color='#3BA541', fg_color='#3BA541',
                                            )
        self.upper_buttons_frame.pack(fill=X)

        self.report_button = CTkButton(self.upper_buttons_frame, text='View Report', text_color='white',
                                        corner_radius=0, bg_color='#3BA541', fg_color='#3BA541', hover_color='#0C8A01',
                                        font=('roboto', 15), image=CTkImage(Image.open(resource_path('icons/report.png')),
                                        size=(15, 15)), compound=LEFT,  height=35, width=150, command=lambda:
                                        self.sliding(self.report_button, self.check_for_secret_code))
        self.report_button.pack(side=LEFT)

        self.sliding(self.report_button, self.check_for_secret_code)

    def hiding(self):
        self.report_button.configure(fg_color='#3BA541')
        # self.change_password_button.configure(fg_color='#3BA541')

    def sliding(self, button, methods):
        self.hiding()
        for widgets in self.display_window.winfo_children()[2::]:
            widgets.destroy()

        button.configure(fg_color='#085f00')

        methods()

    def check_for_secret_code(self):
        def go(event):
            connection = sqlite3.connect(resource_path('munange.db'))
            cursor = connection.cursor()
            cursor.execute("SELECT phone FROM profile WHERE user_id=1")
            secret_code = cursor.fetchone()[0][5:]
            if self.secret_code_entry.get() == secret_code:
                for widget in self.display_window.winfo_children()[2:]:
                    widget.destroy()
                self.report()
            else:
                from main_window import MainWindow
                MainWindow.__new__(MainWindow).unsuccessful_information('Invalid Secret Code')

        frame = CTkFrame(self.display_window, fg_color='white', bg_color='gray95', corner_radius=10)
        frame.pack(pady=100)
        CTkLabel(frame, text='Please enter a secret code to view reports.', fg_color='white', bg_color='white',
                 font=('roboto', 15), text_color='black').pack(padx=40, pady=(30, 20))
        self.secret_code_entry = CTkEntry(frame, fg_color='#f1fcf1', bg_color='white', corner_radius=10,
                                          border_width=1, width=250, text_color='gray20', height=35,
                                          border_color='#4CC053', placeholder_text_color='gray70', show='*',
                                          font=('roboto', 15), placeholder_text='Secret Code')
        self.secret_code_entry.pack(padx=40, fill=X)
        self.secret_code_entry.bind('<FocusIn>', lambda event: self.secret_code_entry.configure(border_color='#44aaee'))
        self.secret_code_entry.bind('<FocusOut>',
                                    lambda event: self.secret_code_entry.configure(border_color='#4CC053'))
        self.secret_code_entry.bind('<Return>', go)

        self.confirm_button = CTkButton(frame, text='GO', bg_color='white', fg_color='#3BA541',
                                        corner_radius=10, width=250, height=35, hover_color='#2D9834', compound=RIGHT,
                                        border_color='gray50', font=('roboto', 15),
                                        image=CTkImage(Image.open(resource_path('images/back_image.png'))),
                                        command=lambda: go(None))
        self.confirm_button.pack(padx=40, fill=X, pady=(20, 40))

    def report(self):
        self.scrollable_frame = CTkScrollableFrame(self.display_window, bg_color='white', fg_color='white',
                                                   scrollbar_button_color='gray90', corner_radius=4,
                                                   scrollbar_button_hover_color='gray95', border_color='#4CC053',
                                                   border_width=1, )
        self.scrollable_frame.pack(fill=BOTH, padx=130, pady=(30, 0), expand=True)

        global frames
        frames = []
        for i in range(3):
            self.widgets_frame = CTkFrame(self.scrollable_frame, bg_color='white', fg_color='white', corner_radius=0,
                                          )
            self.widgets_frame.pack(fill=X, padx=(20, 10), pady=10, expand=True)
            frames.append(self.widgets_frame)

        CTkLabel(frames[0], image=CTkImage(Image.open(resource_path('images/munange_pdf_logo.png')), size=(100, 90)),
                 text='', font=('arial', 17, 'bold'), compound=LEFT).pack(side=LEFT)
        headed_paper_names = CTkFrame(frames[0], bg_color='white', fg_color='white', corner_radius=0,
                                      )
        headed_paper_names.pack(padx=(20, 0), side=LEFT)
        CTkLabel(headed_paper_names, text='MUNANGE FINANCIAL SERVICES LTD', font=('roboto', 16, 'bold'), compound=LEFT,
                 text_color='black', anchor='w', width=300, height=25).pack()

        CTkLabel(headed_paper_names, text='P.0 BOX 268, Masaka, Uganda', font=('roboto', 15, 'bold'), compound=LEFT
                 , text_color='black', justify=LEFT, anchor='w', width=300, fg_color='white', height=10).pack()

        CTkLabel(headed_paper_names, text='Tel: 0701677728/0755299598', font=('roboto', 15, 'bold'), compound=LEFT,
                 anchor='w',
                 text_color='black', fg_color='white', width=300, height=25).pack()
        CTkLabel(headed_paper_names, text="Email: kapalagajameshillary@gmail.com", font=('roboto', 15),
                 compound=LEFT, anchor='w', text_color='black', fg_color='white', width=300, height=15).pack()

        time_method = datetime(date.today().year, date.today().month, date.today().day)
        day = time_method.strftime("%d")
        month = time_method.strftime("%B")
        year = time_method.strftime("%Y")

        current_month = f'{month}, {year}'
        self.title = CTkLabel(frames[1], text=f'CASH FLOW FOR {current_month.upper()}.', bg_color='#44aaee', fg_color='#44aaee',
                              text_color='#FFFFFF', font=('roboto', 15, 'bold'))

        self.title.pack(fill=X, padx=(10, 20))

        heading_frame = CTkFrame(frames[2], fg_color='white', bg_color='white')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'CATEGORY', bg_color='white', fg_color='white',
                 text_color='black', font=('roboto', 15), anchor='w', justify=LEFT,
                 width=200).pack(side=LEFT, padx=(10, 0))

        CTkLabel(heading_frame, text=f'AMOUNT(UGX)', bg_color='white', fg_color='white',
                 text_color='black', font=('roboto', 15), anchor='w', justify=LEFT,
                 width=200).pack(side=LEFT)

        heading_frame = CTkFrame(frames[2], fg_color='#EDF8FF', bg_color='#EDF8FF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'BALANCE IN CLIENTS', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.balance_in_clients = CTkLabel(heading_frame, text=f'', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.balance_in_clients.pack(side=LEFT)
        
        heading_frame = CTkFrame(frames[2], fg_color='#FFFFFF', bg_color='#FFFFFF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'LOANS DISBURSED', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.loans_disbursed = CTkLabel(heading_frame, text=f'', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.loans_disbursed.pack(side=LEFT)

        heading_frame = CTkFrame(frames[2], fg_color='#EDF8FF', bg_color='#EDF8FF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'PROCESSING FEE', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.processing_fee = CTkLabel(heading_frame, text=f'', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.processing_fee.pack(side=LEFT)

        heading_frame = CTkFrame(frames[2], fg_color='#FFFFFF', bg_color='#FFFFFF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'LOG BOOK FEE', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.log_book_fee = CTkLabel(heading_frame, text=f'', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.log_book_fee.pack(side=LEFT)

        heading_frame = CTkFrame(frames[2], fg_color='#EDF8FF', bg_color='#EDF8FF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'REPAYMENTS', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.repayments = CTkLabel(heading_frame, text=f'', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.repayments.pack(side=LEFT)

        heading_frame = CTkFrame(frames[2], fg_color='#FFFFFF', bg_color='#FFFFFF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'INTEREST', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.interest = CTkLabel(heading_frame, text=f'', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.interest.pack(side=LEFT)

        heading_frame = CTkFrame(frames[2], fg_color='#EDF8FF', bg_color='#EDF8FF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'INCOME', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.income = CTkLabel(heading_frame, text=f'', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.income.pack(side=LEFT)

        heading_frame = CTkFrame(frames[2], fg_color='#FFFFFF', bg_color='#FFFFFF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'EXPENDITURE', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.expenditure = CTkLabel(heading_frame, text=f'', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.expenditure.pack(side=LEFT)

        heading_frame = CTkFrame(frames[2], fg_color='#EDF8FF', bg_color='#EDF8FF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'PROFIT/LOSS', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.profit = CTkLabel(heading_frame, text=f'', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.profit.pack(side=LEFT)

        self.getting_reports_values()

    def getting_reports_values(self):
        time_method = datetime(date.today().year, date.today().month, date.today().day)
        day = time_method.strftime("%d")
        month = time_method.strftime("%b")
        year = time_method.strftime("%Y")

        self.current_month = f'{month}-{year}'
        # print(current_month)

        connection = sqlite3.connect(resource_path("munange.db"))
        cursor = connection.cursor()
        cursor.execute("SELECT SUM(amount) FROM loans WHERE loan_date LIKE ? AND status='on going'",
                       (f'%{self.current_month}', ))
        try:
            total_loan_this_month = int(cursor.fetchone()[0])
        except TypeError:
            total_loan_this_month = 0

        self.loans_disbursed.configure(text=f'{total_loan_this_month-total_loan_this_month * 0.05}')
        self.processing_fee.configure(text=f'{total_loan_this_month * 0.05}')
        cursor.execute("SELECT SUM(amount) FROM payments WHERE date LIKE ?", (f'%{self.current_month}', ))

        try:
            total_payments = int(cursor.fetchone()[0])
        except TypeError:
            total_payments = 0
        # print(total_loan_this_month*0.2)
        monthly_interest = total_payments*1/6

        self.interest.configure(text=f'{monthly_interest:.1f}')
        self.repayments.configure(text=f'{total_payments:.1f}')

        # getting total balance in clients
        cursor.execute("SELECT SUM(balance) FROM loans WHERE status='on going'")

        self.balance_in_clients.configure(text=f'{cursor.fetchone()[0]}')
        # self.balance_in_clients.configure(text=f"{((total_loan_this_month-total_loan_this_month * 0.05)-total_payments):.1f}")
        # Getting total fee on log books
        new_current_month_format = f'{year}-{time_method.strftime('%m')}'
        # print(new_current_month_format)
        # print(time_method.strftime('%m'))
        cursor.execute("SELECT COUNT(customer_id) FROM customers WHERE register_date LIKE ?",
                       (f'{new_current_month_format}%', ))
        total_log_fee = int(cursor.fetchone()[0])*5000
        self.log_book_fee.configure(text=f'{total_log_fee:.1f}')
        self.total_expenditure()

        income = total_loan_this_month * 0.05 + total_log_fee + monthly_interest
        self.income.configure(text=f"{income:.1f}")
        profit = income-self.total_expenditure()
        if profit > 0:
            self.profit.configure(text=f'{profit:.1f}', text_color='#3BA541')
        elif profit == 0:
            self.profit.configure(text=f'{profit:.1f}', text_color='gray40')
        else:
            self.profit.configure(text=f'{profit:.1f}', text_color='#ff5c5c')
        cursor.close()
        connection.close()

    def total_expenditure(self):
        connection = sqlite3.connect(resource_path("munange.db"))
        cursor = connection.cursor()
        query = "SELECT expenses FROM expenditure WHERE date LIKE ?"

        cursor.execute(query, (f'%{self.current_month}', ))
        expenses = cursor.fetchall()
        # print(expenses)
        cursor.close()
        connection.close()
        self.total = 0
        for expense in expenses:
            total_expenditure = 0

            for i, item in enumerate(expense[0].split('|')):
                total_expenditure += int(item.split(':')[1])

            self.total += total_expenditure

        self.expenditure.configure(text=f'{self.total:.1f}')
        return self.total

