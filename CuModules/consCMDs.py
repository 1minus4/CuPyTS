import os
import platform

class Commands:
  # Get the initial details about the os.
  def __init__(self):
    self.os = platform.system()
    pass
    
  # Clear the console
  def ClearConsole(self):
    if self.os == 'Linux':
      os.system('clear')
      return
    elif self.os == 'Windows':
      os.system('cls')
      return
