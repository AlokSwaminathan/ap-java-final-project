import tkinter as tk

from settings_store import SettingsStore


class PenButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.canvas = canvas
        # Set the button text and bind the set_pen method
        self.config(text="Pen", command=self.set_pen)

        # Initialize pen size
        self.settings = SettingsStore()
        self.pen_size = self.settings.get_current('pen_size') or 5
        self.pen_color = self.settings.get_current('color') or 'black'

    def set_pen(self):
        # Set the canvas to pen drawing mode
        # Bind the drawing events to the pen drawing methods
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset_last_position)

    def draw(self, event):
        # Draw a circle (or square) at the current cursor position
        x, y = event.x, event.y
        radius = self.pen_size / 2

        # Draw a filled circle centered at the current cursor position
        line_id = self.canvas.create_line(
            self.canvas.lastx, self.canvas.lasty, x, y, fill=self.pen_color, width=self.pen_size)

        # Update the last drawing position
        self.canvas.lastx, self.canvas.lasty = x, y

    def reset_last_position(self, event):
        # Reset the last drawing position
        self.canvas.lastx, self.canvas.lasty = None, None
