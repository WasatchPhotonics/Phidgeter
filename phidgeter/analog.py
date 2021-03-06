""" logging and convenience functions for Phidgets analog out.

Usage:
    alg = Analog()
    alg.zero_enable()

All connections are made and closed during the operations for that
analog output. The connection is not kept open.
"""

import logging

from Phidgets.PhidgetException import PhidgetException
from Phidgets.Devices.Analog import Analog

class AnalogOut(object):
    """ Class wraps language around the  PhidgetAnalog 4-Output
        ID: 1002_0 analog output device.
    """
    def __init__(self, in_serial=None):

        # http://victorlin.me/posts/2012/08/26/\
        # good-logging-practice-in-python
        self.log = logging.getLogger(__name__)
        if in_serial != None:
            # On odroid C1, int conversion raises null byte in argument
            # strip out the null byte first
            in_serial = in_serial.strip('\0')
            self._serial = int(in_serial)
        else:
            self._serial = None
        self.log.debug("Start of phidgeter with serial: %s" % in_serial)

    def open_phidget(self):
        self.log.debug("Attempting to open phidget")

        self.interface = Analog()

        if self._serial != None:
            self.log.debug("Attempt to open serial: %s" % self._serial)
            self.interface.openPhidget(self._serial)
        else:
            self.log.debug("Attempt to open first found")
            self.interface.openPhidget()

        wait_interval = 10300
        self.log.debug("Wait for attach %sms" % wait_interval)
        self.interface.waitForAttach(wait_interval)

        self.log.info("Opened phidget")
        return 1

    def close_phidget(self):
        self.log.debug("Attempting to close phidget")
        self.interface.closePhidget()
        self.log.info("Closed phidget")
        return 1

    def change_enable(self, output=0, status=0):
        """ Toggle the enable of the phidget analog output line to
            enable(1) or disable(0) status
        """
        self.interface.setEnabled(output, status)
        return 1

    def open_operate_close(self, output, status):
        """ Open the phidget, change the enable status of the analog
            output, close phidget.
        """
        self.open_phidget()
        result = self.change_enable(output, status)
        self.close_phidget()
        return result

    def open_toggle_close(self, output):
        """ Find the current enable status of the specified output, and
            set the status to the opposite.
        """
        self.open_phidget()
        curr_state = self.interface.getEnabled(output)
        res_volt = self.interface.setVoltage(output, 3.3)
        result = self.change_enable(output, not curr_state)
        self.close_phidget()
        return result

    def zero_enable(self):
        return self.open_operate_close(output=0, status=1)

    def zero_disable(self):
        return self.open_operate_close(output=0, status=0)

    def zero_toggle(self):
        return self.open_toggle_close(output=0)


    def two_enable(self):
        return self.open_operate_close(output=2, status=1)

    def two_disable(self):
        return self.open_operate_close(output=2, status=0)

    def two_toggle(self):
        return self.open_toggle_close(output=2)
