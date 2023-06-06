# app.py
# -------------------------------------------------------------------

# Engine Digital Twin Interface.
# Written by Rodrigo Murillo Tapia, Alejandro Martinez Licon and Alejandro Gaviria Ramirez.
# 2023

# App class, main interface, calls other classes into 3 grids, 
# other classes handle engine selection, data, and communication.

import customtkinter as ctk     # GUI library
import os                       # For finding theme path

# Import all classes called in App, these frames are arrangend in the app
from engine_selector_frame import EngineSelectorFrame
from signal_frames import MainSignalsFrame, SecondarySignalsFrame
from logo_frame import LogoFrame
from start_stop_frame import StartStopFrame
from engine_info_frame import EngineInfoFrame
from channel_selector_frame import ChannelSelectorFrame

class App(ctk.CTk):                         
    def __init__(self, appearance_mode, window_size):
        super().__init__()

        # App window configuration
        self.title("Engine Digital Twin Interface")
        self.geometry(window_size)
        self.resizable(0, 0)
        # App column weights
        self.columnconfigure((0), weight=1)
        self.columnconfigure((1, 2), weight=3)
        self.rowconfigure(0, weight=1)
        # Sets theme file
        if os.name == 'posix':  # macOS / Linux
            theme_file = os.path.abspath("Graphics/generac_theme.json")
        elif os.name == 'nt':   # Windows
            theme_file = os.path.abspath("Graphics\generac_theme.json")
        # Interface appearance configuration
        ctk.set_default_color_theme(theme_file)
        ctk.set_appearance_mode(appearance_mode)

        #------------------------------------------------------------------------------
        # Left grid with logo, engine selector, start/stop
        self.left_grid = ctk.CTkFrame(self, fg_color="transparent")
        self.left_grid.grid(column=0, row=0, sticky="nsew", padx=(20, 10), pady=20)
        # Left grid weights
        self.left_grid.columnconfigure(0, weight=1)
        self.left_grid.rowconfigure((0, 1, 2), weight=1)

        # Logo frame
        self.logo_frame = LogoFrame(self.left_grid, appearance_mode)
        self.logo_frame.grid(column=0, row=0, sticky="nsew", pady=(0, 10))
        # Engine selector frame
        self.engine_selector_frame = EngineSelectorFrame(self.left_grid, self)
        self.engine_selector_frame.grid(column=0, row=1, sticky="nsew", pady=10)
        # Start/stop frame
        self.start_stop_frame = StartStopFrame(self.left_grid, self)
        self.start_stop_frame.grid(column=0, row=2, sticky="nsew", pady=(10, 0))

        #------------------------------------------------------------------------------
        # Center grid with main signals, engine image and info
        self.center_grid = ctk.CTkFrame(self, fg_color="transparent")
        self.center_grid.grid(column=1, row=0, sticky="nsew", padx=10, pady=20)
        # Center grid weights
        self.center_grid.columnconfigure(0, weight=1)
        self.center_grid.rowconfigure((0, 1), weight=1)

        # Engine image and info frame
        self.image_info_frame = EngineInfoFrame(self.center_grid)
        self.image_info_frame.grid(column=0, row=0, sticky="nsew", pady=(0, 10))    
        # Main signals frame
        self.main_signals_frame = MainSignalsFrame(self.center_grid)
        self.main_signals_frame.grid(column=0, row=1, sticky="nsew", pady=(10, 0))

        #------------------------------------------------------------------------------
        # Right grid with secondary signals
        self.right_grid = ctk.CTkFrame(self, fg_color="transparent")
        self.right_grid.grid(column=2, row=0, sticky="nsew", padx=(10, 20), pady=20)
        # Right grid weights
        self.right_grid.columnconfigure(0, weight=1)
        self.right_grid.rowconfigure((0), weight=0)
        self.right_grid.rowconfigure((1), weight=2)

        # Secondary signals frame
        self.channel_selector_frame = ChannelSelectorFrame(self.right_grid, self)
        self.channel_selector_frame.grid(column=0, row=0, sticky="nsew", pady=(0, 10))
        self.secondary_signals_frame = SecondarySignalsFrame(self.right_grid)
        self.secondary_signals_frame.grid(column=0, row=1, sticky="nsew", pady=(10, 0))    

    # Function called by engine_selector_frame, sets signal switches and engine info for a given engine
    def set_engine(self, main_switch_states, switch_states, engine_range, engine_series):
        self.main_signals_frame.set_switches(main_switch_states)
        self.secondary_signals_frame.set_switches(switch_states)
        self.image_info_frame.set_engine(engine_range, engine_series)

    # Function called by start_stop_frame, gets values from signal frames, appends them together
    def get_values(self):
        values = self.main_signals_frame.get_values()
        secondary_values = self.secondary_signals_frame.get_values()
        for value in secondary_values:
            values.append(value)
        return values
    
    # Called by channel selector, calls start/stop frame to set the selected channel
    def set_channel(self, channel):
        self.start_stop_frame.set_channel(channel)
