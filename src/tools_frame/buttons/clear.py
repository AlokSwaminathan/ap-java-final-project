import tkinter as tk


class ClearButton(tk.Button):
  def __init__(self, master=None, canvas=None):
    super().__init__(master)
    self.canvas = canvas
    self.config(text="Clear", command=self.clear)

  def clear(self):
    pass
