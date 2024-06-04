import tkinter as tk
from tkinter import colorchooser
from settings_store import SettingsStore


class ColorButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.canvas = canvas
        self.settings = SettingsStore()
        self.config(text="Color", command=self.choose_color)

    def choose_color(self):
        # Open a color picker dialog
        color_code = colorchooser.askcolor()[1]
        if color_code:
            self.settings.color = color_code
        self.config(foreground=self.settings.color)
