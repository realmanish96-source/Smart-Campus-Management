import tkinter as tk
import os

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_TEXT = "#34495e"

def show_view_complaints():
    window = tk.Toplevel()
    window.title("Faculty - View Complaints")
    
    if os.name == 'nt': window.state('zoomed')
    else:
        try: window.attributes('-zoomed', True)
        except: window.geometry("1024x768")
            
    window.configure(bg=COLOR_BG)
    
    header = tk.Frame(window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Student Feedback & Complaints", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    card = tk.Frame(window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=100, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Recent Complaints Received", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=30)
    
    table_frame = tk.Frame(card, bg=COLOR_CARD)
    table_frame.pack(pady=10)
    
    headers = ["Date", "Student Name", "Subject", "Complaint Content"]
    for i, h in enumerate(headers):
        w = 40 if i == 3 else 15
        tk.Label(table_frame, text=h, font=("Arial", 14, "bold"), bg="#f8f9fa", width=w, pady=10, borderwidth=1, relief="solid").grid(row=0, column=i)
        
    complaints = [
        ("23 May", "Manish Jha", "Lab PC", "PC #4 in Lab 1 is not turning on."),
        ("22 May", "Rahul Sharma", "Library", "Library AC is making too much noise."),
        ("21 May", "Anjali Singh", "Hostel", "Water supply issue in Block B.")
    ]
    
    for r_idx, row in enumerate(complaints):
        for c_idx, val in enumerate(row):
            w = 40 if c_idx == 3 else 15
            tk.Label(table_frame, text=val, font=("Arial", 12), bg=COLOR_CARD, width=w, pady=12, borderwidth=1, relief="solid").grid(row=r_idx+1, column=c_idx)

    tk.Button(window, text="CLOSE", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", 
              padx=30, pady=10, relief="flat", command=window.destroy).pack(side=tk.BOTTOM, pady=50)
