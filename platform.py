#!/usr/bin/env python3
from time import sleep

class Platform:
    def __init__(self, top=10, bottom=0, error=0.5, delay=0.01):
        # heights of top and bottom of lead screw in mm
        self.TOP = top
        self.BOTTOM = bottom

        # current height of platform in mm
        self.height = self.TOP

        # some height in mm
        self.error = error

        # delay in ms
        self.delay = delay

        # pin numbers for devices
        self.GPIO = {
            "microscope" : 1,
            "uv-camera" : 2,
            "flashlight" : 3,
            "brush" : 4,
            "platform": 5
        }

    # control_platform
    # receives a height (mm) to move the platform
    # returns current platform height (int) and finished moving (bool).
    def set_height(height):
        if(height > self.height and height < self.TOP):
            print("moving platform up")
            sleep(self.delay)
            self.height = height

        elif(height < self.height and height > self.BOTTOM):
            print("moving platform down")
            sleep(self.delay)
            self.height = height

        # turn on platform motor using self.GPIO["platform"]

        # INTERRUPTS ---------------- TO DO!!!
        if(upper_limit_is_pressed is True):
            print("stop moving platform AND move down some")
            sleep(self.delay)
            self.height = height - self.error

        elif(lower_limit_is_pressed is True):
            print("stop moving platform AND move up some")
            sleep(self.delay)
            self.height = height + self.error

        elif(reached_floor is True):
            print("stop moving platform AND move up some")
            sleep(self.delay)
            self.height = height + self.error

        # if interrupted, reset platform using self.GPIO["platform"]

        return self.height, True

    # GETTERS
    def get_height(self):
        return self.height
    
    def get_top(self):
        return self.TOP
    
    def get_bottom(self):
        return self.BOTTOM

    def get_error(self):
        return self.error

    def get_gpio_pins(self):
        return self.GPIO

    # SETTERS
    def set_top(self, top):
        self.TOP = top

    def set_bottom(self, bottom):
        self.BOTTOM = bottom

    def set_error(self, error):
        self.error = error

    # DEVICES
    def device(self, device, status):
        message = "Turning off"
        if(status is True):
            message = "Turning on"

        if(device is "microscope"):
            pin = self.GPIO["microscope"]
            print("{} {} on pin {}".format(message, device, pin))

            # turn on/off microscope
            # stream to basestation via flask server?

        elif(device is "uv-camera"):
            pin = self.GPIO["uv-camera"]
            print("{} {} on pin {}".format(message, device, pin))

            # turn on/off uv camera
            # stream to basestation via flask server?
        
        elif(device is "ir-camera"):
            print("{} {}".format(message, device))

            # turn on/off ir camera
            # stream to basestation via flask server?

        elif(device is "flashlight"):
            pin = self.GPIO["flashlight"]
            print("{} {} on pin {}".format(message, device, pin))

            # turn on/off flashlight

        elif(device is "brush"):
            pin = self.GPIO["brush"]
            print("{} {} on pin {}".format(message, device, pin))

            # turn on/off brush