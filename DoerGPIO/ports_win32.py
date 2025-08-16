# DoerGPIO Python Library
# Copyright (C) 2024  Pasco Tang
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# ports_win32.py  06/18/2025  Pasco Tang
#
# Scan the windows registry to find a list of COM ports

try:
  import _winreg as registry # python2
except ImportError:
  import winreg as registry # python3

KEY = r"HARDWARE\DEVICEMAP\SERIALCOMM"

def scan():
  ports = []

  reg = registry.ConnectRegistry(None, registry.HKEY_LOCAL_MACHINE)
  try:
    key = registry.OpenKey(reg, KEY)
  except:
    # If there is no SERIALCOMM registry entry
    # it means this computer has never seen a serial port.
    # Best action is to return an empty ports list. 
    # When the device is inserted, windows will create the entry for us.
    return ports

  i = 0
  while True:
    try:
      value = registry.EnumValue(key, i)   
      name, value, vtype = value
      print("port[" + str(i) + "]:" + str(value))
      ports.append(value)
      i += 1
    
    except EnvironmentError:
      break
    
  return ports


# TESTER

if __name__ == "__main__":
  d = find()
  print(str(d))
  
# END
