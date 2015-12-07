import time
import unittest
import testfixtures # for log capture

from phidgeter.temperature import IRSensor

class Test(unittest.TestCase):

    def setUp(self):
        from testfixtures import LogCapture
        self.log_capture = LogCapture()
        self.log_group  = "phidgeter.ir_temperature"
        self.lvl = "DEBUG"

    def tearDown(self):
        self.log_capture.uninstall()

    def test_log_captures(self):
        # verification of log matching functionality
        from logging import getLogger
        getLogger().info("a message")
        self.log_capture.check(("root", "INFO", "a message"))

    def test_sensor_is_available(self):
        ir_temp = IRSensor()
        assert ir_temp.open_phidget() == True
        assert ir_temp.get_temperature() >= 0.0
        assert ir_temp.close_phidget() == True

    def test_sensor_is_room_temperature(self):
        ir_temp = IRSensor()
        assert ir_temp.open_phidget() == True
        print ir_temp.get_temperature()
        assert ir_temp.get_temperature() >= 20.0
        assert ir_temp.close_phidget() == True

