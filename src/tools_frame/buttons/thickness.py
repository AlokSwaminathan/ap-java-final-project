import tkinter as tk


class ThicknessButton(tk.Button):
  def __init__(self, master=None, canvas=None):
    super().__init__(master)
    self.canvas = canvas
    self.config(text="Thickness")
