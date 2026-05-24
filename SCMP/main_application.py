import login
import dashboard
import os

# Main Application Entry Point for Student Information System
if __name__ == "__main__":
    session_file = "SCMP/session.txt"
    
    if os.path.exists(session_file):
        # Remembered student
        dashboard.show_dashboard()
    else:
        # No session, start at Login
        login.show_login()
