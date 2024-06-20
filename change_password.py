from customtkinter import *
from main_window import MainWindow
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


class ChangePassword:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        self.info_frame = CTkFrame(self.display_window, fg_color='white', bg_color='gray95', corner_radius=10)
        self.info_frame.pack(pady=30)

        self.infor = CTkLabel(self.info_frame, text='Forgot your password? You can change it using an email associated \n'
                'with your account.', text_color='#2ea5de', bg_color='gray95', font=('roboto', 15, 'bold'),
                 corner_radius=10, fg_color='#d1f3ff',
                compound=LEFT, justify=LEFT, anchor='w')
        self.infor.pack(fill=X, ipadx=30, ipady=20)

        CTkLabel(self.info_frame, text='Old Password', justify=LEFT, anchor='w'
                 , text_color='#0C2844', bg_color='white', font=('roboto', 15),
                 ).pack(fill=X, padx=20, expand=True, pady=(10, 0))
        self.old_entry = CTkEntry(self.info_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                   border_width=1, height=35, text_color='#0C2844', font=('roboto', 15))
        self.old_entry.pack(fill=X, pady=(0, 10), padx=20, expand=True)
        self.old_entry.bind('<FocusIn>', lambda event: self.old_entry.configure(border_color='#44aaee'))
        self.old_entry.bind('<FocusOut>', lambda event: self.old_entry.configure(border_color='#4CC053'))
        self.old_entry.bind('<Return>', self.change_password_command)

        label_frame = CTkFrame(self.info_frame, fg_color='white', bg_color='white', corner_radius=0)
        label_frame.pack(padx=20, fill=X, pady=(20, 0))
        CTkLabel(label_frame, text='New Username', justify=LEFT, anchor='w'
                 , text_color='#0C2844', bg_color='white', font=('roboto', 15,)
                 ).pack(side=LEFT, fill=X, padx=(0, 20), expand=True)
        CTkLabel(label_frame, text='New Password', justify=LEFT, anchor='w'
                 , text_color='#0C2844', bg_color='white', font=('roboto', 15),
                 ).pack(side=LEFT, fill=X, padx=(10, 0), expand=True)

        entry_frame = CTkFrame(self.info_frame, fg_color='white', bg_color='white', corner_radius=0)
        entry_frame.pack(padx=20, fill=X)
        # CTkLabel(first_frame, bg_color='white', fg_color='white', text='Amount',
        #          text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.username_entry = CTkEntry(entry_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                       border_width=1, height=35, text_color='#0C2844', font=('roboto', 15))
        self.username_entry.pack(side=LEFT, fill=X, pady=(0, 10), padx=(0, 20), expand=True)
        self.username_entry.bind('<FocusIn>', lambda event: self.username_entry.configure(border_color='#44aaee'))
        self.username_entry.bind('<FocusOut>', lambda event: self.username_entry.configure(border_color='#4CC053'))

        self.password_entry = CTkEntry(entry_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                       border_width=1, height=35, text_color='#0C2844', font=('roboto', 15))
        self.password_entry.pack(side=LEFT, fill=X, pady=(0, 10), padx=(10, 0), expand=True)
        self.password_entry.bind('<FocusIn>', lambda event: self.password_entry.configure(border_color='#44aaee'))
        self.password_entry.bind('<FocusOut>', lambda event: self.password_entry.configure(border_color='#4CC053'))
        self.password_entry.bind('<Return>', self.change_password_command)
        self.submit_button = CTkButton(self.info_frame, bg_color='white', fg_color='#3BA541', hover_color='#2D9834',
                                       text_color='white', text='Submit', font=('roboto', 15), border_color='#3BA541',
                                       border_width=1, height=35,
                                       command=lambda: self.change_password_command(None))
        self.submit_button.pack(side=RIGHT, padx=20, pady=(10, 20))

    def change_password_command(self, event):
        connection = sqlite3.connect(resource_path('munange.db'))
        cursor = connection.cursor()
        cursor.execute("SELECT password FROM profile WHERE user_id=1")
        old_password = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        if not self.username_entry.get().strip() or not self.password_entry.get().strip() or not self.old_entry.get().strip():
            MainWindow.__new__(MainWindow).unsuccessful_information("All fields are required")
            return
        elif self.old_entry.get() != old_password:
            MainWindow.__new__(MainWindow).unsuccessful_information("Old password is incorrect")
            return
        elif self.password_entry.get().strip() == old_password:
            MainWindow.__new__(MainWindow).unsuccessful_information("New password cannot match the old password.")
            return
        elif len(self.username_entry.get().strip()) < 4:
            MainWindow.__new__(MainWindow).unsuccessful_information("Username is very short")
            return
        elif len(self.password_entry.get().strip()) < 4:
            MainWindow.__new__(MainWindow).unsuccessful_information("New password is very weak")
            return
        else:
            connection = sqlite3.connect(resource_path('munange.db'))
            cursor = connection.cursor()
            cursor.execute("UPDATE profile SET username=?, password=? WHERE user_id=1",
                           (self.username_entry.get().strip(), self.password_entry.get()))
            connection.commit()
            cursor.close()
            connection.close()
            MainWindow.__new__(MainWindow).success_information("Username and Password successfully changed")
            self.old_entry.delete(0, END)
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)

            return


