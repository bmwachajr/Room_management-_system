"""
  name : room management system.
  authr : benjamin wacha
  email: bmwachajr@gmail,com
  descrption: a system to randomly allocate rooms to andela staff and fellows.

"""
class Dojo(object):
  """This is the Dojo class, and andela facility"""
  def __init__(self):
    self.all_rooms = []
  
  def create_room(self,room_name, room_type):
    if (room_name == "") or (room_type == ""):
      raise RuntimeError("Couldnt create Room, both Room Name and Room Type needed")
    else:
      room_obj = room_name + "_" + room_type
      room_obj = Room(room_name, room_type)
      self.all_rooms.append(room_obj)
    
      return room_obj
  
class Room(object):
  """
      Rooms at The Dojo
      
      attributes:
        Room name
        Room Occupants
  """
  def __init__(self, room_name, room_type):
    self.room_name = room_name
    
class livingSpace(Room):
  max_people = 4
    
class Office(Room):
  max_people = 6