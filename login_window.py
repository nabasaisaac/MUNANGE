import sqlite3
from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image, ImageSequence, ImageDraw
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

    def designing_window(self, window):
        self.window.attributes('-topmost', False)
        self.window.after(0, lambda: window.wm_state('zoomed'))
        self.window.iconbitmap(resource_path('icons/login.ico'))
        self.window.title('Login')
        self.window.minsize(450, 600)
        self.window.maxsize(self.window.winfo_screenwidth(), self.window.winfo_screenheight())

        self.background = Frame(window, bg='white')
        self.background.pack(expand=True, fill=BOTH)
        global background_image
        background_image = ImageTk.PhotoImage(Image.open(resource_path('images/i.png')))
        self.logo = Label(self.background, image=background_image, bg='white', text='Tech', font='arial 35 bold',
                          compound=LEFT)
        self.logo.place(x=5, y=5)
        self.logo2 = Label(self.background, bg='white', text='Innovate, Implement, Inspire.', font='roboto 15',
                           compound=LEFT)
        self.logo2.place(x=5, y=75)

        # Create a rounded image with desired corner radius
        rounded_img = self.create_rounded_image("images/munange_flier.jpg", 60)

        self.munange_image_label = CTkLabel(self.background, bg_color='white', fg_color='white',
                                            image=CTkImage(rounded_img, size=(500, 500)))
        self.munange_image_label.pack(side=LEFT, padx=(200, 60), pady=100)

        self.login_frame = CTkFrame(self.background, width=350, height=450, corner_radius=40, fg_color='#ffffff',
                                    bg_color='white')
        self.login_frame.pack(side=LEFT, pady=100)

        self.welcome = CTkLabel(self.login_frame, text='Welcome back', text_color='black', font=('roboto', 25))
        self.welcome.pack(padx=30, pady=(10, 0))
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
                                       border_color='#4CC053')
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
                               image=CTkImage(Image.open(resource_path('icons/open_eye.png')), size=(20, 20)),
                               bg_color='white', fg_color='#f1fcf1', width=10, height=10, text='', hover_color='#f1fcf1',
                               command=hide_password)
        closed_eye.place(relx=0.85, rely=0.1)

        self.login_button = CTkButton(self.login_frame, text='Login', bg_color='white', fg_color='#3BA541',
                                      corner_radius=10,
                                      width=250, height=35, hover_color='#3BA541', compound=RIGHT,
                                      border_color='gray50',
                                      image=CTkImage(Image.open(resource_path('images/back_image.png'))),
                                      font=('roboto', 15),
                                      command=lambda: self.main_window(None, self.window))

        self.login_button.pack(side=BOTTOM, pady=40)
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

        self.logo.place_forget()
        self.logo2.place_forget()
        self.munange_image_label.pack_forget()
        self.login_frame.pack_forget()
        self.login_button.pack_forget()
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

    def success_information(self, display, info, x, y):
        correct_input = CTkLabel(display, text=f'   {info}  ', text_color='#1379FF', bg_color='gray96',
                                 fg_color='#F6FAFF', corner_radius=5, width=70, height=45, compound=LEFT,
                                 image=CTkImage(Image.open(resource_path('icons/tick.png'))))

        correct_input.place(relx=x, rely=y)
        correct_input.after(3000, lambda: correct_input.place_forget())

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
                self.window.after(1500, destroying_label)

        invalid_input = CTkLabel(self.window, text=f'   {info}  ', text_color='red', bg_color='gray96',
                                 fg_color='#FFEEEE',
                                 corner_radius=10, width=70, height=45,
                                 image=CTkImage(Image.open(resource_path('icons/cancel.png'))),
                                 compound=LEFT)
        animating_label()

    def create_rounded_image(self, image_path, corner_radius):
        # Open the image
        image = Image.open(image_path).convert("RGBA")

        # Create a mask with rounded corners
        mask = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0) + image.size, corner_radius, fill=255)

        # Apply the mask to the image
        rounded_image = Image.new('RGBA', image.size)
        rounded_image.paste(image, (0, 0), mask)

        return rounded_image


def main():
    main_window = CTk()
    Login_window(main_window)
    main_window.mainloop()


if __name__ == '__main__':
    main()
