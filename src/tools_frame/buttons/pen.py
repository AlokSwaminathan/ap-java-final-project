import tkinter as tk

class PenButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.canvas = canvas
        # Set the button text and bind the set_pen method
        self.config(text="Pen", command=self.set_pen)
        
        # Initialize pen size
        self.pen_size = self.canvas.pen_size if hasattr(self.canvas, 'pen_size') else 5

    def set_pen(self):
        """Set the canvas to pen drawing mode."""
        # Bind the drawing events to the pen drawing methods
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset_last_position)

    def draw(self, event):
        """Draw a circle (or square) at the current cursor position."""
        x, y = event.x, event.y
        radius = self.pen_size / 2
    
        # Draw a filled circle centered at the current cursor position
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=self.canvas.pen_color, outline=self.canvas.pen_color)

        # Update the last drawing position
        self.canvas.lastx, self.canvas.lasty = x, y

    def reset_last_position(self, event):
        """Reset the last drawing position."""
        self.canvas.lastx, self.canvas.lasty = None, None
