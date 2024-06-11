from customtkinter import *
from PIL import ImageTk, Image


class Repayments:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        self.upper_buttons_frame = CTkFrame(self.display_window, bg_color='#3BA541', fg_color='#3BA541',
                                            )
        self.upper_buttons_frame.pack(fill=X)

        self.repay_debt_button = CTkButton(self.upper_buttons_frame, text='Clear debt', text_color='white',
                                        corner_radius=0, bg_color='#3BA541', fg_color='#3BA541', hover_color='#0C8A01',
                                        font=('roboto', 15), image=CTkImage(Image.open('icons/grant_loan.png'),
                                        size=(20, 20)), compound=LEFT,  height=35, width=150, command=lambda:
                                        self.sliding(self.repay_debt_button, self.repay_debt))
        self.repay_debt_button.pack(side=LEFT)

        self.sliding(self.repay_debt_button, self.repay_debt)
    def repay_debt(self):
        from repay_debt import RepayDebt
        RepayDebt(self.display_window)

    def hiding(self):
        self.repay_debt_button.configure(fg_color='#3BA541')
        # self.add_loan_button.configure(fg_color='#3BA541')

    def sliding(self, button, methods):
        self.hiding()
        for widgets in self.display_window.winfo_children()[2::]:
            widgets.destroy()

        button.configure(fg_color='#085f00')

        methods()