import customtkinter as ctk
import serial.tools.list_ports

class ChannelSelectorFrame(ctk.CTkFrame):         # Engine selector class with 2 menus
    def __init__(self, master, app):
        super().__init__(master, height=160)
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
        self.channel_scan_button = ctk.CTkButton(self.channel_selector_frame, text="SCAN", command=self.scan_channels)
        self.channel_scan_button.grid(column=0, row=1, padx=(70, 0), pady=(0, 30))
        # Scanned channels menu
        self.channel_menu = ctk.CTkOptionMenu(self.channel_selector_frame, command=self.select_channel)
        self.channel_menu.grid(column=1, row=1, padx=(0, 70), pady=(0, 30))
        self.channel_menu.set("Select USB Serial Channel")
        self.channel_menu.configure(state="disabled")

    def select_channel(self, value):   # Function called by engine_range_menu with an engine range
        self.app.set_channel(value)

    def scan_channels(self):
        ports = serial.tools.list_ports.comports()
        self.usb_serial_channels = []
        for port in ports:
            if 'USB Serial' in port.description:
                channel = port.device.replace('/dev/cu.', '/dev/tty.')
                self.usb_serial_channels.append(channel)

        if self.usb_serial_channels:
            self.channel_menu.set("Select USB Serial Channel")
            self.channel_menu.configure(state="enabled", values=self.usb_serial_channels)
            print(self.usb_serial_channels)
        else:
            self.channel_menu.set("No channel found")
            self.channel_menu.configure(state="disabled", values=self.usb_serial_channels)
