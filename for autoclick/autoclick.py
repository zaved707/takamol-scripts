import tkinter as tk
import pyautogui
import ctypes

class DraggablePoint:
    def __init__(self, canvas, x, y, color, key):
        self.canvas = canvas
        self.key = key
        self.oval = canvas.create_oval(x-10, y-10, x+10, y+10, fill=color, outline="")
        self.text = canvas.create_text(x, y, text=key, fill="white")
        self.offset_x = 0
        self.offset_y = 0
        self.dragging = False

        canvas.tag_bind(self.oval, "<Button-1>", self.start_drag)
        canvas.tag_bind(self.oval, "<B1-Motion>", self.drag)
        canvas.tag_bind(self.oval, "<ButtonRelease-1>", self.stop_drag)

    def start_drag(self, event):
        self.dragging = True
        self.offset_x = event.x - self.canvas.coords(self.oval)[0]
        self.offset_y = event.y - self.canvas.coords(self.oval)[1]

    def drag(self, event):
        if self.dragging:
            new_x = event.x - self.offset_x
            new_y = event.y - self.offset_y
            self.canvas.coords(self.oval, new_x, new_y, new_x + 20, new_y + 20)
            self.canvas.coords(self.text, new_x + 10, new_y + 10)

    def stop_drag(self, event):
        self.dragging = False

    def get_center(self):
        coords = self.canvas.coords(self.oval)
        return int((coords[0] + coords[2]) / 2), int((coords[1] + coords[3]) / 2)

def on_key_press(event):
    for point in points:
        if event.char == point.key:
            x, y = point.get_center()
            pyautogui.click(x, y + 10)

# Enable transparent background on Windows
def make_window_transparent(window):
    window.attributes("-transparentcolor", "lightgray")
    if ctypes.windll.shcore:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    window.wm_attributes("-topmost", True)

# Create main window
root = tk.Tk()
root.title("Draggable Points")
root.geometry("800x600")

# Set window style for transparency
root.overrideredirect(True)  # Remove window decorations
root.wm_attributes("-transparent", True)  # Make the background transparent
root.config(bg="lightgray")  # Set the transparent color key
make_window_transparent(root)

# Create a canvas for points
canvas = tk.Canvas(root, width=800, height=600, bg="lightgray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Create draggable points
points = [
    DraggablePoint(canvas, 200, 300, "red", "a"),
    DraggablePoint(canvas, 400, 300, "blue", "b")
]

# Bind key press event
root.bind("<KeyPress>", on_key_press)

# Run the application
root.mainloop()
