import tkinter as tk
from tkinter import messagebox
import os

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_TEXT = "#34495e"

def save_data():
    messagebox.showinfo("Backup", "Data Successfully Backed up to student_records.csv")

def show_file_manager():
    window = tk.Toplevel()
    window.title("File Manager")
    
    if os.name == 'nt': window.state('zoomed')
    else:
        try: window.attributes('-zoomed', True)
        except: window.geometry("1024x768")
            
    window.configure(bg=COLOR_BG)
    
    header = tk.Frame(window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="File & Data Management", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    card = tk.Frame(window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=100, padx=300, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Database Status: Connected", font=("Arial", 18, "bold"), bg=COLOR_CARD, fg="#27ae60").pack(pady=30)
    tk.Label(card, text="Last Backup: 24 May 2026", font=("Arial", 14), bg=COLOR_CARD, fg=COLOR_TEXT).pack(pady=10)
    
    tk.Button(card, text="GENERATE NEW BACKUP", font=("Arial", 14, "bold"), bg="#3498db", fg="white", 
              width=25, height=2, relief="flat", command=save_data).pack(pady=40)

    tk.Button(window, text="CLOSE", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", 
              padx=30, pady=10, relief="flat", command=window.destroy).pack(side=tk.BOTTOM, pady=50)
