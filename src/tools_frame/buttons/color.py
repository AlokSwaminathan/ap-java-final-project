import tkinter as tk
from tkinter import colorchooser
from settings_store import SettingsStore


class ColorButton(tk.Frame):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.config(pady=10)
        self.canvas = canvas
        self.settings = SettingsStore()
        self.color_button = tk.Button(self)
        self.color_button.config(text="Color", command=self.choose_color)
        self.color_button.grid(row=1, column=0, sticky="ew")
        self.grid_columnconfigure(0, weight=1)
        self.color_view = tk.Frame(
            self, bg=self.settings.color, width=20, height=20, padx=5, pady=5)
        self.color_view.grid(row=0, column=0, sticky="ew")

    def choose_color(self):
        # Open a color picker dialog
        color_code = colorchooser.askcolor()[1]
        if color_code:
            self.settings.color = color_code
        self.color_view.config(bg=self.settings.color)

    def release(self):
        pass
