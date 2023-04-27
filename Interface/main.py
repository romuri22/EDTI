import customtkinter as ctk
import tkinter as tk

from app import App

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("/Users/rodrigomurillo/Documents/Python/Generac/generac_orange.json")


if __name__ == "__main__":
    app = App()
    app.mainloop()  