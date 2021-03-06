"""
Usage:
  RoomMgt
  RoomMgt create_room <room_type> <room_name> ...
  RoomMgt add_person <person_name> <FELLOW_or_STAFF> [<wants_accomodation>]
  RoomMgt add_person <person_name> 
  RoomMgt print_room <room_name>
  RoomMgt get_rooms

"""

import sys
import cmd
from docopt import docopt, DocoptExit
from RoomMgt import Dojo

dojo = Dojo()

def docopt_cmd(func):
  """

  This decorator is used to simplify the try/except block and pass the result

  of the docopt parsing to the called action.

  """

  def fn(self, arg):
      try:
          opt = docopt(fn.__doc__, arg)

      except DocoptExit as e:
          print('Invalid Command!')
          print(e)
          return

      except SystemExit:
          return
      return func(self, opt)

  fn.__name__ = func.__name__
  fn.__doc__ = func.__doc__
  fn.__dict__.update(func.__dict__)
  return fn
  

    
class DojoCLI(cmd.Cmd):

  intro = 'Welcome to Dojo Command Line Interface' \
      + ' (type help for a list of commands.)'

  prompt = 'RoomMgt '

  file = None
  
  @docopt_cmd 
  def do_create_room(self, arg):
    """Usage:  create_room <room_type> <room_name> ..."""
    room_type = arg['<room_type>']
    room_list = arg['<room_name>']
    output = dojo.create_room(room_list, room_type, )
    if output.type == "office":
      for name in output.name:
        print("An office called " + name + " has been successfully created! \n")
    if output.type == "livingspace":
      for name in output.name:
        print("A livingspace called " + name + " has been successfully created!\n")
  
  @docopt_cmd 
  def do_add_person(self, arg):
    """Usage:  add_person <first_name> <last_name> <person_type> [<wants_accomodation>]"""
    person_name = arg['<first_name>'] + " " + arg['<last_name>']
    person_type = arg['<person_type>']
    wants_accomodation = arg['<wants_accomodation>']
    output = dojo.add_person( person_type, person_name, wants_accomodation)
    print(output.type + " " + output.name + " has been successfully created!")
    print(output.name + " has been allocated the Office " + output.office[0] + "\n")
    if output.type == "Fellow":
      print(output.name + " has been allocated the livingspace " + output.livingspace + "\n")
      

  
  @docopt_cmd 
  def do_get_occupants(self, arg):
    """Usage:  print_room <room_name>"""
    room_name = arg['<room_name>']
    output = dojo.get_occupants(room_name)
    print(room_name)
    print("__________________________________")
    print(output)
  
  @docopt_cmd 
  def do_print_rooms(self, arg):
    """Usage:  get_rooms """
    output = dojo.get_all_rooms()
    for room in output:
      print(room.name)
  
  @docopt_cmd 
  def do_print_allocations(self, arg):
    """Usage:  print_allocations """
    output = dojo.get_all_rooms()
    for room in output:
      occupant_list = []
      print(room.name)
      print("_____________________________________________")
      for occupant in room.occupants:
        occupant_list.append(occupant.name)
        
      print (''.join(occupant_list))

  @docopt_cmd 
  def do_reallocate_person(self, arg):
    """Usage:  reallocate_person <first_name> <last_name> <new_room_name> """
    print ("Feature uneder development")
    """
    person_name = arg['<first_name>'] + " " + arg['<last_name>']
    new_room_name = arg['<new_room_name>']
    output = dojo.reallocate_person(person_name, new_room_name)
    print( output.name + " has been reallocated the room " + room_name)
    """
    
    
  def do_quit(self, arg):
      """Quits out of Interactive Mode."""
      print('Good Bye!')
      exit()

opt = docopt(__doc__, sys.argv[1:])
DojoCLI().cmdloop()