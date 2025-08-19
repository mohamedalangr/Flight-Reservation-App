# reservations.py
import tkinter as tk
from tkinter import ttk, messagebox

class ReservationsPage(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.tree = None
        self._build_ui()

    def _build_ui(self):
        title = ttk.Label(self, text="All Reservations", font=("Segoe UI", 16, "bold"))
        title.pack(pady=(20, 8))

        toolbar = ttk.Frame(self)
        toolbar.pack(pady=4)
        ttk.Button(toolbar, text="Refresh", command=self._load).pack(side="left", padx=5)
        ttk.Button(toolbar, text="Edit Selected", command=self._edit_selected).pack(side="left", padx=5)
        ttk.Button(toolbar, text="Delete Selected", command=self._delete_selected).pack(side="left", padx=5)
        ttk.Button(toolbar, text="Back", command=lambda: self.app.show_frame("HomePage")).pack(side="left", padx=5)

        cols = ("id", "name", "flight_number", "departure", "destination", "date", "seat_number")
        self.tree = ttk.Treeview(self, columns=cols, show="headings", height=15)
        for c in cols:
            self.tree.heading(c, text=c.replace("_", " ").title())
            self.tree.column(c, width=120 if c != "name" else 160, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=16, pady=(4, 16))

        # initial load
        self._load()

    def _load(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        try:
            rows = self.app.db.list_reservations()
            for r in rows:
                self.tree.insert("", "end", values=r)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load reservations.\n\n{e}")

    def _get_selected_id(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("No selection", "Please select a reservation first.")
            return None
        values = self.tree.item(sel[0], "values")
        return int(values[0])

    def _edit_selected(self):
        rid = self._get_selected_id()
        if rid is not None:
            self.app.show_frame("EditReservationPage", reservation_id=rid)

    def _delete_selected(self):
        rid = self._get_selected_id()
        if rid is None:
            return
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this reservation?"):
            try:
                self.app.db.delete_reservation(rid)
                self._load()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete reservation.\n\n{e}")
    
    # Called by app.show_frame when the page is raised
    def on_show(self, **kwargs):
        self._load()
