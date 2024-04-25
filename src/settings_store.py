import json

class SettingsStore:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(SettingsStore, cls).__new__(cls)
      cls._instance._load_settings()
    return cls._instance

  def _load_settings(self):
    # Load settings from JSON file
    with open('settings.json', 'r') as file:
      self.settings = json.load(file)

  def get_setting(self, key):
    return self.settings.get(key)

  def set_setting(self, key, value):
    self.settings[key] = value

  def save_settings(self):
    # Save settings to JSON file
    with open('settings.json', 'w') as file:
      json.dump(self.settings, file)