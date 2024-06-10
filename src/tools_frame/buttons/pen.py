import tkinter as tk

from settings_store import SettingsStore
from util import get_special_id


class PenButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)

        self.canvas = canvas
        # Set the button text and bind the set_pen method
        self.config(text="Pen", command=self.set_pen, relief=tk.SUNKEN)

        # Initialize pen size
        self.settings = SettingsStore()


    def set_pen(self):
        # Set the active button to be Pen
        self.master.setActiveTool(self)
        self.canvas.config(cursor="pencil")

    def action(self, canvas, event):
        # Draw on the canvas based on mouse movement
        x, y = event.x, event.y
        if canvas.lastx and canvas.lasty:
            # Draw a line using the current pen size and color
            line_id = canvas.logger.create_polygon(
                canvas.lastx, canvas.lasty, x, y, fill=self.settings.color, outline=self.settings.color, width=self.settings.brush_size,special_id=self.special_id)
            # Store the line ID in the history stack for undo functionality

        # Update the last drawing position
        canvas.lastx, canvas.lasty = x, y

    def cursorRelease(self, canvas, event):
        pass
    
    def initialPress(self,canvas,event):
        self.special_id = get_special_id()
