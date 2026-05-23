import tkinter as tk
import os

def show_notices():
    # Create a new top-level window
    notice_window = tk.Toplevel()
    notice_window.title("Campus Notices")
    
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
            
    notice_window.configure(bg="white")
    
    tk.Label(notice_window, text="Important Campus Notices", font=("Arial", 28, "bold"), bg="white", fg="blue").pack(pady=50)
    
    # Container for notices
    content_frame = tk.Frame(notice_window, bg="white")
    content_frame.pack(pady=20)
    
    # UPDATED NOTICES
    notices_list = [
        "1) Semester End exams will be starting from 22 june.",
        "2) Third internal will be startting from 11 june.",
        "3) lab examinations will be starting from 1 june to 5 june.",
        "4) Submit your python projects till 25 may.",
        "5) Maintain your overall attendance minimum 85%."
    ]
    
    # Display each notice as a label
    for notice in notices_list:
        tk.Label(content_frame, text=notice, font=("Arial", 16), bg="white", anchor="w", fg="black").pack(pady=10, padx=50, fill="x")
    
    # Close button
    tk.Button(notice_window, text="Back to Dashboard", font=("Arial", 12, "bold"), bg="blue", fg="white", 
              width=20, command=notice_window.destroy).pack(pady=50)
