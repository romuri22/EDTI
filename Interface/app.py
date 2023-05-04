import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import os
import numpy as np


# Set interface appearance mode: "Dark", "Light"
appearance_mode = "Light"

# Interface appearance configuration
if appearance_mode == "Dark":
    logo_file = os.path.abspath("generac_logo_dark.png")
else:
    logo_file = os.path.abspath("generac_logo_light.png")
ctk.set_appearance_mode(appearance_mode)
ctk.set_default_color_theme(os.path.abspath("generac_theme.json"))


class App(ctk.CTk):     # App class, main interface, calls other frame classes into 3 grids
    def __init__(self):
        super().__init__()

        # App window configuration
        self.title("Engine Signal Simulation Interface")
        self.geometry(f"{1300}x{600}")
        self.resizable(0, 0)
        # App column weights
        self.columnconfigure((0), weight=1)
        self.columnconfigure((1, 2), weight=3)
        self.rowconfigure(0, weight=1)

        #------------------------------------------------------------------------------
        # Left grid with logo, engine selector, start/stop
        self.left_grid = ctk.CTkFrame(self, fg_color="transparent")
        self.left_grid.grid(column=0, row=0, sticky="nsew", padx=(20, 10), pady=20)
        # Left grid weights
        self.left_grid.columnconfigure(0, weight=1)
        self.left_grid.rowconfigure((0, 1, 2), weight=1)

        # Logo frame
        self.logo_frame = LogoFrame(self.left_grid)
        self.logo_frame.grid(column=0, row=0, sticky="nsew", pady=(0, 10))
        # Engine selector frame
        self.engine_selector_frame = EngineSelector(self.left_grid)
        self.engine_selector_frame.grid(column=0, row=1, sticky="nsew", pady=10)
        # Start/stop frame
        self.start_stop_frame = StartStop(self.left_grid)
        self.start_stop_frame.grid(column=0, row=2, sticky="nsew", pady=(10, 0))

        #------------------------------------------------------------------------------
        # Center grid with main signals, engine image and info
        self.center_grid = ctk.CTkFrame(self, fg_color="transparent")
        self.center_grid.grid(column=1, row=0, sticky="nsew", padx=10, pady=20)
        # Center grid weights
        self.center_grid.columnconfigure(0, weight=1)
        self.center_grid.rowconfigure((0, 1), weight=1)

        # Engine image and info frame
        self.image_info_frame = EngineImageAndInfo(self.center_grid)
        self.image_info_frame.grid(column=0, row=0, sticky="nsew", pady=(0, 10))    
        # Main signals frame
        self.main_signals_frame = MainSignals(self.center_grid)
        self.main_signals_frame.grid(column=0, row=1, sticky="nsew", pady=(10, 0))

        #------------------------------------------------------------------------------
        # Right grid with secondary signals
        self.right_grid = ctk.CTkFrame(self, fg_color="transparent")
        self.right_grid.grid(column=2, row=0, sticky="nsew", padx=(10, 20), pady=20)
        # Right grid weights
        self.right_grid.columnconfigure(0, weight=1)
        self.right_grid.rowconfigure(0, weight=1)

        # Secondary signals frame
        self.secondary_signals_frame = SecondarySignals(self.right_grid)
        self.secondary_signals_frame.grid(column=0, row=0, sticky="nsew", pady=(0))    


class LogoFrame(ctk.CTkFrame):              # Logo frame class
    def __init__(self,master):
        super().__init__(master)

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


class EngineSelector(ctk.CTkFrame):         # Engine selector class with 2 menus
    def __init__(self,master):
        super().__init__(master)

        # Engine selector frame configuration
        self.engine_selector_frame = ctk.CTkFrame(master)
        self.engine_selector_frame.grid(sticky="nsew", pady=10)
        self.engine_selector_frame.columnconfigure(0, weight=1)
        self.engine_selector_frame.rowconfigure((0, 2), weight=1)

        # Engine selector label
        self.engine_selector_label = ctk.CTkLabel(self.engine_selector_frame, text="ENGINE SELECTOR")
        self.engine_selector_label.grid(column=0, row=0, padx=10, pady=5)
        # Engine range menu
        self.engine_range_menu = ctk.CTkOptionMenu(self.engine_selector_frame, values=["MTU", "Perkins", "Scania"], command=self.select_engine_range)
        self.engine_range_menu.grid(column=0, row=1, padx=10, pady=5)
        self.engine_range_menu.set("Engine Range")
        # Engine model menu
        self.engine_model_menu = ctk.CTkOptionMenu(self.engine_selector_frame, values=["Engine Model", "1", "2", "3"])
        self.engine_model_menu.grid(column=0, row=2, padx=10, pady=5)

        # Set default values
        self.engine_model_menu.configure(state="disabled")
        self.engine_model_menu.set("Engine Model")

    def select_engine_range(self, value):   # Function called by engine_range_menu with an engine range
        if value == "MTU":
            self.engine_model_menu.configure(state="enabled", values=["ADEC", "MDEC", "ECU8"])
        elif value == "Perkins":
            self.engine_model_menu.configure(state="enabled", values=["1300", "ADEM3", "ADEM4"])
        elif value == "Scania":
            self.engine_model_menu.configure(state="enabled", values=["S6"])
        else:
            self.engine_model_menu.configure(state="disabled", values=["Engine Model"])


