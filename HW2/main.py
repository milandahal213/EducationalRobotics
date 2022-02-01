# LSM9DS1 Gyro example.
import time
from lsm6dsox import LSM6DSOX

from machine import Pin, I2C
lsm = LSM6DSOX(I2C(0, scl=Pin(13), sda=Pin(12)))

while (True):
    print('{"wx":%8.3f,"wy":%8.3f,"wz":%8.3f}'%(lsm.read_gyro()))
    time.sleep_ms(10)

