# booking.py
import tkinter as tk
from tkinter import ttk, messagebox

FIELDS = [
    ("Name", "name"),
    ("Flight Number", "flight_number"),
    ("Departure", "departure"),
    ("Destination", "destination"),
    ("Date (YYYY-MM-DD)", "date"),
    ("Seat Number", "seat_number"),
]

class BookingPage(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.vars = {}
        self._build_ui()

    def _build_ui(self):
        self.columnconfigure(0, weight=1)
        title = ttk.Label(self, text="Book a Flight", font=("Segoe UI", 16, "bold"))
        title.grid(row=0, column=0, pady=(20, 10))

        form = ttk.Frame(self)
        form.grid(row=1, column=0, sticky="n", padx=20)
        for i, (label, key) in enumerate(FIELDS):
            ttk.Label(form, text=label).grid(row=i, column=0, sticky="w", pady=6)
            var = tk.StringVar()
            entry = ttk.Entry(form, textvariable=var, width=40)
            entry.grid(row=i, column=1, sticky="ew", pady=6, padx=(10,0))
            self.vars[key] = var

        actions = ttk.Frame(self)
        actions.grid(row=2, column=0, pady=12)
        save_btn = ttk.Button(actions, text="Save Reservation", command=self._save)
        back_btn = ttk.Button(actions, text="Back", command=lambda: self.app.show_frame("HomePage"))
        save_btn.grid(row=0, column=0, padx=8, ipadx=10, ipady=4)
        back_btn.grid(row=0, column=1, padx=8, ipadx=10, ipady=4)

    def _save(self):
        data = {k: v.get().strip() for k, v in self.vars.items()}
        missing = [k for k, v in data.items() if not v]
        if missing:
            messagebox.showerror("Missing Data", f"Please fill: {', '.join(missing)}")
            return
        try:
            self.app.db.add_reservation(
                data["name"], data["flight_number"], data["departure"],
                data["destination"], data["date"], data["seat_number"]
            )
            messagebox.showinfo("Success", "Reservation saved successfully.")
            for v in self.vars.values():
                v.set("")
            self.app.show_frame("ReservationsPage")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save reservation.\n\n{e}")
