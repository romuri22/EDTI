import customtkinter as ctk


class EngineSelector(ctk.CTkFrame):         # Engine selector class with 2 menus
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
        self.engine_model_menu = ctk.CTkOptionMenu(self.engine_selector_frame, values=["Engine Model", "1", "2", "3"], command=self.select_engine_model)
        self.engine_model_menu.grid(column=0, row=2, padx=10, pady=5)

        # Set default values
        self.engine_model_menu.configure(state="disabled")
        self.engine_model_menu.set("Engine Model")
        self.switch_states = [0 for _ in range(9)]

    def select_engine_range(self, value):   # Function called by engine_range_menu with an engine range
        self.engine_range = value
        self.engine_model_menu.set("Engine Model")
        if value == "MTU":
            self.engine_model_menu.configure(state="enabled", values=["ADEC", "MDEC", "ECU8"])
        elif value == "Perkins":
            self.engine_model_menu.configure(state="enabled", values=["1300", "ADEM3", "ADEM4"])
        elif value == "Scania":
            self.engine_model_menu.configure(state="enabled", values=["S6"])
        else:
            self.engine_model_menu.configure(state="disabled", values=["Engine Model"])

    def select_engine_model(self, value):   # Function called by engine_range_menu with an engine range
        self.main_switch_states = [1, 1, 1, 1]
        engine_series = value
        if value == "ADEC":
            self.switch_states = [1, 1, 1, 1, 1, 0, 0, 1, 1]
        elif value == "MDEC":
            self.switch_states = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        elif value == "ECU8":
            self.switch_states = [0, 0, 0, 1, 0, 0, 0, 1, 1]
        elif value == "1300":
            self.switch_states = [1, 0, 0, 1, 0, 0, 0, 1, 1]
        elif value == "ADEM3":
            self.switch_states = [0, 1, 1, 1, 0, 1, 0, 1, 1]
        elif value == "ADEM4":
            self.switch_states = [0, 1, 1, 1, 0, 1, 1, 1, 1]
        elif value == "S6":
            self.switch_states = [1, 1, 0, 1, 0, 1, 0, 1, 1]
        else:
            self.main_switch_states = [0, 0, 0, 0]
            
        self.app.set_signal_switches(self.main_switch_states, self.switch_states, self.engine_range, engine_series)

