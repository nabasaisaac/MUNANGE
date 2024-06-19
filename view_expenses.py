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
        self.title = CTkLabel(self.display_frame, text=f"EMPLOYEE'S DAILY EXPENDITURE FOR {month.upper()}, {year} ",
                         text_color='#ffffff', font=('roboto', 15, 'bold'), fg_color='#44aaee')
        self.title.pack(fill=X, pady=(10, 5), padx=(10, 20))
        history_frame = CTkFrame(self.display_frame, fg_color='white', bg_color='white')
        history_frame.pack(padx=20, fill=X)

        self.history_button = CTkButton(history_frame, bg_color='white', fg_color='#b7c1d1', font=('roboto', 15),
                                    text='History', text_color='#0C2844', compound=LEFT, hover_color='#98a6bd',
                                    image=CTkImage(Image.open('icons/history.png')), width=20,
                                    command=self.getting_history)
        self.history_button.pack(side=LEFT)

        self.total_amount_label = CTkLabel(history_frame, text=f'Total Expenditure: 0', fg_color='white', width=400,
                                text_color='#0C2844', font=('roboto', 15, 'bold'), anchor='e', justify=RIGHT)
        self.total_amount_label.pack(side=RIGHT)

        self.scrollable_frame = CTkScrollableFrame(self.display_frame, fg_color='white', bg_color='white',
                                                   scrollbar_fg_color='white', scrollbar_button_color='gray95',
                                                   scrollbar_button_hover_color='gray85', height=420)
        self.scrollable_frame.pack(fill=BOTH, expand=True, pady=(0, 5), padx=5)

        month = f'%{time_method.strftime("%b")}-{time_method.strftime("%Y")}'
        self.fetch_all_expenses(month)

    def fetch_all_expenses(self, month):
        connection = sqlite3.connect("munange.db")
        cursor = connection.cursor()
        query = "SELECT date, expenses FROM expenditure WHERE employee_no=? AND date LIKE ?"
        time_method = datetime.datetime(date.today().year, date.today().month, date.today().day)
        day = time_method.strftime("%d")

        # month = f'%May%'

        cursor.execute(query, (self.employee_id, month))
        expenses = cursor.fetchall()

        cursor.close()
        connection.close()

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

    def getting_history(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.title.configure(text='EXPENDITURE HISTORY')
        self.total_amount_label.configure(text='')

        connection = sqlite3.connect("munange.db")
        cursor = connection.cursor()
        cursor.execute("SELECT date FROM expenditure WHERE employee_no=?", (self.employee_id, ))
        dates = cursor.fetchall()
        cursor.close()
        connection.close()

        all_dates = []
        for day in dates:
            all_dates.append(day[0][3:])

        # getting distinct dates
        all_dates.reverse()
        distinct_dates = set(all_dates)
        # print(distinct_dates)
        time_method = datetime.datetime(date.today().year, date.today().month, date.today().day)
        self.current_month = f'{time_method.strftime("%b")}-{time_method.strftime("%Y")}'

        for month in distinct_dates:
            if month == self.current_month:
                month = 'This Month'
            self.button = CTkButton(self.scrollable_frame, text=f'{month}', fg_color='#b7c1d1', bg_color='white',
                                    height=35, hover_color='#98a6bd', text_color='#0C2844')
            self.button.pack(fill=X, pady=(0, 15))

            self.button.configure(command=lambda button=self.button: self.date_expenses(button))

    def date_expenses(self, button):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        month = f'%{button.cget('text')}'
        if button.cget('text') == 'This Month':
            month = f'%{self.current_month}'
        self.title.configure(text=f"EMPLOYEE'S DAILY EXPENDITURE FOR {month[1:].upper()} ")

        self.fetch_all_expenses(month)







