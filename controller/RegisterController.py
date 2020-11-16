"""
============================
author:YAN GAO
student ID:1995106
============================
"""
import tkinter as tk
from tkinter import messagebox

from finalProject.viewer.View_register import View_register
from finalProject.dataBase.Data import Data
from finalProject.controller.AppointmentController import AppointmentController

class RegisterController:
    def __init__(self, _window):
        self.window = _window

        # self.application_index = None
        self.register = []

        self.db = Data("appointment.db")

        self.view = View_register(window=self.window, submit_function=self._submit_registration)


    def _submit_registration(self,app_register):
        # check user unique
        success = self.db.check_register_info(app_register)

        # add new registration
        if success==0:
            # set new userid
            new_id = self.db.get_maxid()
            if new_id != -1:
                app_register.uid= new_id + 1
                if self.db.insert_user(app_register):
                    self.window.destroy()
                    window_appoint = tk.Tk()
                    window_appoint.title("Appointment")

                    AppointmentController(window_appoint, app_register.uname)

        elif success==1:
            messagebox.showerror(title="Failed Register", message="This userName is already exist!")
