import customtkinter as ctk
from PIL import Image
import os

class LogoFrame(ctk.CTkFrame):              # Logo frame class
    def __init__(self, master, appearance_mode):
        super().__init__(master)

        if appearance_mode == "Dark":
            logo_file = os.path.abspath("generac_logo_dark.png")
        else:
            logo_file = os.path.abspath("generac_logo_light.png")

        # Logo frame configuration
        self.logo_frame = ctk.CTkFrame(master)
        self.logo_frame.grid(sticky="nsew", pady=(0, 10))
        self.logo_frame.columnconfigure(0, weight=1)
        self.logo_frame.rowconfigure(0, weight=1)

        # Logo, comment first line for dark theme, second line for light theme
        #self.logo_image = ctk.CTkImage(Image.open(os.path.abspath("generac_logo_light.png")), size=(200, 45))
        self.logo_image = ctk.CTkImage(Image.open(logo_file), size=(200, 45))
        self.logo_label = ctk.CTkLabel(self.logo_frame, image=self.logo_image, text="")
        self.logo_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

