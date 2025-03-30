import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Tk, Label
from tkinter import ttk
import webbrowser
from tkinter import filedialog, messagebox
from MusicLibrary import MusicLibrary
from RemoteSSHcaller import analyze_image

library = MusicLibrary()
import os
selected_image = None
# Create the main window and style(colors)
root = tk.Tk()
style = ttk.Style(root)
style.theme_use("clam") #allows customization

root.title("File Uploader")
root.geometry("800x500")
root.configure(background="#ADD8E6")

# Function to show the second button after 3 seconds
def show_second_button():
	second_button = tk.Button(root, text="Click Here for Your Songs!", command=on_second_button_click)
	second_button.pack(pady=10)
	label_2.pack_forget()

def on_second_button_click():
	if selected_image:
		emotion = analyze_image(selected_image)
		song = library.get_song(emotion.lower())

		label3.config(text="Emotional: " + emotion)

		show_link_popup(song)
	if messagebox.askyesno("Play Song", "Do you want to play a song?"):
		webbrowser.open_new_tab(song)

	else:
		messagebox.showerror("Error", "No image path found.")




#open pop up with link to the song
def show_link_popup(Song_url):
	#popup = tk.Toplevel()
	#popup.title("Click the link for your song!")
	#popup.geometry("400x200")
	#popup.configure(bg="#ADD8E6") #light blue
	Songlink_label.config(text=Song_url)
	Songlink_label.bind("<Button-1>", lambda e: webbrowser.open_new_tab(Song_url))

	def callback(event):
		webbrowser.open_new(Song_url)


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
			image_display(file_path)
			root.after(3000, show_second_button)  # 3000ms = 3 seconds
			label.pack_forget()
		else:
			messagebox.showerror("Invalid File", "Please select a .jpg or .jpeg image.")
	else:
		messagebox.showinfo("No File", "No image selected.")

# Initial label
label = tk.Label(root, text="Click the button below")
label.pack(pady=10)
label.configure(background="#ADD8E6")

# Second label
label_2 = tk.Label(root)
label_2.configure(background="#ADD8E6")

label3 = tk.Label(root, text="", font=("Helvetica", 20), bg="#ADD8E6")
label3.pack(pady=10)



# First button
first_button = tk.Button(root, text="Upload and Scan Image", command=on_first_button_click)
first_button.pack(pady=10)
first_button.configure(background="#ADD8E6")

Songlink_label = tk.Label(root, text="", fg="blue", cursor="hand2", bg="#ADD8E6", font=("Helvetica", 12, "underline"))
Songlink_label.pack(pady=10)

# Image preview label (empty for now, will update after image is selected)
image_label = tk.Label(root, bg="#ADD8E6")
image_label.pack(pady=10)


def image_display(filename):
	#image display:
	img = Image.open(filename)
	img = img.resize((200, 200))
	photo = ImageTk.PhotoImage(img)
	image_label.config(image=photo)
	image_label.image = photo

# Run the app
root.mainloop()
