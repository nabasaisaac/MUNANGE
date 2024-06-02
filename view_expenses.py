from customtkinter import *
from PIL import Image
import datetime
from datetime import date
from main_window import MainWindow
import sqlite3


class ViewExpenses:
    def __init__(self, display_frame, employee_id):
        self.display_frame = display_frame
        self.employee_id = employee_id
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()
        time_method = datetime.datetime(date.today().year, date.today().month, date.today().day)
        day = time_method.strftime("%d")
        month = time_method.strftime("%b")
        year = time_method.strftime("%Y")
        title = CTkLabel(self.display_frame, text=f"EMPLOYEE'S DAILY EXPENDITURE FOR {month.upper()}, {year} ",
                         text_color='#ffffff', font=('roboto', 15, 'bold'), fg_color='#44aaee')
        title.pack(fill=X, pady=(10, 5), padx=(10, 20))

        self.total_amount_label = CTkLabel(self.display_frame, text=f'Total Expenditure: 0', fg_color='white', width=400,
                                text_color='#0C2844', font=('roboto', 15, 'bold'), anchor='e', justify=RIGHT)
        self.total_amount_label.pack(fill=X, padx=20)

        self.scrollable_frame = CTkScrollableFrame(self.display_frame, fg_color='white', bg_color='white',
                                                   scrollbar_fg_color='white', scrollbar_button_color='gray95',
                                                   scrollbar_button_hover_color='gray85', height=450)
        self.scrollable_frame.pack(fill=BOTH, expand=True, pady=(0, 5), padx=5)
        self.fetch_all_expenses()

    def fetch_all_expenses(self):
        connection = sqlite3.connect("munange.db")
        cursor = connection.cursor()
        query = "SELECT date, expenses FROM expenditure WHERE employee_no=? AND date LIKE ?"
        time_method = datetime.datetime(date.today().year, date.today().month, date.today().day)
        day = time_method.strftime("%d")
        month = f'%{time_method.strftime("%b")}%'
        cursor.execute(query, (self.employee_id, month))
        expenses = cursor.fetchall()
        expenses.reverse()
        self.total = 0
        for expense in expenses:
            total_expenditure = 0
            date_label = CTkLabel(self.scrollable_frame, text=f'{expense[0]}', fg_color='white', anchor='w', justify=LEFT,
                             text_color='#0C2844', font=('roboto', 15, 'bold'))
            date_label.pack(fill=X, pady=(10, 0), padx=20)

            item_frame = CTkFrame(self.scrollable_frame, fg_color='white', height=20)
            item_frame.pack(fill=X, padx=20)
            CTkLabel(item_frame, text=f'Item', fg_color='white', width=400,
                                    text_color='gray30', font=('roboto', 15, 'bold'), anchor='w', justify=LEFT).pack(side=LEFT, fill=X)
            amount_label = CTkLabel(item_frame, text=f'Amount', fg_color='white', width=400,
                                    text_color='gray30', font=('roboto', 15, 'bold'), anchor='w', justify=LEFT)
            amount_label.pack(side=LEFT, fill=X)

            for i, item in enumerate(expense[1].split('|')):
                fg_color = 'gray98' if i % 2 == 0 else 'white'
                expense_frame = CTkFrame(self.scrollable_frame, fg_color=fg_color, height=20)
                expense_frame.pack(fill=X, padx=20)
                date_label = CTkLabel(expense_frame, text=f'{item.split(':')[0]}', fg_color=fg_color, width=400,
                                      text_color='#0C2844', font=('roboto', 15), anchor='w', justify=LEFT)
                date_label.pack(side=LEFT, fill=X)
                amount_label = CTkLabel(expense_frame, text=f'{item.split(':')[1]}', fg_color=fg_color, width=400,
                                      text_color='#0C2844', font=('roboto', 15), anchor='w', justify=LEFT)
                amount_label.pack(side=LEFT, fill=X)
                total_expenditure += int(item.split(':')[1])
            total_frame = CTkFrame(self.scrollable_frame, fg_color='white', height=20)
            total_frame.pack(fill=X, padx=20)
            CTkLabel(total_frame, text=f'Total', fg_color='white', width=400,
                                    text_color='gray30', font=('roboto', 15, 'bold'), anchor='w', justify=LEFT).pack(side=LEFT, fill=X)
            total_label = CTkLabel(total_frame, text=f'{total_expenditure}', fg_color='white', width=400,
                                    text_color='gray30', font=('roboto', 15, 'bold'), anchor='w', justify=LEFT)
            total_label.pack(side=LEFT, fill=X)

            self.total += total_expenditure
            self.total_amount_label.configure(text=f'Total expenditure: UGX {self.total}')

