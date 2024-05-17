import tkinter as tk
from settings_store import SettingsStore


class DrawingCanvas(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master)

        # Initialize settings and attributes
        self.settings = SettingsStore()

        # Configure canvas
        self.config(bg="gray75", height=self.settings.canvas_height,
                    width=self.settings.canvas_width,cursor="plus")

        # Initialize drawing position variables
        self.lastx, self.lasty = None, None

        # Event bindings for drawing
        self.bind("<B1-Motion>", self.draw)
        self.bind("<ButtonRelease-1>", self.reset_last_position)

        # Initialize a history stack for undo functionality
        self.history = []

    def draw(self, event):
        self.active_tool.action(self, event)

    def reset_last_position(self, event):
        # Reset the last drawing position
        self.active_tool.reset(self, event) if hasattr(self.active_tool, "reset") else None
        self.lastx, self.lasty = None, None
