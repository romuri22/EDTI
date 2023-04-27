import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Engine Signal Simulation Interface")
        self.geometry(f"{1100}x{580}")
        self.resizable(0.1,0.1)

        self.columnconfigure((0, 1), weight=1)
        self.columnconfigure(2, weight=3)
        self.rowconfigure(0, weight=1)


        self.left_grid = LeftGrid(self)
        self.left_grid.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

        self.center_grid = LeftGrid(self)
        self.center_grid.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)

        self.right_grid = LeftGrid(self)
        self.right_grid.grid(column=2, row=0, sticky="nsew", padx=5, pady=5)
    
import customtkinter as ctk

class LeftGrid(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        # configure window
        self.left_grid = ctk.CTkFrame(master=master)


        self.marca = ctk.CTkLabel(self, text="Engine Range")
        self.marca.place()