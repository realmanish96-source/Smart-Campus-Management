import tkinter as tk
from tkinter import messagebox
import dashboard
import os

def login(event=None): # Added event parameter to handle Enter key
    # UPDATED CREDENTIALS
    username_correct = "manish123"
    password_correct = "050906"
    
    # Getting text from entry fields
    entered_username = user_entry.get()
    entered_password = pass_entry.get()
    
    if entered_username == username_correct and entered_password == password_correct:
        # Success: Close login window and open dashboard
        root.destroy()
        dashboard.show_dashboard()
    else:
        # Failure: Show error popup
        messagebox.showerror("Login Error", "Invalid Username or Password")

def show_login():
    global root, user_entry, pass_entry
    
    root = tk.Tk()
    root.title("SCMP - Login")
    
    # Bind Enter key to the login function
    root.bind('<Return>', login)
    
    # CROSS-PLATFORM FULL SCREEN FIX
    if os.name == 'nt':
        root.state('zoomed') 
    else:
        try:
            root.attributes('-zoomed', True) 
        except tk.TclError:
            width = root.winfo_screenwidth()
            height = root.winfo_screenheight()
            root.geometry(f"{width}x{height}+0+0")
    
    root.configure(bg="white")
    
    # Main container to center content
    main_frame = tk.Frame(root, bg="white")
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    # Header
    title_label = tk.Label(main_frame, text="Welcome", font=("Arial", 36, "bold"), bg="white", fg="blue")
    title_label.pack(pady=50)
    
    # Login Box
    login_box = tk.Frame(main_frame, bg="white", highlightbackground="blue", highlightthickness=2, padx=40, pady=40)
    login_box.pack()
    
    tk.Label(login_box, text="User Login", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
    
    # Username Field
    tk.Label(login_box, text="Username:", font=("Arial", 12), bg="white").pack(anchor="w", pady=(10, 0))
    user_entry = tk.Entry(login_box, font=("Arial", 14), bd=2, width=30)
    user_entry.pack(pady=5)
    
    # Password Field
    tk.Label(login_box, text="Password:", font=("Arial", 12), bg="white").pack(anchor="w", pady=(10, 0))
    pass_entry = tk.Entry(login_box, font=("Arial", 14), bd=2, show="*", width=30)
    pass_entry.pack(pady=5)
    
    # Login Button
    login_btn = tk.Button(login_box, text="Login", font=("Arial", 14, "bold"), bg="blue", fg="white", width=20, command=login)
    login_btn.pack(pady=30)
    
    root.mainloop()

if __name__ == "__main__":
    show_login()
