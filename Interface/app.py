import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Engine Signal Simulation Interface")
        self.geometry(f"{1100}x{580}")