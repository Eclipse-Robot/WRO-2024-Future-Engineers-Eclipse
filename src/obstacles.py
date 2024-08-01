import cv2
import os
import time
import sys
import threading
import serial
import numpy as np
from picamera2 import Picamera2
from libcamera import controls
from PIL import Image
from util import get_limits

Direction = 1
Speed = 0


# Colors in BGR
detected_color = (0, 0, 255)  # Red
detected_color2 = (0, 255, 255)  # Yellow

# Minimum size for the boxes
min_width = 30
min_height = 30

# Flag for loops to run simultaneously
running = True

# CAMERA INITIALIZATION START
def initialize_camera():
    picam2 = None
    max_retry_attempts = 3
    retry_count = 0
    while retry_count < max_retry_attempts:
        try:
            # Attempt to start Pi camera
            picam2 = Picamera2()
            picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (320, 240)}))
            picam2.start()
            picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
            time.sleep(1.0)
            print("Camera initialized")
            return picam2
        except Exception as e:
            print(f"Error initializing camera: {e}")
            if picam2:
                picam2.stop()
            retry_count += 1
            if retry_count < max_retry_attempts:
                print(f"Retrying camera initialization (attempt {retry_count} of {max_retry_attempts})...")
                time.sleep(2) 
            else:
                sys.exit(1)
    return None

# INITIALIZING COMMUNICATION WITH ARDUINO START
def read_from_arduino(ser):
    try:
        input_str = ser.readline().decode('utf-8').strip()
        if input_str:
            print("Read input: " + input_str)
        else:
            print(".")
        return input_str
    except serial.SerialException as e:
        print(f"Error reading from serial: {e}")
        return None

def write_speed_to_arduino(ser, command):
    try:
        ser.write("Speed ", command)
        print(f"Sent command: {command.decode('utf-8').strip()}")
        ser.flush() 
    except serial.SerialException as e:
        print(f"Error writing to serial: {e}")

def write_direction_to_arduino(ser, command):
    try:
        ser.write("Direction ", command)
        print(f"Sent command: Direction {command.decode('utf-8').strip()}")
        ser.flush() 
    except serial.SerialException as e:
        print(f"Error writing to serial: {e}")

def establish_serial_connection(port, baudrate, timeout, retries=5, delay=2):
    for attempt in range(retries):
        try:
            ser = serial.Serial(port, baudrate, timeout=timeout)
            time.sleep(2) 
            print("Serial connection established.")
            return ser
        except serial.SerialException as e:
            print(f"Attempt {attempt + 1}: Error opening serial port: {e}")
            time.sleep(delay)
    print("Failed to establish serial connection after multiple attempts.")
    return None

# Arduino loop
def read_arduino_thread(ser):
    while running:
        read_from_arduino(ser)
        write_speed_to_arduino(ser, Speed)
        write_direction_to_arduino(ser, Direction)
        time.sleep(0.05)

# Camera loop
def camera_processing_thread(picam2):
    while running:
        img = picam2.capture_array("main")
        img = cv2.rotate(img, cv2.ROTATE_180)

        # First color detection
        hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lowerLimit, upperLimit = get_limits(color=detected_color)
        mask = cv2.inRange(hsvImg, lowerLimit, upperLimit)

        # Second color detection
        lowerLimit2, upperLimit2 = get_limits(color=detected_color2)
        mask2 = cv2.inRange(hsvImg, lowerLimit2, upperLimit2)

        # Find contours for the first color (red)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w >= min_width and h >= min_height:  # Filter out small boxes
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                center_x = x + w // 2
                cv2.line(img, (center_x, y), (center_x, y + h), (255, 0, 0), 2)

        # Find contours for the second color (yellow)
        contours2, _ = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours2:
            x, y, w, h = cv2.boundingRect(contour)
            if w >= min_width and h >= min_height:  # Filter out small boxes
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
                center_x = x + w // 2
                cv2.line(img, (center_x, y), (center_x, y + h), (255, 0, 0), 2)

        # Show webcam
        cv2.imshow('frame', img)

        if cv2.waitKey(40) & 0xFF == ord('q'):
            global running
            running = False
            break

# Variables loops
def variables():
    while running:
        # Example: Count laps and other stuff like that
        time.sleep(1)

# MAIN FUNCTION
def main():
    global running

    # Initialize camera
    picam2 = initialize_camera()
    if not picam2:
        return

    # Define the serial port
    port = '/dev/ttyACM0'

    # Check if the serial port exists
    if not os.path.exists(port):
        print(f"Serial port {port} does not exist.")
        return

    ser = establish_serial_connection(port, 115200, timeout=5)
    if not ser:
        return

    # Start the threads
    arduino_thread = threading.Thread(target=read_arduino_thread, args=(ser,))
    camera_thread = threading.Thread(target=camera_processing_thread, args=(picam2,))
    log_thread = threading.Thread(target=variables)

    arduino_thread.start()
    camera_thread.start()
    log_thread.start()

    # Wait for threads to complete
    arduino_thread.join()
    camera_thread.join()
    log_thread.join()

    # Clean up
    if picam2:
        picam2.stop()
        print("Successfully stopped camera")
    cv2.destroyAllWindows()
    ser.close()
    print("Serial connection closed.")

if __name__ == "__main__":
    main()
