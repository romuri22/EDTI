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
        self.engine_range_menu = ctk.CTkOptionMenu(self.engine_selector_frame, values=["Engine Range", "MTU", "Perkins", "Scania"], command=self.select_engine_range)
        self.engine_range_menu.grid(column=0, row=1, padx=10, pady=5)
        # Engine model menu
        self.engine_model_menu = ctk.CTkOptionMenu(self.engine_selector_frame, values=["Engine Model", "1", "2", "3"])
        self.engine_model_menu.grid(column=0, row=2, padx=10, pady=5)

        # Set default values
        self.engine_model_menu.configure(state="disabled")

    def select_engine_range(self, value):   # Function called by engine_range_menu with an engine range
        if value == "MTU":
            self.engine_model_menu.configure(state="enabled", values=["Engine Model", "ADEC", "MDEC", "ECU8"])
        elif value == "Perkins":
            self.engine_model_menu.configure(state="enabled", values=["Engine Model", "1300", "ADEM3", "ADEM4"])
        elif value == "Scania":
            self.engine_model_menu.configure(state="enabled", values=["Engine Model", "S6"])
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

        """ self.main_values = np.array([0, 0, 0, 0]) """

        # Main signals frame configuration
        self.main_signals_frame = ctk.CTkFrame(master)
        self.main_signals_frame.grid(sticky="nsew", pady=(10, 0))
        self.main_signals_frame.grid_columnconfigure((2), weight=3)
        self.main_signals_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Main signals frame title label
        self.main_signals_label = ctk.CTkLabel(self.main_signals_frame, text="MAIN SIGNALS")
        self.main_signals_label.grid(row=0, column=0, columnspan=5, padx=(10, 5), pady=5, sticky="nsew")
        

        # For loop
        self.main_values = [ctk.DoubleVar() for _ in range(4)]

        # Matrix used in setup with data for each main signal
        self.main_signals_setup = [
            {"text": "Engine Speed", "row": 1, "initial": 0, "final": 100, "steps": 100},
            {"text": "Oil Pressure", "row": 2, "initial": 0, "final": 100, "steps": 100},
            {"text": "Coolant Temp", "row": 3, "initial": 0, "final": 100, "steps": 100},
            {"text": "Engine Hours", "row": 4, "initial": 0, "final": 100, "steps": 100},
        ]

        # For loop to create switch, initial and final value labels, slider, and textbox for each signal
        for signal_data in self.main_signals_setup:
            # Signal switch with label
            switch = ctk.CTkSwitch(master=self.main_signals_frame, text=signal_data["text"])
            switch.grid(row=signal_data["row"], column=0, padx=(10, 5), pady=(5, 10), sticky="nsw")
            setattr(self, f"{signal_data['text'].lower().replace(' ', '_')}_switch", switch)
            # Initial value label
            initial_label = ctk.CTkLabel(self.main_signals_frame, text=str(signal_data["initial"]))
            initial_label.grid(row=signal_data["row"], column=1, padx=(5, 0), pady=5, sticky="nsew")
            # Final value label
            final_label = ctk.CTkLabel(self.main_signals_frame, text=str(signal_data["final"]))
            final_label.grid(row=signal_data["row"], column=3, padx=(0, 5), pady=5, sticky="nsew")
            # Signal slider
            slider = ctk.CTkSlider(self.main_signals_frame, from_=signal_data["initial"], to=signal_data["final"], number_of_steps=signal_data["steps"], variable=self.main_values[signal_data["row"]-1], command=self.print_value)
            slider.grid(row=signal_data["row"], column=2, padx=2, pady=5, sticky="ew")
            # Signal textbox entry
            entry = ctk.CTkEntry(master=self.main_signals_frame, width=50, textvariable=self.main_values[signal_data["row"]-1])
            entry.grid(row=signal_data["row"], column=4, padx=(0,10), pady=5)
            # Default values
            switch.select()
            slider.set(signal_data["initial"])

        # Main Signal label/ switch
        """ self.engine_speed_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Engine Speed")
        self.engine_speed_switch.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="nsw")
        self.oil_pressure_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Oil Pressure")
        self.oil_pressure_switch.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="nsw")
        self.coolant_temperature_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Coolant Temp")
        self.coolant_temperature_switch.grid(row=3, column=0, padx=(10, 5), pady=5, sticky="nsw")
        self.engine_hours_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Engine Hours")
        self.engine_hours_switch.grid(row=4, column=0, padx=(10, 5), pady=(5, 10), sticky="nsw") """

        # Main signal initial number labels
        """ self.engine_speed_initial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.engine_speed_initial.grid(row=1, column=1, padx=(5, 0), pady=5, sticky="nsew")
        self.oil_pressure_initial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.oil_pressure_initial.grid(row=2, column=1, padx=(5, 0), pady=5, sticky="nsew")
        self.coolant_temperature_initial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.coolant_temperature_initial.grid(row=3, column=1, padx=(5, 0), pady=5, sticky="nsew")
        self.engine_hours_initial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.engine_hours_initial.grid(row=4, column=1, padx=(5, 0), pady=5, sticky="nsew") """

        # Main signals sliders
        """ self.engine_speed_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=100, number_of_steps=100, variable=self.main_vars[0], command=self.print_value)
        self.engine_speed_slider.grid(row=1, column=2, padx=2, pady=5, sticky="ew")
        self.oil_pressure_slider = ctk.CTkSlider(self.main_signals_frame, from_=5, to=400, number_of_steps=200, variable=self.main_vars[1], command=self.print_value)
        self.oil_pressure_slider.grid(row=2, column=2, padx=2, pady=5, sticky="ew")
        self.coolant_temperature_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=300, number_of_steps=100, variable=self.main_vars[2], command=self.print_value)
        self.coolant_temperature_slider.grid(row=3, column=2, padx=2, pady=5, sticky="ew")
        self.engine_hours_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=100, number_of_steps=300, variable=self.main_vars[3], command=self.print_value)
        self.engine_hours_slider.grid(row=4, column=2, padx=2, pady=5, sticky="ew") """

        # Main signal final number labels
        """ self.engine_speed_final = ctk.CTkLabel(self.main_signals_frame, text="1000")
        self.engine_speed_final.grid(row=1, column=3, padx=(0, 5), pady=5, sticky="nsew")
        self.oil_pressure_final = ctk.CTkLabel(self.main_signals_frame, text="80")
        self.oil_pressure_final.grid(row=2, column=3, padx=(0, 5), pady=5, sticky="nsew")
        self.coolant_temperature_final = ctk.CTkLabel(self.main_signals_frame, text="50")
        self.coolant_temperature_final.grid(row=3, column=3, padx=(0, 5), pady=5, sticky="nsew")
        self.engine_hours_final = ctk.CTkLabel(self.main_signals_frame, text="500")
        self.engine_hours_final.grid(row=4, column=3, padx=(0, 5), pady=5, sticky="nsew") """

        # create main entries
        """ self.engine_speed_entry = ctk.CTkEntry(master=self.main_signals_frame, width=50, textvariable=self.main_vars[0])
        self.engine_speed_entry.grid(row=1, column=4, padx=(0,10), pady=5)
        self.oil_pressure_entry = ctk.CTkEntry(master=self.main_signals_frame, width=50, textvariable=self.main_vars[1])
        self.oil_pressure_entry.grid(row=2, column=4, padx=(0,10), pady=5)
        self.coolant_temperature_entry = ctk.CTkEntry(master=self.main_signals_frame, width=50, textvariable=self.main_vars[2])
        self.coolant_temperature_entry.grid(row=3, column=4, padx=(0,10), pady=5)
        self.engine_hours_entry = ctk.CTkEntry(master=self.main_signals_frame, width=50, textvariable=self.main_vars[3])
        self.engine_hours_entry.grid(row=4, column=4, padx=(0,10), pady=5) """

        # Main signal initial states
        """ self.engine_speed_switch.select()
        self.oil_pressure_switch.select()
        self.coolant_temperature_switch.select()
        self.engine_hours_switch.select() """
        """ self.engine_speed_slider.set(0)
        self.oil_pressure_slider.set(0)
        self.coolant_temperature_slider.set(0)
        self.engine_hours_slider.set(0) """
    
    def print_value(self, value):
        #self.main_vars[0].set(value)
        val_list = []
        for i in range(4):
            val = self.main_values[i].get()
            val_list.append(val)
        print(val_list)



