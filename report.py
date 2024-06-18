from customtkinter import *
from PIL import ImageTk, Image


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

    def report(self):
        pass

    def hiding(self):
        self.report_button.configure(fg_color='#3BA541')
        # self.change_password_button.configure(fg_color='#3BA541')

    def sliding(self, button, methods):
        self.hiding()
        for widgets in self.display_window.winfo_children()[2::]:
            widgets.destroy()

        button.configure(fg_color='#085f00')

        methods()
