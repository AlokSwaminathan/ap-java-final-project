import tkinter as tk


class ClearButton(tk.Button):
    def __init__(self, master=None, canvas=None):
        super().__init__(master)
        self.canvas = canvas
        # Set the button text and bind the clear function to the button
        self.config(text="Clear", command=self.clear)

    def clear(self):
        t = tk.Toplevel()
        t.title("Clear Canvas")
        t.geometry("200x100")

        def clear_canvas(clear):
            self.canvas.delete("all") if clear else None
            t.destroy()

        # Create a label asking for confirmation
        label = tk.Label(
            t, text="Are you sure you want\n to clear the canvas?")
        label.pack()

        # Create yes and no buttons
        yes_button = tk.Button(
            t, text="Yes", command=lambda: clear_canvas(True), width=8, height=2)
        yes_button.pack(side=tk.LEFT)

        no_button = tk.Button(
            t, text="No", command=lambda: clear_canvas(False), width=8, height=2)
        no_button.pack(side=tk.RIGHT)
