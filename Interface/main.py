import customtkinter as ctk
import tkinter as tk

from app import App

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")
# Theme para version final
#ctk.set_default_color_theme("/Users/rodrigomurillo/Documents/Python/EDTI/generac_theme.json")

if __name__ == "__main__":
    app = App()
    app.mainloop()  