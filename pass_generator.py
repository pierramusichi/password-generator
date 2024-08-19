import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    """Generate a random password of specified length."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

def generate_password_gui():
    """Generate password based on user input from GUI."""
    def generate():
        try:
            password_length = int(length_entry.get())
            if password_length <= 0:
                raise ValueError("Password length must be a positive integer.")
            
            generated_password = generate_password(password_length)
            result_text.config(state="normal")
            result_text.delete("1.0", "end")
            result_text.insert("1.0", generated_password)
            result_text.config(state="disabled")
        
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    # Create GUI window
    root = tk.Tk()
    root.title("Password Generator")
    root.configure(bg="dark blue")

    # Create and pack GUI widgets
    length_label = tk.Label(root, text="Enter password length:", fg="white", bg="navy", font=("Arial", 12))
    length_label.pack(pady=10)

    length_entry = tk.Entry(root, width=30, font=("Tahoma", 12))
    length_entry.pack()

    generate_button = tk.Button(root, text="Generate Password", command=generate, bg="white", fg="navy", font=("Arial", 12, "bold"), padx=10, pady=5, bd=0)
    generate_button.pack(pady=10)

    result_text = tk.Text(root, height=2, width=30, font=("Arial", 12), wrap="word", bg="white", fg="navy", bd=2, relief=tk.SOLID)
    result_text.pack(pady=10)
    result_text.config(state="disabled")

    # Run the GUI
    root.mainloop()

if __name__ == "__main__":
    generate_password_gui()
