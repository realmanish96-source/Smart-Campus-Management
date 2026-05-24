import tkinter as tk
from tkinter import messagebox
import os
import course_enrollment

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"

def register_student(window, name_entry):
    name = name_entry.get().strip()
    if name:
        # Create a session file to "remember" the user
        with open("SCMP/session.txt", "w") as f:
            f.write(name)
        
        messagebox.showinfo("Success", f"Welcome {name}! Registration Successful.")
        window.destroy()
        course_enrollment.show_enrollment()
    else:
        messagebox.showwarning("Input Error", "Please enter your name to register.")

def show_registration():
    window = tk.Tk() # This is now our main starting window
    window.title("SCMP - Student Registration")
    
    if os.name == 'nt': window.state('zoomed')
    else:
        try: window.attributes('-zoomed', True)
        except: window.geometry("1024x768")
            
    window.configure(bg=COLOR_BG)
    
    # Header
    header = tk.Frame(window, bg=COLOR_HEADER, height=120)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Student Registration System", font=("Arial", 32, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=35)
    
    # Form Card
    card = tk.Frame(window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=250, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Create Your Student Profile", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=(40, 30))
    
    fields_frame = tk.Frame(card, bg=COLOR_CARD)
    fields_frame.pack(pady=10)

    # We need to capture the name specifically for the session
    tk.Label(fields_frame, text="Full Name:", font=("Arial", 16, "bold"), bg=COLOR_CARD, fg=COLOR_TEXT).grid(row=0, column=0, padx=20, pady=15, sticky="e")
    name_entry = tk.Entry(fields_frame, font=("Arial", 16), width=35, bd=1, relief="solid")
    name_entry.grid(row=0, column=1, padx=20, pady=15)
    name_entry.focus()

    other_fields = ["Father's Name", "Date of Birth", "Roll Number", "Email ID", "Address"]
    for i, field in enumerate(other_fields):
        tk.Label(fields_frame, text=field + ":", font=("Arial", 16, "bold"), bg=COLOR_CARD, fg=COLOR_TEXT).grid(row=i+1, column=0, padx=20, pady=15, sticky="e")
        tk.Entry(fields_frame, font=("Arial", 16), width=35, bd=1, relief="solid").grid(row=i+1, column=1, padx=20, pady=15)
        
    tk.Button(card, text="REGISTER & PROCEED", font=("Arial", 14, "bold"), bg="#27ae60", fg="white", 
              width=30, height=2, relief="flat", command=lambda: register_student(window, name_entry)).pack(pady=40)

    window.mainloop()

if __name__ == "__main__":
    show_registration()
