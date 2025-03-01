import socket
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to perform the port scan
def start_scan():
    # Clear the previous results
    result_text.delete(1.0, tk.END)
    
    # Get the host and port range from the user input
    target = host_entry.get()
    try:
        t_IP = socket.gethostbyname(target)
    except socket.gaierror:
        messagebox.showerror("Error", "Unable to resolve host")
        return
    
    result_text.insert(tk.END, f"Starting scan on host: {t_IP}\n")
    result_text.insert(tk.END, "Scanning...\n")
    
    # Start timer to measure the scan time
    startTime = time.time()

    # Scan ports in the range of 50 to 500
    for i in range(50, 500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect_ex((t_IP, i))
        if conn == 0:
            result_text.insert(tk.END, f"Port {i}: Open\n")
        s.close()
        root.update_idletasks()  # Updates the UI to prevent freezing
    
    # Display time taken for the scan
    elapsed_time = time.time() - startTime
    result_text.insert(tk.END, f"\nScan completed in {elapsed_time:.2f} seconds")

    # Disable the button after scan is done
    start_button.config(state=tk.NORMAL)

# Function to start scan and disable the button during scanning
def on_scan_button_click():
    start_button.config(state=tk.DISABLED)  # Disable the button during the scan
    start_scan()

# Set up the main window
root = tk.Tk()
root.title("Port Scanner")
root.geometry("600x450")
root.config(bg="#2E3B4E")  # Dark background for a sleek look

# Title label with styling
title_label = tk.Label(root, text="Port Scanner", font=("Arial", 24, "bold"), bg="#2E3B4E", fg="white")
title_label.pack(pady=20)

# Input field for host
host_label = tk.Label(root, text="Enter Host/IP to Scan:", font=("Arial", 14), bg="#2E3B4E", fg="white")
host_label.pack(pady=10)

host_entry = tk.Entry(root, font=("Arial", 14), width=30)
host_entry.pack(pady=10)

# Button to start the scan
start_button = tk.Button(root, text="Start Scan", font=("Arial", 14), bg="#4CAF50", fg="white", command=on_scan_button_click)
start_button.pack(pady=20)

# Text area to display the scan results with scroll bar
result_text = tk.Text(root, height=15, width=70, font=("Courier New", 12), bg="#333333", fg="white", insertbackground='white', wrap="word")
result_text.pack(pady=10)

# Scrollbar for the text area
scrollbar = tk.Scrollbar(root, command=result_text.yview)
scrollbar.pack(side="right", fill="y")
result_text.config(yscrollcommand=scrollbar.set)

# Bottom status label for feedback
status_label = tk.Label(root, text="Status: Ready", font=("Arial", 12), bg="#2E3B4E", fg="white")
status_label.pack(side="bottom", pady=10)

# Run the Tkinter main loop
root.mainloop()
