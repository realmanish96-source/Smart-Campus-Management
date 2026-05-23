import tkinter as tk
import notices
import attendance
import complaints
import marks
import sys
import os

def show_dashboard():
    root = tk.Tk()
    root.title("SCMP - Dashboard")
    
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
    
    # HEADER SECTION
    header_frame = tk.Frame(root, bg="blue", height=120)
    header_frame.pack(side=tk.TOP, fill=tk.X)
    
    # Project Title (Left)
    tk.Label(header_frame, text="Smart Campus Dashboard", font=("Arial", 24, "bold"), bg="blue", fg="white").pack(side=tk.LEFT, padx=30, pady=30)
    
    # Profile & Logo Area (Right)
    right_frame = tk.Frame(header_frame, bg="blue")
    right_frame.pack(side=tk.RIGHT, padx=30)
    
    # UPDATED STUDENT INFO (Roll No changed to 29)
    info_text = "Name: Manish Jha\nUsername: manish123\nRoll No: 29\nClass: B.Tech CSE"
    tk.Label(right_frame, text=info_text, font=("Arial", 10), bg="blue", fg="white", justify=tk.LEFT).pack(side=tk.LEFT, padx=20)
    
    # WHATSAPP DEFAULT DP REPLICATION
    logo_canvas = tk.Canvas(right_frame, width=80, height=80, bg="blue", highlightthickness=0)
    logo_canvas.pack(side=tk.RIGHT)
    logo_canvas.create_oval(5, 5, 75, 75, fill="#E1E1E1", outline="#E1E1E1")
    logo_canvas.create_oval(30, 20, 50, 40, fill="#FFFFFF", outline="#FFFFFF") 
    logo_canvas.create_oval(28, 18, 52, 42, fill="#A9A9A9", outline="#A9A9A9")
    logo_canvas.create_arc(15, 45, 65, 95, start=0, extent=180, fill="#A9A9A9", outline="#A9A9A9")

    # MAIN CONTENT SECTION
    tk.Label(root, text="Welcome to the Smart Campus System", font=("Arial", 20), bg="white").pack(pady=50)
    
    # Buttons Container
    btn_frame = tk.Frame(root, bg="white")
    btn_frame.pack(pady=20)
    
    # Grid Layout for buttons
    buttons = [
        ("Notices", notices.show_notices),
        ("Attendance", attendance.show_attendance),
        ("Marks", marks.show_marks),
        ("Complaints", complaints.show_complaints)
    ]
    
    for i, (text, command) in enumerate(buttons):
        tk.Button(btn_frame, text=text, font=("Arial", 16, "bold"), bg="blue", fg="white", 
                  width=25, height=2, command=command).grid(row=i//2, column=i%2, padx=20, pady=20)
    
    # Exit Button at bottom
    tk.Button(root, text="Logout & Exit", font=("Arial", 14, "bold"), bg="red", fg="white", width=20, 
              command=root.quit).pack(side=tk.BOTTOM, pady=50)
    
    root.mainloop()
