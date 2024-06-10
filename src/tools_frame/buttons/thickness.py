import tkinter as tk
from settings_store import SettingsStore


class ThicknessButton(tk.Scale):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.master = master
        self.canvas = canvas
        self.settings = SettingsStore()

        # Set the slider properties
        self.config(from_=1, to=100,
                    orient=tk.HORIZONTAL, label="Thickness(px)")
        self.set(self.settings.brush_size)
        self.bind("<Motion>", self.adjust_thickness)

    def adjust_thickness(self, event):
        self.settings.brush_size = self.get()

    def release(self):
        pass
