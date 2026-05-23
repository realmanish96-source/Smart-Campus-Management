import tkinter as tk
import os

# --- MODERN COLOR PALETTE ---
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"

def show_attendance():
    attendance_window = tk.Toplevel()
    attendance_window.title("SCMP - Attendance Records")
    
    if os.name == 'nt':
        attendance_window.state('zoomed')
    else:
        try:
            attendance_window.attributes('-zoomed', True)
        except tk.TclError:
            width = attendance_window.winfo_screenwidth()
            height = attendance_window.winfo_screenheight()
            attendance_window.geometry(f"{width}x{height}+0+0")
            
    attendance_window.configure(bg=COLOR_BG)
    
    # --- HEADER ---
    header = tk.Frame(attendance_window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Attendance Overview", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    # --- CONTENT CARD ---
    card = tk.Frame(attendance_window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=150, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Subject-wise Presence", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=(40, 30))
    
    # Table Frame
    table_frame = tk.Frame(card, bg=COLOR_CARD)
    table_frame.pack(pady=10)
    
    attendance_data = [
        ("Python", "88%"),
        ("IEE", "76%"),
        ("Maths", "92%"),
        ("Chemistry", "81%"),
        ("AI", "85%"),
        ("Comunication Skills", "90%")
    ]
    
    # Table Headings - INCREASED SIZE
    tk.Label(table_frame, text="SUBJECT NAME", font=("Arial", 16, "bold"), bg="#f8f9fa", fg=COLOR_HEADER, width=30, pady=15, borderwidth=1, relief="solid").grid(row=0, column=0)
    tk.Label(table_frame, text="PERCENTAGE", font=("Arial", 16, "bold"), bg="#f8f9fa", fg=COLOR_HEADER, width=20, pady=15, borderwidth=1, relief="solid").grid(row=0, column=1)
    
    # Rows - INCREASED SIZE
    for i, (subject, percentage) in enumerate(attendance_data):
        tk.Label(table_frame, text=subject, font=("Arial", 16), bg=COLOR_CARD, fg=COLOR_TEXT, width=30, pady=10, borderwidth=1, relief="solid").grid(row=i+1, column=0)
        tk.Label(table_frame, text=percentage, font=("Arial", 16, "bold"), bg=COLOR_CARD, fg=COLOR_ACCENT, width=20, pady=10, borderwidth=1, relief="solid").grid(row=i+1, column=1)
    
    # --- BACK BUTTON ---
    tk.Button(attendance_window, text="CLOSE & GO BACK", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", 
              padx=30, pady=10, relief="flat", command=attendance_window.destroy).pack(side=tk.BOTTOM, pady=50)
