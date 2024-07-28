import tkinter as tk

# Create a window
window = tk.Tk()

# Add code to customize the window (e.g., title, size, etc.)
# Create a label widget
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

# Create a button widget
def on_button_click():
    label.config(text="Button Clicked!")

button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack()

# Start the main event loop
window.mainloop()