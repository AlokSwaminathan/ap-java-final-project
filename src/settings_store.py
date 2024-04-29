import json
import os
from util import get_program_folder
from default_settings import default_settings
import tkinter as tk
from tkinter import colorchooser


class SettingsStore:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SettingsStore, cls).__new__(cls)
            cls._instance.settings_file = os.path.join(
                get_program_folder(), "settings.json")
            cls._instance._load_settings()
        return cls._instance

    def _load_settings(self):
        # Load settings from JSON file
        if not os.path.exists(self.settings_file):
            self._default_settings = default_settings
        else:
            with open(self.settings_file, 'r') as file:
                self._default_settings = json.load(file)
        self._current_settings = self._default_settings.copy()

    def get_default(self, key):
        return self._default_settings.get(key)

    def set_default(self, key, value):
        self._default_settings[key] = value

    def get_current(self, key):
        return self._current_settings.get(key)

    def set_current(self, key, value):
        self._current_settings[key] = value

    def save_settings(self):
        # Save settings to JSON file
        if not os.path.exists(get_program_folder()):
            os.makedirs(get_program_folder())
        with open(self.settings_file, 'w') as file:
            json.dump(self._default_settings, file, indent=2)
        print(f"Settings saved to {self.settings_file}")

    def choose_color(self):
        """Open a color picker dialog and set the chosen color as the drawing color."""
        # Open a color picker dialog
        color_code = colorchooser.askcolor()[1]
        # If a color is chosen
        if color_code:
            self.settings.set_current("color", color_code)
            self.settings.set_default("color", color_code)
            self.canvas.pen_color = color_code
