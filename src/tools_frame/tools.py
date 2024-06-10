import tkinter as tk

from tools_frame.buttons.clear import ClearButton
from tools_frame.buttons.color import ColorButton
from tools_frame.buttons.eraser import EraserButton
from tools_frame.buttons.fill import FillButton
from tools_frame.buttons.fill_color_button import FillColorButton
from tools_frame.buttons.line import LineButton
from tools_frame.buttons.pen import PenButton
from tools_frame.buttons.redo import RedoButton
from tools_frame.buttons.shape import ShapeButton
from tools_frame.buttons.text import TextButton
from tools_frame.buttons.undo import UndoButton
from tools_frame.buttons.thickness import ThicknessButton


class ToolsFrame(tk.Frame):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)

        self.canvas = canvas

        self.grid(row=0, column=0, sticky="nsew")

        self.create_widgets()

        self.setActiveTool(self.pen_button)

    def create_widgets(self):
        self.pen_button = PenButton(self, canvas=self.canvas)
        self.eraser_button = EraserButton(self, canvas=self.canvas)
        self.color_button = ColorButton(self, canvas=self.canvas)
        self.size_button = LineButton(self, canvas=self.canvas)
        self.fill_button = FillButton(self, canvas=self.canvas)
        self.text_button = TextButton(self, canvas=self.canvas)
        self.line_button = LineButton(self, canvas=self.canvas)
        self.shape_button = ShapeButton(self, canvas=self.canvas)
        self.undo_button = UndoButton(self, canvas=self.canvas)
        self.redo_button = RedoButton(self, canvas=self.canvas)
        self.thickness_button = ThicknessButton(self, canvas=self.canvas)
        self.clear_button = ClearButton(self, canvas=self.canvas)
        self.fill_color = FillColorButton(self, canvas=self.canvas)

        # List of buttons, change order of list to change order buttons are rendered
        self.buttons = [self.pen_button, self.eraser_button, self.color_button, self.size_button, self.text_button,
                        self.line_button, self.shape_button, self.fill_color, self.undo_button, self.clear_button, self.thickness_button]
        for i, button in enumerate(self.buttons):
            button.grid(row=i, column=0, sticky="ew")

    def setActiveTool(self, button):
        for b in self.buttons:
            if b != button:
                b.release() if hasattr(b, 'release') else b.config(relief=tk.RAISED)
        self.canvas.active_tool = button
