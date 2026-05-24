import tkinter as tk
from tkinter import messagebox
import student_registration
import faculty_registration
import dashboard
import faculty_dashboard
import os

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"

def perform_login(role_var, user_entry, pass_entry, root):
    role = role_var.get()
    username = user_entry.get().strip()
    password = pass_entry.get().strip()
    
    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter both Username and Password.")
        return

    if role == "Student":
        if username == "manish123" and password == "050906":
            with open("SCMP/session.txt", "w") as f: f.write("Manish Jha")
            messagebox.showinfo("Success", "Welcome Manish Jha (Student)!")
            root.destroy()
            dashboard.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid Student Credentials")
    else: # Faculty
        # User is now also added to Faculty credentials
        if (username == "faculty" and password == "admin") or (username == "manish123" and password == "050906"):
            name = "Manish Jha" if username == "manish123" else "Faculty"
            with open("SCMP/faculty_session.txt", "w") as f: f.write(name)
            messagebox.showinfo("Success", f"Welcome Prof. {name}!")
            root.destroy()
            faculty_dashboard.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid Faculty Credentials")

def open_student_registration(root):
    root.destroy()
    student_registration.show_registration()

def open_faculty_registration(root):
    root.destroy()
    faculty_registration.show_faculty_registration()

def show_login():
    root = tk.Tk()
    root.title("SCMP - Login Portal")
    
    if os.name == 'nt': root.state('zoomed')
    else:
        try: root.attributes('-zoomed', True)
        except: root.geometry("1024x768")
            
    root.configure(bg=COLOR_BG)
    
    # Header
    header = tk.Frame(root, bg=COLOR_HEADER, height=120)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Campus Management Login", font=("Arial", 32, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=35)
    
    # Login Card
    card = tk.Frame(root, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=350, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Access Your Account", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=(40, 20))
    
    # Role Selection
    role_frame = tk.Frame(card, bg=COLOR_CARD)
    role_frame.pack(pady=10)
    tk.Label(role_frame, text="Select Role:", font=("Arial", 14, "bold"), bg=COLOR_CARD, fg=COLOR_TEXT).pack(side=tk.LEFT, padx=10)
    
    role_var = tk.StringVar(value="Student")
    tk.Radiobutton(role_frame, text="Student", variable=role_var, value="Student", font=("Arial", 12), bg=COLOR_CARD).pack(side=tk.LEFT, padx=10)
    tk.Radiobutton(role_frame, text="Faculty", variable=role_var, value="Faculty", font=("Arial", 12), bg=COLOR_CARD).pack(side=tk.LEFT, padx=10)
    
    # Fields
    fields_frame = tk.Frame(card, bg=COLOR_CARD)
    fields_frame.pack(pady=20)
    
    tk.Label(fields_frame, text="Username:", font=("Arial", 14), bg=COLOR_CARD, fg=COLOR_TEXT).grid(row=0, column=0, pady=10, sticky="e")
    user_entry = tk.Entry(fields_frame, font=("Arial", 14), width=30, bd=1, relief="solid")
    user_entry.grid(row=0, column=1, padx=20, pady=10)
    
    tk.Label(fields_frame, text="Password:", font=("Arial", 14), bg=COLOR_CARD, fg=COLOR_TEXT).grid(row=1, column=0, pady=10, sticky="e")
    pass_entry = tk.Entry(fields_frame, font=("Arial", 14), width=30, bd=1, relief="solid", show="*")
    pass_entry.grid(row=1, column=1, padx=20, pady=10)
    
    # Login Button
    tk.Button(card, text="SECURE LOGIN", font=("Arial", 14, "bold"), bg=COLOR_ACCENT, fg="white", 
              width=25, height=2, relief="flat", command=lambda: perform_login(role_var, user_entry, pass_entry, root)).pack(pady=20)
    
    # Register Links
    links_frame = tk.Frame(card, bg=COLOR_CARD)
    links_frame.pack(pady=10)
    
    tk.Button(links_frame, text="Student Register", font=("Arial", 11, "underline"), bg=COLOR_CARD, fg=COLOR_ACCENT, 
              bd=0, cursor="hand2", command=lambda: open_student_registration(root)).pack(side=tk.LEFT, padx=20)
              
    tk.Button(links_frame, text="Faculty Register", font=("Arial", 11, "underline"), bg=COLOR_CARD, fg=COLOR_ACCENT, 
              bd=0, cursor="hand2", command=lambda: open_faculty_registration(root)).pack(side=tk.LEFT, padx=20)

    # Footer
    footer = tk.Frame(root, bg=COLOR_HEADER, height=40)
    footer.pack(side=tk.BOTTOM, fill=tk.X)
    tk.Label(footer, text=" Student/Faculty Identification System v2.1", font=("Arial", 9), bg=COLOR_HEADER, fg="white").pack(side=tk.LEFT, pady=10)

    root.mainloop()

if __name__ == "__main__":
    show_login()
