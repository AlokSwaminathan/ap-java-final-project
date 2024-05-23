import tkinter as tk

class ShapeButton(tk.Frame):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.canvas = canvas

        self.button = tk.Button(self, text="Shape", command=self.select_shape)
        self.button.grid(row=0, column=0, sticky="ew")

        self.shape_var = tk.StringVar(value="Circle")

        self.shape_menu = tk.OptionMenu(self, self.shape_var, "Circle", "Square", "Triangle")
        self.shape_menu.grid(row=1, column=0, sticky="ew")

    def select_shape(self):
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

        shape = self.shape_var.get()
        if shape == "Circle":
            self.shape_preview = self.canvas.create_oval(self.start_x, self.start_y, end_x, end_y, outline=self.canvas.pen_color)
        elif shape == "Square":
            self.shape_preview = self.canvas.create_rectangle(self.start_x, self.start_y, end_x, end_y, outline=self.canvas.pen_color)
        elif shape == "Triangle":
            self.shape_preview = self.canvas.create_polygon(
                self.start_x, self.start_y,
                (self.start_x + end_x) // 2, end_y,
                end_x, self.start_y,
                outline=self.canvas.pen_color, fill="", width=self.canvas.pen_size)

    def finalize_shape(self, event):
        end_x, end_y = event.x, event.y
        if self.shape_preview:
            self.canvas.delete(self.shape_preview)

        shape = self.shape_var.get()
        if shape == "Circle":
            self.canvas.create_oval(self.start_x, self.start_y, end_x, end_y, outline=self.canvas.pen_color, width=self.canvas.pen_size)
        elif shape == "Square":
            self.canvas.create_rectangle(self.start_x, self.start_y, end_x, end_y, outline=self.canvas.pen_color, width=self.canvas.pen_size)
