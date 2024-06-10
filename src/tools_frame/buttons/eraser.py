import tkinter as tk
from settings_store import SettingsStore
from util import get_special_id, bold


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
        self.slider.set(10)

        self.eraser_preview = None

    def set_eraser(self):
        self.master.setActiveTool(self)
        self.slider.grid(row=2, column=0, sticky="ew")
        self.canvas.config(cursor="dot")
        bold(self.button)

    def action(self, canvas, event):
        x, y = event.x, event.y
        r = self.slider.get()
        line_id = self.canvas.logger.create_circle(
            x, y, r, fill=self.settings.background_color, outline=self.settings.background_color, special_id=self.special_id)

        # Draw preview of eraser
        if self.eraser_preview:
            canvas.delete(self.eraser_preview)
        self.eraser_preview = canvas.create_circle(
            x, y, r, fill=self.settings.background_color, outline="black")

    def release(self):
        self.slider.grid_forget()
        bold(self.button, False)

    def cursorRelease(self, canvas, event):
        canvas.delete(self.eraser_preview) if self.eraser_preview else None
        canvas.config(cursor="dot")

    def initialPress(self, canvas, event):
        canvas.config(cursor="none")
        self.special_id = get_special_id()
