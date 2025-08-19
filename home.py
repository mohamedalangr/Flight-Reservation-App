# home.py
import tkinter as tk
from tkinter import ttk

class HomePage(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        title = ttk.Label(self, text="✈️ Simple Flight Reservation", font=("Segoe UI", 20, "bold"))
        title.grid(row=0, column=0, pady=(20, 10), padx=20, sticky="n")

        sub = ttk.Label(self, text="Choose an action", font=("Segoe UI", 11))
        sub.grid(row=1, column=0, pady=(0, 10))

        btns = ttk.Frame(self)
        btns.grid(row=2, column=0, pady=10)

        book_btn = ttk.Button(btns, text="Book Flight", command=lambda: self.app.show_frame("BookingPage"))
        view_btn = ttk.Button(btns, text="View Reservations", command=lambda: self.app.show_frame("ReservationsPage"))

        book_btn.grid(row=0, column=0, padx=8, pady=8, ipadx=10, ipady=5)
        view_btn.grid(row=0, column=1, padx=8, pady=8, ipadx=10, ipady=5)
