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
      self.settings = default_settings
    else:
      with open(self.settings_file,'r') as file:
        self.settings = json.load(file)

  def get_setting(self, key):
    return self.settings.get(key)

  def set_setting(self, key, value):
    self.settings[key] = value

  def save_settings(self):
    # Save settings to JSON file
    with open('settings.json', 'w') as file:
      json.dump(self.settings, file)