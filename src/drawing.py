import tkinter as tk
from settings_store import SettingsStore


class DrawingCanvas(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master)

        # Initialize settings and attributes
        self.settings = SettingsStore()

        # Configure canvas
        self.config(bg="gray75", height=self.settings.canvas_height,
                    width=self.settings.canvas_width)

        # Initialize drawing position variables
        self.lastx, self.lasty = None, None

        # Event bindings for drawing
        self.bind("<B1-Motion>", self.draw)
        self.bind("<ButtonRelease-1>", self.reset_last_position)

        # Initialize a history stack for undo functionality
        self.history = []

    def draw(self, event):
        # Draw on the canvas based on mouse movement
        x, y = event.x, event.y
        if self.lastx and self.lasty:
            # Draw a line using the current pen size and color
            line_id = self.create_polygon(
                self.lastx, self.lasty, x, y, fill=self.settings.color, outline=self.settings.color, width=self.settings.brush_size)
            print(line_id)
            # Store the line ID in the history stack for undo functionality
            self.history.append(line_id)

        # Update the last drawing position
        self.lastx, self.lasty = x, y

    def reset_last_position(self, event):
        # Reset the last drawing position
        
        self.lastx, self.lasty = None, None
