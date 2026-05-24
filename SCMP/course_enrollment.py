import tkinter as tk
from tkinter import messagebox
import os
import dashboard

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"

def confirm_enrollment(window):
    messagebox.showinfo("Success", "Course Enrollment Confirmed!")
    window.destroy()
    dashboard.show_dashboard()

def show_enrollment():
    window = tk.Tk() # Re-initialize root for the flow
    window.title("SCMP - Course Enrollment")
    
    if os.name == 'nt': window.state('zoomed')
    else:
        try: window.attributes('-zoomed', True)
        except: window.geometry("1024x768")
            
    window.configure(bg=COLOR_BG)
    
    # Header
    header = tk.Frame(window, bg=COLOR_HEADER, height=120)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Step 2: Course Enrollment", font=("Arial", 32, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=35)
    
    # Card
    card = tk.Frame(window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=300, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Select Your Core Subjects:", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=30)
    
    courses = ["Python Programming", "Applied Mathematics", "AI & Machine Learning", "Data Structures", "Computer Networks", "Cyber Security"]
    
    for course in courses:
        tk.Checkbutton(card, text=course, font=("Arial", 18), bg=COLOR_CARD, fg=COLOR_TEXT, activebackground=COLOR_CARD).pack(anchor="w", padx=150, pady=12)
        
    tk.Button(card, text="COMPLETE & GO TO DASHBOARD", font=("Arial", 14, "bold"), bg=COLOR_ACCENT, fg="white", 
              width=35, height=2, relief="flat", command=lambda: confirm_enrollment(window)).pack(pady=40)

    window.mainloop()

if __name__ == "__main__":
    show_enrollment()
