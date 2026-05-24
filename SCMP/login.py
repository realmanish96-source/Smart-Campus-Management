import tkinter as tk
from tkinter import messagebox
import student_registration
import dashboard
import os

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"

def perform_login(user_entry, pass_entry, root):
    username = user_entry.get().strip()
    password = pass_entry.get().strip()
    
    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter both Username and Password.")
        return

    # Student Credentials Only
    if username == "manish123" and password == "050906":
        with open("SCMP/session.txt", "w") as f: f.write("Manish Jha")
        messagebox.showinfo("Success", "Welcome Manish Jha!")
        root.destroy()
        dashboard.show_dashboard()
    else:
        messagebox.showerror("Error", "Invalid Student Credentials")

def open_student_registration(root):
    root.destroy()
    student_registration.show_registration()

def show_login():
    root = tk.Tk()
    root.title("SCMP - Student Login Portal")
    
    if os.name == 'nt': root.state('zoomed')
    else:
        try: root.attributes('-zoomed', True)
        except: root.geometry("1024x768")
            
    root.configure(bg=COLOR_BG)
    
    # Header
    header = tk.Frame(root, bg=COLOR_HEADER, height=120)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Student Information System Login", font=("Arial", 32, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=35)
    
    # Login Card
    card = tk.Frame(root, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=350, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Student Access", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=(40, 20))
    
    # Fields
    fields_frame = tk.Frame(card, bg=COLOR_CARD)
    fields_frame.pack(pady=20)
    
    tk.Label(fields_frame, text="Username:", font=("Arial", 14), bg=COLOR_CARD, fg=COLOR_TEXT).grid(row=0, column=0, pady=10, sticky="e")
    user_entry = tk.Entry(fields_frame, font=("Arial", 14), width=30, bd=1, relief="solid")
    user_entry.grid(row=0, column=1, padx=20, pady=10)
    user_entry.focus()
    
    tk.Label(fields_frame, text="Password:", font=("Arial", 14), bg=COLOR_CARD, fg=COLOR_TEXT).grid(row=1, column=0, pady=10, sticky="e")
    pass_entry = tk.Entry(fields_frame, font=("Arial", 14), width=30, bd=1, relief="solid", show="*")
    pass_entry.grid(row=1, column=1, padx=20, pady=10)
    
    # Bindings
    user_entry.bind('<Return>', lambda e: pass_entry.focus())
    pass_entry.bind('<Return>', lambda e: perform_login(user_entry, pass_entry, root))

    # Login Button
    tk.Button(card, text="SECURE LOGIN", font=("Arial", 14, "bold"), bg=COLOR_ACCENT, fg="white", 
              width=25, height=2, relief="flat", command=lambda: perform_login(user_entry, pass_entry, root)).pack(pady=20)
    
    # Register Link
    tk.Button(card, text="New Student? Register Profile", font=("Arial", 11, "underline"), bg=COLOR_CARD, fg=COLOR_ACCENT, 
              bd=0, cursor="hand2", command=lambda: open_student_registration(root)).pack(pady=10)

    # Footer
    footer = tk.Frame(root, bg=COLOR_HEADER, height=40)
    footer.pack(side=tk.BOTTOM, fill=tk.X)
    tk.Label(footer, text=" Student Portal v2.2", font=("Arial", 9), bg=COLOR_HEADER, fg="white").pack(side=tk.LEFT, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    show_login()
