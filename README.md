## Object Tracking with Mobile Vehicle
This project involves developing a system for object tracking using a mobile vehicle. The system uses a Raspberry Pi 4 Model B, a Raspberry Pi Camera Module 3, and a Maestro Motor Driver to track an object based on its color and control the vehicle's movement accordingly. The project was developed as part of an experiment in the Electronics and Communications Engineering department at the University of Kocaeli.

# Equipment and Software

1. Raspberry Pi 4 Model B
- Quad-Core Broadcom BCM2711 A72 (ARM v8) 64-bit SoC
- 4GB LPDDR4 SDRAM
- Bluetooth 5.0, 2.4GHz/5.0GHz IEEE 802.11ac WiFi
- Gigabit Ethernet
- USB Ports: 2 x USB 2.0, 2 x USB 3.0
- 40-pin GPIO Header
- Dual micro HDMI ports (4Kp60 support)
- MicroSD card slot for OS and data storage
- Power input: 5V DC via USB-C connector (min 3A)
- Operating temperature: 0 to 50 °C
- Raspberry Pi 4 Model B will be in production at least until January 2026
  
2. Raspberry Pi Camera Module 3
- 12 Megapixel Sony IMX708 sensor
- High dynamic range (HDR) support
- Phase Detection Auto Focus (PDAF)
- Output: RAW10
- Supported video modes: 1080p50, 720p100, 480p120

3. Maestro Motor Driver
- Used for controlling and managing electric motors
- Suitable for industrial automation applications, CNC machines, and robotic systems
- Provides precise control of motor speed, torque, and position

Flowchart
The flowchart of the object detection process is provided in the documentation.

Connections
# Raspberry Pi GPIO Pins and Connections
- 3V3 Power (Pin 1 and 17): Provides 3.3V power from Raspberry Pi.
- 5V Power (Pin 2 and 4): Provides 5V power from Raspberry Pi.
- GPIO 2 (Pin 3) and GPIO 3 (Pin 5): I2C communication pins (SDA and SCL).
- GPIO 14 (Pin 8) and GPIO 15 (Pin 10): UART communication pins (TXD and RXD).
- Ground (Multiple Pins): Common ground connections.
# Bar30 Pressure Sensor and Raspberry Pi Connections
- Vin (Red): Connects to 3V3 Power pin.
- SCL (Green): Connects to GPIO 3 (SCL) pin.
- SDA (White): Connects to GPIO 2 (SDA) pin.
- GND (Black): Connects to a Ground pin.
# Maestro Motor Driver and Raspberry Pi Connections
- RX (Black): Connects to GPIO 14 (TXD) pin.
- TX (White): Connects to GPIO 15 (RXD) pin.
- Vin (Red): Connects to 5V Power pin.
- GND (Green): Connects to a Ground pin.
# Raspberry Pi Camera Module 3 and Raspberry Pi Connections
- Connects to the GPIO FFC 15-pin connector on the Raspberry Pi board, labeled "CAM."

## Experiment Results
# Observations and Graphs
- Object Location: Detect the location of a specific color object in the image and visualize it with a bounding box.
- Object Area: Calculate and display the area occupied by the detected object.
- Motor Responses: Observe the state (forward, reverse, stop) and power levels (duty cycle) of the motors based on the object's position and size.
# Data to be Recorded
- Object Coordinates: x and y coordinates of the object relative to the screen center.
- Bounding Box Area: Width and height of the bounding box surrounding the object.
- Motor States and Power Levels: Working state and applied power levels of each motor.
# Sampling Time
- Video Frame Rate: The system operates at 32 FPS (frames per second).
- Data Recording Timing: x and y coordinates, object area, and motor states are recorded for each frame.
 
## How to Run the Project
1. Clone the repository to your local machine.
2. Ensure you have all the required components and connect them as specified in the documentation.
3. Install the necessary libraries on your Raspberry Pi.
4. Run the provided Python script Object_Tracking.py to start the object tracking system.

For more detailed information, refer to the provided documentation files.
