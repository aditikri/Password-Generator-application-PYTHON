
import tkinter as tk
from tkinter import messagebox
import secrets
import string


# Password Generator Functions

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 8 or length > 64:
            messagebox.showwarning(
                "Invalid Length",
                "Enter a password length between 8 and 64."
            )
            return

        characters = ""

        if uppercase_var.get():
            characters += string.ascii_uppercase

        if lowercase_var.get():
            characters += string.ascii_lowercase

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += "!@#$%^&*()-_=+?"

        if not characters:
            messagebox.showwarning(
                "Selection Required",
                "Select at least one character type."
            )
            return

        password = "".join(
            secrets.choice(characters) for _ in range(length)
        )

        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")

        check_strength(password)

        history_list.insert(0, password)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid password length."
        )


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()-_=+?" for c in password):
        score += 1

    if score <= 3:
        strength_label.config(
            text="Password Strength: Weak",
            fg="red"
        )
    elif score <= 4:
        strength_label.config(
            text="Password Strength: Medium",
            fg="orange"
        )
    else:
        strength_label.config(
            text="Password Strength: Strong",
            fg="green"
        )


def copy_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning(
            "No Password",
            "Generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo(
        "Success",
        "Password copied to clipboard!"
    )


def clear_all():
    length_entry.delete(0, tk.END)
    length_entry.insert(0, "12")

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.config(state="readonly")

    uppercase_var.set(True)
    lowercase_var.set(True)
    numbers_var.set(True)
    symbols_var.set(True)

    strength_label.config(
        text="Password Strength: Not checked",
        fg="black"
    )


# Main Window

root = tk.Tk()
root.title("Password Generator")
root.geometry("520x650")
root.configure(bg="#eef2f7")
root.resizable(False, False)


# Heading

title_label = tk.Label(
    root,
    text="PASSWORD GENERATOR",
    font=("Arial", 20, "bold"),
    bg="#eef2f7",
    fg="#173b67"
)
title_label.pack(pady=20)


subtitle = tk.Label(
    root,
    text="Create a strong and secure password",
    font=("Arial", 11),
    bg="#eef2f7"
)
subtitle.pack(pady=5)


# Password Length

length_label = tk.Label(
    root,
    text="Password Length (8–64):",
    font=("Arial", 11, "bold"),
    bg="#eef2f7"
)
length_label.pack(pady=(15, 5))

length_entry = tk.Entry(
    root,
    font=("Arial", 12),
    justify="center",
    width=15
)
length_entry.insert(0, "12")
length_entry.pack(pady=5)


# Character Options

options_label = tk.Label(
    root,
    text="Select Character Types",
    font=("Arial", 11, "bold"),
    bg="#eef2f7"
)
options_label.pack(pady=(15, 5))

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)


tk.Checkbutton(
    root,
    text="Uppercase Letters (A-Z)",
    variable=uppercase_var,
    bg="#eef2f7"
).pack(anchor="w", padx=150)

tk.Checkbutton(
    root,
    text="Lowercase Letters (a-z)",
    variable=lowercase_var,
    bg="#eef2f7"
).pack(anchor="w", padx=150)

tk.Checkbutton(
    root,
    text="Numbers (0-9)",
    variable=numbers_var,
    bg="#eef2f7"
).pack(anchor="w", padx=150)

tk.Checkbutton(
    root,
    text="Special Symbols (!@#$)",
    variable=symbols_var,
    bg="#eef2f7"
).pack(anchor="w", padx=150)


# Generate Button

generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 11, "bold"),
    bg="#173b67",
    fg="white",
    width=22
)
generate_button.pack(pady=18)


# Password Output

password_label = tk.Label(
    root,
    text="Generated Password:",
    font=("Arial", 11, "bold"),
    bg="#eef2f7"
)
password_label.pack(pady=5)

password_entry = tk.Entry(
    root,
    font=("Consolas", 12),
    justify="center",
    width=35,
    state="readonly"
)
password_entry.pack(pady=5)


# Strength Indicator

strength_label = tk.Label(
    root,
    text="Password Strength: Not checked",
    font=("Arial", 11, "bold"),
    bg="#eef2f7",
    fg="black"
)
strength_label.pack(pady=10)


# Copy and Clear Buttons

button_frame = tk.Frame(root, bg="#eef2f7")
button_frame.pack(pady=5)

tk.Button(
    button_frame,
    text="Copy Password",
    command=copy_password,
    bg="#218838",
    fg="white",
    width=15
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Clear",
    command=clear_all,
    bg="#6c757d",
    fg="white",
    width=12
).grid(row=0, column=1, padx=5)


# Password History

history_label = tk.Label(
    root,
    text="Generated Password History (Current Session)",
    font=("Arial", 10, "bold"),
    bg="#eef2f7"
)
history_label.pack(pady=(15, 5))

history_list = tk.Listbox(
    root,
    width=48,
    height=4
)
history_list.pack(pady=5)


# Run Application

root.mainloop()
