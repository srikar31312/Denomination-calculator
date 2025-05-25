import tkinter as tk
from tkinter import messagebox

# Function to check password strength
def check_strength():
    password = entry_password.get()
    length = len(password)

    if length == 0:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    if length <= 5:
        strength = "Weak"
        color = "red"
    elif 6 <= length <= 8:
        strength = "Medium"
        color = "yellow"
    elif 9 <= length <= 12:
        strength = "Strong"
        color = "light green"
    else:
        strength = "Very Strong"
        color = "dark green"

    label_result.config(text=f"Password Strength: {strength}", fg=color)

# Create main window
root = tk.Tk()
root.title("Password Strength Checker App")
root.geometry("400x400")
root.resizable(False, False)

# Heading label
label_heading = tk.Label(root, text="Enter your password:", font=("Arial", 14))
label_heading.pack(pady=20)

# Entry widget for password
entry_password = tk.Entry(root, show="*", font=("Arial", 14), width=25)
entry_password.pack(pady=10)

# Button to check strength
btn_check = tk.Button(root, text="Check Strength", command=check_strength, font=("Arial", 12))
btn_check.pack(pady=20)

# Label to display result
label_result = tk.Label(root, text="", font=("Arial", 16))
label_result.pack(pady=10)

# Run the app
root.mainloop()