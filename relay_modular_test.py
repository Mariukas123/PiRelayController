import RPi.GPIO as GPIO
import time

# SET BOARD SETTINGS BCM
GPIO.setmode(GPIO.BCM)

# BOARD PINS
channels = [3, 4, 22, 27]

# SETUP OUTPUTS
for pin in channels:
	GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)


# CODE
try:
	for index, element in enumerate(channels):
		print(f"Turning on channel: {index + 1}")
		GPIO.output(element, GPIO.LOW)
		time.sleep(2)

finally:
	for index, element in enumerate(channels):
		GPIO.output(element, GPIO.HIGH)


print("All channels are off")
GPIO.cleanup()

