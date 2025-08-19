# main.py
import tkinter as tk
from tkinter import ttk
from database import Database
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

APP_TITLE = "Flight Reservation App"
APP_SIZE = "950x600"

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry(APP_SIZE)
        self.minsize(900, 520)

        # Use ttk theme widgets
        self.style = ttk.Style(self)
        try:
            self.style.theme_use("clam")
        except Exception:
            pass

        # Database
        self.db = Database("flights.db")

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            page_name = F.__name__
            frame = F(parent=container, app=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name: str, **kwargs):
        frame = self.frames[page_name]
        if hasattr(frame, "on_show"):
            frame.on_show(**kwargs)
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
