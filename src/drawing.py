import tkinter as tk
from settings_store import SettingsStore

class DrawingCanvas(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master)
        
        # Initialize settings and attributes
        self.settings = SettingsStore()
        self.pen_size = self.settings.get_current("brush_size")  # Set the initial pen size
        self.pen_color = self.settings.get_current("color")  # Set the initial pen color
        
        # Configure canvas
        self.config(bg='gray75', width=self.settings.get_current("canvas_width"), height=self.settings.get_current("canvas_height"))
        
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
            line_id = self.create_line(self.lastx, self.lasty, x, y, fill=self.pen_color, width=self.pen_size)
            # Store the line ID in the history stack for undo functionality
            self.history.append(line_id)
            
        # Update the last drawing position
        self.lastx, self.lasty = x, y

    def reset_last_position(self, event):
        # Reset the last drawing position
        self.lastx, self.lasty = None, None
