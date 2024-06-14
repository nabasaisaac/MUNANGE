import sqlite3
from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageOps, ImageSequence


class MainWindow:
    def __init__(self, display_window):
        self.display_window = display_window
        self.frames_holder = CTkFrame(self.display_window, bg_color='gray95', fg_color='gray95')
        self.frames_holder.pack(expand=True, fill=BOTH)
        self.bottom_frame = CTkFrame(self.display_window, bg_color='gray95', fg_color='gray95', height=40)
        self.bottom_frame.pack(side=BOTTOM, fill=X)
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        global upper_frame
        upper_frame = CTkFrame(self.frames_holder, bg_color='gray95', corner_radius=0, fg_color='#e9edf2',
                                )
        upper_frame.pack(fill=X)

        self.side_frame = CTkFrame(self.frames_holder, bg_color='#3BA541', corner_radius=0, fg_color='#3BA541',
                                   )
        self.side_frame.pack(side=LEFT, fill=Y)
        self.munange_logo = CTkLabel(upper_frame, fg_color='white', corner_radius=0, width=200, text='',
                                     image=CTkImage(Image.open('images/munange_logo_white.png'), size=(180, 100)))
        self.munange_logo.pack(side=LEFT)

        self.display_frame = CTkFrame(self.frames_holder, bg_color='gray95', corner_radius=0, fg_color='gray95',
                                   )
        self.display_frame.pack(side=LEFT, fill=BOTH, expand=True)

        CTkLabel(upper_frame, text='MUNANGE FINANCIAL SERVICES LTD, Tuli Nawe', font=('roboto', 16, 'bold'), fg_color='#e9edf2',
                 bg_color='#e9edf2', text_color='#085f00').pack(side=LEFT, padx=(20, 0))

        """Working on the profile of the user"""
        image = Image.open('images/m.jpg')
        circular_image = self.make_circular_image(image)
        self.profile_button = CTkButton(upper_frame, bg_color='#e9edf2', fg_color='#e9edf2', compound=RIGHT,
                                        image=CTkImage(circular_image, size=(50, 50)), text='NABASA ISAAC\nnabasaisaac',
                                        text_color='#172b4c', font=('roboto', 15), hover_color='#e9edf2')

        self.profile_button.pack(side=RIGHT, padx=(10, 15))

        self.dashboard_button = CTkButton(self.side_frame, bg_color='#3BA541', fg_color='#3BA541', corner_radius=15,
                                     width=150, height=40, hover_color='#2D9834', text_color='white',
                                     text='Dashboard', font=('roboto', 15), compound=LEFT, anchor='w',
                                     image=CTkImage(Image.open('icons/dashboard.png'), size=(20, 20)),
                                     border_color='#3BA541', border_width=1, command=lambda: self.sliding(self.dashboard_button,
                                     self.dashboard, self.display_frame))

        self.dashboard_button.pack(side=TOP, padx=25, pady=(15, 0))

        self.loans_button = CTkButton(self.side_frame, bg_color='#3BA541', fg_color='#3BA541', corner_radius=15,
                                     width=150, height=40, hover_color='#2D9834', text_color='white',
                                     text='Loans', font=('roboto', 15), compound=LEFT, anchor='w',
                                     image=CTkImage(Image.open('icons/loans.png'), size=(20, 20)),
                                     border_color='#3BA541', border_width=1, command=lambda: self.sliding(self.loans_button,
                                     self.loans, self.display_frame))

        self.loans_button.pack(side=TOP)

        self.repayments_button = CTkButton(self.side_frame, bg_color='#3BA541', fg_color='#3BA541', corner_radius=15,
                                     width=150, height=40, hover_color='#2D9834', text_color='white',
                                     text='Repayments', font=('roboto', 15), compound=LEFT, anchor='w',
                                     image=CTkImage(Image.open('icons/repayments.png'), size=(20, 20)),
                                     border_color='#3BA541', border_width=1, command=lambda: self.sliding(self.repayments_button,
                                     self.repayments, self.display_frame))

        self.repayments_button.pack(side=TOP, padx=25)

        self.customers_button = CTkButton(self.side_frame, bg_color='#3BA541', fg_color='#3BA541', corner_radius=15,
                                     width=150, height=40, hover_color='#2D9834', text_color='white',
                                     text='Customers', font=('roboto', 15), compound=LEFT, anchor='w',
                                     image=CTkImage(Image.open('icons/customers.png'), size=(20, 20)),
                                     border_color='#3BA541', border_width=1, command=lambda: self.sliding(self.customers_button,
                                     self.customers, self.display_frame))

        self.customers_button.pack(side=TOP, padx=25)

        self.reports_button = CTkButton(self.side_frame, bg_color='#3BA541', fg_color='#3BA541', corner_radius=15,
                                     width=150, height=40, hover_color='#2D9834', text_color='white',
                                     text='Reports', font=('roboto', 15), compound=LEFT, anchor='w',
                                     image=CTkImage(Image.open('icons/reports.png'), size=(20, 20)),
                                        border_color='#3BA541', border_width=1, command=lambda: self.sliding(self.reports_button,
                                     self.reports, self.display_frame))
        self.reports_button.pack(side=TOP, padx=25)

        self.employees_button = CTkButton(self.side_frame, bg_color='#3BA541', fg_color='#3BA541', corner_radius=15,
                                     width=150, height=40, hover_color='#2D9834', text_color='white',
                                     text='Employees', font=('roboto', 15), compound=LEFT, anchor='w',
                                     image=CTkImage(Image.open('icons/employees.png'), size=(20, 20)),
                                     border_color='#3BA541', border_width=1, command=lambda: self.sliding(self.employees_button,
                                     self.employees, self.display_frame))
        self.employees_button.pack(side=TOP, padx=25)

        self.sliding(self.loans_button, self.loans, self.display_frame)
        # self.sliding(self.customers_button, self.customers, self.display_frame)
        # self.sliding(self.employees_button, self.employees, self.display_frame)
        # self.sliding(self.loans_button, self.loans, self.display_frame)
        # self.sliding(self.repayments_button, self.repayments, self.display_frame)

        self.logout_button = CTkButton(self.side_frame, bg_color='#3BA541', fg_color='#3BA541', corner_radius=15,
                                     width=150, height=40, hover_color='#2D9834', text_color='white',
                                     text='Logout', font=('roboto', 15), compound=LEFT, anchor='w',
                                     image=CTkImage(Image.open('icons/logout.png'), size=(20, 20)),
                                    )
        self.logout_button.pack(side=BOTTOM, padx=25, pady=10)

    def dashboard(self, display_frame):
        pass

    def loans(self, display_frame):
        from loans import Loans
        Loans(display_frame)

    def repayments(self, display_frame):
        from repayments import Repayments
        Repayments(display_frame)

    def customers(self, display_frame):
        from customers import Customers
        Customers(display_frame)

    def reports(self, display_frame):
        pass

    def employees(self, display_frame):
        from employees import Employees
        Employees(display_frame)

    def hiding_hover(self):
        self.dashboard_button.configure(border_color='#3BA541')
        self.loans_button.configure(border_color='#3BA541')
        self.repayments_button.configure(border_color='#3BA541')
        self.customers_button.configure(border_color='#3BA541')
        self.reports_button.configure(border_color='#3BA541')
        self.employees_button.configure(border_color='#3BA541')

    def sliding(self, button, function, parameters):

        self.hiding_hover()
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        button.configure(border_color='white')

        def methods():
            function(parameters)
        self.loading_gif(methods)

    def loading_gif(self, function):
        def animate(index):
            if index < 20:  # Only continue the animation loop until index reaches 20
                frame = gif_frames[index]
                index = (index + 1) % len(gif_frames)
                label.configure(image=frame)
                label.after(25, animate, index)
            else:
                label.pack_forget()
                function()
                return # Call the provided function when index reaches 20

        gif_path = "images/giphy.gif"
        gif = Image.open(gif_path)
        gif2 = ImageTk.PhotoImage(Image.open(gif_path))
        gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]
        label = Label(self.display_frame, image=gif2, bg='white', fg='white', text='', width=100, height=100)
        label.pack(expand=True, fill=BOTH)

        animate(0)  # Start the animation loop

    def success_information(self, info):
        global y, y2
        y = 0
        y2 = 0.4

        def destroying_label():
            global y2
            if y2 >= -0.1:  # Continue animating while y is less than 0.4
                y2 -= 0.01
                correct_input.place(relx=0.5, rely=y2)
                upper_frame.after(2, destroying_label)
            else:
                correct_input.destroy()

        def animating_label():
            global y
            if y < 0.4:  # Continue animating while y is less than 0.4
                y += 0.01
                correct_input.place(relx=0.5, rely=y)
                upper_frame.after(3, animating_label)  # Call the function again after 10ms
            else:  # If y is 0.4 or more, stop animation
                correct_input.place(relx=0.5, rely=y)  # Ensure the label is placed
                # destroying_label()
                upper_frame.after(1500, destroying_label)

        correct_input = CTkLabel(upper_frame, text=f'   {info}  ', text_color='#3BA541', bg_color='#e9edf2',
                                 fg_color='white', corner_radius=5, width=70, height=45, compound=LEFT,
                                 image=CTkImage(Image.open('icons/tick.png')), font=('roboto', 15))

        correct_input.place(relx=0.5, rely=0.3)
        animating_label()

    def unsuccessful_information(self, info):
        global y, y2
        y = 0
        y2 = 0.4

        def destroying_label():
            global y2
            if y2 >= -0.1:  # Continue animating while y is less than 0.4
                y2 -= 0.01
                invalid_input.place(relx=0.5, rely=y2)
                upper_frame.after(2, destroying_label)
            else:
                invalid_input.destroy()

        def animating_label():
            global y
            if y < 0.4:  # Continue animating while y is less than 0.4
                y += 0.01
                invalid_input.place(relx=0.5, rely=y)
                upper_frame.after(3, animating_label)  # Call the function again after 10ms
            else:  # If y is 0.4 or more, stop animation
                invalid_input.place(relx=0.5, rely=y)  # Ensure the label is placed
                # destroying_label()
                upper_frame.after(1500, destroying_label)

        invalid_input = CTkLabel(upper_frame, text=f'   {info}  ', text_color='red', bg_color='#e9edf2', fg_color='#FFEEEE',
                                 corner_radius=10, width=70, height=45, image=CTkImage(Image.open('icons/cancel.png')),
                                 compound=LEFT, font=('roboto', 15))
        animating_label()

    def make_circular_image(self, image):
        diameter = min(image.size)
        # Create a mask (black with a white circle)
        mask = Image.new("L", (diameter, diameter), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, diameter, diameter), fill=255)

        # Crop the image to a square
        square_image = ImageOps.fit(image, (diameter, diameter), centering=(0.5, 0.5))

        # Apply the mask to get the circular image
        circular_image = ImageOps.fit(image, (diameter, diameter), centering=(0.5, 0.5))
        circular_image.putalpha(mask)

        return circular_image

