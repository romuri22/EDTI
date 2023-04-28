import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk


class App(ctk.CTk):     # App class, main interface, calls other classes into 3 grids
    def __init__(self):
        super().__init__()

        # App window configuration
        self.title("Engine Signal Simulation Interface")
        self.geometry(f"{1100}x{580}")
        #self.resizable(0.1,0.1)
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
        # Label temporal, cambiar por codigo de abajo en version final
        self.logo_label = ctk.CTkLabel(self.logo_frame, text="Generac Logo")
        self.logo_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        # Codigo para poner el logo en version final
        #self.logo_image = ctk.CTkImage(Image.open("/Users/rodrigomurillo/Documents/Python/EDTI/generac_logo.png"), size=(200, 50))
        #self.logo_image.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        #self.logo_label = ctk.CTkLabel(self.logo_frame, image=self.logo_image, text="")
        #self.logo_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")


class EngineSelector(ctk.CTkFrame):         # Engine selector class with 2 menus
    def __init__(self,master):
        super().__init__(master)

        # Engine selector frame configuration
        self.engine_selector_frame = ctk.CTkFrame(master)
        self.engine_selector_frame.grid(sticky="nsew", pady=10)
        self.engine_selector_frame.columnconfigure(0, weight=1)
        self.engine_selector_frame.rowconfigure((0, 2), weight=1)

        # Engine selector label
        self.engine_selector_label = ctk.CTkLabel(self.engine_selector_frame, text="Engine Selector")
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


class MainSignals(ctkA.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        # Main signals frame configuration
        self.main_signals_frame = ctk.CTkFrame(master)
        self.main_signals_frame.grid(sticky="nsew", pady=(10, 0))
        self.main_signals_frame.grid_columnconfigure((2), weight=3)
        self.main_signals_frame.grid_rowconfigure((1, 2, 3, 4), weight=1)
        
        # Main Signal label/ switch
        self.main_signals_label = ctk.CTkLabel(self.main_signals_frame, text="MAIN SIGNALS")
        self.main_signals_label.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")
        self.engine_speed_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Engine Speed")
        self.engine_speed_switch.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.oil_pressure_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Oil Pressure")
        self.oil_pressure_switch.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.coolant_temperature_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Coolant Temp")
        self.coolant_temperature_switch.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.engine_hours_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Engine Hours")
        self.engine_hours_switch.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        # Main signal initial number labels
        self.engine_speed_inicial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.engine_speed_inicial.grid(row=1, column=1, padx=(5, 0), pady=5)
        self.oil_pressure_inicial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.oil_pressure_inicial.grid(row=2, column=1, padx=(5, 0), pady=5)
        self.coolant_temperature_inicial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.coolant_temperature_inicial.grid(row=3, column=1, padx=(5, 0), pady=5)
        self.engine_hours_inicial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.engine_hours_inicial.grid(row=4, column=1, padx=(5, 0), pady=5)

        # Main signals sliders
        self.engine_speed_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=1)
        self.engine_speed_slider.grid(row=1, column=2, padx=2, pady=5, sticky="ew")
        self.oil_pressure_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=1)
        self.oil_pressure_slider.grid(row=2, column=2, padx=2, pady=5, sticky="ew")
        self.coolant_temperature_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=1)
        self.coolant_temperature_slider.grid(row=3, column=2, padx=2, pady=5, sticky="ew")
        self.engine_hours_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=1)
        self.engine_hours_slider.grid(row=4, column=2, padx=2, pady=5, sticky="ew")

        # Main signal final number labels
        self.engine_speed_final = ctk.CTkLabel(self.main_signals_frame, text="1000")
        self.engine_speed_final.grid(row=1, column=3, padx=(0, 5), pady=5)
        self.oil_pressure_final = ctk.CTkLabel(self.main_signals_frame, text="80")
        self.oil_pressure_final.grid(row=2, column=3, padx=(0, 5), pady=5)
        self.coolant_temperature_final = ctk.CTkLabel(self.main_signals_frame, text="50")
        self.coolant_temperature_final.grid(row=3, column=3, padx=(0, 5), pady=5)
        self.engine_hours_final = ctk.CTkLabel(self.main_signals_frame, text="500")
        self.engine_hours_final.grid(row=4, column=3, padx=(0, 5), pady=5)

        # create main entries
        self.engine_speed_entry = ctk.CTkEntry(master=self.main_signals_frame, placeholder_text="RPM", width=40)
        self.engine_speed_entry.grid(row=1, column=4, padx=(0,5), pady=5)
        self.oil_pressure_entry = ctk.CTkEntry(master=self.main_signals_frame, placeholder_text="kPa", width=40)
        self.oil_pressure_entry.grid(row=2, column=4, padx=(0,5), pady=5)
        self.coolant_temperature_entry = ctk.CTkEntry(master=self.main_signals_frame, placeholder_text="°C", width=40)
        self.coolant_temperature_entry.grid(row=3, column=4, padx=(0,5), pady=5)
        self.engine_hours_entry = ctk.CTkEntry(master=self.main_signals_frame, placeholder_text="hrs", width=40)
        self.engine_hours_entry.grid(row=4, column=4, padx=(0,5), pady=5)

        # Main signal initial states
        self.engine_speed_switch.select()
        self.oil_pressure_switch.select()
        self.coolant_temperature_switch.select()
        self.engine_hours_switch.select()
        self.engine_speed_slider.set(0)
        self.oil_pressure_slider.set(0)
        self.coolant_temperature_slider.set(0)
        self.engine_hours_slider.set(0)

        # Set slider values with textbox

        # Set textbox values with slider


