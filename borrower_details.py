from customtkinter import *
from PIL import Image
import datetime
from datetime import date, datetime, timedelta
from main_window import MainWindow
import sqlite3
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


class BorrowerDetails:
    def __init__(self, display_window, borrower_data):
        self.display_window = display_window
        self.borrower_data = borrower_data
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        # print(self.borrower_data)
        for widget in self.display_window.winfo_children()[2:]:
            widget.destroy()
        """_______________________Getting some important days_________________________"""
        connection = sqlite3.connect(resource_path('munange.db'))
        cursor = connection.cursor()
        query = (
            "SELECT customers.photo, customers.name, loans.loan_id, loans.loan_date, loans.amount, loans.loan_deadline FROM customers "
            "JOIN loans ON customers.customer_id=loans.customer_no WHERE customer_id=? AND loans.status='on going'")
        self.customer_id = f'{self.borrower_data[0]}'
        cursor.execute(query, (self.customer_id,))
        global customer_info, deadline_date, loan_date, payments_info, remaining_days, current_date
        customer_info = cursor.fetchone()

        cursor.execute("SELECT amount, date FROM payments WHERE payment_id=?", (customer_info[2],))
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
        current_amount = 0
        try:
            for payment in payments_info:
                current_amount += int(payment[0])
                self.paid_days.append(payment[1])
        except IndexError:
            pass
        global missed_days
        missed_days = list(days for days in days_list if days not in self.paid_days)
        """__________________________________End of the code here_____________________________"""

        back_button = CTkButton(self.display_window,
                                image=CTkImage(Image.open(resource_path('icons/back_image.png')), size=(20, 20)), text_color='white',
                                bg_color='gray95', fg_color='#0C2844', text='', width=10,
                                command=self.back_to_overview)
        back_button.place(x=15, y=60)
        back_button.bind('<Enter>', lambda event: back_button.configure(text='Back', width=10))
        back_button.bind('<Leave>', lambda event: back_button.configure(text='', width=10))

        self.scrollable_frame = CTkScrollableFrame(self.display_window, bg_color='white', fg_color='white',
                                                   scrollbar_button_color='gray90', corner_radius=4,
                                                   scrollbar_button_hover_color='gray95', border_color='#4CC053',
                                                   border_width=1, )
        self.scrollable_frame.pack(fill=BOTH, padx=130, pady=(30, 0), expand=True)
        self.lower_frame = CTkFrame(self.display_window, bg_color='gray95', fg_color='gray95', corner_radius=0,
                                    height=50)
        self.lower_frame.pack(fill=X, padx=130, pady=(5, 0))

        global frames
        frames = []
        for i in range(4):
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

        CTkLabel(headed_paper_names, text='Tel: 0701677728/0755299598', font=('roboto', 15, 'bold'), compound=LEFT, anchor='w',
                 text_color='black', fg_color='white', width=300, height=25).pack()
        CTkLabel(headed_paper_names, text="Email: kapalagajameshillary@gmail.com", font=('roboto', 15),
                 compound=LEFT, anchor='w', text_color='black', fg_color='white', width=300, height=15).pack()

        time_method = datetime(date.today().year, date.today().month, date.today().day)
        day = time_method.strftime("%d")
        month = time_method.strftime("%b")
        year = time_method.strftime("%Y")
        global current_date2
        current_date2 = f'{day}-{month}-{year}'
        self.title = CTkLabel(frames[1], text=f'BORROWER PAYMENTS INFO AS OF, {current_date2.upper()}.',
                              text_color='#344767', font=('roboto', 15, 'bold'), compound=LEFT)

        self.title.pack()

        global photo
        photo = Image.open(io.BytesIO(customer_info[0]))

        self.borrower_photo_label = CTkLabel(frames[1], fg_color='white', bg_color='yellow', text='',
                                            image=CTkImage(photo, size=(125, 135)))
        self.borrower_photo_label.pack(side=LEFT)

        left_frame = CTkFrame(frames[1], bg_color='white', fg_color='white', corner_radius=0,
                              )
        left_frame.pack(side=LEFT, fill=X, expand=True, padx=(30, 0))
        right_frame = CTkFrame(frames[1], bg_color='white', fg_color='white', corner_radius=0)

        right_frame.pack(side=LEFT, fill=X, expand=True, padx=(30, 0))

        CTkLabel(left_frame, text='FULL NAME', text_color='#7b809a', bg_color='white', width=200, justify=LEFT,
                 anchor='w', height=25).pack()
        CTkLabel(left_frame, text=f'{self.borrower_data[1].upper()}', text_color='#344767', bg_color='white', width=200,
                 justify=LEFT, anchor='w', height=20).pack()

        CTkLabel(left_frame, text='ACCESS NUMBER', text_color='#7b809a', bg_color='white', width=200, justify=LEFT,
                 anchor='w', height=25).pack()
        CTkLabel(left_frame, text=f'{self.borrower_data[0]}', text_color='#344767', bg_color='white', width=200,
                 justify=LEFT, anchor='w', height=20).pack()

        CTkLabel(left_frame, text='GENDER', text_color='#7b809a', bg_color='white', width=200, justify=LEFT,
                 anchor='w', height=25).pack()
        CTkLabel(left_frame, text=f'{self.borrower_data[2].upper()}', text_color='#344767', bg_color='white', width=200,
                 justify=LEFT, anchor='w', height=20).pack()
        CTkLabel(left_frame, text='LOAN DATE', text_color='#7b809a', bg_color='white', width=200, justify=LEFT,
                 anchor='w', height=25).pack()
        CTkLabel(left_frame, text=f'{customer_info[3]} ({customer_info[5]})', text_color='#344767', bg_color='white', width=200,
                 justify=LEFT, anchor='w', height=20).pack()

        CTkLabel(right_frame, text='MISSED DAYS', text_color='#7b809a', bg_color='white', width=200, justify=LEFT,
                 anchor='w', height=25).pack()
        CTkLabel(right_frame, text=f'{len(missed_days)}', text_color='#344767', bg_color='white', width=200,
                 justify=LEFT, anchor='w', height=20).pack()

        CTkLabel(right_frame, text='DAYS TO DEADLINE', text_color='#7b809a', bg_color='white', width=200, justify=LEFT,
                 anchor='w', height=25).pack()
        """issue here"""
        if current_date > deadline_date:
            remaining_days = f'PASSED DEADLINE ({-1*int(str(deadline_date - current_date).split()[0])} DAYS)'
            if int(self.borrower_data[5]) == 0:
                remaining_days = 'CLOSED'
            else:
                pass

        CTkLabel(right_frame, text=f'{remaining_days}', text_color='#344767', bg_color='white', width=200,
                 justify=LEFT, anchor='w', height=20).pack()

        CTkLabel(right_frame, text='AMOUNT BORROWED', text_color='#7b809a', bg_color='white', width=200, justify=LEFT,
                 anchor='w', height=25).pack()
        interest_frame = CTkFrame(right_frame, bg_color='white', fg_color='white')
        interest_frame.pack()
        CTkLabel(interest_frame, text=f'{self.borrower_data[4]}', text_color='#344767', bg_color='white', width=50,
                 justify=LEFT, anchor='w', height=20).pack(side=LEFT)
        interest = int(self.borrower_data[4]) * 0.2
        CTkLabel(interest_frame, text=f'+{interest}', text_color='#4CC053', bg_color='white', width=70, fg_color='#F1FFF2',
                 justify=LEFT, anchor='w', corner_radius=8, height=20).pack(side=LEFT, padx=(0, 80))

        CTkLabel(right_frame, text='BALANCE', text_color='#7b809a', bg_color='white', width=200, justify=LEFT,
                 anchor='w', height=25).pack()
        CTkLabel(right_frame, text=f'{self.borrower_data[5]}', text_color='#344767', bg_color='white', width=200,
                 justify=LEFT, anchor='w', height=20).pack()

        CTkLabel(frames[2], text=f'LOAN PAYMENTS HISTORY', text_color='#344767', font=('roboto', 15), compound=LEFT
                 ).pack()
        table_title_frame = CTkFrame(frames[2], fg_color='#44aaee', bg_color='#44aaee')
        table_title_frame.pack(fill=X)
        CTkLabel(table_title_frame, text='S/No.', text_color='white', font=('roboto', 14), width=200, fg_color='#44aaee',
                 ).pack(side=LEFT, padx=(0, 40))

        CTkLabel(table_title_frame, text='DATE', text_color='white', font=('roboto', 14), width=200, fg_color='#44aaee',
                 ).pack(side=LEFT, padx=(0, 40))
        CTkLabel(table_title_frame, text='AMOUNT PAID (UGX)', text_color='white', font=('roboto', 14), width=200, fg_color='#44aaee',
                 ).pack(side=LEFT, padx=0)

        cursor.execute(f"SELECT date, amount FROM payments WHERE payment_id=?", (customer_info[2], ))
        payments = cursor.fetchall()
        # payments.reverse()

        for count, payment in enumerate(payments, start=1):
            fg_color = 'gray98' if count % 2 != 0 else 'white'
            payment_frame = CTkFrame(frames[2], fg_color=fg_color, bg_color='white',
                                     corner_radius=0)
            payment_frame.pack(fill=X)
            CTkLabel(payment_frame, text=f'{count}', text_color='gray40', font=('roboto', 14), compound=LEFT
                     , width=200).pack(side=LEFT, padx=(0, 40))
            CTkLabel(payment_frame, text=f'{payment[0]}', text_color='gray40', font=('roboto', 14), compound=LEFT
                     , width=200).pack(side=LEFT, padx=(0, 40))
            CTkLabel(payment_frame, text=f'{payment[1]}', text_color='gray40', font=('roboto', 14), compound=LEFT
                     , width=200, ).pack(side=LEFT, padx=0)

        self.print_button = CTkButton(self.lower_frame, text='', bg_color='gray95', fg_color='#0C2844',
                                       border_color='gray95', width=0,
                                       text_color='white', font=('roboto', 15),
                                       image=CTkImage(Image.open(resource_path('icons/print.png')), size=(20, 20)),
                                       command=self.print_borrower_statement, text_color_disabled='white')
        self.print_button.pack(side=RIGHT)

        self.missed_days_button = CTkButton(self.lower_frame, text='Check missed days', bg_color='gray95', fg_color='#44aaee',
                                    border_color='gray95', hover_color='#44aaee',
                                    text_color='white', font=('roboto', 15), compound=LEFT, image=None,
                                    command=self.missed_days_list)

        self.missed_days_button.pack(side=LEFT)

        cursor.close()
        connection.close()

    def missed_days_list(self):
        # from settle_payments import SettlePayments
        frames[2].pack_forget()

        for items in frames[3].winfo_children():
            items.destroy()

        self.missed_days_button.configure(text='Back to statement', compound=LEFT,
                                    image=CTkImage(Image.open(resource_path('icons/white_back.png')), size=(20, 17)),
                                    command=self.back_to_statement)

        self.title.configure(text=f"BORROWER'S MISSED DAYS AS OF, {current_date2.upper()}")
        self.print_button.configure(state=DISABLED)
        self.title2 = CTkLabel(frames[3], text=f'LIST OF MISSED DAYS',
                              text_color='#344767', font=('roboto', 15, 'bold'), compound=LEFT)

        self.title2.pack(pady=(5, 10))
        if len(missed_days) == 0:
            CTkLabel(frames[3], text=f'Normal progress! no days missed.', text_color='#4CC053', font=('roboto', 15), compound=LEFT
                     , width=200).pack()
        missed_days.reverse()
        for day in missed_days:
            CTkLabel(frames[3], text=f'{day.upper()}', text_color='gray40', font=('roboto', 15), compound=LEFT
                     , width=200).pack()

        print(missed_days)

    def print_borrower_statement(self):
        global remaining_days
        from borrower_statement import BorrowerStatement
        MainWindow.__new__(MainWindow).success_information('Loading student statement ...')
        if current_date > deadline_date:
            remaining_days = f'PASSED DEADLINE ({-1*int(str(deadline_date - current_date).split()[0])} DAYS)'
            if int(self.borrower_data[5]) == 0:
                remaining_days = 'CLOSED'
            else:
                pass

        BorrowerStatement(False, photo, self.borrower_data, loan_date, payments_info, len(missed_days),
                          remaining_days)

    def back_to_statement(self):
        for items in frames[3].winfo_children():
            items.destroy()
        frames[3].pack_forget()
        self.missed_days_button.configure(text='Check missed days', image=None, command=self.missed_days_list)
        self.title.configure(text=f'BORROWER PAYMENTS INFO AS OF, {current_date2.upper()}')
        frames[2].pack(fill=X, padx=(20, 10), pady=10, expand=True)
        frames[3].pack(fill=X, padx=(20, 10), pady=10, expand=True)
        self.print_button.configure(state=NORMAL)

    def back_to_overview(self):
        from view_borrowers import ViewBorrowers
        for widget in self.display_window.winfo_children()[2::]:
            widget.destroy()
        ViewBorrowers.__new__(ViewBorrowers).back_to_view_borrowers(self.display_window)

