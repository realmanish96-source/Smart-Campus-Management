import tkinter as tk
import student_records
import search_sort_students
import faculty_marks
import faculty_attendance
import update_notices
import view_complaints
import sys
import os
from datetime import datetime

# --- MODERN COLOR PALETTE ---
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"
COLOR_HOVER = "#ebf5fb"

def logout(root):
    if os.path.exists("SCMP/faculty_session.txt"):
        os.remove("SCMP/faculty_session.txt")
    root.destroy()
    import login
    login.show_login()

def exit_app(root):
    root.destroy()
    sys.exit()

def show_dashboard():
    root = tk.Tk()
    root.title("SCMP - Faculty Dashboard")
    
    if os.name == 'nt': root.state('zoomed')
    else:
        try: root.attributes('-zoomed', True)
        except: root.geometry("1024x768")
            
    root.configure(bg=COLOR_BG)
    
    # Read faculty name from session
    faculty_name = "Faculty Member"
    if os.path.exists("SCMP/faculty_session.txt"):
        with open("SCMP/faculty_session.txt", "r") as f:
            faculty_name = f.read()

    def on_card_enter(e): e.widget.config(bg=COLOR_HOVER, cursor="hand2")
    def on_card_leave(e): e.widget.config(bg=COLOR_CARD)

    # --- TOP NAV ---
    nav_bar = tk.Frame(root, bg=COLOR_HEADER, height=80)
    nav_bar.pack(side=tk.TOP, fill=tk.X)
    tk.Label(nav_bar, text="Faculty Control Panel", font=("Arial", 22, "bold"), bg=COLOR_HEADER, fg="white").pack(side=tk.LEFT, padx=40, pady=20)
    
    # --- HERO ---
    hero = tk.Frame(root, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    hero.pack(fill=tk.X, padx=50, pady=20)
    
    welcome_frame = tk.Frame(hero, bg=COLOR_CARD)
    welcome_frame.pack(side=tk.LEFT, padx=40, pady=20)
    tk.Label(welcome_frame, text="Welcome back,", font=("Arial", 14), bg=COLOR_CARD, fg=COLOR_TEXT).pack(anchor="w")
    tk.Label(welcome_frame, text=f"Prof. {faculty_name}", font=("Arial", 28, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(anchor="w")
    
    profile_card = tk.Frame(hero, bg=COLOR_CARD)
    profile_card.pack(side=tk.RIGHT, padx=40)
    tk.Label(profile_card, text="Role: Faculty | Branch: CSE", font=("Arial", 12, "bold"), bg=COLOR_CARD, fg=COLOR_ACCENT).pack(side=tk.LEFT, padx=20)
    
    # --- GRID CONTAINER ---
    grid = tk.Frame(root, bg=COLOR_BG)
    grid.pack(pady=10)
    
    cards_config = [
        ("📁", "Student Records", "View Database", student_records.show_records),
        ("🔍", "Search Students", "Query Engine", search_sort_students.show_search),
        ("✍️", "Update Marks", "Entry Portal", faculty_marks.show_marks_entry),
        ("📅", "Update Attendance", "Presence Manager", faculty_attendance.show_attendance_entry),
        ("📢", "Manage Notices", "Post Announcements", update_notices.show_update_notices),
        ("💬", "View Complaints", "Student Feedback", view_complaints.show_view_complaints)
    ]
    
    for i, (icon, title, desc, cmd) in enumerate(cards_config):
        card = tk.Button(grid, bg=COLOR_CARD, width=35, height=8, relief="flat", bd=0, highlightthickness=1, highlightbackground="#ddd", command=cmd)
        card.grid(row=i//3, column=i%3, padx=20, pady=15)
        card.config(text=f"\n{icon}\n{title}\n{desc}", font=("Arial", 11), fg=COLOR_TEXT)
        card.bind("<Enter>", on_card_enter)
        card.bind("<Leave>", on_card_leave)

    # --- LOGOUT & EXIT BUTTONS ---
    footer_btns = tk.Frame(root, bg=COLOR_BG)
    footer_btns.pack(side=tk.BOTTOM, pady=40)
    
    tk.Button(footer_btns, text="LOGOUT", font=("Arial", 12, "bold"), bg="#f39c12", fg="white", width=20, height=2, relief="flat", cursor="hand2", command=lambda: logout(root)).pack(side=tk.LEFT, padx=20)
    tk.Button(footer_btns, text="EXIT", font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", width=20, height=2, relief="flat", cursor="hand2", command=lambda: exit_app(root)).pack(side=tk.LEFT, padx=20)

    # --- FOOTER ---
    footer = tk.Frame(root, bg=COLOR_HEADER, height=40)
    footer.pack(side=tk.BOTTOM, fill=tk.X)
    tk.Label(footer, text=f" System Date: {datetime.now().strftime('%d %B %Y')}", font=("Arial", 9), bg=COLOR_HEADER, fg="white").pack(side=tk.LEFT, pady=10)
    
    root.mainloop()
