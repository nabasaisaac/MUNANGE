import sqlite3

from customtkinter import *
from PIL import ImageTk, Image
from datetime import date, datetime

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

        self.report_button = CTkButton(self.upper_buttons_frame, text='Report', text_color='white',
                                        corner_radius=0, bg_color='#3BA541', fg_color='#3BA541', hover_color='#0C8A01',
                                        font=('roboto', 15), image=CTkImage(Image.open('icons/report.png'),
                                        size=(15, 15)), compound=LEFT,  height=35, width=150, command=lambda:
                                        self.sliding(self.report_button, self.report))
        self.report_button.pack(side=LEFT)

        self.sliding(self.report_button, self.report)

    def hiding(self):
        self.report_button.configure(fg_color='#3BA541')
        # self.change_password_button.configure(fg_color='#3BA541')

    def sliding(self, button, methods):
        self.hiding()
        for widgets in self.display_window.winfo_children()[2::]:
            widgets.destroy()

        button.configure(fg_color='#085f00')

        methods()

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

        CTkLabel(frames[0], image=CTkImage(Image.open('images/munange_pdf_logo.png'), size=(100, 90)),
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
        CTkLabel(heading_frame, text=f'LOANS DISBURSED', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.loans_disbursed = CTkLabel(heading_frame, text=f'', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.loans_disbursed.pack(side=LEFT)
        
        heading_frame = CTkFrame(frames[2], fg_color='#FFFFFF', bg_color='#FFFFFF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'PROCESSING FEE', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.processing_fee = CTkLabel(heading_frame, text=f'', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.processing_fee.pack(side=LEFT)

        heading_frame = CTkFrame(frames[2], fg_color='#EDF8FF', bg_color='#EDF8FF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'INTEREST', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.interest = CTkLabel(heading_frame, text=f'', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.interest.pack(side=LEFT)

        heading_frame = CTkFrame(frames[2], fg_color='#FFFFFF', bg_color='#FFFFFF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'LOANS DISBURSED', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.loans_disbursed1 = CTkLabel(heading_frame, text=f'650000.00', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.loans_disbursed1.pack(side=LEFT)

        heading_frame = CTkFrame(frames[2], fg_color='#EDF8FF', bg_color='#EDF8FF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'REPAYMENTS', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.repayments = CTkLabel(heading_frame, text=f'1000000.00', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.repayments.pack(side=LEFT)

        heading_frame = CTkFrame(frames[2], fg_color='#FFFFFF', bg_color='#FFFFFF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'BALANCE IN CLIENTS', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.balance_in_clients = CTkLabel(heading_frame, text=f'20000000.00', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.balance_in_clients.pack(side=LEFT)

        heading_frame = CTkFrame(frames[2], fg_color='#EDF8FF', bg_color='#EDF8FF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'EXPENDITURE', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.expenditure = CTkLabel(heading_frame, text=f'1000000.00', bg_color='#EDF8FF', fg_color='#EDF8FF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.expenditure.pack(side=LEFT)

        heading_frame = CTkFrame(frames[2], fg_color='#FFFFFF', bg_color='#FFFFFF')
        heading_frame.pack(fill=X, padx=(10, 20), ipady=5)
        CTkLabel(heading_frame, text=f'INCOME', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200).pack(side=LEFT, padx=(10, 0))

        self.income = CTkLabel(heading_frame, text=f'20000000.00', bg_color='#FFFFFF', fg_color='#FFFFFF',
                                text_color='gray40', font=('roboto', 15), anchor='w', justify=LEFT,
                                width=200)
        self.income.pack(side=LEFT)
        self.getting_reports_values()

    def getting_reports_values(self):
        time_method = datetime(date.today().year, date.today().month, date.today().day)
        day = time_method.strftime("%d")
        month = time_method.strftime("%b")
        year = time_method.strftime("%Y")
        current_month = f'{month}-{year}'
        print(current_month)
        connection = sqlite3.connect("munange.db")
        cursor = connection.cursor()
        cursor.execute("SELECT SUM(amount) FROM loans WHERE loan_date LIKE ? AND status='on going'",
                       (f'%{current_month}', ))
        total_loan_this_month = int(cursor.fetchone()[0])
        self.loans_disbursed.configure(text=f'{total_loan_this_month-total_loan_this_month * 0.05}')
        self.processing_fee.configure(text=f'{total_loan_this_month * 0.05}')
