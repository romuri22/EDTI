# engine_info_frame.py
# -------------------------------------------------------------------

# Engine Digital Twin Interface.
# Written by Rodrigo Murillo Tapia, Alejandro Martinez Licon and Alejandro Gaviria Ramirez.
# 2023

# Shows basic info and an image of the selected engine range and series.

import customtkinter as ctk     # GUI library
from PIL import Image           # To open image files
import os                       # For finding image file paths

class EngineInfoFrame(ctk.CTkFrame):     # Class for displaying basic engine info
    def __init__(self,master):
        super().__init__(master)

        # Engine image and info frame configuration
        self.engine_info_frame = ctk.CTkFrame(master)
        self.engine_info_frame.grid(sticky="nsew", pady=(0, 10))
        self.engine_info_frame.grid_columnconfigure(0, weight=1)
        self.engine_info_frame.grid_rowconfigure((0, 1, 2), weight=1)

        # Label
        self.engine_info_label = ctk.CTkLabel(self.engine_info_frame, text="SELECT ENGINE RANGE AND SERIES")
        self.engine_info_label.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="nsew")

        self.range_label = ctk.CTkLabel(self.engine_info_frame)
        self.range_image = ctk.CTkLabel(self.engine_info_frame)
        self.series_label = ctk.CTkLabel(self.engine_info_frame)

        mtu_file = os.path.abspath("mtu_img.png")
        perkins_file = os.path.abspath("perkins_img.png")
        scania_file = os.path.abspath("scania_img.png")

        self.mtu_image = ctk.CTkImage(Image.open(mtu_file), size=(513*0.43, 370*0.43))
        self.perkins_image = ctk.CTkImage(Image.open(perkins_file), size=(256*0.6, 265*0.6))
        self.scania_image = ctk.CTkImage(Image.open(scania_file), size=(1189*0.174, 913*0.174))

    # Function that sets info and image to the selected engine
    def set_engine(self, engine_range, engine_series):
        if engine_range == "MTU":
            self.range_image.configure(text="", image=self.mtu_image)
            self.range_label.configure(text="ENGINE RANGE: MTU")
        if engine_range == "Perkins":
            self.range_image.configure(text="", image=self.perkins_image)
            self.range_label.configure(text="ENGINE RANGE: PERKINS")
        if engine_range == "Scania":
            self.range_image.configure(text="", image=self.scania_image)
            self.range_label.configure(text="ENGINE RANGE: SCANIA")
        self.series_label.configure(text=f"ENGINE SERIES: {engine_series}")

        self.engine_info_label.grid_remove()
        self.range_label.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="nsew")
        self.range_image.grid(row=1, column=0)
        self.series_label.grid(row=2, column=0, padx=20, pady=(5, 20), sticky="nsew")
