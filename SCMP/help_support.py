import tkinter as tk
from tkinter import messagebox
import os

# THEME CONSTANTS
COLOR_BG = "#f4f7f6"
COLOR_HEADER = "#2c3e50"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"

def submit_ticket(text_area):
    issue = text_area.get("1.0", tk.END).strip()
    if issue:
        messagebox.showinfo("Ticket Submitted", "Your support ticket has been raised. A lab assistant will contact you soon.")
        text_area.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Empty Field", "Please describe your issue before submitting.")

def show_help():
    window = tk.Toplevel()
    window.title("SCMP - Help & Support")
    
    if os.name == 'nt': window.state('zoomed')
    else:
        try: window.attributes('-zoomed', True)
        except: window.geometry("1024x768")
            
    window.configure(bg=COLOR_BG)
    
    # Header
    header = tk.Frame(window, bg=COLOR_HEADER, height=100)
    header.pack(side=tk.TOP, fill=tk.X)
    tk.Label(header, text="Student Support Center", font=("Arial", 28, "bold"), bg=COLOR_HEADER, fg="white").pack(pady=25)
    
    # Main Container for two sections
    container = tk.Frame(window, bg=COLOR_BG)
    container.pack(pady=30, padx=50, fill=tk.BOTH, expand=True)
    
    # --- LEFT SIDE: FAQ ---
    faq_card = tk.Frame(container, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    faq_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20)
    
    tk.Label(faq_card, text="Frequently Asked Questions", font=("Arial", 20, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=30)
    
    faqs = [
        ("Q: How to update my profile?", "A: Contact the Administrative Office with your ID card."),
        ("Q: Where to pay pending fees?", "A: Visit the Accounts Department or use the online portal."),
        ("Q: Marks not showing?", "A: Faculty usually updates marks within 48 hours of the exam."),
        ("Q: Technical glitch?", "A: Report it using the form on the right or contact the Lab Assistant.")
    ]
    
    for q, a in faqs:
        f = tk.Frame(faq_card, bg=COLOR_CARD)
        f.pack(fill=tk.X, padx=30, pady=10)
        tk.Label(f, text=q, font=("Arial", 12, "bold"), bg=COLOR_CARD, fg=COLOR_ACCENT, anchor="w").pack(fill=tk.X)
        tk.Label(f, text=a, font=("Arial", 11), bg=COLOR_CARD, fg=COLOR_TEXT, anchor="w", wraplength=400, justify=tk.LEFT).pack(fill=tk.X)

    # --- RIGHT SIDE: CONTACT FORM ---
    contact_card = tk.Frame(container, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#ddd")
    contact_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20)
    
    tk.Label(contact_card, text="Raise a Support Ticket", font=("Arial", 20, "bold"), bg=COLOR_CARD, fg=COLOR_HEADER).pack(pady=30)
    
    tk.Label(contact_card, text="Describe your issue or feedback:", font=("Arial", 12), bg=COLOR_CARD, fg="gray").pack(anchor="w", padx=40)
    
    issue_box = tk.Text(contact_card, font=("Arial", 13), height=10, width=40, bd=1, relief="solid", bg="#fcfcfc")
    issue_box.pack(pady=20, padx=40)
    
    tk.Button(contact_card, text="SUBMIT TICKET", font=("Arial", 13, "bold"), bg=COLOR_ACCENT, fg="white", 
              width=25, height=2, relief="flat", command=lambda: submit_ticket(issue_box)).pack(pady=10)
    
    tk.Label(contact_card, text="Official Email: support@smartcampus.com\nEmergency: +91 98765 43210", 
             font=("Arial", 10), bg=COLOR_CARD, fg="gray").pack(pady=20)

    # Back Button
    tk.Button(window, text="CLOSE & GO BACK", font=("Arial", 12, "bold"), bg=COLOR_HEADER, fg="white", 
              padx=30, pady=10, relief="flat", command=window.destroy).pack(side=tk.BOTTOM, pady=40)
