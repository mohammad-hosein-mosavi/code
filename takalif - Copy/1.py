import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button
def on_button_click():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

button = tk.Button(root, text="Greet", command=on_button_click)
button.pack(pady=10)

# Run the application
root.mainloop()