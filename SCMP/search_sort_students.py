import tkinter as tk
import os

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_TEXT = "#34495e"

def show_search():
    window = tk.Toplevel()
    window.title("Search & Sort Students")
    
    if os.name == 'nt': window.state('zoomed')
    else:
        try: window.attributes('-zoomed', True)
        except: window.geometry("1024x768")
            
    window.configure(bg=COLOR_BG)
    
    header = tk.Frame(window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Search & Query Engine", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    card = tk.Frame(window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=150, fill=tk.BOTH, expand=True)
    
    # Search Controls
    search_frame = tk.Frame(card, bg=COLOR_CARD)
    search_frame.pack(pady=40)
    
    tk.Label(search_frame, text="Enter Student Name:", font=("Arial", 16), bg=COLOR_CARD, fg=COLOR_TEXT).pack(side=tk.LEFT, padx=10)
    tk.Entry(search_frame, font=("Arial", 16), width=30, bd=1, relief="solid").pack(side=tk.LEFT, padx=10)
    tk.Button(search_frame, text="SEARCH", font=("Arial", 12, "bold"), bg="#3498db", fg="white", padx=20).pack(side=tk.LEFT, padx=5)
    tk.Button(search_frame, text="SORT A-Z", font=("Arial", 12, "bold"), bg="#27ae60", fg="white", padx=20).pack(side=tk.LEFT, padx=5)
    
    # Results Area
    tk.Label(card, text="Search Results:", font=("Arial", 18, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=20)
    results_box = tk.Text(card, font=("Arial", 14), height=10, width=80, bd=1, relief="solid", bg="#f9f9f9")
    results_box.pack(pady=10)
    results_box.insert(tk.END, "Search for a student to see records here...")
    results_box.config(state="disabled")

    tk.Button(window, text="CLOSE", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", 
              padx=30, pady=10, relief="flat", command=window.destroy).pack(side=tk.BOTTOM, pady=50)
