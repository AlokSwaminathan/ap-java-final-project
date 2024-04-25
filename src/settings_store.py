import json
import os
from util import get_program_folder
from default_settings import default_settings

class SettingsStore:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(SettingsStore, cls).__new__(cls)
      cls._instance.settings_file = os.path.join(get_program_folder(),"settings.json")
      cls._instance._load_settings()
    return cls._instance

  def _load_settings(self):
    # Load settings from JSON file
    if not os.path.exists(self.settings_file):
      self.default_settings = default_settings
    else:
      with open(self.settings_file,'r') as file:
        self.default_settings = json.load(file)
    self.current_settings = self.default_settings.copy()

  def get_default(self, key):
    return self.default_settings.get(key)

  def set_default(self, key, value):
    self.default_settings[key] = value

  def get_current(self, key):
    return self.current_settings.get(key)

  def set_current(self, key, value):
    self.current_settings[key] = value

  def save_settings(self):
    # Save settings to JSON file
    if not os.path.exists(get_program_folder()):
      os.makedirs(get_program_folder())
    with open(self.settings_file, 'w') as file:
      json.dump(self.default_settings, file,indent=2)
    print(f"Settings saved to {self.settings_file}")