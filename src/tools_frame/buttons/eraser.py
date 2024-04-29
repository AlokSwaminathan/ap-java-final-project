import tkinter as tk

from src.settings_store import SettingsStore


class EraserButton(tk.Frame):
  def __init__(self, master=None, canvas=None):
    super().__init__(master)
    self.canvas = canvas
    self.settings = SettingsStore()
    self.button = tk.Button(self)
    self.button.config(text="Eraser", command=self.set_eraser)
    self.button.grid(row=1, column=0, sticky="ew")
    self.slider = tk.Scale(self, from_=1, to=100, orient=tk.HORIZONTAL)
    self.slider.grid_forget()

  def set_eraser(self):
    self.canvas.bind("<B1-Motion>", self.erase)
    self.slider.grid(row=2, column=0, sticky="ew")

  def erase(self, event):
    x, y = event.x, event.y
    r = self.slider.get()
    self.canvas.create_oval(
        x-r, y-r, x+r, y+r, fill="gray75", outline="gray75")
