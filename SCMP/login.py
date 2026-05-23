import tkinter as tk
from tkinter import messagebox
import dashboard
import os

def login(event=None):
    # UPDATED CREDENTIALS
    username_correct = "manish123"
    password_correct = "050906"
    
    entered_username = user_entry.get()
    entered_password = pass_entry.get()
    
    if entered_username == username_correct and entered_password == password_correct:
        root.destroy()
        dashboard.show_dashboard()
    else:
        # We only show error if both fields are attempted
        messagebox.showerror("Login Error", "Invalid Username or Password")

def clear_fields():
    user_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)
    user_entry.focus()

def toggle_password():
    if show_pass_var.get():
        pass_entry.config(show="")
    else:
        pass_entry.config(show="*")

def on_enter(e):
    if e.widget['text'] == "Login":
        e.widget['background'] = '#0055ff'
    else:
        e.widget['background'] = '#555555'

def on_leave(e):
    if e.widget['text'] == "Login":
        e.widget['background'] = 'blue'
    else:
        e.widget['background'] = 'gray'

def focus_next(event):
    pass_entry.focus()
    return "break" # Prevents the global root Enter binding from firing

def show_login():
    global root, user_entry, pass_entry, show_pass_var
    
    root = tk.Tk()
    root.title("SCMP - Login")
    
    # Global bind for login
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
    
    # Main container
    main_frame = tk.Frame(root, bg="white")
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    # Header
    tk.Label(main_frame, text="Welcome", font=("Arial", 48, "bold"), bg="white", fg="blue").pack(pady=(0, 10))
    tk.Label(main_frame, text="Smart Campus Management System", font=("Arial", 14), bg="white", fg="gray").pack(pady=(0, 40))
    
    # Login Box
    login_box = tk.Frame(main_frame, bg="white", highlightbackground="blue", highlightthickness=2, padx=50, pady=40)
    login_box.pack()
    
    tk.Label(login_box, text="User Login", font=("Arial", 20, "bold"), bg="white").pack(pady=(0, 20))
    
    # Username
    tk.Label(login_box, text="Username:", font=("Arial", 12), bg="white").pack(anchor="w", pady=(10, 0))
    user_entry = tk.Entry(login_box, font=("Arial", 14), bd=2, width=35)
    user_entry.pack(pady=5)
    user_entry.focus()
    
    # NEW: Bind Enter key in username to move focus to password
    user_entry.bind('<Return>', focus_next)
    
    # Password
    tk.Label(login_box, text="Password:", font=("Arial", 12), bg="white").pack(anchor="w", pady=(10, 0))
    pass_entry = tk.Entry(login_box, font=("Arial", 14), bd=2, show="*", width=35)
    pass_entry.pack(pady=5)
    
    # Show Password Checkbox
    show_pass_var = tk.BooleanVar()
    show_pass_check = tk.Checkbutton(login_box, text="Show Password", variable=show_pass_var, 
                                     onvalue=True, offvalue=False, command=toggle_password,
                                     bg="white", font=("Arial", 10))
    show_pass_check.pack(anchor="w", pady=5)
    
    # Buttons Frame
    btn_frame = tk.Frame(login_box, bg="white")
    btn_frame.pack(pady=30)
    
    # Login Button
    login_btn = tk.Button(btn_frame, text="Login", font=("Arial", 14, "bold"), bg="blue", fg="white", 
                          width=15, command=login, cursor="hand2")
    login_btn.pack(side=tk.LEFT, padx=10)
    login_btn.bind("<Enter>", on_enter)
    login_btn.bind("<Leave>", on_leave)
    
    # Clear Button
    clear_btn = tk.Button(btn_frame, text="Clear", font=("Arial", 14, "bold"), bg="gray", fg="white", 
                          width=10, command=clear_fields, cursor="hand2")
    clear_btn.pack(side=tk.LEFT, padx=10)
    clear_btn.bind("<Enter>", on_enter)
    clear_btn.bind("<Leave>", on_leave)
    
    # Footer Status Bar
    status_frame = tk.Frame(root, bg="#f0f0f0", bd=1, relief=tk.SUNKEN)
    status_frame.pack(side=tk.BOTTOM, fill=tk.X)
    tk.Label(status_frame, text="Student Login Portal v1.0", font=("Arial", 9), bg="#f0f0f0").pack(side=tk.LEFT, padx=10)
    tk.Label(status_frame, text="For technical help, contact the Lab Assistant", font=("Arial", 9), bg="#f0f0f0").pack(side=tk.RIGHT, padx=10)
    
    root.mainloop()

if __name__ == "__main__":
    show_login()
