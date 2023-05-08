import customtkinter as ctk


class EngineImageAndInfo(ctk.CTkFrame):     # Class for displaying basic engine info
    def __init__(self,master):
        super().__init__(master)

        # Engine image and info frame configuration
        self.image_info_frame = ctk.CTkFrame(master)
        self.image_info_frame.grid(sticky="nsew", pady=(0, 10))
        self.image_info_frame.grid_columnconfigure(0, weight=1)
        self.image_info_frame.grid_rowconfigure((0), weight=1)

        # Label
        self.image_info_label = ctk.CTkLabel(self.image_info_frame, text="Engine Image and Info")
        self.image_info_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


