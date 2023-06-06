# EDTI - Engine Digital Twin Interface

## Project description.
This python project is a CustomTkinter based GUI that can communicate through CAN bus with a DSE controller.
The interface displays different heavy-duty engine signals that can be manipulated and sent to a controller as J1939 CAN messages.
The app is compatible with Windows or macOS devices, and the CAN messages are transmitted from a computer to a DSE controller using a generic USB-CAN analyzer.

## Usage.
This app is meant to be compiled and run as an executable file, and can simulate signals for seven different engines to communicate with a DSE controller. 
The DSE controller must be configured to be used with the desired engine, and all analogue and digital inputs should be set to "not used".
The USB-CAN analyzer must be connected to any usb port in the computer, and to the "ECU" pins on the DSE controller.

## Libraries and modules.
This project uses different python libraries that need to be installed, such as "customtkinter" for the GUI, "python-can" for CAN bus communication, 
"pillow" for image handling, and "pyserial" for USB serial port identification. Additionally the built-in Python modules "os" and "time" are used.

