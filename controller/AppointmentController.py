"""
============================
author:YAN GAO
student ID:1995106
============================
"""
from finalProject.viewer.View_appointment import View_appointment
from finalProject.dataBase.Data import Data
from tkinter import messagebox

class AppointmentController:
    def __init__(self, _window,user_name):
        self.window = _window

        self.appoint_index = 0
        self.appointments = []
        self.username = user_name

        self.db = Data("appointment.db")
        self.appointments = self.db.load_all_appoint(user_name)
        user_id = self.db.get_userid(user_name)

        user_info = []
        user_info.append(user_id)
        user_info.append(user_name)

        self.view = View_appointment(user_info,window=self.window, appoint_function=self._appoint_function,previous_function=self._previous_appointment, next_function=self._next_appointment, delete_function=self._delete_appointment)



    def _appoint_function(self,added_appointment):

        success = self.db.insert_appointList(added_appointment)
        if success:
            messagebox.showinfo(title="Appointment success", message="New Appointment success!")
        else:
            messagebox.showinfo(title="Appointment failed", message="New Appointment failed: The appointment is already exist!")

    def _previous_appointment(self,prev_appointment):
        self.appointments = self.db.load_all_appoint(self.username)
        if(len(self.appointments)!=0):
            for i in range(0,len(self.appointments)):
                if self.appointments[i].date == prev_appointment.date and self.appointments[i].time == prev_appointment.time and self.appointments[i].d_name == prev_appointment.d_name:
                    self.appoint_index = i-1

            if self.appoint_index < 0:
                self.appoint_index = 0

            self.view.switch_to_appointment(apponintment=self.appointments[self.appoint_index])
        else:
            messagebox.showinfo(title="New appointment", message="You do not have any appointment! please add new appointment!")

    def _next_appointment(self,next_appointment):
        self.appointments = self.db.load_all_appoint(self.username)
        if (len(self.appointments)!=0):
            for i in range(0, len(self.appointments)):
                if self.appointments[i].date == next_appointment.date and self.appointments[i].time == next_appointment.time and self.appointments[i].d_name == next_appointment.d_name:
                    self.appoint_index = i + 1
            if self.appoint_index > len(self.appointments)-1:
                self.appoint_index = len(self.appointments)-1

            self.view.switch_to_appointment(apponintment=self.appointments[self.appoint_index])
        else:
            messagebox.showinfo(title="New appointment", message="You do not have any appointment! please add new appointment!")


    def _delete_appointment(self,deleted_appointment):
        self.appointments = self.db.load_all_appoint(self.username)
        if (len(self.appointments)!=0):
            success = self.db.delete_appointment(deleted_appointment)

            # update array
            if success:
                self.appointments = self.db.load_all_appoint(self.username)
                messagebox.showinfo(title="Appointment delete success", message="Appointment delete success!")
            else:
                messagebox.showinfo(title="Appointment delete failed", message="Appointment delete failed!")
        else:
            messagebox.showinfo(title="New appointment", message="You do not any appointment! Can not delete!")

