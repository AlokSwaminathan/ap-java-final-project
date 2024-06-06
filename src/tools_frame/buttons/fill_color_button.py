import tkinter as tk
from tkinter import colorchooser
from settings_store import SettingsStore


class FillColorButton(tk.Frame):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.config(pady=10)
        self.canvas = canvas
        self.settings = SettingsStore()
        self.color_button = tk.Button(self)
        self.color_button.config(text="Fill Color", command=self.choose_color)
        self.color_button.grid(row=1, column=0, sticky="ew")
        self.grid_columnconfigure(0, weight=1)
        self.color_view = tk.Label(
            self, bg=self.settings.fill_color)
        self.color_view.grid(row=0, column=0, sticky="ew")
        self.transparent_button = tk.Button(self)
        self.transparent_button.config(
            text="Set Transparent", command=self.set_transparent)
        self.transparent_button.grid(row=2, column=0, sticky="ew")
        self.sync_colors_button = tk.Button(self)
        self.sync_colors_button.config(
            text="Sync with Color", command=self.sync_color)
        self.sync_colors_button.grid(row=3, column=0, sticky="ew")
        

    def choose_color(self):
        # Open a color picker dialog
        color_code = colorchooser.askcolor()[1]
        if color_code:
            self.settings.fill_color = color_code
        self.color_view.config(bg=self.settings.fill_color, text="")

    def set_transparent(self):
        self.settings.fill_color = ""
        self.color_view.config(bg="white", text="Transparent", fg="black")
        
    def sync_color(self):
        self.settings.fill_color = self.settings.color
        self.color_view.config(bg=self.settings.color)
