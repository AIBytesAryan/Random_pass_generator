import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive number for length.")
        return
    
    characters = ""
    if letters_var.get():
        characters += string.ascii_letters
    if digits_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    exclude = exclude_entry.get()
    for ch in exclude:
        characters = characters.replace(ch, "")

    include = include_entry.get()

    if not characters:
        messagebox.showwarning("Warning", "No characters available to generate password!")
        return

    # Start password with included characters
    password = list(include)

    # Fill the rest randomly
    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    password = ''.join(password[:length])

    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_to_clipboard():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# Main Window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("420x460")
root.resizable(False, False)

# Heading
tk.Label(root, text="💚 Random Password Generator", font=("Arial", 16, "bold"), fg="green").pack(pady=10)

# Password length input
tk.Label(root, text="Password Length:", font=("Arial", 12)).pack()
length_entry = tk.Entry(root, width=10, font=("Arial", 12))
length_entry.pack(pady=5)

# Options for character types
letters_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var, font=("Arial", 11)).pack()
tk.Checkbutton(root, text="Include Digits", variable=digits_var, font=("Arial", 11)).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, font=("Arial", 11)).pack()

# Include specific characters
tk.Label(root, text="Include These Characters (optional):", font=("Arial", 12)).pack(pady=5)
include_entry = tk.Entry(root, width=20, font=("Arial", 12))
include_entry.pack(pady=5)

# Exclude specific characters
tk.Label(root, text="Exclude These Characters (optional):", font=("Arial", 12)).pack(pady=5)
exclude_entry = tk.Entry(root, width=20, font=("Arial", 12))
exclude_entry.pack(pady=5)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white").pack(pady=10)

# Display generated password
tk.Label(root, text="Generated Password:", font=("Arial", 12)).pack()
result_entry = tk.Entry(root, width=30, font=("Arial", 12))
result_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12, "bold"), bg="#2196F3", fg="white").pack(pady=10)

root.mainloop()
