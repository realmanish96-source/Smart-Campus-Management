import tkinter as tk
from tkinter import messagebox
import os

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"

def post_notice():
    messagebox.showinfo("Success", "New Campus Notice Published!")

def show_update_notices():
    window = tk.Toplevel()
    window.title("Faculty - Manage Notices")
    
    if os.name == 'nt': window.state('zoomed')
    else:
        try: window.attributes('-zoomed', True)
        except: window.geometry("1024x768")
            
    window.configure(bg=COLOR_BG)
    
    header = tk.Frame(window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Campus Notice Management", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    card = tk.Frame(window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=200, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Publish a New Announcement", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=(40, 20))
    
    tk.Label(card, text="Notice Title:", font=("Arial", 14, "bold"), bg=COLOR_CARD, fg=COLOR_TEXT).pack(anchor="w", padx=100, pady=(20, 5))
    tk.Entry(card, font=("Arial", 14), width=60, bd=1, relief="solid").pack(padx=100)

    tk.Label(card, text="Detailed Description:", font=("Arial", 14, "bold"), bg=COLOR_CARD, fg=COLOR_TEXT).pack(anchor="w", padx=100, pady=(20, 5))
    tk.Text(card, font=("Arial", 14), width=60, height=8, bd=1, relief="solid").pack(padx=100)
        
    tk.Button(card, text="PUBLISH NOTICE", font=("Arial", 14, "bold"), bg=COLOR_ACCENT, fg="white", 
              width=25, height=2, relief="flat", command=post_notice).pack(pady=40)

    tk.Button(window, text="CLOSE", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", 
              padx=30, pady=10, relief="flat", command=window.destroy).pack(side=tk.BOTTOM, pady=50)
