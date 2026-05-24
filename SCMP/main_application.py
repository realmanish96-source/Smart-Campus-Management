import login
import dashboard
import faculty_dashboard
import os

# Main Application Entry Point with Dual-Role Session Logic
if __name__ == "__main__":
    student_session = "SCMP/session.txt"
    faculty_session = "SCMP/faculty_session.txt"
    
    if os.path.exists(student_session):
        # Remembered student
        dashboard.show_dashboard()
    elif os.path.exists(faculty_session):
        # Remembered faculty
        faculty_dashboard.show_dashboard()
    else:
        # No session, start at Login
        login.show_login()
