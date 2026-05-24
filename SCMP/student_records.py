import tkinter as tk
import os

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_TEXT = "#34495e"

def show_records():
    window = tk.Toplevel()
    window.title("Student Records")
    
    if os.name == 'nt': window.state('zoomed')
    else:
        try: window.attributes('-zoomed', True)
        except: window.geometry("1024x768")
            
    window.configure(bg=COLOR_BG)
    
    header = tk.Frame(window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Student Records Database", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    card = tk.Frame(window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=100, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Recent Registrations", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=30)
    
    table_frame = tk.Frame(card, bg=COLOR_CARD)
    table_frame.pack(pady=10)
    
    headers = ["ID", "Student Name", "Course", "Email"]
    for i, h in enumerate(headers):
        tk.Label(table_frame, text=h, font=("Arial", 16, "bold"), bg="#f8f9fa", width=20, pady=10, borderwidth=1, relief="solid").grid(row=0, column=i)
        
    records = [
        ("001", "Manish Jha", "B.Tech CSE", "manish@example.com"),
        ("002", "Rahul Sharma", "B.Tech IT", "rahul@example.com"),
        ("003", "Anjali Singh", "B.Tech ECE", "anjali@example.com"),
        ("004", "Vikram Sahay", "B.Tech AI", "vikram@example.com")
    ]
    
    for r_idx, row in enumerate(records):
        for c_idx, val in enumerate(row):
            tk.Label(table_frame, text=val, font=("Arial", 14), bg=COLOR_CARD, width=20, pady=8, borderwidth=1, relief="solid").grid(row=r_idx+1, column=c_idx)

    tk.Button(window, text="CLOSE", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", 
              padx=30, pady=10, relief="flat", command=window.destroy).pack(side=tk.BOTTOM, pady=50)
