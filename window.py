import tkinter as tk

from tools import ToolsFrame

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyDraw")
        self.tools_frame = ToolsFrame(self)
