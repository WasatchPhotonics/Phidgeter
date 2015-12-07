""" temperature - logging and convenience functions for phidgets
wired and ir temperature sensors.
"""

import logging

#from Phidgets.PhidgetException import PhidgetException
#from Phidgets.Devices.InterfaceKit import InterfaceKit
#from Phidgets.Devices.TemperatureSensor import TemperatureSensor, ThermocoupleType

from Phidgets.PhidgetException import PhidgetException
from Phidgets.Devices.TemperatureSensor import TemperatureSensor

log = logging.getLogger(__name__)

class IRSensor(object):
    """ Like IR sensor below, but stripped down to be more close to the demo
    python file. Why? Run it with the test above and see that it fails on
    openPhidget even though everything looks the same.
    """

    def __init__(self,serial=None):
        log.info("Start of init")
        self._serial = serial

    def open_phidget(self):
        #Create an temperaturesensor object
        try:
            temperatureSensor = TemperatureSensor()
        except RuntimeError as e:
            print("Runtime Exception: %s" % e.details)
            print("Exiting....")
            exit(1)

        try:
            temperatureSensor.openPhidget()
        except PhidgetException as e:
            print("Phidget Exception %i: %s" % (e.code, e.details))
            print("Exiting....")
            exit(1)

        try:
            temperatureSensor.waitForAttach(10000)
        except PhidgetException as e:
            print("Phidget Exception %i: %s" % (e.code, e.details))
            try:
                temperatureSensor.closePhidget()
            except PhidgetException as e:
                print("Phidget Exception %i: %s" % (e.code, e.details))
                print("Exiting....")
                exit(1)
            print("Exiting....")
            exit(1)

        self.sensor = temperatureSensor
        return 1


    def close_phidget(self):
        log.debug("Attempting to close phidget")
        self.sensor.closePhidget()
        log.info("Closed phidget")
        return 1

    def get_temperature(self, thermocouple=0):
        sval = self.sensor.getTemperature(thermocouple)
        return sval

    def get_ambient(self):
        sval = self.sensor.getAmbientTemperature()
        return sval