class SecondarySignals(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        # Secondary signals frame configuration
        self.main_signals_frame = ctk.CTkFrame(master)
        self.main_signals_frame.grid(sticky="nsew", pady=(10, 0))
        self.main_signals_frame.grid_columnconfigure((2), weight=3)
        self.main_signals_frame.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

        # Secondary Signal label/ switch
        self.main_signals_label = ctk.CTkLabel(self.main_signals_frame, text="SECONDARY SIGNALS")
        self.main_signals_label.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")
        self.oil_temperature_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Oil Temperature")
        self.oil_temperature_switch.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.coolant_pressure_switch = ctk.CTkSwitch(master=self.main_signals_frame, text="Coolant Pressure")
        self.coolant_pressure_switch.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        # Secondary signal initial number labels
        self.oil_temperature_inicial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.oil_temperature_inicial.grid(row=1, column=1, padx=(5, 0), pady=5)
        self.coolant_pressure_inicial = ctk.CTkLabel(self.main_signals_frame, text="0")
        self.coolant_pressure_inicial.grid(row=2, column=1, padx=(5, 0), pady=5)

        # Secondary signals sliders
        self.oil_temperature_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=1)
        self.oil_temperature_slider.grid(row=1, column=2, padx=2, pady=5, sticky="ew")
        self.coolant_pressure_slider = ctk.CTkSlider(self.main_signals_frame, from_=0, to=1)
        self.coolant_pressure_slider.grid(row=2, column=2, padx=2, pady=5, sticky="ew")

        # Secondary signal final number labels
        self.oil_temperature_final = ctk.CTkLabel(self.main_signals_frame, text="80")
        self.oil_temperature_final.grid(row=1, column=3, padx=(0, 5), pady=5)
        self.coolant_pressure_final = ctk.CTkLabel(self.main_signals_frame, text="50")
        self.coolant_pressure_final.grid(row=2, column=3, padx=(0, 5), pady=5)

        # create secondary entries
        self.oil_temperature_entry = ctk.CTkEntry(master=self.main_signals_frame, placeholder_text="kPa", width=40)
        self.oil_temperature_entry.grid(row=1, column=4, padx=(0,5), pady=5)
        self.coolant_pressure_entry = ctk.CTkEntry(master=self.main_signals_frame, placeholder_text="°C", width=40)
        self.coolant_pressure_entry.grid(row=2, column=4, padx=(0,5), pady=5)

        # Secondary signal initial states
        self.oil_temperature_switch.select()
        self.coolant_pressure_switch.select()
        self.oil_temperature_slider.set(0)
        self.coolant_pressure_slider.set(0)