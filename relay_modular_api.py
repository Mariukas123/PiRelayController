from flask import Flask, jsonify
import RPi.GPIO as GPIO
import time

backend = Flask(__name__)


# SET BOARD SETTINGS BCM
GPIO.setmode(GPIO.BCM)

# BOARD PINS
channels = [3, 4, 22, 27]

# SETUP OUTPUTS
for pin in channels:
	GPIO.setup(pin, GPIO.OUT)




#print("All channels are off")
#GPIO.cleanup()


# SERVER SETUP


# Return all channel pin numbers
@backend.route("/api/relay", methods=["GET"])
def return_relay():
	return jsonify({ "channels": channels })



# Turn on specific channel
@backend.route("/api/relay/turn_on/<int:channel>", methods=["POST"])
def enable_channel(channel):
	GPIO.output(channels[channel - 1], GPIO.LOW)

	print(f"Channel {channel} turned on.")
	return jsonify({ "success": True })



# Turn off specific channel
@backend.route("/api/relay/turn_off/<int:channel>", methods=["POST"])
def disable_channel(channel):
	GPIO.output(channels[channel - 1], GPIO.HIGH)

	print(f"Channel {channel} turned off")
	return jsonify({ "success": True })


# Turn on all channels
@backend.route("/api/relay/turn_on_all", methods=["POST"])
def enable_all_channel():
	for pin in channels:
		GPIO.output(pin, GPIO.LOW)

	print(f"All channels are on")
	return jsonify({ "success": True })

# Turn off all channels
@backend.route("/api/relay/turn_off_all", methods=["POST"])
def disable_all_channel():
	for pin in channels:
		GPIO.output(pin, GPIO.HIGH)

	print(f"All channels are off")
	return jsonify({ "success": True })




print("This server runs on http://localhost:5000")

if __name__ == "__main__":
	backend.run(host="0.0.0.0", port=5000)
