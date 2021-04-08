#!/usr/bin/env python3
from time import sleep

class FunnelCake:
    def __init__(self):
        self.cur_sample = 0
        self.max_samples = 4
        self.cur_position = 0

        # angles for samples on arm in degrees
        self.angle = {
            "current" : 0,
            "sample-1" : 0,
            "sample-2" : 10,
            "sample-3" : 20,
            "sample-4" : 30,
            "sample-5" : 40,
            "pmt" : 50
        }

        # delays for collecting samples
        self.delay = {
            "vacuum" : 1,
            "water-pump" : 1,
            "cuvette-pump" : 1,
            "rotation" : 1,
            "record-data" : 1
        }

        # pin numbers for devices
        self.GPIO = {
            "vacuum" : 1,
            "water-pump" : 2,
            "cuvette-pump" : 3,
            "pmt" : 4
        }

    # GETTERS
    def get_position(self):
        return self.cur_position

    def current_sample(self):
        return self.cur_sample

    # collect
    # starts the process of collecting a sample. this should all be done
    #  autonomously.
    # returns the sample just collected (int) and that it has finished being
    #  collected (bool).
    def collect(self):
        if(self.cur_sample > self.max_samples):
            print("cannot collect any more samples!")
            return self.cur_sample, False

        print("collecting sample #{}".format(self.cur_sample))

        self.device("vacuum",True)
        sleep(self.delay["vacuum"])
        self.device("vacuum", False)

        self.device("water-pump", True)
        sleep(self.delay["water-pump"])
        self.device("water-pump", False)

        self.device("cuvette-pump", True)
        sleep(self.delay["cuvette-pump"])
        self.device("cuvette-pump", False)

        # rotate arm: current sample to pmt
        self.rotate_arm(5)
        sleep(self.delay["rotation"])

        # activate pmt & record/stream data
        self.device("pmt", True)
        sleep(self.delay["record-data"])

        # deactivate pmt & stop record/stream of data
        self.device("pmt", False)

        # rotate arm: to next sample
        if(self.cur_sample < self.max_samples):
            self.cur_sample += 1
            self.rotate_arm(self.cur_sample)
            sleep(self.delay["rotation"])

        return self.cur_sample, True

    # DEVICES
    def device(self, device, status):
        message = "Turning off"
        if(status is True):
            message = "Turning on"

        if(device is "vacuum"):
            pin = self.GPIO["vacuum"]
            print("{} {} on pin {}".format(message, device, pin))

            # turn on/off vacuum

        elif(device is "water-pump"):
            pin = self.GPIO["water-pump"]
            print("{} {} on pin {}".format(message, device, pin))

            # turn on/off water pump

        elif(device is "cuvette-pump"):
            pin = self.GPIO["cuvette-pump"]
            print("{} {} on pin {}".format(message, device, pin))

            # turn on/off cuvette pump

        elif(device is "pmt"):
            pin = self.GPIO["pmt"]
            print("{} {} on pin {}".format(message, device, pin))

            # turn on/off pmt
            # record data
            # stream back to basestation (website?)

    # rotate_arm
    # rotates arm to a requested position (0-4 being the samples
    #  and 5 being the PMT sensor.)
    # returns when it has completed (bool).
    def rotate_arm(self, position):
        angle = self.angle["current"]
        if(position is 0):
            angle = self.angle["sample-1"]
        elif(position is 1):
            angle = self.angle["sample-2"]
        elif(position is 2):
            angle = self.angle["sample-3"]
        elif(position is 3):
            angle = self.angle["sample-4"]
        elif(position is 4):
            angle = self.angle["sample-5"]

        # this is the pmt sensor position
        elif(position is 5):
            angle = self.angle["pmt"]

        # non-existent position requested
        else:
            return False

        print("requesting borealis rotate arm to {}".format(angle))
        # JOSH: request borealis to move and get a completed state
        # grpc?????
        
        self.cur_position = position
        self.angle["current"] = angle

        return True