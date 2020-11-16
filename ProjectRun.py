"""
============================
author:YAN GAO
student ID:1995106
============================
"""
import tkinter as tk
from finalProject.controller.LoginController import LoginController




window = tk.Tk()
window.title("Appointment")

# start the app
LoginController(window)

# start the event listener at the very end to prevent blocking
window.mainloop()
