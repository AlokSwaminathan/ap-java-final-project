import tkinter as tk

from settings_store import SettingsStore


class LineButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.master = master
        self.config(text="Line", command=self.set_line)
        self.start_x = None
        self.start_y = None
        self.line_preview = None
        self.settings = SettingsStore()

    def set_line(self):
        self.master.setActiveTool(self)

    def initialPress(self, canvas, event):
        self.start_x = event.x
        self.start_y = event.y

    def action(self, canvas, event):
        end_x = event.x
        end_y = event.y
        if self.line_preview:
            canvas.delete(self.line_preview)
        self.line_preview = canvas.create_line(
            self.start_x, self.start_y, end_x, end_y, fill=self.settings.color, width=self.settings.brush_size)

    def cursorRelease(self, canvas, event):
        end_x = event.x
        end_y = event.y
        if self.line_preview:
            canvas.delete(self.line_preview)
        line_id = canvas.create_line(self.start_x, self.start_y, end_x, end_y,
                           fill=self.settings.color, width=self.settings.brush_size)
        canvas.history.append(line_id)
        self.start_x = None
        self.start_y = None
