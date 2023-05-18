import can


class MessageCreator():
   def __init__(self):
      
      # Parameters for each signal sent
      self.SPN_info = [
         {"text": "Engine Speed",   "length": 2, "start": 4, "res": 0.125,   "offset": 0},
         {"text": "Oil Pressure",   "length": 1, "start": 4, "res": 4,       "offset": 0},
         {"text": "Coolant Temp",   "length": 1, "start": 1, "res": 1,       "offset": -40},
         {"text": "Engine Hours",   "length": 4, "start": 1, "res": 0.05,    "offset": 0},
         {"text": "Oil Temp",       "length": 2, "start": 3, "res": 0.03125, "offset": -273},
         {"text": "Inlet Temp",     "length": 1, "start": 6, "res": 1,       "offset": -40},
         {"text": "Fuel Temp",      "length": 1, "start": 2, "res": 1,       "offset": -40},
         {"text": "Turbo Pressure", "length": 1, "start": 1, "res": 4,       "offset": 0},
         {"text": "Fuel Pressure",  "length": 1, "start": 1, "res": 4,       "offset": 0},
         {"text": "Fuel Rate",      "length": 2, "start": 1, "res": 0.05,    "offset": 0},
         {"text": "Fuel Used",      "length": 4, "start": 5, "res": 0.5,     "offset": 0},
         #{"text": "DM1 Amber",      "length": 0.2, "start": 6.5, "res": 1,   "offset": 0},
         #{"text": "DM1 Red",        "length": 0.2, "start": 6.3, "res": 1,   "offset": 0}
      ]

      # Paramers and signals included for each PGN, id's are taken from J1939-71 standard
      self.PGN_info = [
         {"pgn": 61444, "can_id": 0x0CF00401, "signals": [0]},
         {"pgn": 65263, "can_id": 0x18FEEF01, "signals": [1, 8]},
         {"pgn": 65262, "can_id": 0x18FEEE01, "signals": [2, 4, 6]},
         {"pgn": 65253, "can_id": 0x18FEE501, "signals": [3]},
         {"pgn": 65269, "can_id": 0x18FEF501, "signals": [5]},
         {"pgn": 65245, "can_id": 0x18FEDD01, "signals": [7]},
         {"pgn": 65266, "can_id": 0x18FEF201, "signals": [9]},
         {"pgn": 65257, "can_id": 0x18FEE901, "signals": [10]},
         #{"pgn": 61441, "can_id": 0x18FEF201, "signals": [11, 12]}
      ]

   # Function that scales a value to a resolution, converts to hex (little endian),
   # and adds it to the correct byte(s) in a data list.
   def add_to_pgn_data(self, decimal, res, data_list, start, length):
      # Scale value to resolution, round to convert to int
      scaled = round(decimal / res)
      # Convert decimal to bytes in big-endian byte order
      new_data = scaled.to_bytes((scaled.bit_length() + 7) // 8, 'little')
      byte_data = bytearray(new_data)
      # Checks if the data is of enough length, adds necessary zeros
      while len(byte_data) < length:
         byte_data.append(0x00)
      # Modify the wanted bytes in the data list
      end = start + length
      data_list[start:end] = byte_data
      return data_list

   # Creates a single can message for a single PNG, with an id and an 8 byte data list
   def create_can_message(self, can_id, can_data):
      # Create a CAN message object
      can_message = can.Message(
         arbitration_id=can_id,  
         data=can_data,
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
         # Loops through each signal included in a pgn, obtains value and other parameters
         for signal in pgn["signals"]:
            value = values[signal]
            print(self.SPN_info[signal]["text"], ": ", value)
            res = self.SPN_info[signal]["res"]           # Signal resolution
            start = self.SPN_info[signal]["start"] - 1   # Starting byte inside the 8-byte array
            length = self.SPN_info[signal]["length"]     # Length in bytes
            data = self.add_to_pgn_data(value, res, data, start, length)
         # With the id and data, creates a can message
         can_message = self.create_can_message(can_id, data)
         print("-------------------")
         print("CAN MESSAGE FOR PGN")
         print(can_message)


