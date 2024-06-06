import tkinter as tk
from tkinter import simpledialog

from settings_store import SettingsStore


class TextButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.master = master
        self.canvas = canvas
        self.text_button = tk.Button(self)
        self.text_button.config(text="Text", command=self.set_text)
        self.text_button.grid(row=1, column=0, sticky="ew")
        self.grid_columnconfigure(0, weight=1)
        self.font_slider = tk.Scale(
            self, from_=1, to=100, orient=tk.HORIZONTAL, label="Font Size")
        self.font_slider.set(10)
        self.current_text_button = tk.Label(
            self, text="Current Text:\nHello World")
        self.current_text = "Hello World"
        self.change_current_text_button = tk.Button(
            self, text="Change Text", command=self.updateCurrentText)
        self.current_text_button.grid(row=3, column=0, sticky="ew")
        self.change_current_text_button.grid(row=4, column=0, sticky="ew")
        self.settings = SettingsStore()

    def set_text(self):
        self.master.setActiveTool(self)
        self.font_slider.grid(row=2, column=0, sticky="ew")
        self.canvas.config(cursor="xterm")

    def release(self):
        self.font_slider.grid_forget()
        self.text_button.config(relief=tk.RAISED)

    def initialPress(self, canvas, event):
        x, y = event.x, event.y
        font_size = self.font_slider.get()
        text = canvas.create_text(x, y, text=self.current_text, font=(
            "Arial", font_size), fill=self.settings.color)
        if text:
            canvas.history.append(text)

    def getUserText(self):
        text = simpledialog.askstring("Text", "Enter text")
        return text

    def updateCurrentText(self):
        self.current_text = self.getUserText()
        self.current_text_button.config(
            text=f"Current Text:\n{self.current_text}")
