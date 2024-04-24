import tkinter as tk

from drawing import DrawingCanvas
from tools import ToolsFrame

class Window(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("PyDraw")

    self.tools_frame = ToolsFrame(self)
    self.tools_frame.grid(row=0,column=0,sticky="ns")

    self.draw_canvas = DrawingCanvas(self) 
    self.draw_canvas.grid(row=0,column=1,sticky="nsew")

    self.rowconfigure(0, weight=1)
    self.columnconfigure(1, weight=4)