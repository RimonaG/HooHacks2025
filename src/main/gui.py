import tkinter as tk
from tkinter import filedialog, messagebox
from MusicLibrary import MusicLibrary
#import EmptionDetection as deepFace
from RemoteSSHcaller import analyze_image

library = MusicLibrary()
import os
selected_image = None
# Create the main window
root = tk.Tk()
root.title("Timer Button Example")
root.geometry("300x200")

# Function to show the second button after 3 seconds
def show_second_button():
	second_button = tk.Button(root, text="Click Here for Your Songs!", command=on_second_button_click)
	second_button.pack(pady=10)
	label_2.pack_forget()

def on_second_button_click():
	if selected_image:
		emotion = analyze_image(selected_image)
		library.get_song(emotion)
	else:
		messagebox.showerror("Error", "No image path found.")
# Function to start the timer
def on_first_button_click():
	global selected_image

	#Open file dialog to select an image
	file_path = filedialog.askopenfilename(
	title="Select an Image",
	filetypes=[("JPEG files", "*.jpg *.jpeg"), ("All files", "*.*")]
	)
	selected_image = file_path
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
			messagebox.showerror("Invalid File", "Please select a .jpg or .jpeg image.")
	else:
		messagebox.showinfo("No File", "No image selected.")

# Initial label
label = tk.Label(root, text="Click the button below")
label.pack(pady=10)

# Second label
label_2 = tk.Label(root)

# First button
first_button = tk.Button(root, text="Upload and Scan Image", command=on_first_button_click)
first_button.pack(pady=10)

# Run the app
root.mainloop()
