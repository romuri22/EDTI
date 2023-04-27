import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Engine Signal Simulation Interface")
        self.geometry(f"{1100}x{580}")



        self.marca = ctk.CTkLabel(self, text="Engine Range")
        self.marca.place(relx=0.02, rely=0.02)

