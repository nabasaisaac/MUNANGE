from customtkinter import *
from PIL import ImageTk, Image
class Customers:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        self.upper_buttons_frame = CTkFrame(self.display_window, bg_color='#3BA541', fg_color='#3BA541',
                                            )
        self.upper_buttons_frame.pack(fill=X)

        self.view_customers_button = CTkButton(self.upper_buttons_frame, text='View Customers', text_color='white',
                                        corner_radius=0, bg_color='#3BA541', fg_color='#3BA541', hover_color='#0C8A01',
                                        font=('roboto', 15), image=CTkImage(Image.open('icons/view_customers.png'),
                                        size=(20, 20)), compound=LEFT,  height=35, width=150, command=lambda:
                                        self.sliding(self.view_customers_button, self.view_customers))
        self.view_customers_button.pack(side=LEFT)

        self.add_customers_button = CTkButton(self.upper_buttons_frame, text='Customers', text_color='white',
                                        corner_radius=0, bg_color='#3BA541', fg_color='#3BA541', hover_color='#0C8A01',
                                        font=('roboto', 15), image=CTkImage(Image.open('icons/add.png'),
                                        size=(20, 20)), compound=LEFT,  height=35, width=150, command=lambda:
                                        self.sliding(self.add_customers_button, self.add_customers))
        self.add_customers_button.pack(side=LEFT, padx=(0, 5))

        self.sliding(self.view_customers_button, self.view_customers)
        # self.sliding(self.add_customers_button, self.add_customers)

    def view_customers(self):
        from view_customers import ViewCustomers
        ViewCustomers(self.display_window)

    def add_customers(self):
        from add_customers import AddCustomers
        AddCustomers(self.display_window)

    def hiding(self):
        self.view_customers_button.configure(fg_color='#3BA541')
        self.add_customers_button.configure(fg_color='#3BA541')

    def sliding(self, button, methods):
        self.hiding()
        for widgets in self.display_window.winfo_children()[2::]:
            widgets.destroy()

        button.configure(fg_color='#085f00')

        methods()





