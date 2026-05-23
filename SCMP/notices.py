import tkinter as tk
import os

# --- MODERN COLOR PALETTE ---
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"

def show_notices():
    notice_window = tk.Toplevel()
    notice_window.title("SCMP - Campus Notices")
    
    # CROSS-PLATFORM FULL SCREEN FIX
    if os.name == 'nt':
        notice_window.state('zoomed')
    else:
        try:
            notice_window.attributes('-zoomed', True)
        except tk.TclError:
            width = notice_window.winfo_screenwidth()
            height = notice_window.winfo_screenheight()
            notice_window.geometry(f"{width}x{height}+0+0")
            
    notice_window.configure(bg=COLOR_BG)
    
    # --- HEADER ---
    header = tk.Frame(notice_window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Campus Notices", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    # --- CONTENT CARD ---
    card = tk.Frame(notice_window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=100, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Latest Announcements", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=(40, 20))
    
    # Container for list
    list_frame = tk.Frame(card, bg=COLOR_CARD)
    list_frame.pack(pady=20, padx=50, fill=tk.X)
    
    notices_list = [
        "1) Semester End exams will be starting from 22 june.",
        "2) Third internal will be startting from 11 june.",
        "3) lab examinations will be starting from 1 june to 5 june.",
        "4) Submit your python projects till 25 may.",
        "5) Maintain your overall attendance minimum 85%."
    ]
    
    for notice in notices_list:
        # INCREASED TEXT SIZE
        tk.Label(list_frame, text=notice, font=("Arial", 18), bg=COLOR_CARD, fg=COLOR_TEXT, 
                 anchor="w", justify=tk.LEFT).pack(pady=15, fill=tk.X)
    
    # --- BACK BUTTON ---
    tk.Button(notice_window, text="CLOSE & GO BACK", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", 
              padx=30, pady=10, relief="flat", command=notice_window.destroy).pack(side=tk.BOTTOM, pady=50)
