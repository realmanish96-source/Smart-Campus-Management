import tkinter as tk
import notices
import attendance
import complaints
import marks
import sys
import os
from datetime import datetime

# --- MODERN COLOR PALETTE ---
COLOR_BG = "#f4f7f6"        # Soft Light Grey
COLOR_HEADER = "#2c3e50"    # Midnight Blue
COLOR_CARD = "#ffffff"      # Pure White
COLOR_ACCENT = "#3498db"    # Modern Blue
COLOR_TEXT = "#34495e"      # Dark Grey-Blue
COLOR_HOVER = "#ebf5fb"    # Very Light Blue for hover

def show_dashboard():
    root = tk.Tk()
    root.title("SCMP - Student Dashboard")
    
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
            
    root.configure(bg=COLOR_BG)
    
    # --- UI EVENT FUNCTIONS ---
    def on_card_enter(e):
        e.widget.config(bg=COLOR_HOVER, cursor="hand2")
        
    def on_card_leave(e):
        e.widget.config(bg=COLOR_CARD)

    def get_greeting():
        hour = datetime.now().hour
        if hour < 12: return "Good Morning"
        elif hour < 17: return "Good Afternoon"
        else: return "Good Evening"

    # --- TOP NAVIGATION BAR ---
    nav_bar = tk.Frame(root, bg=COLOR_HEADER, height=80)
    nav_bar.pack(side=tk.TOP, fill=tk.X)
    
    tk.Label(nav_bar, text="Dashboard", font=("Arial", 22, "bold"), bg=COLOR_HEADER, fg="white").pack(side=tk.LEFT, padx=40, pady=20)
    
    # Logout on the right of Nav Bar
    tk.Button(nav_bar, text="LOGOUT", font=("Arial", 10, "bold"), bg="#e74c3c", fg="white", 
              padx=20, pady=5, relief="flat", command=root.quit).pack(side=tk.RIGHT, padx=40)

    # --- MAIN HEADER / HERO SECTION ---
    hero_frame = tk.Frame(root, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    hero_frame.pack(fill=tk.X, padx=50, pady=30)
    
    # Left Side: Welcome Text
    welcome_frame = tk.Frame(hero_frame, bg=COLOR_CARD)
    welcome_frame.pack(side=tk.LEFT, padx=40, pady=30)
    
    tk.Label(welcome_frame, text=f"{get_greeting()},", font=("Arial", 16), bg=COLOR_CARD, fg=COLOR_TEXT).pack(anchor="w")
    tk.Label(welcome_frame, text="Manish Jha", font=("Arial", 32, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(anchor="w")
    tk.Label(welcome_frame, text="Current Session: 2025-26 | Semester: II", font=("Arial", 11), bg=COLOR_CARD, fg="gray").pack(anchor="w", pady=(5,0))

    # Right Side: Profile Card
    profile_card = tk.Frame(hero_frame, bg=COLOR_CARD)
    profile_card.pack(side=tk.RIGHT, padx=40, pady=20)
    
    # Info
    info_frame = tk.Frame(profile_card, bg=COLOR_CARD)
    info_frame.pack(side=tk.LEFT, padx=20)
    tk.Label(info_frame, text="ROLL NO: 29", font=("Arial", 10, "bold"), bg=COLOR_CARD, fg=COLOR_ACCENT).pack(anchor="e")
    tk.Label(info_frame, text="B.Tech Computer Science", font=("Arial", 10), bg=COLOR_CARD, fg=COLOR_TEXT).pack(anchor="e")
    
    # WhatsApp DP Silhouette
    logo_canvas = tk.Canvas(profile_card, width=70, height=70, bg=COLOR_CARD, highlightthickness=0)
    logo_canvas.pack(side=tk.RIGHT)
    logo_canvas.create_oval(5, 5, 65, 65, fill="#E1E1E1", outline="#E1E1E1")
    logo_canvas.create_oval(25, 15, 45, 35, fill="#A9A9A9", outline="#A9A9A9") 
    logo_canvas.create_arc(10, 40, 60, 90, start=0, extent=180, fill="#A9A9A9", outline="#A9A9A9")

    # --- CARDS CONTAINER (GRID) ---
    grid_container = tk.Frame(root, bg=COLOR_BG)
    grid_container.pack(pady=20)
    
    # Define Card Details
    cards = [
        ("📋", "Notices", "Latest Campus Updates", notices.show_notices),
        ("📊", "Attendance", "View Subject-wise Presence", attendance.show_attendance),
        ("📝", "Academic Marks", "Check Your Performance", marks.show_marks),
        ("📩", "Complaint Box", "Submit Feedback or Issues", complaints.show_complaints)
    ]
    
    for i, (icon, title, desc, cmd) in enumerate(cards):
        # Card Frame
        card = tk.Button(grid_container, bg=COLOR_CARD, width=35, height=10, relief="flat",
                         bd=0, highlightthickness=1, highlightbackground="#ddd", 
                         command=cmd)
        card.grid(row=i//2, column=i%2, padx=25, pady=25)
        
        # We use a trick to put text inside the button area using labels or just formatting
        # For simplicity in beginner code, we can use the button's built-in text with multiple lines
        combined_text = f"\n{icon}\n\n{title}\n\n{desc}"
        card.config(text=combined_text, font=("Arial", 11), fg=COLOR_TEXT, justify="center")
        
        card.bind("<Enter>", on_card_enter)
        card.bind("<Leave>", on_card_leave)

    # --- FOOTER STATUS BAR ---
    status_bar = tk.Frame(root, bg=COLOR_HEADER, height=40)
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    current_time = datetime.now().strftime("%A, %B %d, %Y")
    tk.Label(status_bar, text=f"  System Date: {current_time}", font=("Arial", 9), bg=COLOR_HEADER, fg="white").pack(side=tk.LEFT, pady=10)
    tk.Label(status_bar, text="Campus Network: Connected  ", font=("Arial", 9), bg=COLOR_HEADER, fg="#2ecc71").pack(side=tk.RIGHT, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    show_dashboard()
