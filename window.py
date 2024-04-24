import tkinter as tk

from drawing import DrawingCanvas
from tools import ToolsFrame

class Window(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("PyDraw")
    self.tools_frame = ToolsFrame(self);
    self.draw_canvas = DrawingCanvas(self); 
