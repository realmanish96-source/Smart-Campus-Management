import tkinter as tk
from tkinter import messagebox
import os
import faculty_dashboard

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"

def register_faculty(window, name_entry):
    name = name_entry.get().strip()
    if name:
        # Create a faculty session file
        with open("SCMP/faculty_session.txt", "w") as f:
            f.write(name)
        
        messagebox.showinfo("Success", f"Welcome Prof. {name}! Registration Successful.")
        window.destroy()
        faculty_dashboard.show_dashboard()
    else:
        messagebox.showwarning("Input Error", "Please enter your name to register.")

def show_faculty_registration():
    window = tk.Tk()
    window.title("SCMP - Faculty Registration")
    
    if os.name == 'nt': window.state('zoomed')
    else:
        try: window.attributes('-zoomed', True)
        except: window.geometry("1024x768")
            
    window.configure(bg=COLOR_BG)
    
    # Header
    header = tk.Frame(window, bg=COLOR_HEADER, height=120)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Faculty Registration System", font=("Arial", 32, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=35)
    
    # Card
    card = tk.Frame(window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=100, padx=350, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Join the Faculty Portal", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=(40, 30))
    
    fields_frame = tk.Frame(card, bg=COLOR_CARD)
    fields_frame.pack(pady=10)

    # Simplified fields: Name, Email, Branch
    tk.Label(fields_frame, text="Full Name:", font=("Arial", 16, "bold"), bg=COLOR_CARD, fg=COLOR_TEXT).grid(row=0, column=0, padx=20, pady=15, sticky="e")
    name_entry = tk.Entry(fields_frame, font=("Arial", 16), width=30, bd=1, relief="solid")
    name_entry.grid(row=0, column=1, padx=20, pady=15)
    name_entry.focus()

    tk.Label(fields_frame, text="Official Email:", font=("Arial", 16, "bold"), bg=COLOR_CARD, fg=COLOR_TEXT).grid(row=1, column=0, padx=20, pady=15, sticky="e")
    tk.Entry(fields_frame, font=("Arial", 16), width=30, bd=1, relief="solid").grid(row=1, column=1, padx=20, pady=15)

    tk.Label(fields_frame, text="Department/Branch:", font=("Arial", 16, "bold"), bg=COLOR_CARD, fg=COLOR_TEXT).grid(row=2, column=0, padx=20, pady=15, sticky="e")
    tk.Entry(fields_frame, font=("Arial", 16), width=30, bd=1, relief="solid").grid(row=2, column=1, padx=20, pady=15)
        
    tk.Button(card, text="CREATE FACULTY ACCOUNT", font=("Arial", 14, "bold"), bg=COLOR_ACCENT, fg="white", 
              width=30, height=2, relief="flat", command=lambda: register_faculty(window, name_entry)).pack(pady=40)

    window.mainloop()

if __name__ == "__main__":
    show_faculty_registration()
