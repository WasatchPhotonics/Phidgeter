# Simulate a primitive function generator by issuing a 3.3V pulse every
# interval

import time

from phidgeter.analog import AnalogOut

status = 0
if __name__ == "__main__":
    alg_out = AnalogOut()
    while(1):
        print "\rstatus: %s" % status,
        if status == 0:
            status = 1
        else:
            status = 0
        alg_out.two_toggle()
        time.sleep(1)

