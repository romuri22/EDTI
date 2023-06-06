# signal_frames.py
# -------------------------------------------------------------------

# Engine Digital Twin Interface.
# Written by Rodrigo Murillo Tapia, Alejandro Martinez Licon and Alejandro Gaviria Ramirez.
# 2023

# A signal frame parent class, that creates sliders and entries that control variables.
# Two derived classes with information on the main and secondary signals.

import customtkinter as ctk     # GUI library

class SignalFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        
        # Lists to store switches, sliders and entries for each frame
        self.switches = []
        self.sliders = []
        self.entries = []

    # Function to create switch, initial and final value labels, slider, and entry for each signal
    def create_sliders(self):
        for i, signal_data in enumerate(self.signals_setup):
            signal_row = i + 1
            # Signal switch with label
            self.switch = ctk.CTkSwitch(master=self.signals_frame, text=signal_data["text"], command=self.create_switch_command(i))
            self.switch.grid(row=signal_row, column=0, padx=(10, 5), pady=(5, 10), sticky="nsw")
            self.switches.append(self.switch)
            # Initial value label
            self.initial_label = ctk.CTkLabel(self.signals_frame, text=str(signal_data["initial"]))
            self.initial_label.grid(row=signal_row, column=1, padx=(5, 0), pady=5, sticky="nsew")
            # Final value label
            self.final_label = ctk.CTkLabel(self.signals_frame, text=str(signal_data["final"]))
            self.final_label.grid(row=signal_row, column=3, padx=(0, 5), pady=5, sticky="nsew")
            # Unit label
            self.unit_label = ctk.CTkLabel(self.signals_frame, text=signal_data["unit"])
            self.unit_label.grid(row=signal_row, column=5, padx=(0, 10), pady=5, sticky="nsew")
            # Signal slider
            self.slider = ctk.CTkSlider(self.signals_frame, from_=signal_data["initial"], to=signal_data["final"], number_of_steps=signal_data["steps"], variable=self.values[i], command=self.print_values)
            self.slider.grid(row=signal_row, column=2, padx=2, pady=5, sticky="ew")
            self.sliders.append(self.slider)
            # Signal textbox entry
            self.entry = ctk.CTkEntry(master=self.signals_frame, width=46, textvariable=self.values[i])
            self.entry.grid(row=signal_row, column=4, padx=(0,5), pady=5)
            self.entries.append(self.entry)
            # Default values
            self.slider.set(signal_data["initial"])
            self.sliders[i].configure(state="disabled", button_color="gray")
            self.entries[i].configure(state="disabled")

    # Prints values each time a slider is used (for debugging purposes)
    def print_values(self, value):
        val_list = []
        for i in range(self.number_of_signals):
            val = self.values[i].get()
            val_list.append(round(val, 2))
        print(val_list)

    # Command called whith each switch, disables/enables sliders and entries
    def switch_command(self, signal):
        if self.switches[signal].get() == 0:
            self.sliders[signal].configure(state="disabled", button_color="gray")
            self.entries[signal].configure(state="disabled")
        else:
            self.sliders[signal].configure(state="normal", button_color="#bf6d3a")
            self.entries[signal].configure(state="normal")
        self.sliders[signal].set(self.signals_setup[signal]["initial"])

    # Lambda function to avoid i conflicts when defining the command for each switch
    def create_switch_command(self, i):
        return lambda: self.switch_command(i)
    
    # Function called by app when an engine is selected
    def set_switches(self, switch_states):
        for i, state in enumerate(switch_states):
            if state == 0:
                self.switches[i].deselect()
            else:
                self.switches[i].select()
            self.switch_command(i)

    # Function called by app and start/stop to update all values to send
    def get_values(self):
        val_list = []
        for i in range(self.number_of_signals):
            val = self.values[i].get()
            val_list.append(round(val, 2))
        for constant in self.constants:
            val_list.append(constant)
        return val_list

class MainSignalsFrame(SignalFrame):            # Class with main signals sliders, puts values into a list
    def __init__(self,master):
        super().__init__(master)

        # Signals inside main frame
        self.number_of_signals = 4
        # This frame has no constant signals
        self.constants = []

        # Main signals frame configuration
        self.signals_frame = ctk.CTkFrame(master)
        self.signals_frame.grid(sticky="nsew", pady=(10, 0))
        self.signals_frame.grid_columnconfigure((2), weight=3)
        self.signals_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Main signals frame title label
        self.main_signals_label = ctk.CTkLabel(self.signals_frame, text="MAIN SIGNALS")
        self.main_signals_label.grid(row=0, column=0, columnspan=5, padx=(10, 5), pady=5, sticky="nsew")
        
        # List that stores main signal values
        self.values = [ctk.DoubleVar() for _ in range(self.number_of_signals)]

        # Matrix used in setup with data for each main signal
        self.signals_setup = [
            {"text": "Engine Speed", "initial": 0, "final": 2000, "steps": 16000, "unit": "rpm"},
            {"text": "Oil Pressure", "initial": 0, "final": 1020, "steps": 255, "unit": "kPa"},
            {"text": "Coolant Temp", "initial": -40, "final": 215, "steps": 255, "unit": "ºC"},
            {"text": "Engine Hours", "initial": 0, "final": 10000, "steps": 200000, "unit": "hr"},
        ]
        # Creates main sliders
        self.create_sliders()

class SecondarySignalsFrame(SignalFrame):       # Similar to MainSignals, sends 2 constants
    def __init__(self,master):
        super().__init__(master)

        #Signals inside secondary frame
        self.number_of_signals = 6
        # This frame sends 2 constant signals
        self.ATMOS_PRESSURE = 101.325
        self.RATED_SPEED = 1800
        self.constants = [self.ATMOS_PRESSURE, self.RATED_SPEED]

        # Secondary signals frame configuration
        self.signals_frame = ctk.CTkFrame(master)
        self.signals_frame.grid(sticky="nsew", pady=(10, 0))
        self.signals_frame.grid_columnconfigure((2), weight=3)
        self.signals_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        # Secondary signals label
        self.signals_label = ctk.CTkLabel(self.signals_frame, text="SECONDARY SIGNALS")
        self.signals_label.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

        # List that stores secondary signal values
        self.values = [ctk.DoubleVar() for _ in range(self.number_of_signals)]

        # Matrix used in setup with data for each main signal
        self.signals_setup = [
            {"text": "Oil Temp", "initial": -273, "final": 1500, "steps": 56736, "unit": "ºC"},
            {"text": "Coolant Pressure", "initial": 0, "final": 500, "steps": 250, "unit": "kPa"},
            {"text": "Inlet Temp", "initial": -40, "final": 215, "steps": 255, "unit": "ºC"},
            {"text": "Fuel Temp", "initial": -40, "final": 215, "steps": 255, "unit": "ºC"},
            {"text": "Turbo Pressure", "initial": 0, "final": 1020, "steps": 255, "unit": "kPa"},
            {"text": "Fuel Pressure", "initial": 0, "final": 1020, "steps": 255, "unit": "kPa"},
        ]
        # Creates secondary sliders
        self.create_sliders()

