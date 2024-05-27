import sqlite3

from customtkinter import *
from PIL import ImageTk, Image
from main_window import MainWindow

class AddCustomers:
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

        global default_circular_image
        image = Image.open('images/default_photo.png')
        default_circular_image = MainWindow.__new__(MainWindow).make_circular_image(image)
        self.customer_photo_label = CTkLabel(self.side_frame, fg_color='white', bg_color='white', text='',
                                             image=CTkImage(default_circular_image, size=(150, 150)))
        self.customer_photo_label.pack(padx=80, pady=(80, 10))

        self.upload_photo_button = CTkButton(self.side_frame, bg_color='white', fg_color='#0C2844', font=('roboto', 15),
                                             text='Upload photo', text_color='white', hover_color='#032F5B',
                                             command=self.uploading_photo)
        self.upload_photo_button.pack(pady=(0, 15))

        self.note_label = CTkLabel(self.side_frame, bg_color='white', fg_color='white', text='WARNING',
                                   text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w')
        self.note_label.pack(fill=X, expand=True, padx=20, pady=(0, 5))

        self.warning_text = CTkLabel(self.side_frame, bg_color='white', fg_color='white', text='● Each new member is '
                                   'required to have\n     UGX. 5000 for a new log book. \n● No new member should be '
                                    'registered\n     without this fee.',
                                   text_color='gray30', font=('roboto', 15), justify=LEFT, anchor='w')
        self.warning_text.pack(padx=20, pady=(0, 100))

        # working on customer basic information
        two_frames_holder = CTkFrame(self.basic_infor_frame, fg_color='white', bg_color='white')
        two_frames_holder.pack(fill=X, expand=True, pady=(10, 0))

        first_frame = CTkFrame(two_frames_holder, fg_color='white', bg_color='white')
        first_frame.pack(side=LEFT, fill=X, padx=20, pady=20, expand=True)

        second_frame = CTkFrame(two_frames_holder, fg_color='white', bg_color='white')
        second_frame.pack(side=LEFT, fill=BOTH, padx=(0, 20), pady=20, expand=True)
        CTkLabel(first_frame, bg_color='white', fg_color='white', text='Basic Information',
                text_color='#0C2844', font=('roboto', 16, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10))

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
        self.genders = ['Male', 'Female']
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

        """Save customer button here"""
        save_frame = CTkFrame(self.basic_infor_frame, fg_color='white', bg_color='white')
        save_frame.pack(fill=X, padx=20, pady=(10, 80), expand=True)
        self.save_button = CTkButton(save_frame, bg_color='white', fg_color='#44aaee', hover_color='#2A9AE5',
                                     image=CTkImage(Image.open('icons/save.png'), size=(20, 20)), text_color='white',
                                     text='Save', command=self.saving_customer)
        self.save_button.pack(side=RIGHT)

    def uploading_photo(self):
        try:
            self.passport_image_browsed = 'images/default_photo.png'
            self.passport_image_browsed = filedialog.askopenfilename(title='Select student passport photo',
                                                                filetypes=(('jpg files', '*.jpg'), ('png files', '*.png'),
                                                                           ('All types', '*.*')))

            current_current_passport = Image.open(self.passport_image_browsed)

            circular_image = MainWindow.__new__(MainWindow).make_circular_image(current_current_passport)
            self.customer_photo_label.configure(image=CTkImage(circular_image, size=(150, 150)))
        except AttributeError:
            self.passport_image_browsed = 'images/default_photo.png'
            current_current_passport = Image.open(self.passport_image_browsed)
            circular_image = MainWindow.__new__(MainWindow).make_circular_image(current_current_passport)
            self.customer_photo_label.configure(image=CTkImage(circular_image, size=(150, 150)))

    def saving_customer(self):
        condition1 = self.first_name_entry.get().strip() == '' or self.sur_name_entry.get().strip() == ''
        condition2 = (self.phone_entry.get().strip() == '' or self.gender_value.get().strip() == 'Select' or
                      self.district_entry.get().strip() == '')
        if condition1 or condition2:
            MainWindow.__new__(MainWindow).unsuccessful_information('All fields are required')
            return

        if self.email_entry.get().strip():
            import re
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email_entry.get()):
                MainWindow.__new__(MainWindow).unsuccessful_information('Invalid email address')
                return

        elif not self.phone_entry.get().strip().isdigit() or len(self.phone_entry.get().strip()) > 10:
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid phone number')
            return

        if not self.gender_value.get() in ['Male', 'Female']:
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid gender')
            return

        if self.id_number_entry.get():
            if not len(self.id_number_entry.get().strip()) == 14 or not self.id_number_entry.get().strip().isupper():
                MainWindow.__new__(MainWindow).unsuccessful_information('Invalid NIN')
                return

        else:
            def resetting_fields():
                self.sur_name_entry.delete(0, END)
                self.first_name_entry.delete(0, END)
                if self.other_name_entry.get() == '':
                    pass
                else:
                    self.other_name_entry.delete(0, END)
                self.customer_photo_label.configure(image=CTkImage(default_circular_image, size=(150, 150)))
                self.passport_image_browsed = 'images/default_photo.png'
                self.id_number_entry.delete(0, END)
                self.phone_entry.delete(0, END)
                self.district_entry.delete(0, END)
                self.email_entry.delete(0, END)
                self.sur_name_entry.focus_set()

            connection = sqlite3.connect('munange.db')
            cursor = connection.cursor()

            if self.other_name_entry.get():
                customer_name = (f"{self.sur_name_entry.get().strip().upper()} {self.first_name_entry.get().strip().upper()} "
                                 f"{self.other_name_entry.get().strip().upper()}")
            else:
                customer_name = f"{self.sur_name_entry.get().strip().upper()} {self.first_name_entry.get().strip().upper()}"
            try:
                with open(self.passport_image_browsed, 'rb') as f:
                    photo = f.read()
                if self.email_entry.get() and not self.id_number_entry.get():
                    query = "INSERT INTO customers (photo, name, gender, phone, email, district) VALUES (?, ?, ?, ?, ?, ?)"
                    cursor.execute(query, (photo, customer_name, self.gender_value.get().upper(),
                                           self.phone_entry.get().strip(), self.email_entry.get().strip(),
                                           self.district_entry.get().strip().upper()))

                elif not self.email_entry.get() and self.id_number_entry.get():

                    query = "INSERT INTO customers (photo, name, gender, nin, district) VALUES (?, ?, ?, ?, ?)"
                    cursor.execute(query, (photo, customer_name, self.gender_value.get().upper(),
                                           self.id_number_entry.get().strip(), self.district_entry.get().strip().upper()))

                elif not self.email_entry.get() and not self.id_number_entry.get():

                    query = "INSERT INTO customers (photo, name, gender, phone, district) VALUES (?, ?, ?, ?, ?)"
                    cursor.execute(query, (photo, customer_name, self.gender_value.get().upper(),
                                           self.phone_entry.get().strip(), self.district_entry.get().strip().upper()))

                else:
                    query = "INSERT INTO customers (photo, name, gender, phone, email, nin, district) VALUES (?, ?, ?, ?, ?, ?, ?)"
                    cursor.execute(query, (photo, customer_name, self.gender_value.get().upper(), self.phone_entry.get().strip(),
                                           self.email_entry.get().strip(), self.id_number_entry.get().strip(),
                                           self.district_entry.get().strip().upper()))
                connection.commit()
                cursor.close()
                connection.close()
                MainWindow.__new__(MainWindow).success_information(f'Customer successfully registered.')
                resetting_fields()

            except AttributeError:
                self.passport_image_browsed = 'images/default_photo.png'
                self.saving_customer()










