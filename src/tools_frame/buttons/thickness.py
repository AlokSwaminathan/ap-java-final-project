import tkinter as tk
from settings_store import SettingsStore

class ThicknessButton(tk.Frame):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.canvas = canvas
        self.settings = SettingsStore()
        
        # Create a button for setting thickness
        self.button = tk.Button(self, text="Thickness", command=self.set_thickness)
        self.button.grid(row=1, column=0, sticky="ew")
        
        # Create a slider for adjusting thickness
        self.slider = tk.Scale(self, from_=1, to=100, orient=tk.HORIZONTAL)
        self.slider.grid_forget()  # Hide the slider initially

    def set_thickness(self):
        """Set the canvas to thickness adjustment mode."""
        # Show the slider when the thickness button is clicked
        self.slider.grid(row=2, column=0, sticky="ew")
        
        # Bind the slider to adjust the thickness
        self.slider.bind("<Motion>", self.adjust_thickness)
        self.slider.bind("<ButtonRelease-1>", self.finalize_thickness)

    def adjust_thickness(self, event):
        """Adjust the pen thickness based on the slider value."""
        # Get the slider value
        pen_thickness = self.slider.get()
        
        # Update the canvas pen size
        self.canvas.pen_size = pen_thickness

    def finalize_thickness(self, event):
        """Finalize the thickness adjustment and hide the slider."""
        # Hide the slider when the adjustment is finalized
        self.slider.grid_forget()
