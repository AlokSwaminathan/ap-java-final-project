# tools_frame/buttons/shape.py
import tkinter as tk
from tkinter import simpledialog

class ShapeButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master, text="Shape", command=self.choose_shape)
        self.canvas = canvas
        self.shape_type = None
        self.start_x = None
        self.start_y = None
        self.shape_preview = None

    def choose_shape(self):
        self.shape_type = simpledialog.askstring("Shape", "Enter shape (square, triangle, circle):")
        self.canvas.bind("<Button-1>", self.start_shape)
        self.canvas.bind("<B1-Motion>", self.draw_shape_preview)
        self.canvas.bind("<ButtonRelease-1>", self.finalize_shape)

    def start_shape(self, event):
        self.start_x, self.start_y = event.x, event.y
        self.shape_preview = None

    def draw_shape_preview(self, event):
        end_x, end_y = event.x, event.y
        if self.shape_preview:
            self.canvas.delete(self.shape_preview)
        self.shape_preview = self.draw_shape(self.start_x, self.start_y, end_x, end_y)

    def finalize_shape(self, event):
        end_x, end_y = event.x, event.y
        if self.shape_preview:
            self.canvas.delete(self.shape_preview)
        self.draw_shape(self.start_x, self.start_y, end_x, end_y, finalize=True)
        self.start_x, self.start_y = None, None
        self.shape_preview = None

    def draw_shape(self, start_x, start_y, end_x, end_y, finalize=False):
        shape = None
        color = self.canvas.pen_color if hasattr(self.canvas, 'pen_color') else 'white'
        outline_width = 3  # Set the thickness of the edges

        if self.shape_type == "square":
            shape = self.canvas.create_rectangle(start_x, start_y, end_x, end_y, outline=color, width=outline_width, fill="")
        elif self.shape_type == "triangle":
            shape = self.canvas.create_polygon(start_x, start_y, end_x, start_y, (start_x + end_x) / 2, end_y, outline=color, width=outline_width, fill="")
        elif self.shape_type == "circle":
            shape = self.canvas.create_oval(start_x, start_y, end_x, end_y, outline=color, width=outline_width, fill="")

        if finalize and shape:
            self.canvas.history.append(shape)
        return shape
