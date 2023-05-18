import customtkinter as ctk
from data_converter import DataConverterJ1939

class StartStop(ctk.CTkFrame):              # Start/stop class with 2 buttons
    def __init__(self,master, app):
        super().__init__(master)
        self.app = app

        # Start/stop frame configuration
        self.start_stop_frame = ctk.CTkFrame(master)
        self.start_stop_frame.grid(sticky="nsew", pady=(10, 0))
        self.start_stop_frame.grid_columnconfigure(0, weight=1)
        self.start_stop_frame.grid_rowconfigure((0, 2), weight=1)
        # Start/stop label
        self.start_stop_label = ctk.CTkLabel(self.start_stop_frame, text="SEND CAN MESSAGE")
        self.start_stop_label.grid(column=0, row=0, padx=10, pady=5)
        # Start and stop buttons
        self.start_button = ctk.CTkButton(self.start_stop_frame, text="SEND", command=self.start_communication)
        self.start_button.grid(column=0, row=1, padx=10, pady=5)
        self.stop_button = ctk.CTkButton(self.start_stop_frame, text="STOP", command=self.stop_communication)
        self.stop_button.grid(column=0, row=2, padx=10, pady=5)

        self.data_converter = DataConverterJ1939()
        #self.converter.main_signals(main_signals)

    def start_communication(self):
        print("Communication Started")
        values = self.app.get_values()
        self.data_converter.set_values(values)
        print(values)


    def stop_communication(self):
        print("Communication Stopped")

