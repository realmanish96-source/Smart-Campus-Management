import tkinter as tk
import os

# --- MODERN COLOR PALETTE ---
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"

def show_marks():
    marks_window = tk.Toplevel()
    marks_window.title("SCMP - Academic Marks")
    
    if os.name == 'nt':
        marks_window.state('zoomed')
    else:
        try:
            marks_window.attributes('-zoomed', True)
        except tk.TclError:
            width = marks_window.winfo_screenwidth()
            height = marks_window.winfo_screenheight()
            marks_window.geometry(f"{width}x{height}+0+0")
            
    marks_window.configure(bg=COLOR_BG)
    
    # --- HEADER ---
    header = tk.Frame(marks_window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Semester Examination Marks", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    # --- CONTENT CARD ---
    card = tk.Frame(marks_window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=100, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Student Performance Report", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=(40, 30))
    
    # Table Frame
    table_frame = tk.Frame(card, bg=COLOR_CARD)
    table_frame.pack(pady=10)
    
    # Table Headings - INCREASED SIZE
    tk.Label(table_frame, text="SUBJECT", font=("Arial", 14, "bold"), bg="#f8f9fa", fg=COLOR_HEADER, width=25, pady=10, borderwidth=1, relief="solid").grid(row=0, column=0)
    tk.Label(table_frame, text="TOTAL", font=("Arial", 14, "bold"), bg="#f8f9fa", fg=COLOR_HEADER, width=12, pady=10, borderwidth=1, relief="solid").grid(row=0, column=1)
    tk.Label(table_frame, text="OBTAINED", font=("Arial", 14, "bold"), bg="#f8f9fa", fg=COLOR_HEADER, width=12, pady=10, borderwidth=1, relief="solid").grid(row=0, column=2)
    tk.Label(table_frame, text="GRADE", font=("Arial", 14, "bold"), bg="#f8f9fa", fg=COLOR_HEADER, width=10, pady=10, borderwidth=1, relief="solid").grid(row=0, column=3)
    
    marks_data = [
        ("Python", 50, 45, "A+"),
        ("IEE", 50, 38, "B+"),
        ("Maths", 50, 48, "O"),
        ("Chemistry", 50, 40, "A"),
        ("AI", 50, 44, "A+"),
        ("Comunication Skills", 50, 42, "A")
    ]
    
    # Display each row - INCREASED SIZE
    for i, (sub, total, obtained, grade) in enumerate(marks_data):
        tk.Label(table_frame, text=sub, font=("Arial", 14), bg=COLOR_CARD, fg=COLOR_TEXT, width=25, pady=8, borderwidth=1, relief="solid").grid(row=i+1, column=0)
        tk.Label(table_frame, text=total, font=("Arial", 14), bg=COLOR_CARD, fg=COLOR_TEXT, width=12, pady=8, borderwidth=1, relief="solid").grid(row=i+1, column=1)
        tk.Label(table_frame, text=obtained, font=("Arial", 14, "bold"), bg=COLOR_CARD, fg=COLOR_ACCENT, width=12, pady=8, borderwidth=1, relief="solid").grid(row=i+1, column=2)
        tk.Label(table_frame, text=grade, font=("Arial", 14, "bold"), bg=COLOR_CARD, fg="#27ae60", width=10, pady=8, borderwidth=1, relief="solid").grid(row=i+1, column=3)
    
    # --- BACK BUTTON ---
    tk.Button(marks_window, text="CLOSE & GO BACK", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", 
              padx=30, pady=10, relief="flat", command=marks_window.destroy).pack(side=tk.BOTTOM, pady=50)
