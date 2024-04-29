import tkinter as tk

class PenButton(tk.Button):
  def __init__(self, master=None, canvas=None):
    super().__init__(master)
    self.canvas = canvas
    self.config(text="Pen", command=self.set_pen)

  def set_pen(self):
    self.canvas.bind("<B1-Motion>", self.draw)
    self.canvas.bind("<ButtonRelease-1>", self.reset_last_position)

  def draw(self, event):
    x, y = event.x, event.y
    if self.canvas.lastx and self.canvas.lasty:
      self.canvas.create_line(self.canvas.lastx, self.canvas.lasty, x, y, fill="black", width=2)
    self.canvas.lastx, self.canvas.lasty = x, y

  def reset_last_position(self, event):
    self.canvas.lastx, self.canvas.lasty = None, None