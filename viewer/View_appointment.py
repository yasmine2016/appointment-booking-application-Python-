"""
============================
author:YAN GAO
student ID:1995106
============================
"""
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from finalProject.appGui.App_Appoint import App_Appoint

class View_appointment:
    def __init__(self, user_info,window, appoint_function, previous_function, next_function, delete_function):
        self.window = window
        self.user_info = user_info
        self.app_appoint = None

        # event handlers
        self.appoint = appoint_function
        self.previous = previous_function
        self.next = next_function
        self.delete = delete_function

        # frame
        self.appoint_data_frame = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)
        self.appoint_data_frame.grid(row=1, column=1, padx=5, pady=5)

        self.buttons_frame = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)
        self.buttons_frame.grid(row=3, column=1, padx=5, pady=5)

        # Textboxes & their labels
        self.label_uid = tk.Label(master=self.appoint_data_frame, text="User ID:")
        self.label_uid.grid(row=1, column=1, sticky="w")

        self.e_uid = tk.StringVar()
        self.txt_uid = tk.Entry(master=self.appoint_data_frame, textvariable=self.e_uid,width=50)
        self.txt_uid.grid(row=1, column=2)
        self.e_uid.set(user_info[0])
        self.txt_uid.configure(state='disabled')

        self.label_uname = tk.Label(master=self.appoint_data_frame, text="User Name:")
        self.label_uname.grid(row=2, column=1, sticky="w")

        self.e_uname = tk.StringVar()
        self.txt_uname = tk.Entry(master=self.appoint_data_frame,textvariable=self.e_uname, width=50)
        self.txt_uname.grid(row=2, column=2)
        self.e_uname.set(user_info[1])
        self.txt_uname.configure(state='disabled')

        self.label_date = tk.Label(text="Appointment Date:", master=self.appoint_data_frame)
        self.label_date.grid(row=3, column=1, sticky="w")

        self.txt_date = DateEntry(master=self.appoint_data_frame, width=12, year=2020, month=9, day=22,background='darkblue', foreground='white', borderwidth=2)
        #self.txt_date.pack(padx=10, pady=10)
        self.txt_date.grid(row=3, column=2)


        self.label_time = tk.Label(text="Appointment Time:", master=self.appoint_data_frame)
        self.label_time.grid(row=4, column=1, sticky="w")

        self.txt_time = ttk.Combobox(master=self.appoint_data_frame)
        self.txt_time['value'] = ('10:00am', '10:15am', '10:30am', '10:45am',
                                  '11:00am', '11:15am', '11:30am', '11:45am',
                                  '12:00pm', '12:15pm', '12:30pm', '12:45pm',
                                  '1:00pm', '1:15pm', '1:30pm', '1:45pm',
                                  '2:00pm', '2:15pm', '2:30pm', '2:45pm')
        self.txt_time.current(0)
        self.txt_time.grid(row=4, column=2)

        self.label_doctor = tk.Label(text="Doctor Name:", master=self.appoint_data_frame)
        self.label_doctor.grid(row=5, column=1, sticky="w")

        self.txt_doctor = ttk.Combobox(master=self.appoint_data_frame)
        self.txt_doctor['value'] = ('Andy', 'Charlie')
        self.txt_doctor.current(0)
        self.txt_doctor.grid(row=5, column=2)

        # ----- Buttons -----
        self.button_previous = tk.Button(text="Previous", width=12, master=self.buttons_frame)
        self.button_previous.bind("<ButtonRelease-1>", self._handle_previous)
        self.button_previous.grid(row=1, column=1)

        self.button_next = tk.Button(text="Next", width=12, master=self.buttons_frame)
        self.button_next.bind("<ButtonRelease-1>", self._handle_next)
        self.button_next.grid(row=1, column=2)

        self.button_update = tk.Button(text="Appointment", width=12, master=self.buttons_frame)
        self.button_update.bind("<ButtonRelease-1>", self._handle_appointment)
        self.button_update.grid(row=1, column=3)

        self.button_delete = tk.Button(text="Delete", width=12, master=self.buttons_frame)
        self.button_delete.bind("<ButtonRelease-1>", self._handle_delete)
        self.button_delete.grid(row=1, column=5)

    def switch_to_appointment(self, apponintment=None):
        if apponintment is None:
            # todo: should throwing an error not returning
            print("Missing Apponintment")
            return None

        self.app_appoint = apponintment

        self.txt_date.delete(0, tk.END)
        self.txt_date.insert(0, apponintment.date)
        self.txt_time.delete(0, tk.END)
        self.txt_time.insert(0, apponintment.time)
        self.txt_doctor.delete(0, tk.END)
        self.txt_doctor.insert(0, apponintment.d_name)

    def _handle_appointment(self, _):
        ck_appoint = True

        if self._validate():
            app_appoint = self.get_appoint()
            self.appoint(app_appoint)
        else:
            ck_appoint = False

        return ck_appoint

    def _handle_previous(self, _):
        app_appoint = self.get_appoint()
        self.previous(app_appoint)

    def _handle_next(self, _):
        app_appoint = self.get_appoint()
        self.next(app_appoint)

    def _handle_delete(self, _):
        app_appoint = self.get_appoint()
        self.delete(app_appoint)

    def _validate(self):
        validity = True

        if len(self.txt_uname.get().strip()) == 0:
            self.txt_uname.configure(bg="#FF8786")
            self.txt_uname.insert(0, "Missing User Name!")
            validity = False
        else:
            self.txt_uname.configure(bg="#FFFFFF")

        return validity

    def get_appoint(self):
        app_appoint = App_Appoint(
            userid=self.txt_uid.get(),
            date=self.txt_date.get().strip(),
            time=self.txt_time.get().strip(),
            doctorname=self.txt_doctor.get().strip()
        )
        return app_appoint
