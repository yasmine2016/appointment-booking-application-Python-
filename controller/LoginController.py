"""
============================
author:YAN GAO
student ID:1995106
============================
"""
import tkinter as tk
from tkinter import messagebox
from finalProject.viewer.View_login import View_login
from finalProject.dataBase.Data import Data
from finalProject.controller.AppointmentController import AppointmentController
from finalProject.controller.RegisterController import RegisterController


class LoginController:
    def __init__(self, _window):
        self.window = _window

        self.login_list = []

        self.db = Data("appointment.db")

        self.view = View_login(window=self.window, login_function=self._login_user, register_function=self._register_user)


    def _login_user(self,uname,psw):
        # check login
        ck = self.db.check_user(uname,psw)

        if ck:
            self.window.destroy()
            window_appoint = tk.Tk()
            window_appoint.title("Appointment")
            AppointmentController(window_appoint,uname)
        else:
            # print("Failed Login")
            messagebox.showerror(title="Failed Login", message="user is not exist Or username/password is wrong!")

    def _register_user(self):
        self.window.destroy()
        window_register = tk.Tk()
        window_register.title("Registration")
        RegisterController(window_register)
