import tkinter as tk
from tkinter import messagebox
import socket

# Function to get IP address
def get_ip():
    host = entry.get()  # Get the domain name from the input field
    try:
        ip_address = socket.gethostbyname(host)
        result_label.config(text=f"IP Address: {ip_address}")
        copy_button.config(state="normal")  # Enable the copy button
        global current_ip
        current_ip = ip_address  # Store the IP address for copying
    except socket.gaierror:
        messagebox.showerror("Error", "Invalid domain name or network issue.")

# Function to copy the IP address to clipboard
def copy_to_clipboard():
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(current_ip)  # Append only the IP address
    root.update()  # Update the clipboard contents
    messagebox.showinfo("Copied", f"IP Address '{current_ip}' copied to clipboard!")

# Create the main Tkinter window
root = tk.Tk()
root.title("Domain to IP Resolver")
root.geometry("400x200")

# Create a label for instructions
instruction_label = tk.Label(root, text="Enter the domain name:", font=("Arial", 12))
instruction_label.pack(pady=10)

# Create an entry field for the domain name
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

# Create a button to trigger the IP lookup
resolve_button = tk.Button(root, text="Resolve IP", command=get_ip, font=("Arial", 12))
resolve_button.pack(pady=10)

# Create a label to display the results
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# Create a button to copy the IP address to the clipboard
copy_button = tk.Button(root, text="Copy IP", command=copy_to_clipboard, font=("Arial", 12), state="disabled")
copy_button.pack(pady=5)

# Run the Tkinter main event loop
root.mainloop()
