import tkinter as tk
from tkinter.colorchooser import askcolor
from drawing import DrawingPad
from saving import DrawingSaver
import settings

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")
        self.canvas = DrawingPad(self.root, settings.CANVAS_WIDTH, settings.CANVAS_HEIGHT)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.toolbar_frame = tk.Frame(self.root)
        self.toolbar_frame.pack(side=tk.RIGHT, fill=tk.Y)
        self.drawing_saver = DrawingSaver()
        self.brush_color = settings.DEFAULT_COLOR
        self.brush_size = settings.DEFAULT_BRUSH_SIZE
        self.canvas.bind("<B1-Motion>", self.draw)
        self.add_toolbar_widgets()

    def add_toolbar_widgets(self):
        color_button = tk.Button(self.toolbar_frame, text="Color", command=self.choose_color)
        color_button.pack(pady=5)
        brush_size_slider = tk.Scale(self.toolbar_frame, from_=1, to=20, orient=tk.VERTICAL, label="Brush Size", command=self.change_brush_size)
        brush_size_slider.set(self.brush_size)
        brush_size_slider.pack(pady=5)
        clear_button = tk.Button(self.toolbar_frame, text="Clear", command=self.clear_canvas)
        clear_button.pack(pady=5)
        save_button = tk.Button(self.toolbar_frame, text="Save", command=self.save_canvas)
        save_button.pack(pady=5)

    def draw(self, event):
        self.canvas.draw(event, self.brush_color, self.brush_size)

    def choose_color(self):
        color = askcolor(color=self.brush_color)[1]
        if color:
            self.brush_color = color

    def change_brush_size(self, value):
        self.brush_size = int(value)

    def clar_canvas(self):
        self.canvas.clear()

    def save_canvas(self):
        self.drawing_saver.save_as_png(self.canvas, settings.DEFAULT_SAVE_PATH)

    def run(self):
        self.root.mainloop()