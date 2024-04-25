import tkinter as tk

class FillButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.canvas = canvas
        self.config(text="Fill", command=self.fill)