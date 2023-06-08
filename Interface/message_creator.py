# message_creator.py
# -------------------------------------------------------------------

# Engine Digital Twin Interface.
# Written by Rodrigo Murillo Tapia, Alejandro Martinez Licon and Alejandro Gaviria Ramirez.
# 2023

# Message creator class, takes signal data and a channel, converts to J1939 messages,
# sends them through the selected channel using CAN Bus protocol.

import can     # CAN Bus protocol library, to create CAN messages and to define a CAN bus.

class MessageCreator():                     # Message creator class
   def __init__(self, start_stop_frame):
      
      self.start_stop_frame = start_stop_frame

      # Parameters for each signal sent
      self.SPN_info = [
         {"text": "Engine Speed",   "level": "byte", "length": 2, "start": 4, "res": 0.125, "offset": 0},
         {"text": "Oil Pressure",   "level": "byte", "length": 1, "start": 4, "res": 4,     "offset": 0},
         {"text": "Coolant Temp",   "level": "byte", "length": 1, "start": 1, "res": 1,     "offset":-40},
         {"text": "Engine Hours",   "level": "byte", "length": 4, "start": 1, "res": 0.05,  "offset": 0},
         {"text": "Oil Temp",       "level": "byte", "length": 2, "start": 3, "res":0.03125,"offset":-273},
         {"text": "Coolant Pressure","level":"byte", "length": 1, "start": 7, "res": 2,     "offset": 0},
         {"text": "Inlet Temp",     "level": "byte", "length": 1, "start": 3, "res": 1,     "offset":-40},
         {"text": "Fuel Temp",      "level": "byte", "length": 1, "start": 2, "res": 1,     "offset":-40},
         {"text": "Turbo Pressure", "level": "byte", "length": 1, "start": 2, "res": 2,     "offset": 0},
         {"text": "Fuel Pressure",  "level": "byte", "length": 1, "start": 1, "res": 4,     "offset": 0},
         {"text": "Atmos Pressure", "level": "byte", "length": 2, "start": 1, "res": 0.5,   "offset": 0},
         {"text": "Rated Speed",    "level": "byte", "length": 2, "start": 3, "res": 0.125, "offset": 0}
      ]

      # Paramers and signals included for each PGN, id's are taken from J1939-71 standard
      # Last two bytes of "can_id" are set at a source adress of '00', different applications may need adjusting
      self.PGN_info = [
         {"pgn": 61444, "can_id": 0x0CF00400, "signals": [0]}, # "signals" stands for which SPN's are included in each PGN
         {"pgn": 65263, "can_id": 0x18FEEF00, "signals": [1, 5, 9]},
         {"pgn": 65262, "can_id": 0x18FEEE00, "signals": [2, 4, 7]},
         {"pgn": 65253, "can_id": 0x18FEE500, "signals": [3]},
         {"pgn": 65270, "can_id": 0x18FEF600, "signals": [6, 8]},
         {"pgn": 65269, "can_id": 0x18FEF500, "signals": [10]},
         {"pgn": 65214, "can_id": 0x18FEBE00, "signals": [11]}
      ]


   # Function that scales a value to a resolution, converts to hex (little endian),
   # and adds it to the correct byte(s) in a PGN's data list.
   def add_to_pgn_data(self, decimal, res, offset, data_list, start, length, level):
      # Scale value to resolution, round to convert to int
      scaled = round((decimal - offset) / res)
      # All signals in this program have full byte-level lengths, bit-level lengths 
      # are common in the J1939 standard for alerts and other low-resolution signals
      if level == "byte":     # For byte-level length signals
         # Convert decimal to bytes in big-endian byte order
         new_data = scaled.to_bytes((scaled.bit_length() + 7) // 8, 'little')
         byte_data = bytearray(new_data)
         # Checks if the data is of enough length, adds necessary zeros
         while len(byte_data) < length:
            byte_data.append(0x00)
         # Modify the wanted bytes in the data list
         end = start + length
         data_list[start:end] = byte_data
      else:       # For bit-level length signals
         # Calculate the byte index and bit offset
         byte_index = int(start)
         bit_offset = int((start - byte_index) * 8)
         # Calculate the mask to clear the target bits
         mask = ~(0b11 << bit_offset)
         # Update the corresponding bits in the array
         data_list[byte_index] &= mask  # Clear the target bits
         data_list[byte_index] |= (scaled << bit_offset)  # Set the new bits

      return data_list

   # Creates a single can message for a single PNG, with an id and an 8 byte data list
   def create_can_message(self, can_id, can_data):
      # Create a CAN message object
      can_message = can.Message(
         arbitration_id=can_id,  
         data=can_data,
         is_rx=False,            # Rx is for receiver, Tx for transmitter
         is_extended_id=True,    # J1939 standard uses extended can id (29 bits)
      )
      return can_message

   # Loops through a dictionary to define id and data structure for each pgn.
   def create_J1939_messages(self, values):
      for pgn in self.PGN_info:
         # Each message is printed on the serial monitor for debugging purposes
         print("----------------------------------------------------------------------------------------------------")
         print("PGN: ", pgn["pgn"])
         # Looks for id for each PGN
         can_id = pgn["can_id"]
         data = bytearray(8)     # Zeros array of 8 bytes
         # Loops through each signal included in a pgn to write the 8 byte data-chain
         for signal in pgn["signals"]:
            # Collects all relevant info for each signal
            value = values[signal]
            print(self.SPN_info[signal]["text"], ": ", value)
            res = self.SPN_info[signal]["res"]           # Signal resolution
            offset = self.SPN_info[signal]["offset"]     # Signal offset
            start = self.SPN_info[signal]["start"] - 1   # Starting byte inside the 8-byte array
            length = self.SPN_info[signal]["length"]     # Length in bytes
            level = self.SPN_info[signal]["level"]
            # Calls add to pgn data to write the signal values to the J1939 data list
            data = self.add_to_pgn_data(value, res, offset, data, start, length, level)
         # With the id and data, creates a can message
         can_message = self.create_can_message(can_id, data)
         # Each pgn message is printed to console for debugging purposes
         print("-------------------")
         print("CAN MESSAGE FOR PGN")
         print(can_message)
         try:
            self.bus.send(can_message)
         except:
            print("No bus configured")
            self.start_stop_frame.stop_communication()
   
   # Function called by start_stop_frame to update and send all can messages
   def start_communication(self, values):
      self.create_J1939_messages(values)

   # Sets the bus channel to the selected serial port
   def set_channel(self, channel):
      self.bus = can.interface.Bus(interface='seeedstudio', channel=channel, bitrate=250000)
      print(channel)



