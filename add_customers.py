import sqlite3
import io
from customtkinter import *
from PIL import ImageTk, Image
from main_window import MainWindow
from tkinter import messagebox


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
                                             text_color_disabled='white', command=self.uploading_photo)
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
        self.basic_infor_label = CTkLabel(first_frame, bg_color='white', fg_color='white', text='Basic Information',
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

        """Save customer button here"""
        self.save_frame = CTkFrame(self.basic_infor_frame, fg_color='white', bg_color='white')
        self.save_frame.pack(fill=X, padx=20, pady=(10, 80), expand=True)
        self.save_button = CTkButton(self.save_frame, bg_color='white', fg_color='#44aaee', hover_color='#2A9AE5',
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

        if self.email_entry.get().strip() == '':
            pass
        else:
            import re
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email_entry.get()):
                MainWindow.__new__(MainWindow).unsuccessful_information('Invalid email address')
                return

        if not self.phone_entry.get().strip().isdigit() or len(self.phone_entry.get().strip()) != 10:
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid phone number')
            return

        if not self.gender_value.get() in ['MALE', 'FEMALE']:
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid gender')
            return
        if self.id_number_entry.get().strip() == '':
            pass
        else:
            if not len(self.id_number_entry.get().strip()) == 14 or not self.id_number_entry.get().strip().isupper():
                MainWindow.__new__(MainWindow).unsuccessful_information('Invalid NIN')
                return

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
            customer_name = (
                f"{self.sur_name_entry.get().strip().upper()} {self.first_name_entry.get().strip().upper()} "
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
                cursor.execute(query,
                               (photo, customer_name, self.gender_value.get().upper(), self.phone_entry.get().strip(),
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

    def updating_customer(self, window, customer_data):
        self.customer_data = customer_data
        for widget in window.winfo_children()[2:]:
            widget.destroy()
        self.display_window = window
        self.designing_window()

        image = Image.open(io.BytesIO(customer_data[1]))
        customer_photo = MainWindow.__new__(MainWindow).make_circular_image(image)
        self.customer_photo_label.configure(image=CTkImage(customer_photo, size=(150, 150)))

        self.note_label.pack_forget()
        self.warning_text.pack_forget()

        self.name = CTkLabel(self.side_frame, bg_color='white', fg_color='white', text=f'{customer_data[2]}',
                                   text_color='gray40', font=('roboto', 15, 'bold'))
        self.name.pack(fill=X, padx=20, pady=(0, 5))

        CTkLabel(self.side_frame, bg_color='white', fg_color='white', text='EMAIL',
                                   text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w'
                 ).pack(fill=X, padx=20)

        self.email = CTkLabel(self.side_frame, bg_color='white', fg_color='white', text=f'{customer_data[5]}',
                                   text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w')
        self.email.pack(fill=X, padx=20)

        CTkLabel(self.side_frame, bg_color='white', fg_color='white', text='ACCESS NO',
                                   text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w'
                 ).pack(fill=X, padx=20, pady=(5, 0))

        self.access_no = CTkLabel(self.side_frame, bg_color='white', fg_color='white', text=f'{customer_data[0]}',
                                   text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w')
        self.access_no.pack(fill=X, padx=20)

        self.back_button = CTkButton(self.side_frame, bg_color='white', fg_color='#0C2844', font=('roboto', 15),
                                    text='Back', text_color='white', compound=LEFT,
                                    image=CTkImage(Image.open('icons/back_image.png')), width=20,
                                    command=self.back_to_view_customers)
        self.back_button.pack(side=LEFT, pady=(0, 10), padx=(20, 0))
        self.guarantor = CTkButton(self.side_frame, bg_color='white', fg_color='#b7c1d1', font=('roboto', 15),
                                    text='', text_color='#0C2844', compound=LEFT, hover_color='#98a6bd',
                                    image=CTkImage(Image.open('icons/guarantor.png')), width=20)
                                    # command=self.back_to_view_customers)
        self.guarantor.pack(side=RIGHT, pady=(0, 10), padx=(0, 20))

        connection = sqlite3.connect('munange.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM guarantors WHERE guarantor_id=?", (customer_data[0],))
        guarantor_details = cursor.fetchone()
        # print(guarantor_details)
        if not guarantor_details:
            self.guarantor.configure(text='Add Guarantor', command=lambda: self.add_guarantor(customer_data))
        else:
            self.guarantor.configure(text='View Guarantor', command=lambda: self.view_guarantor(guarantor_details))
        cursor.close()
        connection.close()

        if len(customer_data[2].split()) >= 3:
            self.sur_name_entry.insert(0, customer_data[2].split()[0])
            self.first_name_entry.insert(0, customer_data[2].split()[1])
            self.other_name_entry.insert(0, customer_data[2].split()[2::])
        else:
            self.sur_name_entry.insert(0, customer_data[2].split()[0])
            self.first_name_entry.insert(0, customer_data[2].split()[1])
        self.phone_entry.insert(0, customer_data[4])
        self.gender_value.set(customer_data[3])
        if customer_data[5] == 'Not Provided':
            # self.email_entry.configure(placeholder_text_color='example@gmail.com')
            pass
        else:
            self.email_entry.insert(0, customer_data[5])
        if customer_data[6] == 'Not Provided':
            # self.id_number_entry.configure(placeholder_text_color="Customer's NIN")
            pass
        else:
            self.id_number_entry.insert(0, customer_data[6])

        self.district_entry.insert(0, customer_data[7])

        self.delete_button = CTkButton(self.save_frame, bg_color='white', fg_color='#ff5c5c', font=('roboto', 15),
                                    text='Delete', text_color='white', compound=LEFT, width=100, hover_color='#ff3f3f',
                                    image=CTkImage(Image.open('icons/DELETE.png'), size=(15, 15)),
                                    command=lambda: self.deleting_customer(customer_data))
        self.delete_button.pack(side=RIGHT, padx=(0, 15))

        self.upload_photo_button.configure(text='Change Image', command=self.update_photo)
        self.save_button.configure(width=100, text='Update', command=lambda: self.update_customer_command(customer_data))

    def update_customer_command(self, customer_data):
        condition1 = self.first_name_entry.get().strip() == '' or self.sur_name_entry.get().strip() == ''
        condition2 = (self.phone_entry.get().strip() == '' or self.gender_value.get().strip() == 'Select' or
                      self.district_entry.get().strip() == '')
        if condition1 or condition2:
            MainWindow.__new__(MainWindow).unsuccessful_information('All fields are required')
            return

        if self.email_entry.get().strip() == '':
            pass
        else:
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

            if self.email_entry.get().strip() and not self.id_number_entry.get().strip():
                query = ("UPDATE customers SET photo=?, name=?, gender=?, phone=?, email=?, nin='Not Provided',"
                         " district=? WHERE customer_id=?")

                cursor.execute(query, (photo, customer_name, self.gender_value.get().upper(),
                                       self.phone_entry.get().strip(), self.email_entry.get().strip(),
                                       self.district_entry.get().strip().upper(), customer_data[0]))

            elif not self.email_entry.get().strip() and self.id_number_entry.get().strip():

                query = ("UPDATE customers SET photo=?, name=?, gender=?, phone=?, email='Not Provided',"
                         " nin=?, district=? WHERE customer_id=?")

                cursor.execute(query, (photo, customer_name, self.gender_value.get().upper(),
                                       self.phone_entry.get().strip(), self.id_number_entry.get().strip(),
                                       self.district_entry.get().strip().upper(), customer_data[0]))

            elif not self.email_entry.get().strip() and not self.id_number_entry.get().strip():
                print('second phase')
                query = ("UPDATE customers SET photo=?, name=?, gender=?, phone=?, email='Not Provided',"
                         " nin='Not Provided', district=? WHERE customer_id=?")

                cursor.execute(query, (photo, customer_name, self.gender_value.get().upper(),
                                       self.phone_entry.get().strip(), self.district_entry.get().strip().upper()
                                       , customer_data[0]))

            else:
                query = ("UPDATE customers SET photo=?, name=?, gender=?, phone=?, email=?, nin=?, district=? WHERE "
                         "customer_id=?")
                cursor.execute(query, (
                    photo, customer_name, self.gender_value.get().upper(), self.phone_entry.get().strip(),
                    self.email_entry.get().strip(), self.id_number_entry.get().strip(),
                    self.district_entry.get().strip().upper(), customer_data[0]))
            connection.commit()
            cursor.close()
            connection.close()
            MainWindow.__new__(MainWindow).success_information(f'Customer successfully updated.')
            self.back_to_view_customers()
        except Exception:
            photo = bytes(customer_data[1])
            change_format = Image.open(io.BytesIO(customer_data[1]))
            self.customer_photo_label.configure(image=CTkImage(change_format, size=(125, 130)))
            if self.email_entry.get().strip() and not self.id_number_entry.get().strip():
                query = ("UPDATE customers SET photo=?, name=?, gender=?, phone=?, email=?, nin='Not Provided',"
                         " district=? WHERE customer_id=?")

                cursor.execute(query, (photo, customer_name, self.gender_value.get().upper(),
                                       self.phone_entry.get().strip(), self.email_entry.get().strip(),
                                       self.district_entry.get().strip().upper(), customer_data[0]))

            elif not self.email_entry.get().strip() and self.id_number_entry.get().strip():

                query = ("UPDATE customers SET photo=?, name=?, gender=?, phone=?, email='Not Provided',"
                         " nin=?, district=? WHERE customer_id=?")

                cursor.execute(query, (photo, customer_name, self.gender_value.get().upper(),
                                       self.phone_entry.get().strip(), self.id_number_entry.get().strip(),
                                       self.district_entry.get().strip().upper(), customer_data[0]))

            elif not self.email_entry.get().strip() and not self.id_number_entry.get().strip():
                query = ("UPDATE customers SET photo=?, name=?, gender=?, phone=?, email='Not Provided',"
                         " nin='Not Provided', district=? WHERE customer_id=?")

                cursor.execute(query, (photo, customer_name, self.gender_value.get().upper(),
                                       self.phone_entry.get().strip(), self.district_entry.get().strip().upper()
                                       , customer_data[0]))

            else:
                query = ("UPDATE customers SET photo=?, name=?, gender=?, phone=?, email=?, nin=?, district=? WHERE "
                         "customer_id=?")
                cursor.execute(query, (
                    photo, customer_name, self.gender_value.get().upper(), self.phone_entry.get().strip(),
                    self.email_entry.get().strip(), self.id_number_entry.get().strip(),
                    self.district_entry.get().strip().upper(), customer_data[0]))
            connection.commit()
            cursor.close()
            connection.close()
            MainWindow.__new__(MainWindow).success_information(f'Customer successfully updated.')
            self.back_to_view_customers()

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

    def back_to_view_customers(self):
        for widget in self.display_window.winfo_children()[2:]:
            widget.destroy()
        from view_customers import ViewCustomers
        ViewCustomers(self.display_window)

    def deleting_customer(self, customer_data):
        confirm_deletion = messagebox.askyesno('Confirm deletion', f'Are you sure you want to \n'
                                                f'permanently delete {customer_data[2].split()[-1]}',
                                               parent=self.display_window)
        if confirm_deletion:
            connection = sqlite3.connect('munange.db')
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(f"DELETE FROM customers WHERE customer_id='{customer_data[0]}'")
            connection.commit()
            cursor.close()
            connection.close()
            MainWindow.__new__(MainWindow).success_information(f'Customer successfully deleted.')
            self.back_to_view_customers()

    def emptying_data_fields(self):
        self.upload_photo_button.configure(state=DISABLED)
        # self.basic_infor_label.configure(text='Add a guarantor')
        self.sur_name_entry.delete(0, END)
        self.first_name_entry.delete(0, END)
        self.other_name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.id_number_entry.delete(0, END)
        self.district_entry.delete(0, END)
        self.gender_value.set('Select')
        # self.delete_button.pack_forget()
        # self.save_button.configure(text='Save', command=lambda : self.save_guarantor(customer_data))
        self.phone_entry.focus_set()
        self.email_entry.focus_set()
        self.id_number_entry.focus_set()
        self.sur_name_entry.focus_set()

    def add_guarantor(self, customer_data):
        self.emptying_data_fields()
        self.basic_infor_label.configure(text='Add a guarantor')
        self.delete_button.pack_forget()
        self.save_button.configure(text='Save', command=lambda : self.save_guarantor(customer_data))

    def save_guarantor(self, customer_data):
        condition1 = self.first_name_entry.get().strip() == '' or self.sur_name_entry.get().strip() == ''
        condition2 = (self.phone_entry.get().strip() == '' or self.gender_value.get().strip() == 'Select' or
                      self.district_entry.get().strip() == '')
        if condition1 or condition2:
            MainWindow.__new__(MainWindow).unsuccessful_information('All fields are required')
            return

        if self.email_entry.get().strip() == '':
            pass
        else:
            import re
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email_entry.get()):
                MainWindow.__new__(MainWindow).unsuccessful_information('Invalid email address')
                return

        if not self.phone_entry.get().strip().isdigit() or len(self.phone_entry.get().strip()) != 10:
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid phone number')
            return

        if not self.gender_value.get() in ['MALE', 'FEMALE']:
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

        if self.other_name_entry.get():
            guarantor_name = (
                f"{self.sur_name_entry.get().strip().upper()} {self.first_name_entry.get().strip().upper()} "
                f"{self.other_name_entry.get().strip().upper()}")
        else:
            guarantor_name = f"{self.sur_name_entry.get().strip().upper()} {self.first_name_entry.get().strip().upper()}"
        guarantor_id = customer_data[0]
        if self.email_entry.get() and not self.id_number_entry.get():
            query = "INSERT INTO guarantors (guarantor_id, name, gender, phone, email, district) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (guarantor_id, guarantor_name, self.gender_value.get().upper(),
                                   self.phone_entry.get().strip(), self.email_entry.get().strip(),
                                   self.district_entry.get().strip().upper()))

        elif not self.email_entry.get() and self.id_number_entry.get():

            query = "INSERT INTO guarantors (guarantor_id, name, gender, nin, district) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, (guarantor_id, guarantor_name, self.gender_value.get().upper(),
                                   self.id_number_entry.get().strip(), self.district_entry.get().strip().upper()))

        elif not self.email_entry.get() and not self.id_number_entry.get():

            query = "INSERT INTO guarantors (guarantor_id, name, gender, phone, district) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, (guarantor_id, guarantor_name, self.gender_value.get().upper(),
                                   self.phone_entry.get().strip(), self.district_entry.get().strip().upper()))

        else:
            query = "INSERT INTO guarantors (guarantor_id, name, gender, phone, email, nin, district) VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query,
                           (guarantor_id, guarantor_name, self.gender_value.get().upper(), self.phone_entry.get().strip(),
                            self.email_entry.get().strip(), self.id_number_entry.get().strip(),
                            self.district_entry.get().strip().upper()))
        connection.commit()
        cursor.close()
        connection.close()
        self.updating_customer(self.display_window, self.customer_data)
        MainWindow.__new__(MainWindow).success_information(f'Guarantor successfully registered.')
        # self.add_guarantor(customer_data)

    def view_guarantor(self, guarantor_data):
        self.emptying_data_fields()
        self.basic_infor_label.configure(text='Guarantor Basic Information')
        self.save_button.configure(text='Update', command=lambda: self.update_guarantor(guarantor_data))
        self.delete_button.configure(command=lambda: self.deleting_guarantor(guarantor_data))
        # self.delete_button = CTkButton(self.save_frame, bg_color='white', fg_color='#ff5c5c', font=('roboto', 15),
        #                             text='Delete', text_color='white', compound=LEFT, width=100, hover_color='#ff3f3f',
        #                             image=CTkImage(Image.open('icons/DELETE.png'), size=(15, 15)),
        #                             command=lambda: self.deleting_guarantor(guarantor_data))
        #
        # self.delete_button.pack(side=RIGHT, padx=(0, 15))

        if len(guarantor_data[1].split()) >= 3:
            self.sur_name_entry.insert(0, guarantor_data[1].split()[0])
            self.first_name_entry.insert(0, guarantor_data[1].split()[1])
            self.other_name_entry.insert(0, guarantor_data[1].split()[2::])
        else:
            self.sur_name_entry.insert(0, guarantor_data[1].split()[0])
            self.first_name_entry.insert(0, guarantor_data[1].split()[1])
        self.phone_entry.insert(0, guarantor_data[3])
        self.gender_value.set(guarantor_data[2])
        if guarantor_data[4] == 'Not Provided':
            # self.email_entry.configure(placeholder_text_color='example@gmail.com')
            pass
        else:
            self.email_entry.insert(0, guarantor_data[4])
        if guarantor_data[5] == 'Not Provided':
            # self.id_number_entry.configure(placeholder_text_color="Customer's NIN")
            pass
        else:
            self.id_number_entry.insert(0, guarantor_data[5])

        self.district_entry.insert(0, guarantor_data[6])

    def update_guarantor(self, guarantor_data):
        condition1 = self.first_name_entry.get().strip() == '' or self.sur_name_entry.get().strip() == ''
        condition2 = (self.phone_entry.get().strip() == '' or self.gender_value.get().strip() == 'Select' or
                      self.district_entry.get().strip() == '')
        if condition1 or condition2:
            MainWindow.__new__(MainWindow).unsuccessful_information('All fields are required')
            return

        if self.email_entry.get().strip() == '':
            pass
        else:
            import re
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email_entry.get()):
                MainWindow.__new__(MainWindow).unsuccessful_information('Invalid email address')
                return

        if not self.phone_entry.get().strip().isdigit() or len(self.phone_entry.get().strip()) != 10:
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid phone number')
            return

        if not self.gender_value.get() in ['MALE', 'FEMALE']:
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

        if self.other_name_entry.get():
            guarantor_name = (
                f"{self.sur_name_entry.get().strip().upper()} {self.first_name_entry.get().strip().upper()} "
                f"{self.other_name_entry.get().strip().upper()}")
        else:
            guarantor_name = f"{self.sur_name_entry.get().strip().upper()} {self.first_name_entry.get().strip().upper()}"
        guarantor_id = guarantor_data[0]
        # print(guarantor_id)
        if self.email_entry.get() and not self.id_number_entry.get():
            query = "UPDATE guarantors SET name=?, gender=?, phone=?, email=?, nin='Not Provided', district=? WHERE guarantor_id=?"
            cursor.execute(query, (guarantor_name, self.gender_value.get().upper(),
                                   self.phone_entry.get().strip(), self.email_entry.get().strip(),
                                   self.district_entry.get().strip().upper(), guarantor_id))

        elif not self.email_entry.get() and self.id_number_entry.get():

            query = "UPDATE guarantors SET name=?, gender=?, email='Not Provided', nin=?, district=? WHERE guarantor_id=?"
            cursor.execute(query, (guarantor_name, self.gender_value.get().upper(),
                                   self.id_number_entry.get().strip(), self.district_entry.get().strip().upper(), guarantor_id))

        elif not self.email_entry.get() and not self.id_number_entry.get():

            query = "UPDATE guarantors SET name=?, gender=?, email='Not Provided', nin='Not Provided', phone=?, district=? WHERE guarantor_id=?"
            cursor.execute(query, (guarantor_name, self.gender_value.get().upper(),
                                   self.phone_entry.get().strip(), self.district_entry.get().strip().upper(), guarantor_id))

        else:
            query = "UPDATE guarantors SET name=?, gender=?, phone=?, email=?, nin=?, district=? WHERE guarantor_id=?"
            cursor.execute(query,
                           (guarantor_name, self.gender_value.get().upper(),
                            self.phone_entry.get().strip(), self.email_entry.get().strip(), self.id_number_entry.get().strip(),
                            self.district_entry.get().strip().upper(), guarantor_id))
        connection.commit()

        cursor.execute("SELECT * FROM guarantors WHERE guarantor_id=?", (guarantor_id, ))
        guarantor_details = cursor.fetchone()
        cursor.close()
        connection.close()
        self.view_guarantor(guarantor_details)
        MainWindow.__new__(MainWindow).success_information(f'Guarantor successfully updated.')

    def deleting_guarantor(self, guarantor_data):
        confirm_deletion = messagebox.askyesno('Delete Guarantor', f'Are you sure you want to delete '
                                                f'{guarantor_data[1].split()[1]}\nas a guarantor?', parent=self.display_window)
        if confirm_deletion:
            connection = sqlite3.connect('munange.db')
            cursor = connection.cursor()
            cursor.execute("DELETE FROM guarantors WHERE guarantor_id=?", (guarantor_data[0],))
            connection.commit()
            cursor.close()
            connection.close()
            self.updating_customer(self.display_window, self.customer_data)
            MainWindow.__new__(MainWindow).success_information(f'Guarantor successfully deleted.')

        else:
            pass
















