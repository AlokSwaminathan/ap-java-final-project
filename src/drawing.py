import tkinter as tk

class DrawingCanvas(tk.Canvas):
  def __init__(self, master=None):
    super().__init__(master)
    self.grid(row=0, column=1, sticky="nsew")
    self.create_text(400, 300, text="Welcome to PyDraw!", font=("Helvetica", 32))
    self.config(bg="white", width=800, height=600)

    self.lastx, self.lasty = None, None
    self.bind("<B1-Motion>", self.draw)
    self.bind("<ButtonRelease-1>",self.reset_last_position)

  def draw(self, event):
    x, y = event.x, event.y
    if self.lastx and self.lasty:
      self.create_line(self.lastx, self.lasty, x, y,fill="black", width=2)
    self.lastx, self.lasty = x, y
  
  def reset_last_position(self,event):
    self.lastx, self.lasty = None, None

