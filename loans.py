from customtkinter import *
from PIL import ImageTk, Image


class Loans:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        self.upper_buttons_frame = CTkFrame(self.display_window, bg_color='#3BA541', fg_color='#3BA541',
                                            )
        self.upper_buttons_frame.pack(fill=X)

        self.view_borrowers_button = CTkButton(self.upper_buttons_frame, text='View Borrowers', text_color='white',
                                        corner_radius=0, bg_color='#3BA541', fg_color='#3BA541', hover_color='#0C8A01',
                                        font=('roboto', 15), image=CTkImage(Image.open('icons/view_customers.png'),
                                        size=(20, 20)), compound=LEFT,  height=35, width=150)
        self.view_borrowers_button.pack(side=LEFT)

        self.add_loan_button = CTkButton(self.upper_buttons_frame, text='Grant loan', text_color='white',
                                        corner_radius=0, bg_color='#3BA541', fg_color='#3BA541', hover_color='#0C8A01',
                                        font=('roboto', 15), image=CTkImage(Image.open('icons/add.png'),
                                        size=(20, 20)), compound=LEFT,  height=35, width=150)
        self.add_loan_button.pack(side=LEFT, padx=(0, 5))
