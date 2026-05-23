import tkinter as tk
from tkinter import messagebox
import os

# --- MODERN COLOR PALETTE ---
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"

def submit_complaint(text_area):
    complaint_text = text_area.get("1.0", tk.END).strip()
    if complaint_text:
        messagebox.showinfo("Success", "Complaint Submitted Successfully!")
        text_area.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Empty", "Please describe your complaint before submitting.")

def show_complaints():
    complaints_window = tk.Toplevel()
    complaints_window.title("SCMP - Complaint Box")
    
    if os.name == 'nt':
        complaints_window.state('zoomed')
    else:
        try:
            complaints_window.attributes('-zoomed', True)
        except tk.TclError:
            width = complaints_window.winfo_screenwidth()
            height = complaints_window.winfo_screenheight()
            complaints_window.geometry(f"{width}x{height}+0+0")
            
    complaints_window.configure(bg=COLOR_BG)
    
    # --- HEADER ---
    header = tk.Frame(complaints_window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Support & Complaint Box", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    # --- CONTENT CARD ---
    card = tk.Frame(complaints_window, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    card.pack(pady=50, padx=100, fill=tk.BOTH, expand=True)
    
    tk.Label(card, text="How can we help you?", font=("Arial", 22, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=(40, 10))
    tk.Label(card, text="Please provide detailed information about your concern.", font=("Arial", 12), bg=COLOR_CARD, fg="gray").pack(pady=(0, 20))
    
    # Text Area - INCREASED SIZE
    complaint_box = tk.Text(card, font=("Arial", 16), width=70, height=10, bd=1, relief="solid", bg="#fcfcfc")
    complaint_box.pack(pady=20, padx=50)
    
    # Buttons Frame
    btn_frame = tk.Frame(card, bg=COLOR_CARD)
    btn_frame.pack(pady=20)
    
    # Submit Button - INCREASED SIZE
    submit_btn = tk.Button(btn_frame, text="SUBMIT COMPLAINT", font=("Arial", 14, "bold"), 
                           bg=COLOR_ACCENT, fg="white", width=25, height=2, relief="flat", 
                           command=lambda: submit_complaint(complaint_box))
    submit_btn.pack(side=tk.LEFT, padx=20)
    
    # --- BACK BUTTON ---
    tk.Button(complaints_window, text="CLOSE & GO BACK", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", 
              padx=30, pady=10, relief="flat", command=complaints_window.destroy).pack(side=tk.BOTTOM, pady=50)
