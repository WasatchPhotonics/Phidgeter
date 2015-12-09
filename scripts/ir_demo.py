import time

from phidgeter.temperature import IRSensor

if __name__ == "__main__":
    ir_temp = IRSensor()
    ir_temp.open_phidget()
    while(1):
        print ir_temp.get_temperature()
        time.sleep(0.10)

