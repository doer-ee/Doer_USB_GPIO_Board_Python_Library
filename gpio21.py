from DoerGPIO import GPIO
import time

GPIO.setup(21, GPIO.OUT)

try:
    GPIO.output(21, GPIO.HIGH)
    time.sleep(1)
finally:
    GPIO.output(21, GPIO.LOW)
