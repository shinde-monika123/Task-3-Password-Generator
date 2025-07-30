import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Too Short", "Password should be at least 4 characters long.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text="Generated Password:\n" + password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")

# Instruction
tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack(pady=10)

# Entry box for length
length_entry = tk.Entry(root, width=10)
length_entry.pack()

# Button to generate password
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=15)

# Label to display result
result_label = tk.Label(root, text="", font=("Courier", 12), wraplength=300)
result_label.pack()

# Run GUI
root.mainloop()