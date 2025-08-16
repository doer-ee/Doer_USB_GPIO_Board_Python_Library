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

# anyio/arduino/GPIO.py  5/7/2025 Pasco Tang
# An ardunio (serial) based GPIO link

# CONFIGURATION ========================================================

DEBUG = False
# There was the option to use the serial library pre-installed. This has changed so that we know the python lib in use is the one distributed with the doer library.
#If you wish to use the built in one instead change the import doerserial to import serial which is below (Approx line 38)

MIN_PIN = 0
MAX_PIN = 27

IN      = 0
OUT     = 1
PWM     = 2
ADC     = 3
HIGH    = 1
LOW     = 0

PUD_OFF = 20
PUD_DOWN = 21
PUD_UP = 22

VERSION = "DoerGPIO.GPIO 0.4"

# OS INTERFACE =========================================================

from DoerGPIO import protocol
from DoerGPIO import adaptors


#from os import sys, path
#thisdir = path.dirname(path.abspath(__file__))
#sys.path.append(thisdir)

#import doerserial as serial

#Temporarily changing back to normal serial

from DoerGPIO import doerserial

instance = protocol.GPIOClient(adaptors.SerialAdaptor(doerserial.s), DEBUG)

def setup(channel, mode,pull_up_down=None,initial=0):
  if type(channel) is list:
    for c in channel:
      instance.setup(c, mode,pull_up_down,initial)
  else:
    instance.setup(channel, mode,pull_up_down,initial)

def input(channel):
  return instance.input(channel)

def output(channel, value):
  instance.output(channel, value)

def pwm_set_duty(channel, duty):
  instance.pwm_set_duty(channel, duty)

def pwm_set_frequency(channel, frequency):
  instance.pwm_set_frequency(channel, frequency)

def adc_read(channel):
  return instance.adc_read(channel)

def cleanup(number=0):
  instance.cleanup()


# END