# from PIL import Image, ImageFilter, ImageDraw, ImageTk, ImageEnhance
# import customtkinter as ctk
# def process_image(image_path, blur_radius=10, transparency=128, corner_radius=40):
#     # Open the image
#     image = Image.open(image_path).convert("RGBA")
#
#     # Apply Gaussian blur
#     blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
#
#     # Apply transparency
#     alpha = blurred_image.split()[3]
#     alpha = ImageEnhance.Brightness(alpha).enhance(transparency / 255.0)
#     blurred_image.putalpha(alpha)
#
#     # Create a mask for rounded corners
#     mask = Image.new('L', blurred_image.size, 0)
#     draw = ImageDraw.Draw(mask)
#     draw.rounded_rectangle((0, 0) + blurred_image.size, corner_radius, fill=255)
#
#     # Apply the mask to the blurred image to create rounded corners
#     rounded_blurred_image = Image.new('RGBA', blurred_image.size)
#     rounded_blurred_image.paste(blurred_image, (0, 0), mask)
#
#     return rounded_blurred_image
#
# # Initialize the main window
# root = ctk.CTk()
#
# # Path to your image
# image_path = "images/munange_flier.jpg"
#
# # Process the image with blur, transparency, and rounded corners
# processed_img = process_image(image_path, blur_radius=7, transparency=200, corner_radius=40)
#
# # Convert to PhotoImage for use in Tkinter
# background_photo = ImageTk.PhotoImage(processed_img)
#
# # Create a label and set the processed image as the background
# label = ctk.CTkLabel(root, text="Good morning Isaac", image=ctk.CTkImage(processed_img, size=(400, 400)))
# label.pack(fill="both", expand=True)
#
# # Run the main loop
# root.mainloop()

"""blur image here"""

# from PIL import Image, ImageFilter, ImageTk, ImageEnhance
# from customtkinter import *
#
#
# def process_image(image_path, blur_radius=10, transparency=128):
#     # Open the image
#     image = Image.open(image_path).convert("RGBA")
#
#     # Apply Gaussian blur
#     blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
#
#     # Apply transparency
#     alpha = blurred_image.split()[3]
#     alpha = ImageEnhance.Brightness(alpha).enhance(transparency / 255.0)
#     blurred_image.putalpha(alpha)
#
#     return blurred_image

# Initialize the main window
# root = CTk()
#
# # Path to your image
# image_path = "images/munange_flier.jpg"

# Process the image with blur and transparency
# processed_img = process_image(image_path, blur_radius=7, transparency=150)
#
# # Convert to PhotoImage for use in Tkinter
# background_photo = ImageTk.PhotoImage(processed_img)
# new = Image.open(background_photo)
# # Create a label and set the processed image as the background
# label = CTkLabel(root, text="WELCOME BACK KAPALAGA JIMMY, ", image=CTkImage(processed_img, size=(500, 500)), font=('roboto', 20))
# label.pack(fill="both", expand=True)
#
# Run the main loop
# root.mainloop()
