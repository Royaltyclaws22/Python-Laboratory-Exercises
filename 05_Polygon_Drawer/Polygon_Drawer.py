import tkinter as tk
from tkinter import colorchooser


# Represents and draws a point on the canvas
class Point:

    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y

        # Draw a small white point
        canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="white")


# Stores polygon vertices and handles polygon drawing
class Polygon:

    def __init__(self, canvas, board, points=None):
        if points is None:
            points = []

        self.points = points
        self.canvas = canvas
        self.board = board

    # Add a new point and connect it to the previous one
    def add_point(self, point):

        self.points.append(point)

        if len(self.points) > 1:
            previous = self.points[-2]
            current = self.points[-1]

            self.canvas.create_line(
                previous.x,
                previous.y,
                current.x,
                current.y,
                fill="white",
                width=2,
            )

    # Draw the completed filled polygon
    def draw(self):

        coordinates = []

        for point in self.points:
            coordinates.extend([point.x, point.y])

        self.canvas.create_polygon(
            coordinates,
            fill=self.board.current_color,
            outline=self.board.current_color,
        )


# Creates the color palette
class Palette:

    def __init__(self, frame, board, colors):
        self.colors = colors
        self.board = board
        self.color_frames = []

        for color in colors:
            color_frame = tk.Frame(frame, bg="lightgrey", bd=3)
            color_frame.pack(expand=True, fill="both", side="left")

            if self.board.current_color == color:
                color_frame.config(bg="red")

            self.color_frames.append(color_frame)

            color_label = tk.Label(color_frame, bg=color)
            color_label.pack(expand=True, fill="both", padx=2, pady=2)

            # Left click: select color
            color_label.bind("<1>", self.set_color)

            # Right click: customize color
            color_label.bind("<3>", self.choose_custom_color)

    # Open the color picker and replace the selected palette color
    def choose_custom_color(self, event):

        result = colorchooser.askcolor(
            color=event.widget["bg"],
            title="Choose a Color",
        )

        if result[1]:
            event.widget["bg"] = result[1]
            self.board.current_color = result[1]
            self.highlight_selected(event.widget.master)

    # Set the current drawing color
    def set_color(self, event):

        self.board.current_color = event.widget["bg"]
        self.highlight_selected(event.widget.master)

    # Highlight the currently selected color
    def highlight_selected(self, selected_frame):

        for frame in self.color_frames:
            frame.config(bg="lightgrey")

        selected_frame.config(bg="red")


# Main application class
class Board:

    def __init__(self, root):
        self.colors = [
            "#B4FE98",
            "#77E4D4",
            "#F4EEA9",
            "#F0BB62",
            "#FF5F7E",
            "#9A0680",
        ]

        self.root = root
        self.current_color = self.colors[0]

        # Color palette frame
        self.palette_frame = tk.Frame(root)
        self.palette_frame.pack(expand=True, fill="both", padx=5)

        # Drawing canvas frame
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(expand=True, fill="both")

        self.canvas = tk.Canvas(
            self.canvas_frame,
            bg="#000D6B",
            height=550,
        )
        self.canvas.pack(expand=True, fill="both", padx=5, pady=5)

        self.palette = Palette(
            self.palette_frame,
            self,
            self.colors,
        )

        # Mouse bindings
        self.canvas.bind("<1>", self.add_point)
        self.canvas.bind("<Double-1>", self.finish_polygon)

        self.polygon = None

    # Add a new polygon vertex
    def add_point(self, event):

        point = Point(self.canvas, event.x, event.y)

        if self.polygon is None:
            self.polygon = Polygon(self.canvas, self, [point])
        else:
            self.polygon.add_point(point)

    # Complete and draw the polygon
    def finish_polygon(self, event):

        if self.polygon and len(self.polygon.points) > 2:
            self.polygon.add_point(Point(self.canvas, event.x, event.y))
            self.polygon.draw()
            self.polygon = None
        else:
            self.add_point(event)


# Main Program
root = tk.Tk()
root.title("Polygon Drawer")
root.geometry("600x700+700+50")
root.resizable(False, False)
Board(root)
tk.mainloop()
