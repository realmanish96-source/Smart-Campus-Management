import tkinter as tk
import os

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_TEXT = "#34495e"

def calculate_fee():
    # Simple logic
    pass

def show_fee():
    window = tk.Toplevel()
    window.title("Fee Calculation")
    
    if os.name == 'nt': window.state('zoomed')
    else:
        try: window.attributes('-zoomed', True)
        except: window.geometry("1024x768")
            
    window.configure(bg=COLOR_BG)
    
    header = tk.Frame(window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Fee Management System", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    card = tk.Frame(window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=250, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Calculate Outstanding Fees", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=30)
    
    items = ["Tuition Fee", "Library Fee", "Laboratory Fee", "Hostel Fee", "Examination Fee"]
    for item in items:
        f = tk.Frame(card, bg=COLOR_CARD)
        f.pack(pady=10)
        tk.Label(f, text=item + ":", font=("Arial", 16), bg=COLOR_CARD, fg=COLOR_TEXT, width=20, anchor="w").pack(side=tk.LEFT)
        tk.Entry(f, font=("Arial", 16), width=15, bd=1, relief="solid").pack(side=tk.LEFT)
        
    tk.Button(card, text="CALCULATE TOTAL", font=("Arial", 14, "bold"), bg="#2ecc71", fg="white", 
              width=25, height=2, relief="flat").pack(pady=30)

    tk.Button(window, text="CLOSE", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", 
              padx=30, pady=10, relief="flat", command=window.destroy).pack(side=tk.BOTTOM, pady=50)
