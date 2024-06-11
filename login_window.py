import socket
from customtkinter import *
import asyncio
import sqlite3
from tkinter import *
import numpy as np
from email.message import EmailMessage
import ssl
import smtplib
from PIL import ImageTk, Image, ImageFilter, ImageTk, ImageEnhance, ImageSequence
import os
import sys


# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Login_window:
    def __init__(self, window):
        self.window = window

        window.title('')
        # window.minsize(500, 500)
        window.geometry(f'1000x600+200+100')
        # window.geometry('1000x700+100+100')
        window.iconbitmap(resource_path('icons/splash.ico'))
        self.calling_all_methods_here()

    def calling_all_methods_here(self):
        self.designing_window(self.window)
        # self.splash_screen()
    """Splash window here"""
    # def splash_screen(self):
    #     screen_width = self.window.winfo_screenwidth() // 2 - 40
    #     screen_height = self.window.winfo_screenheight() // 2 - 50
    #     # print(screen_width, screen_height)
    #     self.window.geometry(f'450x250+{screen_width}+{screen_height}')
    #     # self.window.resizable(False, False)
    #     self.window.minsize(450, 250)
    #     self.window.maxsize(450, 250)
    #     self.window.attributes('-topmost', True)
    #
    #     splash_window_frame = CTkFrame(self.window, fg_color='white', bg_color='white')
    #     splash_window_frame.place(relheight=1, relwidth=1)
    #
    #     CTkLabel(splash_window_frame, text='BursarPlus', font=('roboto', 30), text_color='#1379FF', fg_color='white',
    #              bg_color='white').place(x=150, y=50)
    #     CTkLabel(splash_window_frame, image=CTkImage(Image.open(resource_path('icons/plus.png')), size=(20, 20)),
    #              text='',
    #              bg_color='white', fg_color='white').place(x=293, y=43)
    #
    #     progress_bar = CTkProgressBar(splash_window_frame, orientation='horizontal', mode='determinate',
    #                                   fg_color='white', bg_color='white', progress_color='#1379FF', width=130,
    #                                   height=5)
    #     progress_bar.place(x=160, y=100)
    #     progress_bar.set(0)
    #     progress_bar.start()
    #
    #     #
    #     CTkLabel(splash_window_frame, text='Loading...', font=('roboto', 15), fg_color='white', bg_color='white'
    #              , text_color='#1379FF').place(x=20, y=180)
    #
    #     CTkLabel(splash_window_frame, text='\t© All rights reserved by Itech co ltd 2024.', font=('roboto', 12),
    #              text_color='black', bg_color='white', fg_color='white').place(x=170, y=220)
    #
    #     def kill():
    #         progress_bar.stop()
    #         self.designing_window(self.window)
    #
    #     self.window.after(1700, kill)
    def process_image(self, image_path, blur_radius=20, transparency=20):
        # Open the image
        image = Image.open(image_path).convert("RGBA")

        # Apply Gaussian blur
        blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))

        # Apply transparency
        alpha = blurred_image.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(transparency / 255.0)
        blurred_image.putalpha(alpha)

        return blurred_image

    def designing_window(self, window):
        self.window.attributes('-topmost', False)
        self.window.after(0, lambda: window.wm_state('zoomed'))
        self.window.iconbitmap(resource_path('icons/login.ico'))
        self.window.title('Login')
        self.window.minsize(450, 600)
        self.window.maxsize(self.window.winfo_screenwidth(), self.window.winfo_screenheight())

        self.background = Frame(window, bg='white')
        self.background.pack(expand=True, fill=BOTH)
        global background_photo, processed_img

        processed_img = self.process_image("images/background12.jpg", blur_radius=8, transparency=120)
        background_photo = ImageTk.PhotoImage(processed_img)
        self.side_frame_canvas = Canvas(self.background, bg='white', highlightbackground='gray80')
        self.side_frame_canvas.place(rely=1, relheight=1, anchor='sw', relwidth=1)

        # Making image fit in the side frame using this function
        def side_resizer(e):
            global b, resized_b, new_b
            b = processed_img
            resized_b = b.resize((e.width, e.height), Image.LANCZOS)
            new_b = ImageTk.PhotoImage(resized_b)
            self.side_frame_canvas.create_image(0, 0, image=new_b, anchor='nw')

        self.side_frame_canvas.bind('<Configure>', side_resizer)
        # CTkFrame(side_frame_canvas, fg_color='white', corner_radius=50).pack(pady=200)
        global background_image
        background_image = ImageTk.PhotoImage(Image.open(resource_path('images/i.png')))
        # self.side_frame_canvas.create_image(100, 500, image=background_image)


        # self.logo = CTkLabel(side_frame_canvas, image=CTkImage(background_image, size=(50, 50)), text='Tech',
        #                      font=('arial', 35, 'bold'), text_color='black', compound=LEFT)
        # self.logo.place(x=5, y=5)
        # self.logo2 = CTkLabel(side_frame_canvas, text='Innovate, Implement, Inspire.', font=('roboto', 15),
        #                    text_color='black')
        # self.logo2.place(x=5, y=54)
        #self.side_frame_canvas.create_text(40, 30, text='I', fill='#398FFF', font=('roboto', 40))
        self.side_frame_canvas.create_image(50, 50, image=background_image)
        self.side_frame_canvas.create_text(140, 50, text='Tech', fill='black', font=('arial', 35, 'bold'))

        self.side_frame_canvas.create_text(140, 90, text='Innovate, Implement, Inspire.', fill='black', font=('roboto', 15))

        # global login_frame_image
        # login_frame_image = ImageTk.PhotoImage(Image.open(resource_path('images/login_frame.png')))
        #
        # self.side_frame_canvas.create_image(500, 200, image=login_frame_image,)
        self.login_frame = CTkFrame(self.background, width=350, height=450, corner_radius=40, fg_color='#ffffff',
                                    bg_color='white')
        self.login_frame.pack(pady=100)

        self.welcome = CTkLabel(self.login_frame, text='Welcome back', text_color='black', font=('roboto', 25))
        self.welcome.pack(padx=30, pady=(20, 0))
        slogan = CTkLabel(self.login_frame, text='Very many things are waiting for you!\n\n', text_color='gray60',
                          font=('roboto', 13))
        slogan.pack()

        self.user_name = CTkLabel(self.login_frame, text='Username\t\t\t', text_color='black', font=('roboto', 15))
        self.user_name.pack()

        self.user_name_entry = CTkEntry(self.login_frame, fg_color='#f1fcf1', bg_color='white', corner_radius=10,
                                        border_width=1, width=250, text_color='gray20', height=35,
                                        border_color='#4CC053',
                                        font=('roboto', 15))
        self.user_name_entry.pack(padx=40)
        self.user_name_entry.bind('<FocusIn>', lambda event: self.user_name_entry.configure(border_color='#44aaee'))
        self.user_name_entry.bind('<FocusOut>', lambda event: self.user_name_entry.configure(border_color='#4CC053'))

        CTkLabel(self.login_frame, text='').pack()

        self.password = CTkLabel(self.login_frame, text='Password\t\t\t', text_color='black', font=('roboto', 15))
        self.password.pack()

        self.password_entry = CTkEntry(self.login_frame, fg_color='#f1fcf1', bg_color='white', corner_radius=10,
                                       border_width=1, width=250, text_color='gray20', height=35, font=('roboto', 15),
                                       border_color='#4CC053', show='●')
        self.password_entry.pack(padx=40)
        self.password_entry.bind('<FocusIn>', lambda event: self.password_entry.configure(border_color='#44aaee'))
        self.password_entry.bind('<FocusOut>', lambda event: self.password_entry.configure(border_color='#4CC053'))

        def hide_password():
            closed_eye.configure(image=CTkImage(Image.open(resource_path('icons/closed_eye.png')), size=(20, 20)),
                                 command=show_password)
            self.password_entry.configure(show='●')

        def show_password():
            closed_eye.configure(image=CTkImage(Image.open(resource_path('icons/open_eye.png')), size=(20, 20)),
                                 command=hide_password)
            self.password_entry.configure(show='')

        closed_eye = CTkButton(self.password_entry,
                               image=CTkImage(Image.open(resource_path('icons/closed_eye.png')), size=(20, 20)),
                               bg_color='white', fg_color='#f1fcf1', width=10, height=10, text='', hover_color='#f1fcf1',
                               command=show_password)
        closed_eye.place(relx=0.85, rely=0.1)

        self.forgot_password = CTkButton(self.login_frame, text='Forgot password?', text_color='#4CC053', font=('roboto', 15),
                                         bg_color='white', fg_color='white', hover_color='white',
                                         command=self.forgot_password)
        self.forgot_password.pack(side=BOTTOM, pady=(15, 25))

        self.login_button = CTkButton(self.login_frame, text='Login', bg_color='white', fg_color='#3BA541',
                                      corner_radius=10,
                                      width=250, height=35, hover_color='#2D9834', compound=RIGHT,
                                      border_color='gray50',
                                      image=CTkImage(Image.open(resource_path('images/back_image.png'))),
                                      font=('roboto', 15),
                                      command=lambda: self.main_window(None, self.window))

        self.login_button.pack(side=BOTTOM, pady=(30, 0))
        self.window.bind('<Return>', lambda event: self.main_window(event, window))
        # self.window.resizable(True, True)

    def main_window(self, event, window):

        self.window.iconbitmap(resource_path('icons/home2.ico'))
        self.window.title('Home')
        # if self.user_name_entry.get().strip() == '' or self.password_entry.get().strip() == '':
        #     self.unsuccessful_information('All fields are required')
        #     return
        # connection = sqlite3.connect('bursarplus.db')
        # cursor = connection.cursor()
        # cursor.execute("SELECT username, password FROM bursar")
        # bursar_information = cursor.fetchone()
        # username = bursar_information[0]
        # password = bursar_information[1]
        # cursor.close()
        # connection.close()
        # if self.user_name_entry.get() != username or self.password_entry.get() != password:
        #     self.unsuccessful_information('Invalid username or password')
        #     return

        self.window.after(0, lambda: window.wm_state('zoomed'))

        from main_window import MainWindow

        # self.logo.place_forget()
        # self.logo2.place_forget()
        # # self.munange_image_label.pack_forget()
        self.login_frame.pack_forget()
        self.side_frame_canvas.place_forget()
        self.background.config(bg='white')
        CTkLabel(self.background, text='Getting things ready for you . . .', bg_color='white', fg_color='#3BA541',
                 corner_radius=15, width=150, height=40, font=('roboto', 15)).pack(side=TOP, pady=15)

        self.window.unbind('<Return>')

        def next_window():
            self.login_button.pack_forget()
            self.background.pack_forget()
            MainWindow(window)

        self.loading_gif(next_window)

    def loading_gif(self, function):
        def animate(index):
            if index < 20:  # Only continue the animation loop until index reaches 20
                frame = gif_frames[index]
                index = (index + 1) % len(gif_frames)
                label.configure(image=frame)
                label.after(50, animate, index)
            else:
                label.pack_forget()
                function()  # Call the provided function when index reaches 20
                return

        gif_path = "images/giphy.gif"
        gif = Image.open(gif_path)
        gif2 = ImageTk.PhotoImage(Image.open(resource_path(gif_path)))
        gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]
        label = Label(self.background, image=gif2, bg='white', fg='white', text='', width=200, height=200)
        label.pack(fill=BOTH, expand=True, side=TOP)

        animate(0)  # Start the animation loop

    def success_information(self, info):
        global y, y2
        y = 0
        y2 = 0.07

        def destroying_label():
            global y2
            if y2 >= -0.1:  # Continue animating while y is less than 0.4
                y2 -= 0.01
                correct_input.place(relx=0.35, rely=y2)
                self.window.after(4, destroying_label)
            else:
                correct_input.destroy()
                self.back_here()

        def animating_label():
            global y
            if y < 0.07:  # Continue animating while y is less than 0.4
                y += 0.01
                correct_input.place(relx=0.35, rely=y)
                self.window.after(5, animating_label)  # Call the function again after 10ms
            else:  # If y is 0.4 or more, stop animation
                correct_input.place(relx=0.35, rely=y)  # Ensure the label is placed
                # destroying_label()
                self.window.after(2000, destroying_label)

        correct_input = CTkLabel(self.window, text=f'   {info}  ', text_color='#3BA541', bg_color='#e9edf2',
                                 fg_color='white', corner_radius=5, width=70, height=45, compound=LEFT,
                                 image=CTkImage(Image.open('icons/tick.png')), font=('roboto', 15))

        correct_input.place(relx=0.35, rely=0.3)
        animating_label()

    def unsuccessful_information(self, info):
        global y, y2
        y = 0
        y2 = 0.07

        def destroying_label():
            global y2
            if y2 >= -0.1:  # Continue animating while y is less than 0.4
                y2 -= 0.01
                invalid_input.place(relx=0.43, rely=y2)
                self.window.after(4, destroying_label)
            else:
                invalid_input.destroy()

        def animating_label():
            global y
            if y < 0.07:  # Continue animating while y is less than 0.4
                y += 0.01
                invalid_input.place(relx=0.43, rely=y)
                self.window.after(5, animating_label)  # Call the function again after 10ms
            else:  # If y is 0.4 or more, stop animation
                invalid_input.place(relx=0.43, rely=y)  # Ensure the label is placed
                # destroying_label()
                self.window.after(2000, destroying_label)

        invalid_input = CTkLabel(self.window, text=f'   {info}  ', text_color='red', bg_color='gray96',
                                 fg_color='#FFEEEE', font=('roboto', 15),
                                 corner_radius=10, width=70, height=45,
                                 image=CTkImage(Image.open(resource_path('icons/cancel.png'))),
                                 compound=LEFT)
        animating_label()

    def forgot_password(self):
        self.window.title('Password Reset')
        self.window.unbind('<Return>')
        self.side_frame_canvas.place_forget()
        self.login_frame.pack_forget()
        self.background.configure(bg='gray95')
        self.designing_forgot_password_window()

    """=========================================FORGOT PASSWORD IS HERE==========================================="""

    def designing_forgot_password_window(self):
        self.upper_buttons_frame = CTkFrame(self.background, bg_color='#3BA541', fg_color='#3BA541',
                                            )
        self.upper_buttons_frame.pack(fill=X)
        self.change_password_label = CTkLabel(self.upper_buttons_frame, text=' Change Password', text_color='white',
                                        corner_radius=0, bg_color='#3BA541', fg_color='#085f00',
                                        font=('roboto', 15), image=CTkImage(Image.open('icons/preferences2.png'),
                                        size=(20, 20)), compound=LEFT,  height=35, width=150)
        self.change_password_label.pack(side=LEFT)

        back_frame = CTkFrame(self.background, fg_color='gray95', bg_color='gray95', corner_radius=10)
        back_frame.pack(fill=X, padx=20, pady=(20, 0))
        self.back = CTkButton(back_frame, bg_color='gray95', fg_color='#0C2844', font=('roboto', 15),
                                    text='', text_color='white', compound=LEFT,
                                    image=CTkImage(Image.open('icons/back_image.png')), width=20,
                                    command=self.back_here)
        self.back.pack(side=LEFT)
        self.info_frame = CTkFrame(self.background, fg_color='white', bg_color='gray95', corner_radius=10)
        self.info_frame.pack(pady=30)

        self.infor = CTkLabel(self.info_frame, text='The reset code has been sent to your email address. Use it below to\n'
                'change your password', text_color='#2ea5de', bg_color='gray95', font=('roboto', 15, 'bold'),
                 corner_radius=10, fg_color='#d1f3ff',
                compound=LEFT, justify=LEFT, anchor='w')
        self.infor.pack(fill=X, ipadx=30, ipady=20)

        self.code_label = CTkLabel(self.info_frame, text='Do you have a reset code?', justify=LEFT, anchor='w'
                                    , text_color='#0C2844', bg_color='white', font=('roboto', 15, 'bold'))
        self.code_label.pack(fill=X, pady=(40, 0), padx=20)

        self.no_button = CTkButton(self.info_frame, bg_color='white', fg_color='white', hover_color='white',
                                    text_color='#3BA541', text='No', font=('roboto', 15), border_color='#3BA541',
                                   border_width=1, height=35, command=self.no_command)

        self.no_button.pack(side=LEFT, fill=X, padx=20, pady=(10, 20), expand=True)

        self.yes_button = CTkButton(self.info_frame, bg_color='white', fg_color='#3BA541', hover_color='#2D9834',
                                    text_color='white', text='Yes', font=('roboto', 15), border_color='#3BA541',
                                   border_width=1, height=35, text_color_disabled='white',
                                   command=self.changing_password)
        self.yes_button.pack(side=LEFT, fill=X, padx=(0, 20), pady=(10, 20), expand=True)
        # from login_window import Login_window
        # Login_window.__new__(Login_window).unsuccessful_information("Ooops! it seems you're offline")
        # self.unsuccessful_information("Ooops! it looks like you're offline")
        self.sent_otp()

    def no_command(self):
        self.infor.configure(text="We have resent you a reset code on your email. Use it below to\n"
                "change your password")
        self.sent_otp()

    def changing_password(self):
        self.code_label.pack_forget()
        self.no_button.pack_forget()
        self.yes_button.pack_forget()
        self.infor.configure(text='The reset code has been sent to your email address. Use it below to\n'
                'change your password')
        label_frame = CTkFrame(self.info_frame, fg_color='white', bg_color='white', corner_radius=0)
        label_frame.pack(padx=20, fill=X, pady=(20, 0))
        CTkLabel(label_frame, text='New Username', justify=LEFT, anchor='w'
                , text_color='#0C2844', bg_color='white', font=('roboto', 15, )
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

        CTkLabel(self.info_frame, text='Reset Code', justify=LEFT, anchor='w'
                , text_color='#0C2844', bg_color='white', font=('roboto', 15),
                 ).pack(fill=X, padx=20, expand=True, pady=(10, 0))
        self.code_entry = CTkEntry(self.info_frame, bg_color='white', border_color='#4CC053', fg_color='#f1fcf1',
                                       border_width=1, height=35, text_color='#0C2844', font=('roboto', 15))
        self.code_entry.pack(fill=X, pady=(0, 10), padx=20, expand=True)
        self.code_entry.bind('<FocusIn>', lambda event: self.code_entry.configure(border_color='#44aaee'))
        self.code_entry.bind('<FocusOut>', lambda event: self.code_entry.configure(border_color='#4CC053'))
        self.code_entry.bind('<Return>', self.change_password_command)
        self.submit_button = CTkButton(self.info_frame, bg_color='white', fg_color='#3BA541', hover_color='#2D9834',
                                    text_color='white', text='Submit', font=('roboto', 15), border_color='#3BA541',
                                    border_width=1, height=35,
                                    command=lambda: self.change_password_command(None))
        self.submit_button.pack(side=RIGHT, padx=20, pady=(10, 20))

    def change_password_command(self, event):
        if not self.username_entry.get().strip() or not self.password_entry.get().strip() or not self.code_entry.get().strip():
            self.unsuccessful_information("All fields are required")
            return
        elif len(self.username_entry.get().strip()) < 4:
            self.unsuccessful_information("Username is very short")
            return

        elif len(self.password_entry.get().strip()) < 4:
            self.unsuccessful_information("New password is very weak")
            return
        else:
            try:
                # if int(self.code_entry.get().strip()) != self.sent_otp():
                if int(self.code_entry.get().strip()) != 12345:
                    self.unsuccessful_information("Invalid OTP")
                    return
            except ValueError:
                self.unsuccessful_information("Invalid OTP")
                return
            self.success_information('Username and password successfully changed')
            # self.back_here()

    def sent_otp(self):
        self.yes_button.configure(state=NORMAL)
        try:
            otp_code = np.random.randint(1000, 9000)
            email_sender = 'nabasaisaac16@gmail.com'
            password = 'ozqz uqbz hbry ysxg'  # Needs use of environment variables to hide the password
            # email_receiver = f'{registered_email}'
            email_receiver = 'nabasaisaac16@gmail.com'
            subject = 'Munange password reset code'
            body = f'Your munange password reset OTP is: {otp_code}'
            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)
            context = ssl.create_default_context()
            # await asyncio.to_thread(self.send_email, email_sender, password, email_receiver, em, context)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

            return otp_code
        except socket.gaierror:
            self.unsuccessful_information("Ooops! it looks like you're offline")
            self.infor.configure(text='Connect to internet for us to send you OTP on your email')
            self.yes_button.configure(state=DISABLED)

    def back_here(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        Login_window(self.window)

    # def create_rounded_image(self, image_path, corner_radius):
    #     # Open the image
    #     image = Image.open(image_path).convert("RGBA")
    #
    #     # Create a mask with rounded corners
    #     mask = Image.new('L', image.size, 0)
    #     draw = ImageDraw.Draw(mask)
    #     draw.rounded_rectangle((0, 0) + image.size, corner_radius, fill=255)
    #
    #     # Apply the mask to the image
    #     rounded_image = Image.new('RGBA', image.size)
    #     rounded_image.paste(image, (0, 0), mask)
    #
    #     return rounded_image


def main():
    main_window = CTk()
    Login_window(main_window)
    main_window.mainloop()


if __name__ == '__main__':
    main()
