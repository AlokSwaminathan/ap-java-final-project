import tkinter as tk

class ToolsFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.grid(row=0, column=0, sticky="nsew")

        self.create_widgets()

    def create_widgets(self):
        self.color_button = tk.Button(self, text="Color")
        self.color_button.grid(row=0, column=0, sticky="ew")

        self.size_button = tk.Button(self, text="Thickness")
        self.size_button.grid(row=1, column=0, sticky="ew")

        self.fill_button = tk.Button(self, text="Fill")
        self.fill_button.grid(row=2, column=0, sticky="ew")

        self.text_button = tk.Button(self, text="Text")
        self.text_button.grid(row=3, column=0, sticky="ew")

        self.line_button = tk.Button(self, text="Line")
        self.line_button.grid(row=4, column=0, sticky="ew")

        self.polygon_button = tk.Button(self, text="Shape")
        self.polygon_button.grid(row=5, column=0, sticky="ew")

        self.undo_button = tk.Button(self, text="Undo")
        self.undo_button.grid(row=6, column=0, sticky="ew")

        self.redo_button = tk.Button(self, text="Redo")
        self.redo_button.grid(row=7, column=0, sticky="ew")

        self.clear_button = tk.Button(self, text="Clear")
        self.clear_button.grid(row=8, column=0, sticky="ew")

        self.quit_button = tk.Button(self, text="Quit")
        self.quit_button.grid(row=9, column=0, sticky="ew")