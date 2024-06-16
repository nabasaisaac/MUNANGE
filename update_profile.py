import sqlite3
import io
from customtkinter import *
from PIL import ImageTk, Image
from main_window import MainWindow
from tkinter import messagebox


class UpdateProfile:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        self.scrollable_frame = CTkScrollableFrame(self.display_window, fg_color='gray95', bg_color='gray95',
                                                   )
        self.scrollable_frame.pack(fill=BOTH, expand=True)

        self.side_frame = CTkFrame(self.scrollable_frame, bg_color='gray95', fg_color='white',
                                   corner_radius=15, )
        self.side_frame.pack(side=LEFT, fill=Y, padx=20, pady=20)

        self.basic_infor_frame = CTkFrame(self.scrollable_frame, bg_color='gray95', fg_color='white',
                                   corner_radius=15,)
        self.basic_infor_frame.pack(side=LEFT, pady=20, padx=(0, 20), fill=X, expand=True)
        connection = sqlite3.connect("munange.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM profile")
        user_details = cursor.fetchone()
        # print(user_details)

        global default_circular_image
        image = Image.open(io.BytesIO(user_details[1]))
        default_circular_image = MainWindow.__new__(MainWindow).make_circular_image(image)
        self.customer_photo_label = CTkLabel(self.side_frame, fg_color='white', bg_color='white', text='',
                                             image=CTkImage(default_circular_image, size=(150, 150)))
        self.customer_photo_label.pack(padx=80, pady=(80, 10))

        self.upload_photo_button = CTkButton(self.side_frame, bg_color='white', fg_color='#0C2844', font=('roboto', 15),
                                             text='Change Image', text_color='white', hover_color='#032F5B',
                                             text_color_disabled='white', command=self.update_photo)
        self.upload_photo_button.pack(pady=(0, 15))

        self.name = CTkLabel(self.side_frame, bg_color='white', fg_color='white', text=f'{user_details[2]}',
                             text_color='gray40', font=('roboto', 15, 'bold'))
        self.name.pack(fill=X, padx=20, pady=(0, 5))

        CTkLabel(self.side_frame, bg_color='white', fg_color='white', text='EMAIL',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w'
                 ).pack(fill=X, padx=20)

        self.email = CTkLabel(self.side_frame, bg_color='white', fg_color='white', text=f'{user_details[5]}',
                              text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w')
        self.email.pack(fill=X, padx=20)


        # working on customer basic information
        two_frames_holder = CTkFrame(self.basic_infor_frame, fg_color='white', bg_color='white')
        two_frames_holder.pack(fill=X, expand=True, pady=(10, 0))

        first_frame = CTkFrame(two_frames_holder, fg_color='white', bg_color='white')
        first_frame.pack(side=LEFT, fill=X, padx=20, pady=20, expand=True)

        second_frame = CTkFrame(two_frames_holder, fg_color='white', bg_color='white')
        second_frame.pack(side=LEFT, fill=BOTH, padx=(0, 20), pady=20, expand=True)
        self.basic_infor_label = CTkLabel(first_frame, bg_color='white', fg_color='white', text='User Profile',
                text_color='#0C2844', font=('roboto', 16, 'bold'), justify=LEFT, anchor='w')
        self.basic_infor_label.pack(fill=X, pady=(0, 10))

        CTkLabel(first_frame, bg_color='white', fg_color='white', text='Surname',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.sur_name_entry = CTkEntry(first_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                   border_width=1, height=35, text_color='#0C2844')
        self.sur_name_entry.pack(fill=X, pady=(0, 10))
        self.sur_name_entry.bind('<FocusIn>', lambda event: self.sur_name_entry.configure(border_color='#44aaee'))
        self.sur_name_entry.bind('<FocusOut>', lambda event: self.sur_name_entry.configure(border_color='#4CC053'))

        CTkLabel(first_frame, bg_color='white', fg_color='white', text='Other Names',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.other_name_entry = CTkEntry(first_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                   border_width=1, height=35, text_color='#0C2844')
        self.other_name_entry.pack(fill=X, pady=(0, 10))
        self.other_name_entry.bind('<FocusIn>', lambda event: self.other_name_entry.configure(border_color='#44aaee'))
        self.other_name_entry.bind('<FocusOut>', lambda event: self.other_name_entry.configure(border_color='#4CC053'))

        CTkLabel(first_frame, bg_color='white', fg_color='white', text='Email',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.email_entry = CTkEntry(first_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                   border_width=1, height=35, text_color='#0C2844', placeholder_text=
                                   'example@gmail.com', placeholder_text_color='gray50')
        self.email_entry.pack(fill=X, pady=(0, 10))
        self.email_entry.bind('<FocusIn>', lambda event: self.email_entry.configure(border_color='#44aaee'))
        self.email_entry.bind('<FocusOut>', lambda event: self.email_entry.configure(border_color='#4CC053'))

        CTkLabel(first_frame, bg_color='white', fg_color='white', text='National ID No.',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.id_number_entry = CTkEntry(first_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                   border_width=1, height=35, text_color='#0C2844', placeholder_text=
                                   "Customer's NIN", placeholder_text_color='gray50')
        self.id_number_entry.pack(fill=X)
        self.id_number_entry.bind('<FocusIn>', lambda event: self.id_number_entry.configure(border_color='#44aaee'))
        self.id_number_entry.bind('<FocusOut>', lambda event: self.id_number_entry.configure(border_color='#4CC053'))

        """Working on the second frame"""
        CTkLabel(second_frame, bg_color='white', fg_color='white', text='',
                text_color='#0C2844', font=('roboto', 16, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10))

        CTkLabel(second_frame, bg_color='white', fg_color='white', text='First Name',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.first_name_entry = CTkEntry(second_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                   border_width=1, height=35, text_color='#0C2844')
        self.first_name_entry.pack(fill=X, pady=(0, 10))
        self.first_name_entry.bind('<FocusIn>', lambda event: self.first_name_entry.configure(border_color='#44aaee'))
        self.first_name_entry.bind('<FocusOut>', lambda event: self.first_name_entry.configure(border_color='#4CC053'))

        CTkLabel(second_frame, bg_color='white', fg_color='white', text='Phone Number',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.phone_entry = CTkEntry(second_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                   border_width=1, height=35, text_color='#0C2844', placeholder_text=
                                   '07XXXXXXXXXX', placeholder_text_color='gray50')
        self.phone_entry.pack(fill=X, pady=(0, 10))
        self.phone_entry.bind('<FocusIn>', lambda event: self.phone_entry.configure(border_color='#44aaee'))
        self.phone_entry.bind('<FocusOut>', lambda event: self.phone_entry.configure(border_color='#4CC053'))

        CTkLabel(second_frame, bg_color='white', fg_color='white', text='Gender',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)

        self.gender_value = StringVar()
        self.gender_value.set('Select')
        self.genders = ['MALE', 'FEMALE']
        self.gender_combo = CTkComboBox(second_frame, variable=self.gender_value, text_color='gray20', border_color='#4CC053',
                                  fg_color='#f1fcf1', values=self.genders, border_width=1, bg_color='white', height=35,
                                  dropdown_fg_color='white', dropdown_hover_color='#DBEAFF', dropdown_text_color='black'
                                  , button_hover_color='#4CC053', button_color='#4CC053')
        self.gender_combo.pack(fill=X, pady=(0, 10))

        CTkLabel(second_frame, bg_color='white', fg_color='white', text='District',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.district_entry = CTkEntry(second_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                   border_width=1, height=35, text_color='#0C2844')
        self.district_entry.pack(fill=X)
        self.district_entry.bind('<FocusIn>', lambda event: self.district_entry.configure(border_color='#44aaee'))
        self.district_entry.bind('<FocusOut>', lambda event: self.district_entry.configure(border_color='#4CC053'))

        """Inserting other data in the entries"""
        if len(user_details[2].split()) >= 3:
            self.sur_name_entry.insert(0, user_details[2].split()[0])
            self.first_name_entry.insert(0, user_details[2].split()[1])
            self.other_name_entry.insert(0, user_details[2].split()[2::])
        else:
            self.sur_name_entry.insert(0, user_details[2].split()[0])
            self.first_name_entry.insert(0, user_details[2].split()[1])
        self.phone_entry.insert(0, user_details[4])
        self.gender_value.set(user_details[3])
        self.district_entry.insert(0, user_details[7])
        self.email_entry.insert(0, user_details[5])
        if user_details[6] == 'Not Provided':
            # self.id_number_entry.configure(placeholder_text_color="Customer's NIN")
            pass
        else:
            self.id_number_entry.insert(0, user_details[6])

        """Save customer button here"""
        self.save_frame = CTkFrame(self.basic_infor_frame, fg_color='white', bg_color='white')
        self.save_frame.pack(fill=X, padx=20, pady=(10, 80), expand=True)
        self.update_button = CTkButton(self.save_frame, bg_color='white', fg_color='#44aaee', hover_color='#2A9AE5',
                                     image=CTkImage(Image.open('icons/save.png'), size=(20, 20)), text_color='white',
                                     text='Update', command=lambda: self.update_my_profile(user_details))
        self.update_button.pack(side=RIGHT)

    def update_photo(self):

        try:
            self.new_passport_image_browsed = filedialog.askopenfilename(title='Select student passport photo',
                                                                filetypes=(
                                                                    ('jpg files', '*.jpg'), ('png files', '*.png'),
                                                                    ('All types', '*.*')))

            current_current_passport = Image.open(self.new_passport_image_browsed)

            circular_image = MainWindow.__new__(MainWindow).make_circular_image(current_current_passport)
            self.customer_photo_label.configure(image=CTkImage(circular_image, size=(150, 150)))
            self.previous_directory = self.new_passport_image_browsed
        except AttributeError:
            try:
                self.new_passport_image_browsed = self.previous_directory
            except AttributeError:
                pass

    def update_my_profile(self, user_details):
        
        condition1 = self.first_name_entry.get().strip() == '' or self.sur_name_entry.get().strip() == ''
        condition2 = (self.phone_entry.get().strip() == '' or self.gender_value.get().strip() == 'Select' or
                      self.district_entry.get().strip() == '' or self.email_entry.get().strip() == '')
        if condition1 or condition2:
            MainWindow.__new__(MainWindow).unsuccessful_information('All fields are required')
            return

        import re
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email_entry.get()):
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid email address')
            return

        if not self.phone_entry.get().strip().isdigit() or len(self.phone_entry.get().strip()) != 10:
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid phone number')
            return

        if self.gender_value.get() not in ['MALE', 'FEMALE']:
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid gender')
            return

        if self.id_number_entry.get().strip() == '':
            pass
        else:
            if not len(self.id_number_entry.get().strip()) == 14 or not self.id_number_entry.get().strip().isupper():
                MainWindow.__new__(MainWindow).unsuccessful_information('Invalid NIN')
                return

        connection = sqlite3.connect('munange.db')
        cursor = connection.cursor()

        if self.other_name_entry.get().strip():
            customer_name = (
                f"{self.sur_name_entry.get().strip().upper()} {self.first_name_entry.get().strip().upper()} "
                f"{self.other_name_entry.get().strip().upper()}")
        else:
            customer_name = f"{self.sur_name_entry.get().strip().upper()} {self.first_name_entry.get().strip().upper()}"

        try:
            with open(self.new_passport_image_browsed, 'rb') as f:
                photo = f.read()

            if not self.id_number_entry.get().strip():
                query = ("UPDATE profile SET photo=?, name=?, gender=?, phone=?, email=?, nin='Not Provided',"
                         " district=? WHERE user_id=?")

                cursor.execute(query, (photo, customer_name, self.gender_value.get().upper(),
                                       self.phone_entry.get().strip(), self.email_entry.get().strip(),
                                       self.district_entry.get().strip().upper(), user_details[0]))
            else:
                query = ("UPDATE profile SET photo=?, name=?, gender=?, phone=?, email=?, nin=?, district=? WHERE "
                         "user_id=?")
                cursor.execute(query, (
                    photo, customer_name, self.gender_value.get().upper(), self.phone_entry.get().strip(),
                    self.email_entry.get().strip(), self.id_number_entry.get().strip(),
                    self.district_entry.get().strip().upper(), user_details[0]))
            connection.commit()
            cursor.close()
            connection.close()
            for widget in self.display_window.winfo_children()[2:]:
                widget.destroy()
            UpdateProfile(self.display_window)
            MainWindow.__new__(MainWindow).getting_user_info()
            MainWindow.__new__(MainWindow).success_information(f'Profile successfully updated.')
            # self.back_to_view_customers()

        except Exception:
            photo = bytes(user_details[1])
            change_format = Image.open(io.BytesIO(user_details[1]))
            same_photo = MainWindow.__new__(MainWindow).make_circular_image(change_format)
            self.customer_photo_label.configure(image=CTkImage(same_photo, size=(150, 150)))
            if not self.id_number_entry.get().strip():
                query = ("UPDATE profile SET photo=?, name=?, gender=?, phone=?, email=?, nin='Not Provided',"
                         " district=? WHERE user_id=?")

                cursor.execute(query, (photo, customer_name, self.gender_value.get().upper(),
                                       self.phone_entry.get().strip(), self.email_entry.get().strip(),
                                       self.district_entry.get().strip().upper(), user_details[0]))

            else:
                query = ("UPDATE profile SET photo=?, name=?, gender=?, phone=?, email=?, nin=?, district=? WHERE "
                         "user_id=?")
                cursor.execute(query, (
                    photo, customer_name, self.gender_value.get().upper(), self.phone_entry.get().strip(),
                    self.email_entry.get().strip(), self.id_number_entry.get().strip(),
                    self.district_entry.get().strip().upper(), user_details[0]))
            connection.commit()
            cursor.close()
            connection.close()
            for widget in self.display_window.winfo_children()[2:]:
                widget.destroy()
            UpdateProfile(self.display_window)
            MainWindow.__new__(MainWindow).getting_user_info()
            MainWindow.__new__(MainWindow).success_information(f'Profile successfully updated.')


