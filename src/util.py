import os


# Gets folder for program files
def get_program_folder():
    if os.name == 'posix':  # Unix-based systems (Linux, macOS)
        return os.path.expanduser("~/Documents/Programs/PyDraw")
    elif os.name == 'nt':  # Windows
        return os.path.expanduser("~\\Documents\\Programs\\PyDraw")
    else:
        return None  # Unsupported operating system
