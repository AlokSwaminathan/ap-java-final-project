import tkinter as tk


class UndoButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.canvas = canvas
        self.config(text="Undo", command=self.canvas.undo)
