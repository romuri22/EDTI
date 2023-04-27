import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # App window configuration
        self.title("Engine Signal Simulation Interface")
        self.geometry(f"{1100}x{580}")
        #self.resizable(0.1,0.1)
        # App column weights
        self.columnconfigure((0, 1), weight=1)
        self.columnconfigure(2, weight=3)
        self.rowconfigure(0, weight=1)

        #------------------------------------------------------------------------------
        # Left grid with logo, engine selector, start/stop
        self.left_grid = ctk.CTkFrame(self)
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
        # Center grid with main variables, engine image and info
        self.center_grid = CenterGrid(self)
        self.center_grid.grid(column=1, row=0, sticky="nsew", padx=10, pady=20)


        #------------------------------------------------------------------------------
        # Right grid with secondary variables
        self.right_grid = RightGrid(self)
        self.right_grid.grid(column=2, row=0, sticky="nsew", padx=(10, 20), pady=20)
    
class LogoFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        # Logo frame configuration
        self.logo_frame = ctk.CTkFrame(master)
        self.logo_frame.grid(sticky="nsew", pady=(0, 10))
        self.logo_frame.columnconfigure(0, weight=1)
        self.logo_frame.rowconfigure(0, weight=1)

        # Label temporal hasta tener el logo
        self.logo_label = ctk.CTkLabel(self.logo_frame, text="Generac Logo")
        self.logo_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

class EngineSelector(ctk.CTkFrame):
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
        # Specific engine menu
        self.engine_menu = ctk.CTkOptionMenu(self.engine_selector_frame, values=["Engine", "1", "2", "3"])
        self.engine_menu.grid(column=0, row=2, padx=10, pady=5)

        # Set default values
        self.engine_menu.configure(state="disabled")

    def select_engine_range(self, value):
        if value == "MTU":
            self.engine_menu.configure(state="enabled", values=["Engine", "ADEC", "MDEC", "ECU8"])
        elif value == "Perkins":
            self.engine_menu.configure(state="enabled", values=["Engine", "1300", "ADEM3", "ADEM4"])
        elif value == "Scania":
            self.engine_menu.configure(state="enabled", values=["Engine", "S6"])
        else:
            self.engine_menu.configure(state="disabled", values=["Engine"])

class StartStop(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        # Start/stop frame configuration
        self.start_stop_frame = ctk.CTkFrame(master)
        self.start_stop_frame.grid(sticky="nsew", pady=10)
        self.start_stop_frame.grid_columnconfigure(0, weight=1)
        self.start_stop_frame.grid_rowconfigure((0, 2), weight=1)
        # Start/stop label
        self.start_stop_label = ctk.CTkLabel(self.start_stop_frame, text="Start/Stop")
        self.start_stop_label.grid(column=0, row=0, padx=10, pady=5)
        # Start and stop buttons
        self.start_button = ctk.CTkButton(self.start_stop_frame, text="Start Communication")
        self.start_button.grid(column=0, row=1, padx=10, pady=5)
        self.stop_button = ctk.CTkButton(self.start_stop_frame, text="Stop Communication")
        self.stop_button.grid(column=0, row=2, padx=10, pady=5)

class CenterGrid(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        # configure window
        self.left_grid = ctk.CTkFrame(master)


        self.marca = ctk.CTkLabel(self, text="Engine Range")
        self.marca.place()

class RightGrid(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        # configure window
        self.left_grid = ctk.CTkFrame(master)


        self.marca = ctk.CTkLabel(self, text="Engine Range")
        self.marca.place()