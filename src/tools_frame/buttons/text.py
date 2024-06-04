import tkinter as tk


class TextButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.canvas = canvas
        self.config(text="Text",command=self.set_text)
        
    def set_text(self):
        self.canvas.setActiveTool(self)
    
    def initialPress(self, canvas, event):
        pass
