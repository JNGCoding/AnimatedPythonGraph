import tkinter as tk


class Window:
    def __init__(self, width, height, title) -> None:
        self.root = tk.Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title(title)
        self.root.config(background="lightGray")

    @staticmethod
    def add_button(width, height, label, x, y) -> tk.Button:
        wid = tk.Button(width=width, height=height, text=label, borderwidth=2, relief=tk.SOLID)
        wid.place(x=x, y=y)

        return wid

    @staticmethod
    def add_text(width, height, label, x, y) -> tk.Label:
        text = tk.Label(width=width, height=height, text=label, borderwidth=2, relief=tk.SOLID)
        text.place(x=x, y=y)

        return text

    @staticmethod
    def add_function(widget: tk.Button, Button, function):
        widget.bind(Button, function)
