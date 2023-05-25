import customtkinter as ctk
from PIL import Image
import os

class EngineImageAndInfo(ctk.CTkFrame):     # Class for displaying basic engine info
    def __init__(self,master):
        super().__init__(master)

        # Engine image and info frame configuration
        self.image_info_frame = ctk.CTkFrame(master)
        self.image_info_frame.grid(sticky="nsew", pady=(0, 10))
        self.image_info_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.image_info_frame.grid_rowconfigure((0, 1, 2), weight=1)

        # Label
        self.image_info_label = ctk.CTkLabel(self.image_info_frame, text="SELECT ENGINE RANGE AND SERIES")
        self.image_info_label.grid(row=1, column=1, padx=20, pady=(0, 10), sticky="nsew")

        self.range_label = ctk.CTkLabel(self.image_info_frame, text="**** RANGE")
        self.series_label = ctk.CTkLabel(self.image_info_frame, text="SERIES: ****")

        mtu_file = os.path.abspath("mtu_img.png")
        perkins_file = os.path.abspath("perkins_img.png")
        scania_file = os.path.abspath("scania_img.png")

        self.mtu_image = ctk.CTkImage(Image.open(mtu_file), size=(513*0.43, 370*0.43))
        self.perkins_image = ctk.CTkImage(Image.open(perkins_file), size=(256*0.6, 265*0.6))
        self.scania_image = ctk.CTkImage(Image.open(scania_file), size=(1189*0.174, 913*0.174))

    def set_image(self, engine_range, engine_series):
        #self.image_info_frame.configure(fg_color="gray90")
        
        if engine_range == "MTU":
            self.image_info_label.configure(text="", image=self.mtu_image)
            self.range_label.configure(text="ENGINE RANGE: MTU")
        if engine_range == "Perkins":
            self.image_info_label.configure(text="", image=self.perkins_image)
            self.range_label.configure(text="ENGINE RANGE: PERKINS")
        if engine_range == "Scania":
            self.image_info_label.configure(text="", image=self.scania_image)
            self.range_label.configure(text="ENGINE RANGE: SCANIA")
        self.series_label.configure(text=f"ENGINE SERIES: {engine_series}")

        self.image_info_label.grid(row=2, column=0)
        self.range_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="nsew")
        self.series_label.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
