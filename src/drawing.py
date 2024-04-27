import tkinter as tk
from settings_store import SettingsStore


class DrawingCanvas(tk.Canvas):
  def __init__(self, master=None):
    super().__init__(master)

    self.settings = SettingsStore()

    self.grid(row=0, column=1, sticky="nsew")
    self.config(bg="gray75", width=self.settings.get_default(
        "canvas_width"), height=self.settings.get_default("canvas_height"))

    self.lastx, self.lasty = None, None
    self.bind("<B1-Motion>", self.draw)
    self.bind("<ButtonRelease-1>", self.reset_last_position)

  def draw(self, event):
    x, y = event.x, event.y
    if self.lastx and self.lasty:
      self.create_line(self.lastx, self.lasty, x, y, fill="black", width=2)
    self.lastx, self.lasty = x, y

  def reset_last_position(self, event):
    self.lastx, self.lasty = None, None
