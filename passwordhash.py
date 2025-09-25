import hashlib
import re
import tkinter as tk
from tkinter import ttk

# Predefined list of common passwords (extendable to Top 100)
common_passwords = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "111111", "123123", "password1", "1234", "iloveyou",
    "12345", "000000", "qwerty123"
]

def hash_password(password: str) -> str:
    """Hash the password using SHA-256"""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def check_strength(password: str) -> tuple:
    """Check password strength and return (category, reason)"""
    if password.lower() in common_passwords:
        return "WEAK", "Password is too common"

    if len(password) < 6:
        return "WEAK", "Password is too short (less than 6 characters)"

    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_digit = re.search(r"\d", password)
    has_symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum(bool(x) for x in [has_upper, has_lower, has_digit, has_symbol])

    if len(password) >= 8 and score >= 3:
        return "STRONG", "Good length and includes uppercase, lowercase, numbers, and symbols"
    elif len(password) >= 6 and score >= 2:
        return "MEDIUM", "Decent password but could be stronger"
    else:
        return "WEAK", "Lacks complexity (needs mix of uppercase, lowercase, numbers, and symbols)"

def evaluate_password(event=None):
    """Evaluate password when button is clicked or Enter is pressed"""
    password = entry.get().strip()

    if not password:
        result_label.config(text="⚠️ Please enter a password", fg="black")
        hash_label.config(text="")
        reason_label.config(text="")
        return

    # Hash the password
    hashed = hash_password(password)
    hash_label.config(text=f"SHA-256: {hashed}", wraplength=480)

    # Check strength
    strength, reason = check_strength(password)
    colors = {"WEAK": "red", "MEDIUM": "orange", "STRONG": "green"}

    result_label.config(text=f"Password Strength: {strength}", fg=colors[strength])
    reason_label.config(text=f"Reason: {reason}", fg=colors[strength])

def toggle_password():
    """Show or hide password based on checkbox"""
    if show_var.get():
        entry.config(show="")  # Show password
    else:
        entry.config(show="*")  # Hide password

# --- GUI Setup ---
root = tk.Tk()
root.title("Password Hashing & Strength Checker")
root.geometry("550x340")
root.resizable(False, False)

# Title
title = tk.Label(root, text="🔐 Password Hashing & Strength Checker", font=("Arial", 14, "bold"))
title.pack(pady=10)

# Frame for entry + button
frame = tk.Frame(root)
frame.pack(pady=5)

entry = ttk.Entry(frame, width=30, show="*")  # Masked input
entry.grid(row=0, column=0, padx=5)

btn = ttk.Button(frame, text="Check", command=evaluate_password)
btn.grid(row=0, column=1, padx=5)

# Show/Hide Password checkbox
show_var = tk.BooleanVar(value=False)
show_check = tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password)
show_check.pack()

# Bind Enter key to trigger evaluation
entry.bind("<Return>", evaluate_password)

# Output labels
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

reason_label = tk.Label(root, text="", font=("Arial", 10))
reason_label.pack(pady=5)

hash_label = tk.Label(root, text="", font=("Arial", 9), wraplength=500, justify="center")
hash_label.pack(pady=10)

# Run GUI
root.mainloop()