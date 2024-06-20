from customtkinter import *
from PIL import Image

import os
import sys

# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Profile:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        self.upper_buttons_frame = CTkFrame(self.display_window, bg_color='#3BA541', fg_color='#3BA541',
                                            )
        self.upper_buttons_frame.pack(fill=X)

        self.update_profile_button = CTkButton(self.upper_buttons_frame, text='Update Profile', text_color='white',
                                        corner_radius=0, bg_color='#3BA541', fg_color='#3BA541', hover_color='#0C8A01',
                                        font=('roboto', 15), image=CTkImage(Image.open(resource_path('icons/user_profile.png')),
                                        size=(15, 15)), compound=LEFT,  height=35, width=150, command=lambda:
                                        self.sliding(self.update_profile_button, self.update_profile))
        self.update_profile_button.pack(side=LEFT)

        self.change_password_button = CTkButton(self.upper_buttons_frame, text='Change Password', text_color='white',
                                        corner_radius=0, bg_color='#3BA541', fg_color='#3BA541', hover_color='#0C8A01',
                                        font=('roboto', 15), image=CTkImage(Image.open(resource_path('icons/preferences2.png')),
                                        size=(15, 15)), compound=LEFT,  height=35, width=150, command=lambda:
                                        self.sliding(self.change_password_button, self.change_password))
        self.change_password_button.pack(side=LEFT, padx=(0, 5))

        self.sliding(self.update_profile_button, self.update_profile)

    def update_profile(self):
        from update_profile import UpdateProfile
        UpdateProfile(self.display_window)

    def change_password(self):
        from change_password import ChangePassword
        ChangePassword(self.display_window)

    def hiding(self):
        self.update_profile_button.configure(fg_color='#3BA541')
        self.change_password_button.configure(fg_color='#3BA541')

    def sliding(self, button, methods):
        self.hiding()
        for widgets in self.display_window.winfo_children()[2::]:
            widgets.destroy()

        button.configure(fg_color='#085f00')

        methods()


