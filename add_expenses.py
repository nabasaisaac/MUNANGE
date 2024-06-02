from customtkinter import *
from PIL import Image
import datetime
from datetime import date
from main_window import MainWindow
import sqlite3


class AddExpenses:
    def __init__(self, display_frame, employee_id):
        self.display_frame = display_frame
        self.employee_id = employee_id
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        two_frames_holder = CTkFrame(self.display_frame, fg_color='white', bg_color='white')
        two_frames_holder.pack(fill=BOTH, expand=True, pady=(10, 0))
        CTkLabel(two_frames_holder, bg_color='white', fg_color='white', text='Add new expenses',
                 text_color='#0C2844', font=('roboto', 16, 'bold'), justify=LEFT, anchor='w'
                 ).pack(fill=X, pady=(0, 10), padx=20)

        global date_frame
        date_frame = CTkFrame(two_frames_holder, bg_color='white', fg_color='white', height=20)
        date_frame.pack(fill=X, padx=20, pady=10)

        first_frame = CTkFrame(two_frames_holder, fg_color='white', bg_color='white')
        first_frame.pack(side=LEFT, fill=BOTH, padx=20, pady=(20, 270), expand=True)

        second_frame = CTkFrame(two_frames_holder, fg_color='white', bg_color='white')
        second_frame.pack(side=LEFT, fill=BOTH, padx=(0, 20), pady=(20, 270), expand=True)

        self.date = IntVar()
        self.date.set(1)

        self.date_check_button = CTkCheckBox(date_frame, text_color='black', width=150, text='Use system date',
                                             variable=self.date, font=('roboto', 15),
                                             command=lambda: self.getting_time(None))
        self.date_check_button.pack(side=LEFT)
        # self.date_check_button.configure(command=l

        CTkLabel(first_frame, bg_color='white', fg_color='white', text='ITEM',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.item_name_entry = CTkEntry(first_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                       border_width=1, height=35, text_color='#0C2844')
        self.item_name_entry.pack(fill=X, pady=(0, 10))
        self.item_name_entry.bind('<FocusIn>', lambda event: self.item_name_entry.configure(border_color='#44aaee'))
        self.item_name_entry.bind('<FocusOut>', lambda event: self.item_name_entry.configure(border_color='#4CC053'))

        # CTkLabel(second_frame, bg_color='white', fg_color='white', text='',
        #          text_color='#0C2844', font=('roboto', 16, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10))

        CTkLabel(second_frame, bg_color='white', fg_color='white', text='AMOUNT (UGX)',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.item_amount_entry = CTkEntry(second_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                       border_width=1, height=35, text_color='#0C2844')
        self.item_amount_entry.pack(fill=X, pady=(0, 10))
        self.item_amount_entry.bind('<FocusIn>', lambda event: self.item_amount_entry.configure(border_color='#44aaee'))
        self.item_amount_entry.bind('<FocusOut>', lambda event: self.item_amount_entry.configure(border_color='#4CC053'))
        self.item_amount_entry.bind('<Return>', self.add_expenses_in_database)

        self.save_frame = CTkFrame(self.display_frame, fg_color='white', bg_color='white')
        self.save_frame.pack(fill=X, padx=20, pady=10, expand=True)
        self.save_button = CTkButton(self.save_frame, bg_color='white', fg_color='#44aaee', hover_color='#2A9AE5',
                                     image=CTkImage(Image.open('icons/save.png'), size=(20, 20)), text_color='white',
                                     text='Save', command=lambda: self.add_expenses_in_database(False))
        self.save_button.pack(side=RIGHT)

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

    def add_expenses_in_database(self, event):

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

        if self.item_name_entry.get().strip() == '' and self.item_amount_entry.get().strip() == '':
            MainWindow.__new__(MainWindow).unsuccessful_information('All fields are required')
            return
        elif not self.item_amount_entry.get().isdigit():
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid amount entered')

        else:
            connection = sqlite3.connect('munange.db')
            cursor = connection.cursor()
            cursor.execute("SELECT employee_no, date FROM expenditure")
            initial_expenses = cursor.fetchall()
            if (self.employee_id, self.date_to_use) in initial_expenses:
                cursor.execute(f"SELECT expenses FROM expenditure WHERE employee_no='{self.employee_id}' AND date='{self.date_to_use}'")
                expense_string = cursor.fetchone()[0]
                expense_string += (f'|{self.item_name_entry.get().strip().title()}:'
                                    f'{self.item_amount_entry.get().strip()}')

                query = (f"UPDATE expenditure SET expenses='{expense_string}' WHERE employee_no='{self.employee_id}' AND "
                         f"date='{self.date_to_use}'")
                cursor.execute(query)

            else:
                query = "INSERT INTO expenditure VALUES(?, ?, ?)"
                cursor.execute(query, (self.employee_id, self.date_to_use,
                    f'{self.item_name_entry.get().strip().title()}:{self.item_amount_entry.get().strip().title()}'))

            connection.commit()
            cursor.close()
            connection.close()
            MainWindow.__new__(MainWindow).success_information('Expenses successfully saved')
            self.item_name_entry.delete(0, END)
            self.item_amount_entry.delete(0, END)
            self.item_name_entry.focus_set()
