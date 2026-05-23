import tkinter as tk
import os

def show_marks():
    # Create a new top-level window
    marks_window = tk.Toplevel()
    marks_window.title("Marks Interface")
    
    # CROSS-PLATFORM FULL SCREEN FIX
    if os.name == 'nt':
        marks_window.state('zoomed')
    else:
        try:
            marks_window.attributes('-zoomed', True)
        except tk.TclError:
            width = marks_window.winfo_screenwidth()
            height = marks_window.winfo_screenheight()
            marks_window.geometry(f"{width}x{height}+0+0")
            
    marks_window.configure(bg="white")
    
    # Header
    tk.Label(marks_window, text="Academic Performance - Semester Marks", font=("Arial", 24, "bold"), bg="white", fg="blue").pack(pady=50)
    
    # Table Header Frame
    table_frame = tk.Frame(marks_window, bg="white")
    table_frame.pack(pady=20)
    
    # Table Headings
    tk.Label(table_frame, text="Subject", font=("Arial", 14, "bold"), bg="lightgray", width=25, borderwidth=1, relief="solid").grid(row=0, column=0)
    tk.Label(table_frame, text="Total Marks", font=("Arial", 14, "bold"), bg="lightgray", width=15, borderwidth=1, relief="solid").grid(row=0, column=1)
    tk.Label(table_frame, text="Marks Obtained", font=("Arial", 14, "bold"), bg="lightgray", width=15, borderwidth=1, relief="solid").grid(row=0, column=2)
    tk.Label(table_frame, text="Grade", font=("Arial", 14, "bold"), bg="lightgray", width=10, borderwidth=1, relief="solid").grid(row=0, column=3)
    
    # UPDATED SUBJECTS WITH RANDOM MARKS OUT OF 50
    marks_data = [
        ("Python", 50, 45, "A+"),
        ("IEE", 50, 38, "B+"),
        ("Maths", 50, 48, "O"),
        ("Chemistry", 50, 40, "A"),
        ("AI", 50, 44, "A+"),
        ("Comunication Skills", 50, 42, "A")
    ]
    
    # Display each row with marks out of 50
    for i, (sub, total, obtained, grade) in enumerate(marks_data):
        tk.Label(table_frame, text=sub, font=("Arial", 12), bg="white", width=25, borderwidth=1, relief="solid").grid(row=i+1, column=0)
        tk.Label(table_frame, text=total, font=("Arial", 12), bg="white", width=15, borderwidth=1, relief="solid").grid(row=i+1, column=1)
        tk.Label(table_frame, text=obtained, font=("Arial", 12), bg="white", width=15, borderwidth=1, relief="solid").grid(row=i+1, column=2)
        tk.Label(table_frame, text=grade, font=("Arial", 12), bg="white", width=10, borderwidth=1, relief="solid").grid(row=i+1, column=3)
    
    # Close button
    tk.Button(marks_window, text="Back to Dashboard", font=("Arial", 12, "bold"), bg="blue", fg="white", 
              width=20, command=marks_window.destroy).pack(pady=50)
