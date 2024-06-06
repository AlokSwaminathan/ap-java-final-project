# tools_frame/buttons/shape.py
import tkinter as tk
from tkinter.ttk import OptionMenu

from settings_store import SettingsStore


class ShapeButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master, text="Shape", command=self.choose_shape)
        self.master = master
        self.canvas = canvas
        self.shape_type = None
        self.start_x = None
        self.start_y = None
        self.shape_preview = None
        self.settings = SettingsStore()

    def choose_shape(self):
        t = tk.Toplevel()
        t.title("Shape Selection")
        t.geometry("200x100")
        def select_shape(shape):
            self.shape_type = shape
            t.destroy()

        square_button = tk.Button(t, text="Square", command=lambda: select_shape("square"))
        square_button.pack()

        triangle_button = tk.Button(t, text="Triangle", command=lambda: select_shape("triangle"))
        triangle_button.pack()

        circle_button = tk.Button(t, text="Circle", command=lambda: select_shape("circle"))
        circle_button.pack()
        
        self.master.setActiveTool(self)
        self.canvas.config(cursor="tcross")

    def initialPress(self, canvas, event):
        self.start_x, self.start_y = event.x, event.y
        self.shape_preview = None

    def action(self, canvas, event):
        end_x, end_y = event.x, event.y
        if self.shape_preview:
            canvas.delete(self.shape_preview)
        self.shape_preview = self.draw_shape(
            canvas, self.start_x, self.start_y, end_x, end_y)

    def cursorRelease(self, canvas, event):
        end_x, end_y = event.x, event.y
        if self.shape_preview:
            canvas.delete(self.shape_preview)
        self.draw_shape(canvas, self.start_x, self.start_y,
                        end_x, end_y, finalize=True)
        self.start_x, self.start_y = None, None
        self.shape_preview = None

    def draw_shape(self, canvas, start_x, start_y, end_x, end_y, finalize=False):
        shape = None
        color = self.settings.color
        outline_width = self.settings.brush_size  # Set the thickness of the edges
        fill_color = self.settings.fill_color

        if self.shape_type == "square":
            shape = canvas.create_rectangle(
                start_x, start_y, end_x, end_y, outline=color, width=outline_width, fill=fill_color)
        elif self.shape_type == "triangle":
            shape = canvas.create_polygon(start_x, start_y, end_x, start_y, (
                start_x + end_x) / 2, end_y, outline=color, width=outline_width, fill=fill_color)
        elif self.shape_type == "circle":
            shape = canvas.create_oval(
                start_x, start_y, end_x, end_y, outline=color, width=outline_width, fill=fill_color)

        if finalize and shape:
            canvas.history.append(shape)
        return shape
