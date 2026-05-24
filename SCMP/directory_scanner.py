import tkinter as tk
import os

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_TEXT = "#34495e"

def show_scanner():
    window = tk.Toplevel()
    window.title("Directory Scanner")
    
    if os.name == 'nt': window.state('zoomed')
    else:
        try: window.attributes('-zoomed', True)
        except: window.geometry("1024x768")
            
    window.configure(bg=COLOR_BG)
    
    header = tk.Frame(window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="System Directory Scanner", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    card = tk.Frame(window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=200, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Files in Project Directory:", font=("Arial", 20, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=30)
    
    listbox = tk.Listbox(card, font=("Arial", 14), width=60, height=15, bd=1, relief="solid")
    listbox.pack(pady=10)
    
    # Scan files
    try:
        files = os.listdir('.')
        for f in files:
            listbox.insert(tk.END, f"  📄 {f}")
    except Exception as e:
        listbox.insert(tk.END, f"Error: {e}")

    tk.Button(window, text="CLOSE", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", 
              padx=30, pady=10, relief="flat", command=window.destroy).pack(side=tk.BOTTOM, pady=50)
