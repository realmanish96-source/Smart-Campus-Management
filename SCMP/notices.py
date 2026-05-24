import tkinter as tk
import os

COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_TEXT = "#34495e"

def show_notices():
    window = tk.Toplevel()
    window.title("SCMP - Campus Notices")
    if os.name == 'nt': window.state('zoomed')
    else:
        try: window.attributes('-zoomed', True)
        except: window.geometry("1024x768")
    window.configure(bg=COLOR_BG)
    
    header = tk.Frame(window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Campus Notices", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    card = tk.Frame(window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=100, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Latest Announcements", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=(40, 20))
    
    notices_list = [
        "1) Semester End exams will be starting from 22 june.",
        "2) Third internal will be startting from 11 june.",
        "3) lab examinations will be starting from 1 june to 5 june.",
        "4) Submit your python projects till 25 may.",
        "5) Maintain your overall attendance minimum 85%."
    ]
    
    for notice in notices_list:
        tk.Label(card, text=notice, font=("Arial", 18), bg=COLOR_CARD, fg=COLOR_TEXT, anchor="w", justify=tk.LEFT).pack(pady=15, padx=100, fill=tk.X)
    
    tk.Button(window, text="CLOSE", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", padx=30, pady=10, relief="flat", command=window.destroy).pack(side=tk.BOTTOM, pady=50)
