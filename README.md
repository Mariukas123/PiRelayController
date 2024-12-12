# Raspberry Pi GPIO Relay Control API

This project demonstrates how to use Raspberry Pi's GPIO interface to control a 4-channel relay module via a REST API built with Flask. The relay module allows controlling electrical devices, such as lights, through GPIO pins.

## Features
- **Retrieve relay states**: Get a list of configured relay GPIO pins.
- **Control individual relays**: Turn specific relays on or off.
- **Control all relays**: Turn all relays on or off at once.

## Use Case
This project was used to control a 4-channel relay module connected to electrical circuits. Each relay channel could activate or deactivate electrical devices, such as controlling which light in a room is turned on or off. The relays are controlled programmatically via HTTP requests to the REST API.

## Requirements
- Raspberry Pi (tested on Raspberry Pi 4)
- 4-channel relay module
- Electrical wiring setup for devices (e.g. lights)
- Python 3

## Installation
1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. Install dependencies:
    ```bash
    pip install flask RPi.GPIO
    ```

3. Connect the relays to the following GPIO pins:
    ```bash
    GPIO 3
    GPIO 4
    GPIO 22
    GPIO 27
    ```

4. Run the application
    ```bash
    python relay_modular_api.py
    ```