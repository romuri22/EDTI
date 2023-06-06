# channel_selector_frame.py
# -------------------------------------------------------------------

# Engine Digital Twin Interface.
# Written by Rodrigo Murillo Tapia, Alejandro Martinez Licon and Alejandro Gaviria Ramirez.
# 2023

# Channel selector class, scanns usb devices and shows their channels in a menu to be selected.

import customtkinter as ctk     # GUI library
import serial.tools.list_ports  # For searching usb serial ports
import os                       # For OS differences whith serial ports

class ChannelSelectorFrame(ctk.CTkFrame):       # Channel selector class with a button and a menu
    def __init__(self, master, app):
        super().__init__(master, height=160)    # Height should be adjusted if app window size is changed
        self.app = app

        # Channel selector frame configuration
        self.channel_selector_frame = ctk.CTkFrame(master)
        self.channel_selector_frame.grid(sticky="nsew", pady=(0, 10))
        self.channel_selector_frame.columnconfigure((0, 1), weight=1)
        self.channel_selector_frame.rowconfigure((0, 1), weight=1)

        # Channel selector label
        self.channel_selector_label = ctk.CTkLabel(self.channel_selector_frame, text="USB SERIAL CHANNEL")
        self.channel_selector_label.grid(column=0, row=0, padx=10, pady=(20, 0), columnspan=2)
        # Button
        self.channel_scan_button = ctk.CTkButton(self.channel_selector_frame, text="Search Ports", command=self.scan_channels)
        self.channel_scan_button.grid(column=0, row=1, padx=(70, 0), pady=(0, 30))
        # Scanned channels menu
        self.channel_menu = ctk.CTkOptionMenu(self.channel_selector_frame, command=self.select_channel)
        self.channel_menu.grid(column=1, row=1, padx=(0, 70), pady=(0, 30))
        self.channel_menu.set("Select USB Serial Channel")
        self.channel_menu.configure(state="disabled")

    def select_channel(self, value):    # Function called by the menu with a bus channel
        self.app.set_channel(value)     # Sets the channel through app

    # Scans all serial ports connected to a computer
    def scan_channels(self):
        ports = serial.tools.list_ports.comports()  # Looks for all serial ports active
        self.usb_serial_channels = []               # List of channels to be displayed in menu
        for port in ports:
            if os.name == 'posix':  # macOS / Linux
                if 'USB Serial' in port.description:
                    channel = port.device.replace('/dev/cu.', '/dev/tty.')  # Corrects macOs channel names
                    self.usb_serial_channels.append(channel)                # Adds to the channels list
            elif os.name == 'nt':   # Windows
                self.usb_serial_channels.append(port.device)                # Adds to the channels list
        if self.usb_serial_channels:    # Checks if a serial port was found
            self.channel_menu.set("Select USB Serial Channel")          # Enables the channel selector
            self.channel_menu.configure(state="enabled", values=self.usb_serial_channels)
            print(self.usb_serial_channels)
        else:
            self.channel_menu.set("No channels found")                  # Disables the channel selector
            self.channel_menu.configure(state="disabled", values=self.usb_serial_channels)