class SecondarySignals(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        # Secondary signals frame configuration
        self.main_signals_frame = ctk.CTkFrame(master)
        self.main_signals_frame.grid(sticky="nsew")
        self.main_signals_frame.grid_columnconfigure((2), weight=3)
        self.main_signals_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

        # Secondary signals label
        self.main_signals_label = ctk.CTkLabel(self.main_signals_frame, text="SECONDARY SIGNALS")
        self.main_signals_label.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

        # Secondary signals switches
        self.oil_temperature_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Oil Temperature")
        self.oil_temperature_switch.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="nsw")
        self.inlet_temperature_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Inlet Temperature")
        self.inlet_temperature_switch.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="nsw")
        self.fuel_temperature_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Fuel Temperature")
        self.fuel_temperature_switch.grid(row=3, column=0, padx=(10, 5), pady=5, sticky="nsw")
        self.turbo_pressure_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Turbo Pressure")
        self.turbo_pressure_switch.grid(row=4, column=0, padx=(10, 5), pady=5, sticky="nsw")
        self.fuel_pressure_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Fuel Pressure")
        self.fuel_pressure_switch.grid(row=5, column=0, padx=(10, 5), pady=5, sticky="nsw")
        self.fuel_consumption_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Fuel Consumption")
        self.fuel_consumption_switch.grid(row=6, column=0, padx=(10, 5), pady=5, sticky="nsw")
        self.fuel_used_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Fuel Used")
        self.fuel_used_switch.grid(row=7, column=0, padx=(10, 5), pady=5, sticky="nsw")
        self.dm1_amber_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="DM1 Amber")
        self.dm1_amber_switch.grid(row=8, column=0, padx=(10, 5), pady=5, sticky="nsw")
        self.dm1_red_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="DM1 Red")
        self.dm1_red_switch.grid(row=9, column=0, padx=(10, 5), pady=(5, 10), sticky="nsw")

        # Secondary signal initial number labels
        self.oil_temperature_initial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.oil_temperature_initial.grid(row=1, column=1, padx=(5, 0), pady=5)
        self.inlet_temperature_initial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.inlet_temperature_initial.grid(row=2, column=1, padx=(5, 0), pady=5)
        self.fuel_temperature_initial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.fuel_temperature_initial.grid(row=3, column=1, padx=(5, 0), pady=5)
        self.turbo_pressure_initial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.turbo_pressure_initial.grid(row=4, column=1, padx=(5, 0), pady=5)
        self.fuel_pressure_initial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.fuel_pressure_initial.grid(row=5, column=1, padx=(5, 0), pady=5)
        self.fuel_consumption_initial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.fuel_consumption_initial.grid(row=6, column=1, padx=(5, 0), pady=5)
        self.fuel_used_initial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.fuel_used_initial.grid(row=7, column=1, padx=(5, 0), pady=5)
        self.dm1_amber_initial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.dm1_amber_initial.grid(row=8, column=1, padx=(5, 0), pady=5)
        self.dm1_red_initial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.dm1_red_initial.grid(row=9, column=1, padx=(5, 0), pady=5)

        # Secondary signals sliders
        self.oil_temperature_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=1)
        self.oil_temperature_slider.grid(row=1, column=2, padx=2, pady=5, sticky="ew")
        self.inlet_temperature_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=1)
        self.inlet_temperature_slider.grid(row=2, column=2, padx=2, pady=5, sticky="ew")
        self.fuel_temperature_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=1)
        self.fuel_temperature_slider.grid(row=3, column=2, padx=2, pady=5, sticky="ew")
        self.turbo_pressure_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=1)
        self.turbo_pressure_slider.grid(row=4, column=2, padx=2, pady=5, sticky="ew")
        self.fuel_pressure_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=1)
        self.fuel_pressure_slider.grid(row=5, column=2, padx=2, pady=5, sticky="ew")
        self.fuel_consumption_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=1)
        self.fuel_consumption_slider.grid(row=6, column=2, padx=2, pady=5, sticky="ew")
        self.fuel_used_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=1)
        self.fuel_used_slider.grid(row=7, column=2, padx=2, pady=5, sticky="ew")
        self.dm1_amber_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=1)
        self.dm1_amber_slider.grid(row=8, column=2, padx=2, pady=5, sticky="ew")
        self.dm1_red_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=1)
        self.dm1_red_slider.grid(row=9, column=2, padx=2, pady=5, sticky="ew")


        # Secondary signal final number labels
        self.oil_temperature_final = ctk.CTkLabel(self.main_signals_frame, text="80")
        self.oil_temperature_final.grid(row=1, column=3, padx=(0, 5), pady=5)
        self.coolant_pressure_final = ctk.CTkLabel(self.main_signals_frame, text="50")
        self.coolant_pressure_final.grid(row=2, column=3, padx=(0, 5), pady=5)

        # create secondary entries
        self.oil_temperature_entry = ctk.CTkEntry(master=self.main_signals_frame, placeholder_text="kPa", width=40)
        self.oil_temperature_entry.grid(row=1, column=4, padx=(0, 10), pady=5)
        self.coolant_pressure_entry = ctk.CTkEntry(master=self.main_signals_frame, placeholder_text="°C", width=40)
        self.coolant_pressure_entry.grid(row=2, column=4, padx=(0, 10), pady=5)

        # Secondary signal initial states
        self.oil_temperature_switch.select()
        #self.coolant_pressure_switch.select()
        self.oil_temperature_slider.set(0)