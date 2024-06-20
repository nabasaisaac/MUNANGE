import io
import random
from customtkinter import *
import sqlite3
import datetime
from datetime import date, datetime
from tkinter import *
from PIL import Image, ImageFilter, ImageTk, ImageEnhance, ImageDraw

from main_window import MainWindow
import os
import sys

# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Dashboard:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        self.upper_buttons_frame = CTkFrame(self.display_window, bg_color='#3BA541', fg_color='#3BA541',
                                            )
        self.upper_buttons_frame.pack(fill=X)

        self.dashboard_button = CTkButton(self.upper_buttons_frame, text='Dashboard', text_color='white',
                                        corner_radius=0, bg_color='#3BA541', fg_color='#3BA541', hover_color='#0C8A01',
                                        font=('roboto', 15), image=CTkImage(Image.open(resource_path('icons/filled-dashboard.png')),
                                        size=(15, 15)), compound=LEFT,  height=35, width=150, command=lambda:
                                        self.sliding(self.dashboard_button, self.dashboard))
        self.dashboard_button.pack(side=LEFT)

        self.sliding(self.dashboard_button, self.dashboard)

    def dashboard(self):
        canvas_frame = CTkFrame(self.display_window, fg_color='gray95', bg_color='gray95')
        canvas_frame.pack(pady=(20, 0), fill=X)
        self.image_canvas = Canvas(canvas_frame, highlightbackground='gray95',
                                   width=850, height=400)
        # self.image_canvas.place(relx=0.1, rely=0.1, anchor='sw')
        self.image_canvas.pack(padx=20, side=LEFT)

        def process_image(image_path, blur_radius=8, transparency=500, corner_radius=20):
            # Open the image
            image = Image.open(resource_path(image_path)).convert("RGBA")

            # Apply Gaussian blur
            blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))

            # Apply transparency
            alpha = blurred_image.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(transparency / 255.0)
            blurred_image.putalpha(alpha)

            # Create a mask for rounded corners
            mask = Image.new('L', blurred_image.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.rounded_rectangle((0, 0) + blurred_image.size, corner_radius, fill=255)

            # Apply the mask to the blurred image to create rounded corners
            rounded_blurred_image = Image.new('RGBA', blurred_image.size)
            rounded_blurred_image.paste(blurred_image, (0, 0), mask)

            return rounded_blurred_image

        global background_image, same_photo, change_format
        image_path = ["images/money_image.png", "images/money_image2.png", "images/money_image3.png",
                      "images/money_image4.png", "images/money_image5.png", "images/money_image6.png",
                      "images/money_image7.png", "images/money_image8.png", "images/money_image9.png", ]
        background_image = ImageTk.PhotoImage(process_image(random.choice(image_path)).resize((840, 350)))
        self.image_canvas.create_image(10, 20, image=background_image, anchor='nw')

        connection = sqlite3.connect(resource_path('munange.db'))
        cursor = connection.cursor()
        cursor.execute("SELECT photo, name FROM profile WHERE user_id=1")
        user_details = cursor.fetchone()
        cursor.close()
        connection.close()

        change_format = Image.open(io.BytesIO(user_details[0])).resize((200, 200))
        same_photo = ImageTk.PhotoImage(MainWindow.__new__(MainWindow).make_circular_image(change_format))
        self.image_canvas.create_image(50, 70, image=same_photo, anchor='nw')
        self.image_canvas.create_text(300, 100, text='Welcome', fill='white', font=('arial', 23, 'bold'), anchor='w')
        self.image_canvas.create_text(440, 100, text=f'{user_details[1]},', fill='white', font=('roboto', 23), anchor='w')
        self.image_canvas.create_text(300, 150, text='Manage your', fill='white', font=('roboto', 18), anchor='w')
        self.image_canvas.create_text(445, 150, text='finances', fill='white', font=('roboto', 18, 'bold'), anchor='w')
        self.image_canvas.create_text(550, 150, text='confidently with our', fill='white', font=('roboto', 18), anchor='w')
        self.image_canvas.create_text(300, 200, text='secure', fill='white', font=('roboto', 18, 'bold'), anchor='w')
        self.image_canvas.create_text(390, 200, text='money lending services.', fill='white', font=('roboto', 18), anchor='w')

        self.right_frame1 = CTkFrame(canvas_frame, bg_color='gray95', fg_color='gray95')
        self.right_frame1.pack(side=LEFT, fill=BOTH, expand=True, padx=(10, 20), pady=(10, 20))
        self.working_on_right_frame1()
        left_frame = CTkFrame(self.display_window, bg_color='gray95', fg_color='white',
                              corner_radius=20)
        left_frame.pack(side=LEFT, padx=20, ipady=5, ipadx=20)
        self.right_frame2 = CTkFrame(self.display_window, bg_color='gray95', fg_color='white', corner_radius=10)
        self.right_frame2.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 20))
        self.working_on_the_defaulters()
        from line_graph import LineGraph
        LineGraph(left_frame)

    def working_on_right_frame1(self):
        self.customers_frame = CTkFrame(self.right_frame1, bg_color='gray95', fg_color='white'
                                        )
        self.customers_frame.grid(row=0, column=0, padx=(5, 10), pady=(10, 40))

        self.borrowers_frame = CTkFrame(self.right_frame1, bg_color='gray95', fg_color='white')
        self.borrowers_frame.grid(row=0, column=1, pady=(10, 40))

        self.overdue_frame = CTkFrame(self.right_frame1, bg_color='gray95', fg_color='white')
        self.overdue_frame.grid(row=1, column=0, pady=(0, 10))

        self.employees_frame = CTkFrame(self.right_frame1, bg_color='gray95', fg_color='white')
        self.employees_frame.grid(row=1, column=1, pady=(0, 10))

        connection = sqlite3.connect(resource_path('munange.db'))
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(customer_id) FROM customers")
        customers = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(employee_id) FROM employees")
        employees = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(customer_no) FROM loans WHERE status='on going'")
        borrowers = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        customers_image_label = CTkLabel(self.customers_frame, text=f'   {customers}', font=('roboto', 16, 'bold'),
                                image=CTkImage(Image.open(resource_path('icons/customers-dashboard.png')), size=(70, 80)),
                                compound=LEFT, text_color='black', width=200, justify=LEFT, anchor='w',
                                fg_color='white')
        customers_image_label.pack(side=LEFT, padx=5, pady=5)
        CTkLabel(self.customers_frame, text='Customers', fg_color='white', bg_color='white',
                 text_color='gray50', font=('roboto', 16)).place(x=90, y=60)

        borrowers_image_label = CTkLabel(self.borrowers_frame, text=f'   {borrowers}', font=('roboto', 16, 'bold'),
                                image=CTkImage(Image.open(resource_path('icons/dashboard-borrowers.png')), size=(70, 80)),
                                compound=LEFT, text_color='black', width=200, justify=LEFT, anchor='w',
                                fg_color='white')
        borrowers_image_label.pack(side=LEFT, padx=5, pady=5)
        CTkLabel(self.borrowers_frame, text='Borrowers', fg_color='white', bg_color='white',
                 text_color='gray50', font=('roboto', 16)).place(x=90, y=60)

        self.overdue_image_label = CTkLabel(self.overdue_frame, text='0', font=('roboto', 16, 'bold'),
                                image=CTkImage(Image.open(resource_path('icons/deadline.png')), size=(80, 80)),
                                compound=LEFT, text_color='black', width=200, justify=LEFT, anchor='w',
                                fg_color='white')
        self.overdue_image_label.pack(side=LEFT, padx=5, pady=5)
        CTkLabel(self.overdue_frame, text='Overdue', fg_color='white', bg_color='white',
                 text_color='gray50', font=('roboto', 16)).place(x=85, y=60)

        self.employees_image_label = CTkLabel(self.employees_frame, text=f'   {employees}', font=('roboto', 16, 'bold'),
                                image=CTkImage(Image.open(resource_path('icons/dashboard-employees.png')), size=(60, 70)),
                                compound=LEFT, text_color='black', width=200, justify=LEFT, anchor='w',
                                fg_color='white')
        self.employees_image_label.pack(side=LEFT, padx=5, pady=10)
        CTkLabel(self.employees_frame, text='Employees', fg_color='white', bg_color='white',
                 text_color='gray50', font=('roboto', 16)).place(x=80, y=60)

    def working_on_the_defaulters(self):

        connection = sqlite3.connect(resource_path('munange.db'))
        cursor = connection.cursor()
        cursor.execute("SELECT customer_no, loan_deadline FROM LOANS WHERE status='on going' LIMIT 7")

        loans_list = cursor.fetchall()

        time_method = datetime(date.today().year, date.today().month, date.today().day)
        cur_date = f"{time_method.strftime('%d')}-{time_method.strftime('%b')}-{time_method.strftime('%Y')}"
        current_date = datetime.strptime(cur_date, '%d-%b-%Y')
        # print(loans_list)
        over_due_list = []
        for deadline_date in loans_list:
            if current_date > datetime.strptime(deadline_date[1], '%d-%b-%Y'):
                over_due_list.append((deadline_date[0], deadline_date[1]))

        # over_due_list = []
        cursor.close()
        connection.close()
        defaulters_label = CTkLabel(self.right_frame2, text='Defaulters List', font=('roboto', 16),
                 text_color='black', fg_color='white', bg_color='white')
        defaulters_label.pack(pady=(10, 0), fill=X, padx=20)

        line = CTkFrame(self.right_frame2, height=1, bg_color='gray90', fg_color='gray90')
        line.pack(fill=X)

        if len(over_due_list) == 0:
            CTkLabel(self.right_frame2, text='Normal progress! All repayments are up-to-date.', font=('roboto', 16),
                     text_color='#3BA541', fg_color='white', bg_color='white').pack(pady=(50, 0))
        else:
            self.overdue_image_label.configure(text=f'{len(over_due_list)}')
            line.pack_forget()
            defaulters_label.configure(justify=LEFT, anchor='w', font=('roboto', 15, 'bold'))
            CTkLabel(self.right_frame2, text='S/No.\t\tAccess No.\tDeadline Date', font=('roboto', 16),
                     text_color='black', fg_color='white', bg_color='white', justify=LEFT, anchor='w').pack(fill=X, padx=20)
            CTkFrame(self.right_frame2, height=1, bg_color='gray90', fg_color='gray90').pack(fill=X, padx=20)
            for i, info in enumerate(over_due_list, start=1):
                (CTkLabel(self.right_frame2, text=f'{i}.\t\t{info[0]}\t\t{info[1]}', font=('roboto', 16),
                         text_color='gray50', fg_color='white', bg_color='white', justify=LEFT, anchor='w')
                 .pack(fill=X, padx=20))
    def hiding(self):
        self.dashboard_button.configure(fg_color='#3BA541')
        # self.change_password_button.configure(fg_color='#3BA541')

    def sliding(self, button, methods):
        self.hiding()
        for widgets in self.display_window.winfo_children()[2::]:
            widgets.destroy()

        button.configure(fg_color='#085f00')

        methods()



