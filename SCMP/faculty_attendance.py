import tkinter as tk
from tkinter import messagebox
import os

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"

def save_attendance():
    messagebox.showinfo("Success", "Attendance Data Recorded!")

def show_attendance_entry():
    window = tk.Toplevel()
    window.title("Faculty - Update Attendance")
    
    if os.name == 'nt': window.state('zoomed')
    else:
        try: window.attributes('-zoomed', True)
        except: window.geometry("1024x768")
            
    window.configure(bg=COLOR_BG)
    
    header = tk.Frame(window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Attendance Management System", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    card = tk.Frame(window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=250, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Daily Attendance Input", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=(40, 30))
    
    fields_frame = tk.Frame(card, bg=COLOR_CARD)
    fields_frame.pack(pady=10)

    fields = ["Student ID", "Subject Code", "Session Date", "Status (P/A)"]
    for i, field in enumerate(fields):
        tk.Label(fields_frame, text=field + ":", font=("Arial", 16, "bold"), bg=COLOR_CARD, fg=COLOR_TEXT).grid(row=i, column=0, padx=20, pady=15, sticky="e")
        tk.Entry(fields_frame, font=("Arial", 16), width=25, bd=1, relief="solid").grid(row=i, column=1, padx=20, pady=15)
        
    tk.Button(card, text="RECORD ATTENDANCE", font=("Arial", 14, "bold"), bg=COLOR_ACCENT, fg="white", 
              width=25, height=2, relief="flat", command=save_attendance).pack(pady=40)

    tk.Button(window, text="CLOSE", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", 
              padx=30, pady=10, relief="flat", command=window.destroy).pack(side=tk.BOTTOM, pady=50)
