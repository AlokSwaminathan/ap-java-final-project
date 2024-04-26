import tkinter as tk

from src.settings_store import SettingsStore


class EraserButton(tk.Button):
  def __init__(self, master=None, canvas=None):
    super().__init__(master)
    self.canvas = canvas
    self.settings = SettingsStore()
    self.config(text="Eraser", command=self.set_eraser)

  def set_eraser(self):
    pass
