# edit_reservation.py
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

class EditReservationPage(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.vars = {}
        self.current_id = None
        self._build_ui()

    def _build_ui(self):
        title = ttk.Label(self, text="Edit Reservation", font=("Segoe UI", 16, "bold"))
        title.grid(row=0, column=0, pady=(20, 10), columnspan=2)

        form = ttk.Frame(self)
        form.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
        for i, (label, key) in enumerate(FIELDS):
            ttk.Label(form, text=label).grid(row=i, column=0, sticky="w", pady=6)
            var = tk.StringVar()
            entry = ttk.Entry(form, textvariable=var, width=42)
            entry.grid(row=i, column=1, sticky="ew", pady=6, padx=(10,0))
            self.vars[key] = var

        actions = ttk.Frame(self)
        actions.grid(row=2, column=0, columnspan=2, pady=12)
        ttk.Button(actions, text="Update", command=self._update).grid(row=0, column=0, padx=8, ipadx=10, ipady=4)
        ttk.Button(actions, text="Back", command=lambda: self.app.show_frame("ReservationsPage")).grid(row=0, column=1, padx=8, ipadx=10, ipady=4)

    def on_show(self, reservation_id=None, **_):
        """Called when this page is shown; populate fields from DB."""
        self.current_id = reservation_id
        if reservation_id is None:
            messagebox.showerror("Error", "No reservation ID provided.")
            self.app.show_frame("ReservationsPage")
            return
        rec = self.app.db.get_reservation(reservation_id)
        if not rec:
            messagebox.showerror("Not Found", f"No reservation with ID {reservation_id}.")
            self.app.show_frame("ReservationsPage")
            return
        # rec: (id, name, flight_number, departure, destination, date, seat_number)
        _, name, flight_number, departure, destination, date, seat_number = rec
        self.vars["name"].set(name)
        self.vars["flight_number"].set(flight_number)
        self.vars["departure"].set(departure)
        self.vars["destination"].set(destination)
        self.vars["date"].set(date)
        self.vars["seat_number"].set(seat_number)

    def _update(self):
        if self.current_id is None:
            return
        data = {k: v.get().strip() for k, v in self.vars.items()}
        missing = [k for k, v in data.items() if not v]
        if missing:
            messagebox.showerror("Missing Data", f"Please fill: {', '.join(missing)}")
            return
        try:
            self.app.db.update_reservation(
                self.current_id,
                data["name"], data["flight_number"], data["departure"],
                data["destination"], data["date"], data["seat_number"]
            )
            messagebox.showinfo("Success", "Reservation updated successfully.")
            self.app.show_frame("ReservationsPage")
        except Exception as e:
            messagebox.showerror("Error", f"Could not update reservation.\n\n{e}")
