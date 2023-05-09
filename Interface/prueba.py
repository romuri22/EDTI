#import can
import numpy

class J1939():
   def __init__(self):
      super().__init__()
        
      self.pgn_engine_speed=61444
      self.pgn_oil_pressure=65263
      self.pgn_coolant_T=65262
      self.pgn_engine_hours=65253

        #bus = can.interface.Bus(channel='can0', bustype='socketcan')

      #Se determina la ID de can
      self.canID_engine_speed=(self.pgn_engine_speed<<8) | 0x18  #18 bits=2 bytes, al pasar una cadena a pgn se usan dos bytes lo que significa que se deben recorrer 8 lugares en total (8 bits por byte x 2 bytes = 16 bits = 2 bytes).
      self.canID_oil_pressure=(self.pgn_oil_pressure<<8) | 0x18
      self.canID_coolant_T=(self.pgn_coolant_T<<8) | 0x18
      self.canID_engine_hours=(self.pgn_engine_hours<<8) | 0x18

   def set_main_values(self, main_values):
      #Main Signals
      self.engine_speed = main_values[0]
      self.oil_pressure = main_values[1]
      self.coolant_T = main_values[2]
      self.engine_hours = main_values[3]
      #pasar a cadenas de bytes
      self.byte_chain()
   
   def byte_chain(self):
      _engine_speed = int(self.engine_speed)
      _oil_pressure = int(self.oil_pressure)
      _coolant_T = int(self.coolant_T)
      _engine_hours = int(self.engine_hours)
      bytes_engine_speed = _engine_speed.to_bytes(2,byteorder='big') # En caso de utilizar big se almacenan los bytes mas significativos en la memoria y little es para almacenar los bytes menos significativos de primerp.
      bytes_oil_pressure = _oil_pressure.to_bytes(1,byteorder='big') #segun el data lenght se agrega en el parentesis 
      bytes_coolantT= _coolant_T.to_bytes(1,byteorder='big')
      bytes_engine_hours= _engine_hours.to_bytes(4,byteorder='big')
      #Se determinan los pgn de los mains. El pgn es un id de 18 bits. se compone de pgn (8bits), msp (3 bits) un bit 0 y poseriormente un id para saber si es extendido o no
      
      
      print(self.canID_engine_speed)
      print(self.canID_oil_pressure)
      print(self.canID_coolant_T)
      print(self.canID_engine_hours)
      print(bytes_engine_speed)
      print(bytes_oil_pressure)
      print(bytes_coolantT)
      print(bytes_engine_hours)



   #se crea el mensaje de can de forma extendida para cada variable (29 bits)
   #msg_engine_speed=can.message(
   #   arbitrationID_engine_speed=canID_engine_speed,
   #  bytes_engine_speed=bytes_engine_speed,
      # extended_id=True
   ##)
   #msg_oil_pressure=can.message(
   #   arbitrationID_oil_pressure=canID_oil_pressure,
   #  bytes_oil_pressure=bytes_oil_pressure,
      # extended_id=True
   #)
   #msg_coolantT=can.message(
   #   arbitrationID_coolant_T=canID_coolant_T,
   #  bytes_coolantT=bytes_coolantT,
      # extended_id=True
   #)
   #msg_engine_hours=can.message(
   #   arbitrationID_engine_hours=canID_engine_hours,
   #  bytes_engine_hours=bytes_engine_hours,
      # extended_id=True
   #)
   #bus.send(msg_engine_speed)
   #bus.send(msg_oil_pressure)
   #bus.send(msg_coolantT)
   #bus.send(msg_engine_hours)


   # Crear el mensaje CAN con el identificador 0x100 y los datos de la presión
   #mensaje_motor =can.Message(arbitration_id=0x00FEEC, data=bytes_motor, is_extended_id=True) ## cambiar ID
   #mensaje=can.Message(arbitration_id=0x)

   # Enviar el mensaje a través del bus CAN
   #bus.send(mensaje)

