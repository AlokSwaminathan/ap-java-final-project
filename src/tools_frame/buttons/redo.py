import tkinter as tk


class RedoButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.canvas = canvas
        self.config(text="Redo", command=self.canvas.redo)
