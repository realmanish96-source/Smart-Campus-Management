import tkinter as tk
import os

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"

def show_analytics():
    window = tk.Toplevel()
    window.title("Performance Analytics")
    
    if os.name == 'nt': window.state('zoomed')
    else:
        try: window.attributes('-zoomed', True)
        except: window.geometry("1024x768")
            
    window.configure(bg=COLOR_BG)
    
    header = tk.Frame(window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Student Performance Analytics", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    card = tk.Frame(window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=150, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="Academic Insights", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=30)
    
    # Stats Frame
    stats_frame = tk.Frame(card, bg=COLOR_CARD)
    stats_frame.pack(pady=10)
    
    stats = [("Overall CGPA", "8.5"), ("Attendance", "90%"), ("Rank", "#5"), ("Credits", "22")]
    
    for s_title, s_val in stats:
        f = tk.Frame(stats_frame, bg=COLOR_CARD, padx=20)
        f.pack(side=tk.LEFT)
        tk.Label(f, text=s_val, font=("Arial", 24, "bold"), bg=COLOR_CARD, fg=COLOR_ACCENT).pack()
        tk.Label(f, text=s_title, font=("Arial", 12), bg=COLOR_CARD, fg="gray").pack()
    
    # Simple Bar Chart Simulation using Canvas
    tk.Label(card, text="Semester-wise Trend:", font=("Arial", 16, "bold"), bg=COLOR_CARD, fg=COLOR_TEXT).pack(pady=(40, 10))
    canvas = tk.Canvas(card, width=600, height=250, bg="white", highlightthickness=1, highlightbackground="#eee")
    canvas.pack(pady=10)
    
    # Draw simple bars
    data = [40, 70, 90, 85, 95]
    colors = ["#e74c3c", "#f1c40f", "#2ecc71", "#3498db", "#9b59b6"]
    for i, val in enumerate(data):
        canvas.create_rectangle(100 + i*100, 200, 150 + i*100, 200 - val, fill=colors[i], outline="")
        canvas.create_text(125 + i*100, 220, text=f"Sem {i+1}", font=("Arial", 10))

    tk.Button(window, text="CLOSE", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", 
              padx=30, pady=10, relief="flat", command=window.destroy).pack(side=tk.BOTTOM, pady=50)
