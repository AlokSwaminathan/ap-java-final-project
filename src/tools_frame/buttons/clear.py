import tkinter as tk


class ClearButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.canvas = canvas
        # Set the button text and bind the clear function to the button
        self.config(text="Clear", command=self.clear)

    def clear(self):
        # Clear the entire canvas
        # Use canvas.delete("all") to remove all content from the canvas
        self.canvas.delete("all")
