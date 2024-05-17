import tkinter as tk
from settings_store import SettingsStore


class EraserButton(tk.Frame):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)

        self.canvas = canvas
        self.settings = SettingsStore()
        self.button = tk.Button(self)
        self.button.config(text="Eraser", command=self.set_eraser)
        self.button.grid(row=1, column=0, sticky="ew")
        self.grid_columnconfigure(0, weight=1)
        self.slider = tk.Scale(self, from_=1, to=100, orient=tk.HORIZONTAL)
        self.slider.grid_forget()

    def set_eraser(self):
        self.master.setActiveTool(self)
        self.slider.grid(row=2, column=0, sticky="ew")
        self.canvas.config(cursor="dot")

    def action(self, canvas, event):
        x, y = event.x, event.y
        r = self.slider.get()
        self.canvas.create_polygon(
            canvas.lastx, canvas.lasty, x, y, fill=self.settings.background_color, outline=self.settings.background_color, width=self.slider.get())

    def release(self):
        self.slider.grid_forget()
        self.button.config(relief=tk.RAISED)
