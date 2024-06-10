import tkinter as tk
from drawing_logger import DrawingLogger
from settings_store import SettingsStore


class DrawingCanvas(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master)

        # Initialize settings and attributes
        self.settings = SettingsStore()

        # Configure canvas
        self.config(bg=self.settings.background_color, height=self.settings.canvas_height,
                    width=self.settings.canvas_width, cursor="pencil")

        # Initialize drawing position variables
        self.lastx, self.lasty = None, None

        # Event bindings for drawing
        self.bind("<Button-1>", self.initialPress)
        self.bind("<B1-Motion>", self.draw)
        self.bind("<ButtonRelease-1>", self.reset_last_position)

        # Set up the logger for undo and redo functionality
        self.logger = DrawingLogger(self)

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

    def undo(self, event=None):
        self.logger.undo()

    def redo(self, event=None):
        self.logger.redo()

    def create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

    def save(self, event=None):
        print(event)
        from PIL import Image, ImageTk
        from io import BytesIO

        # Output canvas to eps file in memory
        eps = self.postscript(colormode='color')

        # Convert eps to png

        im = Image.open(BytesIO(bytes(eps, 'ascii')))

        # Ask the user for a path to save the file to
        path = self.get_save_path()

        im.save(path, "png")

    def get_save_path(self):
        from tkinter import filedialog
        import os

        initialdir = self.settings.save_path

        if not os.path.exists(initialdir):
            os.makedirs(initialdir)

        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[
                                            ("PNG files", "*.png")], initialdir=initialdir, initialfile="drawing.png")
        return path
