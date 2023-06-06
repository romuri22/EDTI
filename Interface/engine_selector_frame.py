import customtkinter as ctk


class EngineSelectorFrame(ctk.CTkFrame):         # Engine selector class with 2 menus
    def __init__(self, master, app):
        super().__init__(master)

        self.app = app
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
        self.engine_series_menu = ctk.CTkOptionMenu(self.engine_selector_frame, command=self.select_engine_model)
        self.engine_series_menu.grid(column=0, row=2, padx=10, pady=5)

        # Set default values
        self.engine_series_menu.configure(state="disabled")
        self.engine_series_menu.set("Engine Series")
        self.switch_states = [0 for _ in range(9)]

    def select_engine_range(self, value):   # Function called by engine_range_menu with an engine range
        self.engine_range = value
        self.engine_series_menu.set("Engine Series")
        if value == "MTU":
            self.engine_series_menu.configure(state="enabled", values=["ADEC", "MDEC", "ECU8"])
        elif value == "Perkins":
            self.engine_series_menu.configure(state="enabled", values=["1300", "ADEM3", "ADEM4"])
        elif value == "Scania":
            self.engine_series_menu.configure(state="enabled", values=["S6"])
        else:
            self.engine_series_menu.configure(state="disabled", values=["Engine Series"])

    def select_engine_model(self, value):   # Function called by engine_range_menu with an engine range
        self.main_switch_states = [1, 1, 1, 1]
        engine_series = value
        if value == "ADEC":
            self.switch_states = [1, 0, 1, 1, 1, 1]
        elif value == "MDEC":
            self.switch_states = [1, 0, 1, 1, 1, 1]
        elif value == "ECU8":
            self.switch_states = [0, 1, 0, 0, 1, 0]
        elif value == "1300":
            self.switch_states = [1, 0, 0, 0, 1, 0]
        elif value == "ADEM3":
            self.switch_states = [0, 0, 1, 1, 1, 0]
        elif value == "ADEM4":
            self.switch_states = [0, 0, 1, 1, 1, 0]
        elif value == "S6":
            self.switch_states = [1, 0, 1, 0, 1, 0]
        else:
            self.main_switch_states = [0, 0, 0, 0]
            
        self.app.set_engine(self.main_switch_states, self.switch_states, self.engine_range, engine_series)

