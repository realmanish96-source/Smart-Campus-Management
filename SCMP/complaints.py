import tkinter as tk
from tkinter import messagebox
import os

def submit_complaint(text_area):
    complaint_text = text_area.get("1.0", tk.END).strip()
    
    if complaint_text:
        # Show success popup
        messagebox.showinfo("Success", "Complaint Submitted Successfully! Our team will review it.")
        # Clear the text area
        text_area.delete("1.0", tk.END)
    else:
        # Show warning if text area is empty
        messagebox.showwarning("Empty", "Please describe your complaint before submitting.")

def show_complaints():
    # Create a new top-level window
    complaints_window = tk.Toplevel()
    complaints_window.title("Complaint Submission")
    
    # CROSS-PLATFORM FULL SCREEN FIX
    if os.name == 'nt':
        complaints_window.state('zoomed')
    else:
        try:
            complaints_window.attributes('-zoomed', True)
        except tk.TclError:
            width = complaints_window.winfo_screenwidth()
            height = complaints_window.winfo_screenheight()
            complaints_window.geometry(f"{width}x{height}+0+0")
            
    complaints_window.configure(bg="white")
    
    tk.Label(complaints_window, text="Lodge a Complaint", font=("Arial", 28, "bold"), bg="white", fg="blue").pack(pady=50)
    
    # Centered container
    content_frame = tk.Frame(complaints_window, bg="white")
    content_frame.pack(pady=20)
    
    tk.Label(content_frame, text="Please provide detailed information about your issue:", font=("Arial", 14), bg="white").pack(anchor="w", pady=10)
    
    # Larger Text area for full screen
    complaint_box = tk.Text(content_frame, font=("Arial", 14), width=80, height=15, bd=2, relief="solid")
    complaint_box.pack(pady=10)
    
    # Buttons Frame
    btn_frame = tk.Frame(content_frame, bg="white")
    btn_frame.pack(pady=20)
    
    # Submit Button
    submit_btn = tk.Button(btn_frame, text="Submit Complaint", font=("Arial", 14, "bold"), 
                           bg="blue", fg="white", width=25, height=2, command=lambda: submit_complaint(complaint_box))
    submit_btn.pack(side=tk.LEFT, padx=20)
    
    # Back Button
    tk.Button(btn_frame, text="Back to Dashboard", font=("Arial", 14, "bold"), bg="gray", fg="white", 
              width=25, height=2, command=complaints_window.destroy).pack(side=tk.LEFT, padx=20)
