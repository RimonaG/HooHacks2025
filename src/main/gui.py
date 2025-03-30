import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Create the main window
root = tk.Tk()
root.title("Timer Button Example")
root.geometry("300x200")

# Function to show the second button after 3 seconds
def show_second_button():
	second_button = tk.Button(root, text="Click Here for Your Songs!")
	second_button.pack(pady=10)
	label_2.pack_forget()

# Function to start the timer
def on_first_button_click():
	#Open file dilog to select an image
	file_path = filedialog.askopenfilename(
	title="Select an Image",
	filetypes=[("JPEG files", "*.jpg *.jpeg"), ("All files", "*.*")]
	)

	#Check if the user selected a file
	if file_path:
		if file_path.lower().endswith(('.jpg', '.jpeg')):
			label.config(text="Waiting 3 seconds...")
			first_button.pack_forget()
			label_2.config(text="Analyzing Photo...")
			label_2.pack(pady=10)
			root.after(3000, show_second_button)  # 3000ms = 3 seconds
			label.pack_forget()
		else:


# Initial label
label = tk.Label(root, text="Click the button below")
label.pack(pady=10)
# Second label
label_2 = tk.Label(root)


# First button
first_button = tk.Button(root, text="Click me", command=on_first_button_click)
first_button.pack(pady=10)

# Run the app
root.mainloop()
