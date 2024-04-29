from util import get_program_folder
import os

default_settings = {
    "color": "black",
    "brush_size": 5,
    "canvas_width": 900,
    "canvas_height": 600,
    "save_path": "drawings/",
    "font": "Helvetica",
    "font_size": 32,
    "font_color": "black",
    "save_folder": os.path.join(get_program_folder(), "drawings/")
}
