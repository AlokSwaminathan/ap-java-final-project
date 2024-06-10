import tkinter as tk
from settings_store import SettingsStore


class DrawingCanvas(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master)

        # Initialize settings and attributes
        self.settings = SettingsStore()

        # Configure canvas
        self.config(bg="gray75", height=self.settings.canvas_height,
                    width=self.settings.canvas_width, cursor="pencil")

        # Initialize drawing position variables
        self.lastx, self.lasty = None, None

        # Event bindings for drawing
        self.bind("<Button-1>", self.initialPress)
        self.bind("<B1-Motion>", self.draw)
        self.bind("<ButtonRelease-1>", self.reset_last_position)

        # Initialize a history stack for undo functionality
        self.history = []

    def draw(self, event):
        self.active_tool.action(self, event) if hasattr(
            self.active_tool, "action") else None

    def reset_last_position(self, event):
        self.active_tool.cursorRelease(self, event) if hasattr(
            self.active_tool, "cursorRelease") else None
        self.lastx, self.lasty = None, None

    def initialPress(self, event):
        self.lastx, self.lasty = event.x, event.y
        self.active_tool.initialPress(self, event) if hasattr(
            self.active_tool, "initialPress") else None

    def undo_last_action(self, event=None):
        if len(self.history) > 0:
            last_item = self.history.pop()
            if type(last_item) == list:
                for item in last_item:
                    self.delete(item)
            else:
                self.delete(last_item)

    def create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
