import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x500")
root.title("Login Screen")
root.configure(bg="#c5dff8")  

login_frame = tk.Frame(root, bg="white", bd=0, relief="flat")
login_frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=350)

title_label = tk.Label(
    login_frame,
    text="Login",
    font=("Arial", 20, "bold"),
    bg="white",
    fg="#3b3b3b"
)
title_label.pack(pady=20) #qwewaznd

username_label = tk.Label(
    login_frame,
    text="Username",
    font=("Arial", 12),
    bg="white",
    fg="#a0a0a0"
)
username_label.pack(pady=(10, 5), anchor="w", padx=40)
username_entry = tk.Entry(login_frame, font=("Arial", 12), bg="#f0f0f0", bd=0, relief="flat")
username_entry.pack(pady=(0, 10), padx=40, fill="x")

password_label = tk.Label(
    login_frame,
    text="Password",
    font=("Arial", 12),
    bg="white",
    fg="#a0a0a0"
)
password_label.pack(pady=(10, 5), anchor="w", padx=40)
password_entry = tk.Entry(login_frame, font=("Arial", 12), bg="#f0f0f0", bd=0, relief="flat", show="*")
password_entry.pack(pady=(0, 20), padx=40, fill="x")

login_button = tk.Button(
    login_frame,
    text="Login",
    font=("Arial", 12, "bold"),
    bg="#3b3b3b",
    fg="white",
    relief="flat",
    cursor="hand2"
)
login_button.pack(pady=(10, 5), padx=40, fill="x")


signup_button = tk.Button(
    login_frame,
    text="Sign Up",
    font=("Arial", 12, "bold"),
    bg="#c5dff8",
    fg="#3b3b3b",
    relief="flat",
    cursor="hand2"
)
signup_button.pack(pady=5, padx=40, fill="x")

root.mainloop()