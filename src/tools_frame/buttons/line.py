import tkinter as tk

class LineButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.canvas = canvas
        self.config(text="Line", command=self.set_line)
        self.start_x = None
        self.start_y = None

    def set_line(self):
        self.canvas.bind("<Button-1>", self.start_line)
        self.canvas.bind("<ButtonRelease-1>", self.end_line)

    def start_line(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def end_line(self, event):
        end_x = event.x
        end_y = event.y
        self.canvas.create_line(self.start_x, self.start_y, end_x, end_y, fill=self.canvas.pen_color, width=self.canvas.pen_size)
        self.start_x = None
        self.start_y = None
