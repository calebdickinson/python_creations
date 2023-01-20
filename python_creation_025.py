"""
Attempt at Code for pressing a button on _window1 that will open _window2.
_window2 has a button that will open _window3, and vice versa.
"""
import tkinter as tk


class SampleApp(tk.Tk):
    """
    0
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("516x516")
        self.title("CHOOSE YOUR OWN ADVENTURE")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Page1, Page2, Page3, Page4, Page5, Page6):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame("Page1")

    def show_frame(self, page_name):
        """
        show_frame
        """
        frame = self.frames[page_name]
        frame.tkraise()


class Page1(tk.Frame):
    """
    1
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self, text="This is Page 1")
        label.pack(side="top", fill="x", pady=10)
        button2 = tk.Button(
            self, text="Go to Page 2",
            command=lambda: controller.show_frame("Page2")
        )
        button3 = tk.Button(
            self, text="Go to Page 3",
            command=lambda: controller.show_frame("Page3")
        )
        button4 = tk.Button(
            self, text="Go to Page 4",
            command=lambda: controller.show_frame("Page4")
        )
        button5 = tk.Button(
            self, text="Go to Page 5",
            command=lambda: controller.show_frame("Page5")
        )
        button6 = tk.Button(
            self, text="Go to Page 6",
            command=lambda: controller.show_frame("Page6")
        )
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()


class Page2(tk.Frame):
    """
    2
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self, text="This is page 2")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(
            self, text="Go Back",
            command=lambda: controller.show_frame("Page1")
        )
        button.pack()


class Page3(tk.Frame):
    """
    3
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(
            self, text="Go Back",
            command=lambda: controller.show_frame("Page1")
        )
        button.pack()


class Page4(tk.Frame):
    """
    4
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 4")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(
            self, text="Go Back",
            command=lambda: controller.show_frame("Page1")
        )
        button.pack()


class Page5(tk.Frame):
    """
    5
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 5")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(
            self, text="Go Back",
            command=lambda: controller.show_frame("Page1")
        )
        button.pack()


class Page6(tk.Frame):
    """
    6
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 6")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(
            self, text="Go Back",
            command=lambda: controller.show_frame("Page1")
        )
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
