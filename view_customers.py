from customtkinter import *
from PIL import ImageTk, Image
from main_window import MainWindow
from tkinter import ttk
import sqlite3


class ViewCustomers:
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

        CTkLabel(self.buttons_frame, text='Customers', text_color='#0C2844', fg_color='white', bg_color='white',
                 font=('roboto', 16), height=50).pack(side=LEFT, padx=20)

        self.download_button = CTkButton(self.buttons_frame, fg_color='#0C2844', bg_color='white', text='Download',
                                         text_color='white', font=('roboto', 15), compound=LEFT, width=100,
                                         image=CTkImage(Image.open('icons/download.png'), size=(20, 20)),
                                         command=lambda: self.print_or_download_students(True))
        self.download_button.pack(side=RIGHT, padx=10)

        self.print_button = CTkButton(self.buttons_frame, fg_color='#0C2844', bg_color='white', text='Print',
                                         text_color='white', font=('roboto', 15), compound=LEFT, width=100,
                                         image=CTkImage(Image.open('icons/print.png'), size=(15, 15)),
                                      command=lambda: self.print_or_download_students(False))
        self.print_button.pack(side=RIGHT, padx=(5, 0))

        self.search_customers_entry = CTkEntry(self.buttons_frame, bg_color='white',
                                               fg_color='gray95', border_width=0, placeholder_text='Search',
                                               placeholder_text_color='gray50', font=('roboto', 15),
                                               text_color='#0C2844', corner_radius=20, width=150)
        self.search_customers_entry.pack(side=RIGHT, padx=20)
        self.search_customers_entry.bind('<KeyRelease>', self.searching_for_customers)

        CTkLabel(self.search_customers_entry, bg_color='gray95', fg_color='gray95', text='', width=10,
                 image=CTkImage(Image.open('icons/search2.png'), size=(15, 15))).place(relx=0.8, rely=0.01)
        self.working_on_treeview(self.scrollable_frame)

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
        customers_tree['columns'] = ['customer_id', 'name', 'gender', 'phone', 'district']
        # format columns
        customers_tree.column('#0', width=0, stretch=NO)
        customers_tree.column('customer_id', width=150, minwidth=150, anchor=CENTER)
        customers_tree.column('name', width=300, minwidth=200, anchor='w')
        customers_tree.column('gender', width=150, minwidth=100, anchor='w')
        customers_tree.column('phone', width=150, minwidth=120, anchor='w')
        customers_tree.column('district', width=150, minwidth=120, anchor='w')

        # creating headings
        customers_tree.heading('#0', text='')
        customers_tree.heading('customer_id', text='CUSTOMER ID', anchor=CENTER)
        customers_tree.heading('name', text='NAME', anchor='w')
        customers_tree.heading('gender', text='GENDER', anchor='w')
        customers_tree.heading('phone', text='PHONE', anchor='w')
        customers_tree.heading('district', text='DISTRICT', anchor='w')

        customers_tree.pack(fill=BOTH, expand=True, pady=5, padx=5)

        self.showing_customers_in_tree()
        customers_tree.bind('<Double-1>', lambda event: self.double_click(event))

    def showing_customers_in_tree(self):
        customers_tree.delete(*customers_tree.get_children())
        customers_tree.tag_configure('color1', background='gray98')
        customers_tree.tag_configure('color2', background='white')

        my_tag = 'color2'
        # Getting data from database
        connection = sqlite3.connect('munange.db')
        cursor = connection.cursor()
        query = "SELECT customer_id, name, gender, phone, district FROM customers ORDER BY name ASC"
        cursor.execute(query)
        customers = cursor.fetchall()
        cursor.close()
        connection.close()
        count = 0
        for columns in customers:
            my_tag = 'color1' if my_tag == 'color2' else 'color2'
            customers_tree.insert(parent='', index='end', iid=count, values=(columns[0], columns[1], columns[2],
                                                                            columns[3], columns[4]), tags=my_tag)
            count += 1

    def searching_for_customers(self, event):
        customers_tree.delete(*customers_tree.get_children())
        customers_tree.tag_configure('color1', background='gray98')
        customers_tree.tag_configure('color2', background='white')
        my_tag = 'color2'

        # Getting data from database
        connection = sqlite3.connect('munange.db')
        cursor = connection.cursor()
        query = "SELECT customer_id, name, gender, phone, district FROM customers WHERE name LIKE ? ORDER BY name ASC"
        cursor.execute(query, (f'%{self.search_customers_entry.get().strip().upper()}%', ))
        customers = cursor.fetchall()
        cursor.close()
        connection.close()
        count = 0
        for columns in customers:
            my_tag = 'color1' if my_tag == 'color2' else 'color2'
            customers_tree.insert(parent='', index='end', iid=count, values=(columns[0], columns[1], columns[2],
                                                                            columns[3], columns[4]), tags=my_tag)

            count += 1
        if len(customers) == 0:
            MainWindow.__new__(MainWindow).unsuccessful_information(f'No customers match your search.')
        return len(customers)

    def print_or_download_students(self, isdirectory):
        from customers_cards import CustomerExcel
        if isdirectory:
            directory = filedialog.askdirectory(title='Select folder to save this file')
            if directory:
                CustomerExcel(directory)
                MainWindow.__new__(MainWindow).success_information('Customers file successfully saved.')
        else:
            MainWindow.__new__(MainWindow).success_information('Loading....')
            CustomerExcel(False)

    def double_click(self, event):
        global row_double_click
        row_double_click = customers_tree.identify_row(event.y)
        customer_info = customers_tree.item(row_double_click, 'values')

        # print(customers_data)
        if row_double_click:
            from add_customers import AddCustomers
            connection = sqlite3.connect('munange.db')
            cursor = connection.cursor()
            customer_id = customer_info[0]
            cursor.execute(f"SELECT * FROM customers WHERE customer_id='{customer_id}'")
            customers_data = cursor.fetchone()
            cursor.close()
            connection.close()
            AddCustomers.__new__(AddCustomers).updating_customer(self.display_window, customers_data)
        else:
            pass






