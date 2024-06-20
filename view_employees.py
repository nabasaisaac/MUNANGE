from customtkinter import *
from PIL import Image
from main_window import MainWindow
from tkinter import ttk
import sqlite3

import os
import sys


# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class ViewEmployees:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        self.buttons_frame = CTkFrame(self.display_window, bg_color='gray95', fg_color='white')
        self.buttons_frame.pack(fill=X, pady=20, padx=20)

        self.scrollable_frame = CTkFrame(self.display_window, fg_color='white', bg_color='gray95',
                                                   )
        self.scrollable_frame.pack(fill=BOTH, expand=True, padx=20)

        CTkLabel(self.buttons_frame, text='Employees', text_color='#0C2844', fg_color='white', bg_color='white',
                 font=('roboto', 16), height=50).pack(side=LEFT, padx=20)

        self.download_button = CTkButton(self.buttons_frame, fg_color='#0C2844', bg_color='white', text='Download',
                                         text_color='white', font=('roboto', 15), compound=LEFT, width=100,
                                         image=CTkImage(Image.open(resource_path('icons/download.png')), size=(20, 20)),
                                         command=lambda: self.print_or_download_students(True))
        self.download_button.pack(side=RIGHT, padx=10)

        self.print_button = CTkButton(self.buttons_frame, fg_color='#0C2844', bg_color='white', text='Print',
                                         text_color='white', font=('roboto', 15), compound=LEFT, width=100,
                                         image=CTkImage(Image.open(resource_path('icons/print.png')), size=(15, 15)),
                                      command=lambda: self.print_or_download_students(False))
        self.print_button.pack(side=RIGHT, padx=(5, 0))

        self.search_employees_entry = CTkEntry(self.buttons_frame, bg_color='white',
                                               fg_color='gray95', border_width=0, placeholder_text='Search',
                                               placeholder_text_color='gray50', font=('roboto', 15),
                                               text_color='#0C2844', corner_radius=20, width=150)
        self.search_employees_entry.pack(side=RIGHT, padx=20)
        self.search_employees_entry.bind('<KeyRelease>', self.searching_for_employees)

        CTkLabel(self.search_employees_entry, bg_color='gray95', fg_color='gray95', text='', width=10,
                 image=CTkImage(Image.open(resource_path('icons/search2.png')), size=(15, 15))).place(relx=0.8, rely=0.01)
        self.working_on_treeview(self.scrollable_frame)

    def working_on_treeview(self, tree_frame):
        style = ttk.Style()
        # Modify the font of the body
        global employees_tree

        style.configure("mystyle.Treeview", font=('arial', 17), foreground='gray30', rowheight=40)

        # Modify the font of the headings
        style.configure("mystyle.Treeview.Heading", font='arial 18', foreground='black')

        # Apply the layout to the Treeview
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
        employees_tree = ttk.Treeview(tree_frame, style="mystyle.Treeview")

        # employees_tree.
        employees_tree['columns'] = ['employee_id', 'name', 'gender', 'phone', 'district']
        # format columns
        employees_tree.column('#0', width=0, stretch=NO)
        employees_tree.column('employee_id', width=150, minwidth=150, anchor=CENTER)
        employees_tree.column('name', width=300, minwidth=200, anchor='w')
        employees_tree.column('gender', width=150, minwidth=100, anchor='w')
        employees_tree.column('phone', width=150, minwidth=120, anchor='w')
        employees_tree.column('district', width=150, minwidth=120, anchor='w')

        # creating headings
        employees_tree.heading('#0', text='')
        employees_tree.heading('employee_id', text='EMPLOYEE ID', anchor=CENTER)
        employees_tree.heading('name', text='NAME', anchor='w')
        employees_tree.heading('gender', text='GENDER', anchor='w')
        employees_tree.heading('phone', text='PHONE', anchor='w')
        employees_tree.heading('district', text='DISTRICT', anchor='w')

        employees_tree.pack(fill=BOTH, expand=True, pady=5, padx=5)

        self.showing_employees_in_tree()
        employees_tree.bind('<Double-1>', lambda event: self.double_click(event))

    def showing_employees_in_tree(self):
        employees_tree.delete(*employees_tree.get_children())
        employees_tree.tag_configure('color1', background='gray98')
        employees_tree.tag_configure('color2', background='white')

        my_tag = 'color2'
        # Getting data from database
        connection = sqlite3.connect(resource_path('munange.db'))
        cursor = connection.cursor()
        query = "SELECT employee_id, name, gender, phone, district FROM employees ORDER BY name ASC"
        cursor.execute(query)
        employees = cursor.fetchall()
        cursor.close()
        connection.close()
        count = 0
        for columns in employees:
            my_tag = 'color1' if my_tag == 'color2' else 'color2'
            employees_tree.insert(parent='', index='end', iid=count, values=(columns[0], columns[1], columns[2],
                                                                            columns[3], columns[4]), tags=my_tag)
            count += 1

    def searching_for_employees(self, event):
        employees_tree.delete(*employees_tree.get_children())
        employees_tree.tag_configure('color1', background='gray98')
        employees_tree.tag_configure('color2', background='white')
        my_tag = 'color2'

        # Getting data from database
        connection = sqlite3.connect(resource_path('munange.db'))
        cursor = connection.cursor()
        query = "SELECT employee_id, name, gender, phone, district FROM employees WHERE name LIKE ? ORDER BY name ASC"
        cursor.execute(query, (f'%{self.search_employees_entry.get().strip().upper()}%', ))
        employees = cursor.fetchall()
        cursor.close()
        connection.close()
        count = 0
        for columns in employees:
            my_tag = 'color1' if my_tag == 'color2' else 'color2'
            employees_tree.insert(parent='', index='end', iid=count, values=(columns[0], columns[1], columns[2],
                                                                            columns[3], columns[4]), tags=my_tag)

            count += 1
        if len(employees) == 0:
            MainWindow.__new__(MainWindow).unsuccessful_information(f'No employees match your search.')
        return len(employees)

    def print_or_download_students(self, isdirectory):
        from employees_excel import EmployeeExcel
        if isdirectory:
            directory = filedialog.askdirectory(title='Select folder to save this file')
            if directory:
                EmployeeExcel(directory)
                MainWindow.__new__(MainWindow).success_information('Employees file successfully saved.')
        else:
            MainWindow.__new__(MainWindow).success_information('Loading....')
            EmployeeExcel(False)

    def double_click(self, event):
        global row_double_click
        row_double_click = employees_tree.identify_row(event.y)
        employee_info = employees_tree.item(row_double_click, 'values')

        # print(employees_data)
        if row_double_click:
            from add_employees import AddEmployees
            employee_id = employee_info[0]
            connection = sqlite3.connect(resource_path('munange.db'))
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM employees WHERE employee_id='{employee_id}'")
            employees_data = cursor.fetchone()
            cursor.close()
            connection.close()

            AddEmployees.__new__(AddEmployees).updating_employee(self.display_window, employees_data)
        else:
            pass






