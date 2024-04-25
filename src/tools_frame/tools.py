import tkinter as tk

from tools_frame.buttons.canvas_size import CanvasSizeButton
from tools_frame.buttons.clear import ClearButton
from tools_frame.buttons.color import ColorButton
from tools_frame.buttons.fill import FillButton
from tools_frame.buttons.line import LineButton
from tools_frame.buttons.quit import QuitButton
from tools_frame.buttons.redo import RedoButton
from tools_frame.buttons.shape import ShapeButton
from tools_frame.buttons.text import TextButton
from tools_frame.buttons.undo import UndoButton

class ToolsFrame(tk.Frame):
    def __init__(self, master=None,canvas=None):
        super().__init__(master)

        self.canvas = canvas

        self.grid(row=0, column=0, sticky="nsew")

        self.create_widgets()

    def create_widgets(self):

        self.color_button = ColorButton(self,canvas=self.canvas)
        self.color_button.grid(row=0, column=0, sticky="ew")

        self.size_button = LineButton(self,canvas=self.canvas)
        self.size_button.grid(row=1, column=0, sticky="ew")

        self.fill_button = FillButton(self,canvas=self.canvas)
        self.fill_button.grid(row=2, column=0, sticky="ew")

        self.text_button = TextButton(self,canvas=self.canvas)
        self.text_button.grid(row=3, column=0, sticky="ew")

        self.line_button = LineButton(self,canvas=self.canvas)
        self.line_button.grid(row=4, column=0, sticky="ew")

        self.shape_button = ShapeButton(self,canvas=self.canvas)
        self.shape_button.grid(row=5, column=0, sticky="ew")

        self.undo_button = UndoButton(self,canvas=self.canvas)
        self.undo_button.grid(row=6, column=0, sticky="ew")

        self.redo_button = RedoButton(self,canvas=self.canvas)
        self.redo_button.grid(row=7, column=0, sticky="ew")

        self.clear_button = ClearButton(self,canvas=self.canvas)
        self.clear_button.grid(row=8, column=0, sticky="ew")

        self.canvas_size = CanvasSizeButton(self,canvas=self.canvas)
        self.canvas_size.grid(row=10, column=0, sticky="ew")
    