# Simple Drawing Pad

import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Simple Drawing Pad")

# Track current tools and sizes using a dictionary
settings = {"color": "black",
            "size": 5,
            "prev_x": None,
            "prev_y": None}


# Functions for tools
def choose_color():
    color = colorchooser.askcolor(title="Select Brush Color")[1]
    if color:
        settings["color"] = color


def use_eraser():
    settings["color"] = "white"


def change_size(val):
    settings["size"] = int(val)


def clear_canvas():
    canvas.delete("all")


# Drawing functions
def start_draw(event):
    settings["prev_x"] = event.x
    settings["prev_y"] = event.y


def draw(event):
    if settings["prev_x"] and settings["prev_y"]:
        # Draw smooth lines instead of disconnected dots
        canvas.create_line(settings["prev_x"], settings["prev_y"], event.x, event.y,
                           fill=settings["color"], width=settings["size"],
                           capstyle=tk.ROUND, smooth=tk.TRUE)
    settings["prev_x"] = event.x
    settings["prev_y"] = event.y


def reset_draw(event):
    settings["prev_x"] = None
    settings["prev_y"] = None


# Toolbar layout
toolbar = tk.Frame(root)
toolbar.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

# Control items
color_btn = tk.Button(toolbar, text="Brush Color", command=choose_color)
color_btn.pack(side=tk.LEFT, padx=5)

eraser_btn = tk.Button(toolbar, text="Eraser", command=use_eraser)
eraser_btn.pack(side=tk.LEFT, padx=5)

clear_btn = tk.Button(toolbar, text="Clear All", command=clear_canvas)
clear_btn.pack(side=tk.LEFT, padx=5)

size_label = tk.Label(toolbar, text=" Size:")
size_label.pack(side=tk.LEFT)

size_slider = tk.Scale(toolbar, from_=1, to=20, orient=tk.HORIZONTAL, command=change_size)
size_slider.set(settings["size"])
size_slider.pack(side=tk.LEFT, padx=5)

# Canvas setup
canvas = tk.Canvas(root, bg="white", width=600, height=450)
canvas.pack(fill=tk.BOTH, expand=True)

# Event bindings
canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset_draw)

root.mainloop()
