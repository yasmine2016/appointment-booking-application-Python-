"""
============================
author:YAN GAO
student ID:1995106
============================
"""
import tkinter as tk
from tkinter import messagebox
from finalProject.appGui.App_User import App_User


class View_register:
    def __init__(self, window, submit_function):
        self.window = window

        self.registration = None

        # event handlers
        self.submit = submit_function

        # variables used by radio buttons & checkboxes
        self.shift_gender = tk.StringVar()
        self.shift_gender.set("male")

        # Textboxes & their labels
        self.personal_data_frame = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)
        self.personal_data_frame.grid(row=1, column=1, padx=5, pady=5)

        self.buttons_frame = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)
        self.buttons_frame.grid(row=3, column=1, padx=5, pady=5)

        self.label_uname = tk.Label(master=self.personal_data_frame, text="UserName:")
        self.label_uname.grid(row=1, column=1, sticky="w")

        self.txt_uname = tk.Entry(master=self.personal_data_frame, width=50)
        self.txt_uname.grid(row=1, column=2)

        self.label_psw = tk.Label(text="Password:", master=self.personal_data_frame)
        self.label_psw.grid(row=2, column=1, sticky="w")

        self.txt_psw = tk.Entry(master=self.personal_data_frame, width=50)
        self.txt_psw.grid(row=2, column=2)

        self.label_fname = tk.Label(text="First Name:", master=self.personal_data_frame)
        self.label_fname.grid(row=3, column=1, sticky="w")

        self.txt_fname = tk.Entry(master=self.personal_data_frame, width=50)
        self.txt_fname.grid(row=3, column=2)

        self.label_lname = tk.Label(text="Last Name:", master=self.personal_data_frame)
        self.label_lname.grid(row=4, column=1, sticky="w")

        self.txt_lname = tk.Entry(master=self.personal_data_frame, width=50)
        self.txt_lname.grid(row=4, column=2)

        self.label_age = tk.Label(text="Age:", master=self.personal_data_frame)
        self.label_age.grid(row=5, column=1, sticky="w")

        self.txt_age = tk.Entry(master=self.personal_data_frame, width=50)
        self.txt_age.grid(row=5, column=2)

        self.label_city = tk.Label(text="City:", master=self.personal_data_frame)
        self.label_city.grid(row=6, column=1, sticky="w")

        self.txt_city = tk.Entry(master=self.personal_data_frame, width=50)
        self.txt_city.grid(row=6, column=2)

        self.label_address = tk.Label(text="Address:", master=self.personal_data_frame)
        self.label_address.grid(row=8, column=1, sticky="w")

        self.txt_address = tk.Entry(master=self.personal_data_frame, width=50)
        self.txt_address.grid(row=8, column=2)

        # ----- gender -----
        self.radio_male = tk.Radiobutton(text="Male", variable=self.shift_gender, value="male", master=self.personal_data_frame)
        self.radio_male.grid(row=7, column=1, sticky="w")

        self.radio_female = tk.Radiobutton(text="Female", variable=self.shift_gender, value="female", master=self.personal_data_frame)
        self.radio_female.grid(row=7, column=2, sticky="w")

        # ----- Buttons -----
        self.button_submit = tk.Button(text="Submit", width=12, master=self.buttons_frame)
        self.button_submit.bind("<ButtonRelease-1>", self._handle_submit)
        self.button_submit.grid(row=1, column=1)

        self.button_reset = tk.Button(text="Reset", width=12, master=self.buttons_frame)
        self.button_reset.bind("<ButtonRelease-1>", self._handle_reset)
        self.button_reset.grid(row=1, column=2)


    def _handle_submit(self, _):
        ck_appoint = True
        if self._validate():
            registration = App_User(
                userid = 0,
                uname=self.txt_uname.get().strip(),
                password=self.txt_psw.get().strip(),
                fname=self.txt_fname.get().strip(),
                lname=self.txt_lname.get().strip(),
                age=self.txt_age.get().strip(),
                city=self.txt_city.get().strip(),
                gender = self.shift_gender.get().strip(),
                address = self.txt_address.get().strip()
            )
            self.submit(registration)
        else:
            ck_appoint = False

        return ck_appoint

    def _handle_reset(self, _):
        self.txt_uname.delete(0,'end')
        self.txt_psw.delete(0,'end')
        self.txt_fname.delete(0,'end')
        self.txt_lname.delete(0,'end')
        self.txt_age.delete(0,'end')
        self.txt_city.delete(0,'end')
        self.shift_gender.set("male")
        self.txt_address.delete(0,'end')

    def _validate(self):
        validity = True

        if len(self.txt_uname.get().strip()) == 0:
            self.txt_uname.configure(bg="#FF8786")
            self.txt_uname.insert(0, "Missing User Name!")
            validity = False
        else:
            self.txt_uname.configure(bg="#FFFFFF")

        if len(self.txt_psw.get().strip()) == 0:
            self.txt_psw.configure(bg="#FF8786")
            self.txt_psw.insert(0, "Missing Password!")
            validity = False
        else:
            self.txt_psw.configure(bg="#FFFFFF")

        if len(self.txt_fname.get().strip()) == 0:
            self.txt_fname.configure(bg="#FF8786")
            self.txt_fname.insert(0, "Missing First Name!")
            validity = False
        else:
            self.txt_fname.configure(bg="#FFFFFF")

        if len(self.txt_lname.get().strip()) == 0:
            self.txt_lname.configure(bg="#FF8786")
            self.txt_lname.insert(0, "Missing Last Name!")
            validity = False
        else:
            self.txt_lname.configure(bg="#FFFFFF")

        if len(self.txt_age.get().strip()) == 0:
            self.txt_age.configure(bg="#FF8786")
            self.txt_age.insert(0, "Missing Age!")
            validity = False
        else:
            self.txt_age.configure(bg="#FFFFFF")

        if len(self.txt_city.get().strip()) == 0:
            self.txt_city.configure(bg="#FF8786")
            self.txt_city.insert(0, "Missing City!")
            validity = False
        else:
            self.txt_city.configure(bg="#FFFFFF")

        if len(self.txt_address.get().strip()) == 0:
            self.txt_address.configure(bg="#FF8786")
            self.txt_address.insert(0, "Missing Address!")
            validity = False
        else:
            self.txt_address.configure(bg="#FFFFFF")


        return validity