class StartStop(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        # Start/stop frame configuration
        self.start_stop_frame = ctk.CTkFrame(master)
        self.start_stop_frame.grid(sticky="nsew", pady=(10, 0))
        self.start_stop_frame.grid_columnconfigure(0, weight=1)
        self.start_stop_frame.grid_rowconfigure((0, 2), weight=1)
        # Start/stop label
        self.start_stop_label = ctk.CTkLabel(self.start_stop_frame, text="SEND CAN MESSAGE")
        self.start_stop_label.grid(column=0, row=0, padx=10, pady=5)
        # Start and stop buttons
        self.start_button = ctk.CTkButton(self.start_stop_frame, text="SEND", command=self.start_commnication)
        self.start_button.grid(column=0, row=1, padx=10, pady=5)
        self.stop_button = ctk.CTkButton(self.start_stop_frame, text="STOP", command=self.stop_commnication)
        self.stop_button.grid(column=0, row=2, padx=10, pady=5)

    def start_commnication(self):
        print("Communication Started")

    def stop_commnication(self):
        print("Communication Stopped")


class EngineImageAndInfo(ctk.CTkFrame):
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


class MainSignals(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        # Main signals frame configuration
        self.main_signals_frame = ctk.CTkFrame(master)
        self.main_signals_frame.grid(sticky="nsew", pady=(10, 0))
        self.main_signals_frame.grid_columnconfigure((2), weight=3)
        self.main_signals_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Main signals frame title label
        self.main_signals_label = ctk.CTkLabel(self.main_signals_frame, text="MAIN SIGNALS")
        self.main_signals_label.grid(row=0, column=0, columnspan=5, padx=(10, 5), pady=5, sticky="nsew")
        
        # List that stores main signal values
        self.main_values = [ctk.DoubleVar() for _ in range(4)]
        # Lists with main switches, sliders and entries
        self.main_switches = []
        self.main_sliders = []
        self.main_entries = []

        # Matrix used in setup with data for each main signal
        self.main_signals_setup = [
            {"text": "Engine Speed", "row": 1, "initial": 0, "final": 100, "steps": 100},
            {"text": "Oil Pressure", "row": 2, "initial": 0, "final": 100, "steps": 100},
            {"text": "Coolant Temp", "row": 3, "initial": 0, "final": 100, "steps": 100},
            {"text": "Engine Hours", "row": 4, "initial": 0, "final": 100, "steps": 100},
        ]

        # For loop to create switch, initial and final value labels, slider, and textbox for each signal
        for signal_data in self.main_signals_setup:
            signal_row = signal_data["row"]
            i = signal_row - 1
            # Signal switch with label
            self.switch = ctk.CTkSwitch(master=self.main_signals_frame, text=signal_data["text"], command=self.create_switch_command(i))
            self.switch.grid(row=signal_row, column=0, padx=(10, 5), pady=(5, 10), sticky="nsw")
            self.main_switches.append(self.switch)
            # Initial value label
            self.initial_label = ctk.CTkLabel(self.main_signals_frame, text=str(signal_data["initial"]))
            self.initial_label.grid(row=signal_row, column=1, padx=(5, 0), pady=5, sticky="nsew")
            # Final value label
            self.final_label = ctk.CTkLabel(self.main_signals_frame, text=str(signal_data["final"]))
            self.final_label.grid(row=signal_row, column=3, padx=(0, 5), pady=5, sticky="nsew")
            # Signal slider
            self.slider = ctk.CTkSlider(self.main_signals_frame, from_=signal_data["initial"], to=signal_data["final"], number_of_steps=signal_data["steps"], variable=self.main_values[i], command=self.print_values)
            self.slider.grid(row=signal_row, column=2, padx=2, pady=5, sticky="ew")
            self.main_sliders.append(self.slider)
            # Signal textbox entry
            self.entry = ctk.CTkEntry(master=self.main_signals_frame, width=50, textvariable=self.main_values[i])
            self.entry.grid(row=signal_row, column=4, padx=(0,10), pady=5)
            self.main_entries.append(self.entry)
            # Default values
            self.switch.select()
            self.slider.set(signal_data["initial"])
    
    def print_values(self, value):
        val_list = []
        for i in range(4):
            val = self.main_values[i].get()
            val_list.append(val)
        print(val_list)

    def switch_command(self, signal):
        print("Switch")
        if self.main_switches[signal].get() == 0:
            self.main_sliders[signal].configure(state="disabled")
            self.main_sliders[signal].set(0)
            self.main_entries[signal].configure(state="disabled")
        else:
            self.main_sliders[signal].configure(state="normal")
            self.main_entries[signal].configure(state="normal")
        self.print_values(0)

    def create_switch_command(self, i):
        return lambda: self.switch_command(i)


class SecondarySignals(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        # Secondary signals frame configuration
        self.secondary_signals_frame = ctk.CTkFrame(master)
        self.secondary_signals_frame.grid(sticky="nsew")
        self.secondary_signals_frame.grid_columnconfigure((2), weight=3)
        self.secondary_signals_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

        # Secondary signals label
        self.secondary_signals_label = ctk.CTkLabel(self.secondary_signals_frame, text="SECONDARY SIGNALS")
        self.secondary_signals_label.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

        # List that stores secondary signal values
        self.secondary_values = [ctk.DoubleVar() for _ in range(9)]
        # Lists with secondary switches, sliders and entries
        self.secondary_switches = []
        self.secondary_sliders = []
        self.secondary_entries = []

        # Matrix used in setup with data for each main signal
        self.secondary_signals_setup = [
            {"text": "Oil Temp", "row": 1, "initial": 0, "final": 100, "steps": 100},
            {"text": "Inlet Temp", "row": 2, "initial": 0, "final": 100, "steps": 100},
            {"text": "Fuel Temp", "row": 3, "initial": 0, "final": 100, "steps": 100},
            {"text": "Turbo Pressure", "row": 4, "initial": 0, "final": 100, "steps": 100},
            {"text": "Fuel Pressure", "row": 5, "initial": 0, "final": 100, "steps": 100},
            {"text": "Fuel Consumption", "row": 6, "initial": 0, "final": 100, "steps": 100},
            {"text": "Fuel Used", "row": 7, "initial": 0, "final": 100, "steps": 100},
            {"text": "DM1 Amber", "row": 8, "initial": 0, "final": 100, "steps": 100},
            {"text": "DM1 Red", "row": 9, "initial": 0, "final": 100, "steps": 100},
        ]

        # For loop to create switch, initial and final value labels, slider, and textbox for each signal
        for signal_data in self.secondary_signals_setup:
            signal_row = signal_data["row"]
            i = signal_row - 1
            # Signal switch with label
            self.switch = ctk.CTkSwitch(master=self.secondary_signals_frame, text=signal_data["text"], command=self.create_switch_command(i))
            self.switch.grid(row=signal_row, column=0, padx=(10, 5), pady=(5, 10), sticky="nsw")
            self.secondary_switches.append(self.switch)
            # Initial value label
            self.initial_label = ctk.CTkLabel(self.secondary_signals_frame, text=str(signal_data["initial"]))
            self.initial_label.grid(row=signal_row, column=1, padx=(5, 0), pady=5, sticky="nsew")
            # Final value label
            self.final_label = ctk.CTkLabel(self.secondary_signals_frame, text=str(signal_data["final"]))
            self.final_label.grid(row=signal_row, column=3, padx=(0, 5), pady=5, sticky="nsew")
            # Signal slider
            self.slider = ctk.CTkSlider(self.secondary_signals_frame, from_=signal_data["initial"], to=signal_data["final"], number_of_steps=signal_data["steps"], variable=self.secondary_values[i], command=self.print_values)
            self.slider.grid(row=signal_row, column=2, padx=2, pady=5, sticky="ew")
            self.secondary_sliders.append(self.slider)
            # Signal textbox entry
            self.entry = ctk.CTkEntry(master=self.secondary_signals_frame, width=50, textvariable=self.secondary_values[i])
            self.entry.grid(row=signal_row, column=4, padx=(0,10), pady=5)
            self.secondary_entries.append(self.entry)
            # Default values
            self.switch.select()
            self.slider.set(signal_data["initial"])

    def print_values(self, value):
        val_list = []
        for i in range(9):
            val = self.secondary_values[i].get()
            val_list.append(val)
        print(val_list)

    def switch_command(self, signal):
        print("Switch")
        if self.secondary_switches[signal].get() == 0:
            self.secondary_sliders[signal].configure(state="disabled")
            self.secondary_sliders[signal].set(0)
            self.secondary_entries[signal].configure(state="disabled")
        else:
            self.secondary_sliders[signal].configure(state="normal")
            self.secondary_entries[signal].configure(state="normal")
        self.print_values(0)

    def create_switch_command(self, i):
        return lambda: self.switch_command(i)

    def slider_event2(self, value, variable):
        self.values2[variable] = value
        val2 = self.values2[variable]
        print(self.values2)


