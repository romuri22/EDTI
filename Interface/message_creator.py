import can
import time

class MessageCreator():                     # Message creator class
   def __init__(self):
      
      # Parameters for each signal sent
      self.SPN_info = [
         {"text": "Engine Speed",   "level": "byte", "length": 2, "start": 4, "res": 0.125,   "offset": 0},
         {"text": "Oil Pressure",   "level": "byte", "length": 1, "start": 4, "res": 4,       "offset": 0},
         {"text": "Coolant Temp",   "level": "byte", "length": 1, "start": 1, "res": 1,       "offset": -40},
         {"text": "Engine Hours",   "level": "byte", "length": 4, "start": 1, "res": 0.05,    "offset": 0},
         {"text": "Oil Temp",       "level": "byte", "length": 2, "start": 3, "res": 0.03125, "offset": -273},
         {"text": "Coolant Pressure","level":"byte", "length": 1, "start": 7, "res": 2,       "offset": 0},
         {"text": "Inlet Temp",     "level": "byte", "length": 1, "start": 3, "res": 1,       "offset": -40},
         {"text": "Fuel Temp",      "level": "byte", "length": 1, "start": 2, "res": 1,       "offset": -40},
         {"text": "Turbo Pressure", "level": "byte", "length": 1, "start": 2, "res": 4,       "offset": 0},
         {"text": "Fuel Pressure",  "level": "byte", "length": 1, "start": 1, "res": 4,       "offset": 0},
         {"text": "DM1 Amber",      "level": "bit", "length": 0.2, "start": 6.5, "res": 1,    "offset": 0},
         {"text": "DM1 Red",        "level": "bit", "length": 0.2, "start": 6.3, "res": 1,    "offset": 0},
         {"text": "Atmos Pressure", "level": "byte", "length": 2, "start": 1, "res": 0.5,     "offset": 0},
         {"text": "Rated Speed",    "level": "byte", "length": 2, "start": 3, "res": 0.125,   "offset": 0}
      ]

      # Paramers and signals included for each PGN, id's are taken from J1939-71 standard
      self.PGN_info = [
         {"pgn": 61444, "can_id": 0x0CF00400, "signals": [0]},
         {"pgn": 65263, "can_id": 0x18FEEF00, "signals": [1, 5, 9]},
         {"pgn": 65262, "can_id": 0x18FEEE00, "signals": [2, 4, 7]},
         {"pgn": 65253, "can_id": 0x18FEE500, "signals": [3]},
         {"pgn": 65270, "can_id": 0x18FEF600, "signals": [6, 8]},
         {"pgn": 61441, "can_id": 0x18FEF200, "signals": [10, 11]},
         {"pgn": 65269, "can_id": 0x18FEF500, "signals": [12]},
         {"pgn": 65214, "can_id": 0x19FEBE00, "signals": [13]}
      ]
      #try:
      self.bus = can.interface.Bus(interface='seeedstudio', channel='/dev/tty.usbserial-1420', bitrate=250000)
      #except:
         #pass


   # Function that scales a value to a resolution, converts to hex (little endian),
   # and adds it to the correct byte(s) in a PGN's data list.
   def add_to_pgn_data(self, decimal, res, offset, data_list, start, length, level):
      # Scale value to resolution, round to convert to int
      scaled = round((decimal - offset) / res)
      if level == "byte":
         # Convert decimal to bytes in big-endian byte order
         new_data = scaled.to_bytes((scaled.bit_length() + 7) // 8, 'little')
         byte_data = bytearray(new_data)
         # Checks if the data is of enough length, adds necessary zeros
         while len(byte_data) < length:
            byte_data.append(0x00)
         # Modify the wanted bytes in the data list
         end = start + length
         data_list[start:end] = byte_data
      else:
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
         is_rx=False,
         is_extended_id=True,    # J1939 standard uses extended can id (29 bits)
      )
      return can_message

   # Loops through a dictionary to define id and data structure for each pgn.
   def create_J1939_messages(self, values):
      for pgn in self.PGN_info:
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
         # Each pgn message is printed to console and stored in a message array
         print("-------------------")
         print("CAN MESSAGE FOR PGN")
         print(can_message)
         #try:
         self.bus.send(can_message)
         #except:
            #pass
         


   def start_communication(self, values):
      self.create_J1939_messages(values)



