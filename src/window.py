import tkinter as tk

from drawing import DrawingCanvas
from settings_store import SettingsStore
from tools_frame.tools import ToolsFrame


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyDraw")

        self.draw_canvas = DrawingCanvas(self)
        self.draw_canvas.grid(row=0, column=1, sticky="nsew")

        self.tools_frame = ToolsFrame(self, canvas=self.draw_canvas)
        self.tools_frame.grid(row=0, column=0, sticky="ns")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)

    def run(self):
        self.mainloop()
        SettingsStore().save_settings()
