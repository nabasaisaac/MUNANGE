from customtkinter import *
from PIL import ImageTk, Image
from main_window import MainWindow


class ViewCustomers:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        self.scrollable_frame = CTkScrollableFrame(self.display_window, fg_color='gray95', bg_color='gray95',
                                                   )
        self.scrollable_frame.pack(fill=BOTH, expand=True)
        self.buttons_frame = CTkFrame(self.scrollable_frame, bg_color='gray95', fg_color='white')
        self.buttons_frame.pack(fill=X, pady=20, padx=10)

        CTkLabel(self.buttons_frame, text='Customers', text_color='#0C2844', fg_color='white', bg_color='white',
                 font=('roboto', 15), height=50).pack(side=LEFT, padx=20)

        self.download_button = CTkButton(self.buttons_frame, fg_color='#0C2844', bg_color='white', text='Download',
                                         text_color='white', font=('roboto', 15), compound=LEFT, width=100,
                                         image=CTkImage(Image.open('icons/download.png'), size=(20, 20)))
        self.download_button.pack(side=RIGHT, padx=10)

        self.print_button = CTkButton(self.buttons_frame, fg_color='#0C2844', bg_color='white', text='Print',
                                         text_color='white', font=('roboto', 15), compound=LEFT, width=100,
                                         image=CTkImage(Image.open('icons/print.png'), size=(15, 15)))
        self.print_button.pack(side=RIGHT, padx=(5, 0))

        self.search_customers_entry = CTkEntry(self.buttons_frame, bg_color='white',
                                               fg_color='gray95', border_width=0, placeholder_text='Search',
                                               placeholder_text_color='gray50', font=('roboto', 15),
                                               text_color='#0C2844', corner_radius=20, width=150)
        self.search_customers_entry.pack(side=RIGHT, padx=20)

        CTkLabel(self.search_customers_entry, bg_color='gray95', fg_color='gray95', text='', width=10,
                 image=CTkImage(Image.open('icons/search2.png'), size=(15, 15))).place(relx=0.8, rely=0.01)

        for i in range(100):
            CTkFrame(self.scrollable_frame, fg_color='white').pack()