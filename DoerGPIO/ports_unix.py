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

# ports_unix.py  06/18/2025  Pasco Tang
#
# Get a list of ports on a unix system
# Note that the precise /dev/* filter depends on the platform

# SYSTEM AND VERSION VARIANCE ==========================================

#this is for linux
DEV_TTY    = "/dev/tty*"

#TODO for mac, it's /dev/cua*???
  
  
# BODY =================================================================

import glob

def scan():
  """ scan devices that might be com ports """
  devices = glob.glob(DEV_TTY)
  #print("found " + str(len(devices)) + " devices")
  return devices


# TEST HARNESS =========================================================
 
if __name__ == "__main__":
  d = scan()
  print(str(d)) 
    
# END
