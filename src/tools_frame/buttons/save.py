import tkinter as tk

class SaveButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.canvas = canvas
        self.config(text="Save", command=self.canvas.save)