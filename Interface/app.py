# App class, main interface, calls other classes into 3 grids

import customtkinter as ctk
import os

# Import all classes called in App
from engine_selector import EngineSelector
from signals import MainSignals, SecondarySignals
from logo_frame import LogoFrame
from start_stop import StartStop
from engine_info import EngineImageAndInfo


class App(ctk.CTk):                         
    def __init__(self, appearance_mode):
        super().__init__()

        # App window configuration
        self.title("Engine Signal Simulation Interface")
        self.geometry(f"{1300}x{600}")
        self.resizable(0, 0)
        # App column weights
        self.columnconfigure((0), weight=1)
        self.columnconfigure((1, 2), weight=3)
        self.rowconfigure(0, weight=1)
        # Interface appearance configuration
        ctk.set_appearance_mode(appearance_mode)
        ctk.set_default_color_theme(os.path.abspath("generac_theme.json"))

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
        self.engine_selector_frame = EngineSelector(self.left_grid, self)
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

    def set_signal_switches(self, main_switch_states, switch_states):
        self.main_signals_frame.set_switches(main_switch_states)
        self.secondary_signals_frame.set_switches(switch_states)




