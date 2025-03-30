import tkinter as tk

def say_hello():
	label.config(text="Hello, Rimon!")

root = tk.Tk()
root.title("My First GUI")

root.geometry("500x300")

label = tk.Label(root, text="Click the button!")
label.pack()

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()

root.mainloop()

