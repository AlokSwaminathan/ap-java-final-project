import tkinter as tk

from settings_store import SettingsStore


class PenButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)

        # Set the button text and bind the set_pen method
        self.config(text="Pen", command=self.set_pen)

        # Initialize pen size
        self.settings = SettingsStore()

    def set_pen(self):
        # Set the active button to be Pen
        self.master.active_button = self

    def draw(self, canvas, event):
        # Draw a circle (or square) at the current cursor position
        x, y = event.x, event.y

        line_id = canvas.create_line(
            self.canvas.lastx, self.canvas.lasty, x, y, fill=self.settings.color, width=self.settings.brush_size)

        # Update the last drawing position
        canvas.lastx, canvas.lasty = x, y

    def reset_last_position(self, canvas, event):
        # Reset the last drawing position
        canvas.lastx, canvas.lasty = None, None
