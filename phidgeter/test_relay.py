import unittest
import time
import testfixtures # for log capture

from phidgeter.relay import Relay

class Test(unittest.TestCase):

    def setUp(self):
        from testfixtures import LogCapture
        self.log_capture = LogCapture() 
        self.log_group  = 'phidgeter.relay'
        self.lvl = 'DEBUG'

    def tearDown(self):
        self.log_capture.uninstall()

    def test_log_captures(self):
        # verification of log matching functionality
        from logging import getLogger
        getLogger().info('a message')
        self.log_capture.check(('root', 'INFO', 'a message'))

    def test_zero_on_off_toggle(self):
        phd_relay = Relay()
        result = phd_relay.zero_off()
        self.assertTrue(result, "Successfully turned off")

        result = phd_relay.zero_on()
        self.assertTrue(result, "Successfully turned off")

        result = phd_relay.zero_toggle()
        self.assertTrue(result, "Successfully toggled")

    def test_one_on_off_toggle(self):
        phd_relay = Relay()
        result = phd_relay.one_off()
        self.assertTrue(result, "Successfully turned off")

        result = phd_relay.one_on()
        self.assertTrue(result, "Successfully turned off")

        result = phd_relay.one_toggle()
        self.assertTrue(result, "Successfully toggled")

    def test_two_on_off_toggle(self):
        phd_relay = Relay()
        result = phd_relay.two_off()
        self.assertTrue(result, "Successfully turned off")

        result = phd_relay.two_on()
        self.assertTrue(result, "Successfully turned off")

        result = phd_relay.two_toggle()
        self.assertTrue(result, "Successfully toggled")

    def test_three_on_off_toggle(self):
        phd_relay = Relay()
        result = phd_relay.three_off()
        self.assertTrue(result, "Successfully turned off")

        result = phd_relay.three_on()
        self.assertTrue(result, "Successfully turned off")

        result = phd_relay.three_toggle()
        self.assertTrue(result, "Successfully toggled")


    def test_open_phidget(self):
        """ Apparently, LogCapture is setup to compare the entire log
         entries at once. So go through all of the operations, then
         check the total log output at the end.
        """
        phd = Relay()
        self.assertTrue(phd.zero_on())

        gr = self.log_group
        self.log_capture.check(
            (gr, "DEBUG", "Start of phidgeter with serial: None"),
            (gr, "DEBUG", "Attempting to open phidget"),
            (gr, "DEBUG", "Attempt to open first found"),
            (gr, "DEBUG", "Wait for attach 10300ms"),
            (gr, "INFO", "Opened phidget"),
            (gr, "DEBUG", "Attempting to close phidget"),
            (gr, "INFO", "Closed phidget")
            )

    def test_phidget_by_serial(self):
        # Get the serial number of the phidget from the usb descriptor
        serial = self.find_serial()

        # connect to that phidget precisely
        phd = Relay(serial)
        self.assertTrue(phd.zero_on())

    def find_serial(self):
        """ On linux only, use pyusb to enumerate all devices connected
        to the bus, return the string from the usb descriptor, which is
        the device serial number.
        """
        import platform
        if platform.system() != "Linux":
            return self.find_windows_serial()

        print "Finding serial number using pyusb"
        import usb
        for bus in usb.busses():
            devices = bus.devices
            for dev in devices:
                if dev.idVendor == 0x06c2:
                    print "  idVendor:",hex(dev.idVendor)
                    print "  idProduct:",hex(dev.idProduct)
                    ld = dev.open()
                    local_serial = ld.getString(dev.iSerialNumber, 256)
                    return local_serial

        raise ValueError("Can't find phidget (linux)")

    def find_windows_serial(self):
        """ On windows, the phidget appears as an HID, and will not be
        enumerated by pyusb. Use the windows management information command to
        find ther deviceid, which has the serial number at the end.
        """

        from subprocess import Popen, PIPE
        
        print "Finding serial number using wmic"

        # Be careful how quotres are used in windows .bat files. 
        wmic_cmd = "wmic path CIM_LogicalDevice where " + \
                   "\'DeviceID like \"%%VID_06C2%%\"\' get /value"

        # Can call popen directly, if you can figure out the escaping
        bat_out = open("wmic_cmd.bat", "w")
        bat_out.write(wmic_cmd)
        bat_out.close()

        sp = Popen("wmic_cmd.bat", stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = sp.communicate()

        # on the command line stdout is the return code, stderr is the
        # response of the wmic command. In popen land it is reversed.
        # Mogrify the string to be the end of the deviceid line, and
        # nothing after
        for line in stdout.split("\r"):
            if "DeviceID=USB" in line:
                local_serial = line.split("\\")[-1]
                local_serial = local_serial.split("\r")[0]
                return local_serial

        return "serial not found"

if __name__ == "__main__":
    unittest.main()
