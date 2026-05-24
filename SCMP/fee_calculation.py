import tkinter as tk
from tkinter import messagebox
import os

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"

def calculate_total(tuition_val, hostel_var, transport_var, result_label):
    try:
        total = int(tuition_val)
        if hostel_var.get(): total += 45000
        if transport_var.get(): total += 15000
        result_label.config(text=f"Total Outstanding: ₹ {total:,}")
    except ValueError:
        messagebox.showerror("Error", "Invalid Tuition Fee value.")

def show_fee():
    window = tk.Toplevel()
    window.title("SCMP - Fees Update System")
    
    if os.name == 'nt': window.state('zoomed')
    else:
        try: window.attributes('-zoomed', True)
        except: window.geometry("1024x768")
            
    window.configure(bg=COLOR_BG)
    
    # Header
    header = tk.Frame(window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Fees Management & Updates", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    # Card
    card = tk.Frame(window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=300, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Fee Component Selection", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=(40, 20))
    
    # Tuition Section (Fixed)
    tuition_frame = tk.Frame(card, bg=COLOR_CARD)
    tuition_frame.pack(pady=20)
    tk.Label(tuition_frame, text="Tuition Fee (Annual):", font=("Arial", 16), bg=COLOR_CARD, fg=COLOR_TEXT).pack(side=tk.LEFT, padx=10)
    tk.Label(tuition_frame, text="₹ 85,000", font=("Arial", 16, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(side=tk.LEFT, padx=10)
    
    # Optional Sections (Checkboxes)
    options_frame = tk.Frame(card, bg=COLOR_CARD)
    options_frame.pack(pady=20)
    
    hostel_var = tk.BooleanVar()
    tk.Checkbutton(options_frame, text="Include Hostel Fee (₹ 45,000)", variable=hostel_var, 
                   font=("Arial", 14), bg=COLOR_CARD, fg=COLOR_TEXT, activebackground=COLOR_CARD).pack(anchor="w", pady=10)
    
    transport_var = tk.BooleanVar()
    tk.Checkbutton(options_frame, text="Include Transport Fee (₹ 15,000)", variable=transport_var, 
                   font=("Arial", 14), bg=COLOR_CARD, fg=COLOR_TEXT, activebackground=COLOR_CARD).pack(anchor="w", pady=10)
    
    # Result Area
    result_label = tk.Label(card, text="Total Outstanding: ₹ 85,000", font=("Arial", 24, "bold"), bg=COLOR_CARD, fg="#e74c3c")
    result_label.pack(pady=30)
    
    # Calculate Button
    tk.Button(card, text="UPDATE & CALCULATE TOTAL", font=("Arial", 14, "bold"), bg=COLOR_ACCENT, fg="white", 
              width=30, height=2, relief="flat", command=lambda: calculate_total(85000, hostel_var, transport_var, result_label)).pack(pady=10)
    
    tk.Label(card, text="*Please update your selection to see the final amount due.", font=("Arial", 10, "italic"), bg=COLOR_CARD, fg="gray").pack(pady=20)

    # Close Button
    tk.Button(window, text="CLOSE & GO BACK", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", 
              padx=30, pady=10, relief="flat", command=window.destroy).pack(side=tk.BOTTOM, pady=50)
