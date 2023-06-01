import customtkinter as ctk
from PIL import Image
import os

class EngineInfoFrame(ctk.CTkFrame):     # Class for displaying basic engine info
    def __init__(self,master):
        super().__init__(master)

        # Engine image and info frame configuration
        self.engine_info_frame = ctk.CTkFrame(master)
        self.engine_info_frame.grid(sticky="nsew", pady=(0, 10))
        self.engine_info_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.engine_info_frame.grid_rowconfigure((0, 1, 2), weight=1)

        # Label
        self.engine_info_label = ctk.CTkLabel(self.engine_info_frame, text="SELECT ENGINE RANGE AND SERIES")
        self.engine_info_label.grid(row=1, column=1, padx=20, pady=(0, 10), sticky="nsew")

        self.range_label = ctk.CTkLabel(self.engine_info_frame)
        self.range_image = ctk.CTkLabel(self.engine_info_frame)
        self.series_label = ctk.CTkLabel(self.engine_info_frame)
        self.series_image = ctk.CTkLabel(self.engine_info_frame)

        mtu_file = os.path.abspath("mtu_img.png")
        perkins_file = os.path.abspath("perkins_img.png")
        scania_file = os.path.abspath("scania_img.png")

        self.mtu_image = ctk.CTkImage(Image.open(mtu_file), size=(513*0.43, 370*0.43))
        self.perkins_image = ctk.CTkImage(Image.open(perkins_file), size=(256*0.6, 265*0.6))
        self.scania_image = ctk.CTkImage(Image.open(scania_file), size=(1189*0.174, 913*0.174))

    def set_engine(self, engine_range, engine_series):
        #self.image_info_frame.configure(fg_color="gray90")
        
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
        self.range_image.grid(row=2, column=0)
        self.range_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="nsew")
        self.series_label.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
