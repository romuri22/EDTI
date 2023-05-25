import customtkinter as ctk


class MainSignals(ctk.CTkFrame):            # Class with main signals sliders, puts values into a list
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
            {"text": "Engine Speed", "row": 1, "initial": 0, "final": 2000, "steps": 16000, "unit": "rpm"},
            {"text": "Oil Pressure", "row": 2, "initial": 0, "final": 1020, "steps": 255, "unit": "kPa"},
            {"text": "Coolant Temp", "row": 3, "initial": -40, "final": 215, "steps": 255, "unit": "ºC"},
            {"text": "Engine Hours", "row": 4, "initial": 0, "final": 10000, "steps": 200000, "unit": "hr"},
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
            # Unit label
            self.unit_label = ctk.CTkLabel(self.main_signals_frame, text=signal_data["unit"])
            self.unit_label.grid(row=signal_row, column=5, padx=(0, 10), pady=5, sticky="nsew")
            # Signal slider
            self.slider = ctk.CTkSlider(self.main_signals_frame, from_=signal_data["initial"], to=signal_data["final"], number_of_steps=signal_data["steps"], variable=self.main_values[i], command=self.print_values)
            self.slider.grid(row=signal_row, column=2, padx=2, pady=5, sticky="ew")
            self.main_sliders.append(self.slider)
            # Signal textbox entry
            self.entry = ctk.CTkEntry(master=self.main_signals_frame, width=46, textvariable=self.main_values[i])
            self.entry.grid(row=signal_row, column=4, padx=(0,5), pady=5)
            self.main_entries.append(self.entry)
            # Default values
            self.slider.set(signal_data["initial"])
            self.main_sliders[i].configure(state="disabled", button_color="gray")
            self.main_entries[i].configure(state="disabled")
    
    def print_values(self, value):
        val_list = []
        for i in range(4):
            val = self.main_values[i].get()
            val_list.append(round(val, 2))
        print(val_list)

    def switch_command(self, signal):
        if self.main_switches[signal].get() == 0:
            self.main_sliders[signal].configure(state="disabled", button_color="gray")
            self.main_entries[signal].configure(state="disabled")
        else:
            self.main_sliders[signal].configure(state="normal", button_color="#bf6d3a")
            self.main_entries[signal].configure(state="normal")
        self.main_sliders[signal].set(self.main_signals_setup[signal]["initial"])

    def create_switch_command(self, i):
        return lambda: self.switch_command(i)
    
    def set_switches(self, switch_states):
        i = 0
        for state in switch_states:
            if state == 0:
                self.main_switches[i].deselect()
            else:
                self.main_switches[i].select()
            self.switch_command(i)
            i += 1

    def get_main_values(self):
        val_list = []
        for i in range(4):
            val = self.main_values[i].get()
            val_list.append(round(val, 2))
        return val_list


class SecondarySignals(ctk.CTkFrame):       # Similar to MainSignals, can turn certain sliders on/off
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
            {"text": "Oil Temp", "row": 1, "initial": -273, "final": 1500, "steps": 56736, "unit": "ºC"},
            {"text": "Inlet Temp", "row": 2, "initial": -40, "final": 215, "steps": 255, "unit": "ºC"},
            {"text": "Fuel Temp", "row": 3, "initial": -40, "final": 215, "steps": 255, "unit": "ºC"},
            {"text": "Turbo Pressure", "row": 4, "initial": 0, "final": 1020, "steps": 255, "unit": "kPa"},
            {"text": "Fuel Pressure", "row": 5, "initial": 0, "final": 1020, "steps": 255, "unit": "kPa"},
            {"text": "Fuel Rate", "row": 6, "initial": 0, "final": 3000, "steps": 60000, "unit": "L/h"},
            {"text": "Fuel Used", "row": 7, "initial": 0, "final": 1000, "steps": 20000, "unit": "L"},
            {"text": "DM1 Amber", "row": 8, "initial": 0, "final": 1, "steps": 1, "unit": ""},
            {"text": "DM1 Red", "row": 9, "initial": 0, "final": 1, "steps": 1, "unit": ""},
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
            # Unit label
            self.unit_label = ctk.CTkLabel(self.secondary_signals_frame, text=signal_data["unit"])
            self.unit_label.grid(row=signal_row, column=5, padx=(0, 10), pady=5, sticky="nsew")
            # Signal slider
            self.slider = ctk.CTkSlider(self.secondary_signals_frame, from_=signal_data["initial"], to=signal_data["final"], number_of_steps=signal_data["steps"], variable=self.secondary_values[i], command=self.print_values)
            self.slider.grid(row=signal_row, column=2, padx=2, pady=5, sticky="ew")
            self.secondary_sliders.append(self.slider)
            # Signal textbox entry
            self.entry = ctk.CTkEntry(master=self.secondary_signals_frame, width=46, textvariable=self.secondary_values[i])
            self.entry.grid(row=signal_row, column=4, padx=(0,5), pady=5)
            self.secondary_entries.append(self.entry)
            # Default values
            self.slider.set(signal_data["initial"])
            self.secondary_sliders[i].configure(state="disabled", button_color="gray")
            self.secondary_entries[i].configure(state="disabled")
        
    def print_values(self, value):
        val_list = []
        for i in range(9):
            val = self.secondary_values[i].get()
            val_list.append(round(val, 2))
        print(val_list)

    def switch_command(self, signal):
        if self.secondary_switches[signal].get() == 0:
            self.secondary_sliders[signal].configure(state="disabled", button_color="gray")
            self.secondary_entries[signal].configure(state="disabled")
        else:
            self.secondary_sliders[signal].configure(state="normal", button_color="#bf6d3a")
            self.secondary_entries[signal].configure(state="normal")
        self.secondary_sliders[signal].set(self.secondary_signals_setup[signal]["initial"])

    def create_switch_command(self, i):
        return lambda: self.switch_command(i)

    def set_switches(self, switch_states):
        i = 0
        for state in switch_states:
            if state == 0:
                self.secondary_switches[i].deselect()
                self.secondary_switches[i].configure(state="disabled")
            else:
                self.secondary_switches[i].configure(state="enabled")
                self.secondary_switches[i].select()
            self.switch_command(i)
            i += 1

    def get_secondary_values(self):
        val_list = []
        for i in range(9):
            val = self.secondary_values[i].get()
            val_list.append(round(val, 2))
        return val_list
