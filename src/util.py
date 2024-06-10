from tkinter.font import Font
import os


# Gets folder for program files
def get_program_folder():
    if os.name == 'posix':  # Unix-based systems (Linux, macOS)

        path_str = os.path.expanduser("~/Documents/Programs/PyDraw")

    elif os.name == 'nt':  # Windows
        path_str = os.path.expanduser("~\\Documents\\Programs\\PyDraw")
    else:
        return None  # Unsupported operating system

    if not os.path.exists(path_str):
        os.makedirs(path_str)
    return path_str


special_id = 0


def get_special_id():
    global special_id
    special_id += 1
    return special_id


def bold(button, bold=True):
    current_font = Font(button, button.cget("font"))
    current_font.config(weight="bold" if bold else "normal")
    button.config(font=current_font)
