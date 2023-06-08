# start_stop_frame.py
# -------------------------------------------------------------------

# Engine Digital Twin Interface.
# Written by Rodrigo Murillo Tapia, Alejandro Martinez Licon and Alejandro Gaviria Ramirez.
# 2023

# Start/stop frame class, has two buttons, calls the message creator when communicating.

import customtkinter as ctk                 # GUI library
from message_creator import MessageCreator  # This frame intances a MessageCreator object

class StartStopFrame(ctk.CTkFrame):              # Start/stop class with 2 buttons
    def __init__(self,master, app):
        super().__init__(master)
        self.app = app

        # Start/stop frame configuration
        self.start_stop_frame = ctk.CTkFrame(master)
        self.start_stop_frame.grid(sticky="nsew", pady=(10, 0))
        self.start_stop_frame.grid_columnconfigure(0, weight=1)
        self.start_stop_frame.grid_rowconfigure((0, 2), weight=1)
        # Start/stop label
        self.start_stop_label = ctk.CTkLabel(self.start_stop_frame, text="CAN COMMUNICATION")
        self.start_stop_label.grid(column=0, row=0, padx=10, pady=5)
        # Start and stop buttons
        self.start_button = ctk.CTkButton(self.start_stop_frame, text="START", command=self.start_communication)
        self.start_button.grid(column=0, row=1, padx=10, pady=5)
        self.stop_button = ctk.CTkButton(self.start_stop_frame, text="STOP", command=self.stop_communication)
        self.stop_button.grid(column=0, row=2, padx=10, pady=5)
        # Default configuration
        self.message_creator = MessageCreator(self)

    # Starts communication loop
    def start_communication(self):
        print("Communication Started")
        self.running = True
        self.send_messages()

    # Stops communication loop
    def stop_communication(self):
        print("Communication Stopped")
        self.running = False

    # Loop that updates all signal values and calls the message creator
    def send_messages(self):
        if self.running:
            values= self.app.get_values()
            print(values)
            self.message_creator.start_communication(values)
        self.after(50, self.send_messages)      # Updates and sends messages every 50 ms

    # Function to set the CAN bus channel
    def set_channel(self, channel):
        self.message_creator.set_channel(channel)