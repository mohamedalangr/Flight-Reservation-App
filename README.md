# Simple Flight Reservation Desktop App (Tkinter + SQLite)

A minimal, clean desktop app to **book, view, update, and delete** flight reservations using **Tkinter** and **SQLite**.

## Features
- GUI pages: Home, Booking, Reservations list, Edit reservation
- SQLite database with CRUD operations
- Packaged file structure and `README` for easy running
- PyInstaller instructions to build a Windows `.exe`

## Quick Start
1. **Install Python 3.10+** from https://www.python.org
2. (Optional) Create & activate a virtual environment
3. Run the app:
   ```bash
   python main.py
   ```

On first run, `flights.db` is created automatically (if not present).

## File Structure
```
/flight_reservation_app
  ├── main.py                # Main application entry point
  ├── database.py            # SQLite database helper + schema
  ├── home.py                # Home page
  ├── booking.py             # Booking page
  ├── reservations.py        # List + delete + navigation to edit
  ├── edit_reservation.py    # Edit page
  ├── flights.db             # SQLite DB (auto-created if missing)
  ├── requirements.txt       # PyInstaller for building exe
  ├── README.md
  ├── .gitignore
  └── assets/
```

## Build a Windows Executable (.exe)
1. Install PyInstaller:
   ```bash
   pip install -r requirements.txt
   # or
   pip install pyinstaller
   ```
2. From the project folder, run:
   ```bash
   pyinstaller --onefile --windowed main.py
   ```
3. The executable will be in the `dist/` folder as `main.exe`.

### Optional icon
If you have an icon file at `assets/icon.ico`, you can include:
```bash
pyinstaller --onefile --windowed --icon=assets/icon.ico main.py
```

## GitHub Upload
1. Initialize Git
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Flight Reservation App"
   ```
2. Create a new repository on GitHub and follow the push instructions.

## Notes
- Date is free text (format: `YYYY-MM-DD`). You can later replace it with a datepicker widget/library if needed.
- Seat format is free text so you can use any pattern (e.g., `12A`).

