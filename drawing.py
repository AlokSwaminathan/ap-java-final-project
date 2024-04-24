import tkinter as tk

class DrawingCanvas(tk.Canvas):
  def __init__(self, master=None):
    super().__init__(master)
    self.grid(row=0, column=1, sticky="nsew")
    self.config(bg="blue", width=800, height=600)
  
