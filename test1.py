import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define pins
channel_1 = 22

# Setup the GPIO pins as outputs
GPIO.setup(channel_1, GPIO.OUT)

# CODING

try:
        print("Turning channel 1 on")
        GPIO.output(channel_1, GPIO.LOW)
        time.sleep(2)

finally:
        print("Turning all channels off")
        GPIO.output(channel_1, GPIO.HIGH)

        # Cleaning up GPIO settings
        GPIO.cleanup()
