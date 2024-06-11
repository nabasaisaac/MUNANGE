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
                                        size=(20, 20)), compound=LEFT,  height=35, width=150, command=lambda:
                                        self.sliding(self.view_borrowers_button, self.view_borrowers))
        self.view_borrowers_button.pack(side=LEFT)

        self.add_loan_button = CTkButton(self.upper_buttons_frame, text='Grant loan', text_color='white',
                                        corner_radius=0, bg_color='#3BA541', fg_color='#3BA541', hover_color='#0C8A01',
                                        font=('roboto', 15), image=CTkImage(Image.open('icons/grant_loan.png'),
                                        size=(20, 20)), compound=LEFT,  height=35, width=150, command=lambda:
                                        self.sliding(self.add_loan_button, self.add_borrowers))
        self.add_loan_button.pack(side=LEFT, padx=(0, 5))

        """Initial opening here """
        # self.sliding(self.view_borrowers_button, self.view_borrowers)
        self.sliding(self.add_loan_button, self.add_borrowers)

    def view_borrowers(self):
        from view_borrowers import ViewBorrowers
        ViewBorrowers(self.display_window)

    def add_borrowers(self):
        from add_borrowers import AddBorrowers
        AddBorrowers(self.display_window)
        pass

    def hiding(self):
        self.view_borrowers_button.configure(fg_color='#3BA541')
        self.add_loan_button.configure(fg_color='#3BA541')

    def sliding(self, button, methods):
        self.hiding()
        for widgets in self.display_window.winfo_children()[2::]:
            widgets.destroy()

        button.configure(fg_color='#085f00')

        methods()


