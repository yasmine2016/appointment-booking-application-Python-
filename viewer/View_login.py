"""
============================
author:YAN GAO
student ID:1995106
============================
"""
import tkinter as tk
from tkinter import messagebox
from finalProject.appGui.App_User import App_User

class View_login:
    def __init__(self, window, login_function, register_function):
        self.window = window

        self.App_User = None

        # event handlers
        self.register = register_function
        self.login = login_function


        # Textboxes & their labels
        self.login_frame = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)
        self.login_frame.grid(row=1, column=1, padx=5, pady=5)

        self.buttons_frame = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)
        self.buttons_frame.grid(row=20, column=1, padx=5, pady=5)

        self.label_uname = tk.Label(master=self.login_frame, text="UserName:")
        self.label_uname.grid(row=6, column=1, sticky="w")

        self.txt_uname = tk.Entry(master=self.login_frame, width=30)
        self.txt_uname.grid(row=6, column=2)

        self.label_psw = tk.Label(text="Password:", master=self.login_frame)
        self.label_psw.grid(row=14, column=1, sticky="w")

        self.txt_psw = tk.Entry(master=self.login_frame, width=30)
        self.txt_psw.grid(row=14, column=2)

        # ----- Buttons -----
        self.button_register = tk.Button(text="Register", width=12, master=self.buttons_frame)
        self.button_register.bind("<ButtonRelease-1>", self._handle_register)
        self.button_register.grid(row=1, column=1)

        self.button_login = tk.Button(text="Login", width=12, master=self.buttons_frame)
        self.button_login.bind("<ButtonRelease-1>", self._handle_login)
        self.button_login.grid(row=1, column=2)


    def _handle_register(self, _):
        self.register()


    def _handle_login(self, _):
        if self._validate():
            user_name = self.txt_uname.get().strip()
            user_psw = self.txt_psw.get().strip()

            self.login(user_name,user_psw)
        else:
            return

    def _validate(self):
        validity = True

        if len(self.txt_uname.get().strip()) == 0:
            self.txt_uname.configure(bg="#FF8786")
            self.txt_uname.insert(0, "Missing UserName!")
            validity = False
        else:
            self.txt_uname.configure(bg="#FFFFFF")

        if len(self.txt_psw.get().strip()) == 0:
            self.txt_psw.configure(bg="#FF8786")
            self.txt_psw.insert(0, "Missing password!")
            validity = False
        else:
            self.txt_psw.configure(bg="#FFFFFF")

        return validity
