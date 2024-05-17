import tkinter as tk

from settings_store import SettingsStore


class PenButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)

        self.canvas = canvas
        # Set the button text and bind the set_pen method
        self.config(text="Pen", command=self.set_pen,relief=tk.SUNKEN)

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
            line_id = canvas.create_polygon(
                canvas.lastx, canvas.lasty, x, y, fill=self.settings.color, outline=self.settings.color, width=self.settings.brush_size)
            # Store the line ID in the history stack for undo functionality
            canvas.history.append(line_id)

        # Update the last drawing position
        canvas.lastx, canvas.lasty = x, y

    def reset(self, canvas, event):
        # Reset the last drawing position
        canvas.lastx, canvas.lasty = None, None
