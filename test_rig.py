#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

motor = 26
led1 = 18
led2 = 23
led3 = 25
led4 = 5
led5 = 6
led6 = 21

vacuum = microscope = led1
water = uvcam = led2
cuvette = flashlight = led3
pmt = brush = led4
platform = led5
ircam = led6

def setup():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(motor, GPIO.OUT)
    
    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)
    GPIO.setup(led3, GPIO.OUT)
    GPIO.setup(led4, GPIO.OUT)
    GPIO.setup(led5, GPIO.OUT)
    GPIO.setup(led6, GPIO.OUT)

def test_leds(delay):
    GPIO.output(led1, GPIO.HIGH)
    sleep(delay)
    GPIO.output(led1, GPIO.LOW)

    GPIO.output(led2, GPIO.HIGH)
    sleep(delay)
    GPIO.output(led2, GPIO.LOW)

    GPIO.output(led3, GPIO.HIGH)
    sleep(delay)
    GPIO.output(led3, GPIO.LOW)

    GPIO.output(led4, GPIO.HIGH)
    sleep(delay)
    GPIO.output(led4, GPIO.LOW)

    GPIO.output(led5, GPIO.HIGH)
    sleep(delay)
    GPIO.output(led5, GPIO.LOW)

    GPIO.output(led6, GPIO.HIGH)
    sleep(delay)
    GPIO.output(led6, GPIO.LOW)

def test_motor(delay):
    """
    pwm = GPIO.PWM(motor, 1000)
    pwm.start(0)
    for dc in range(0,101,1):
        pwm.ChangeDutyCycle(dc)
        sleep(0.01)
    sleep(delay)
    for dc in range(100,-1,-1):
        pwm.ChangeDutyCycle(dc)
        sleep(0.01)
    pwm.stop()
    """

    GPIO.output(motor, GPIO.HIGH)
    sleep(delay)
    GPIO.output(motor, GPIO.LOW)

def test_device(device, has_motor):
    GPIO.output(device, GPIO.HIGH)
    GPIO.output(motor, GPIO.HIGH)
    sleep(3)
    GPIO.output(device, GPIO.LOW)
    GPIO.output(motor, GPIO.LOW)

def test_all_devices():
    # test motors
    test_device(vacuum, True)
    test_device(water, True)
    test_device(cuvette, True)

    test_device(brush, True)
    test_device(platform, True)

    # test other devices
    test_device(microscope, False)
    test_device(uvcam, False)
    test_device(flashlight, False)
    test_device(ircam, False)
    test_device(pmt, False)

def loop(delay):
    #test_leds(delay)
    test_motor(delay)

def main():
    setup()

    # test connections
    for x in range(3):
        loop(0.5)

    GPIO.cleanup()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
        GPIO.output(led3, GPIO.LOW)
        GPIO.output(led4, GPIO.LOW)
        GPIO.output(led5, GPIO.LOW)
        GPIO.output(led6, GPIO.LOW)
        GPIO.output(motor, GPIO.LOW)

        GPIO.cleanup()
