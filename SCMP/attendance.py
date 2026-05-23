import tkinter as tk
import os

def show_attendance():
    # Create a new top-level window
    attendance_window = tk.Toplevel()
    attendance_window.title("Attendance Records")
    
    # CROSS-PLATFORM FULL SCREEN FIX
    if os.name == 'nt':
        attendance_window.state('zoomed')
    else:
        try:
            attendance_window.attributes('-zoomed', True)
        except tk.TclError:
            width = attendance_window.winfo_screenwidth()
            height = attendance_window.winfo_screenheight()
            attendance_window.geometry(f"{width}x{height}+0+0")
            
    attendance_window.configure(bg="white")
    
    tk.Label(attendance_window, text="Student Attendance Overview", font=("Arial", 28, "bold"), bg="white", fg="blue").pack(pady=50)
    
    # Table-like container
    table_frame = tk.Frame(attendance_window, bg="white")
    table_frame.pack(pady=20)
    
    # UPDATED SUBJECTS AND PLACEHOLDER ATTENDANCE
    subjects = [
        "Python",
        "IEE",
        "Maths",
        "Chemistry",
        "AI",
        "Comunication Skills"
    ]
    
    # Table Headings
    tk.Label(table_frame, text="Subject Name", font=("Arial", 16, "bold"), bg="lightgray", width=30, borderwidth=1, relief="solid").grid(row=0, column=0)
    tk.Label(table_frame, text="Attendance Percentage", font=("Arial", 16, "bold"), bg="lightgray", width=30, borderwidth=1, relief="solid").grid(row=0, column=1)
    
    # Display each subject and a '-' for attendance
    for i, subject in enumerate(subjects):
        tk.Label(table_frame, text=subject, font=("Arial", 14), bg="white", width=30, borderwidth=1, relief="solid").grid(row=i+1, column=0)
        tk.Label(table_frame, text="-", font=("Arial", 14), bg="white", width=30, borderwidth=1, relief="solid").grid(row=i+1, column=1)
    
    # Close button
    tk.Button(attendance_window, text="Back to Dashboard", font=("Arial", 12, "bold"), bg="blue", fg="white", 
              width=20, command=attendance_window.destroy).pack(pady=50)
