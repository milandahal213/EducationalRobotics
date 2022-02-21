import time
from lsm6dsox import LSM6DSOX
import gc
from machine import Pin, I2C
lsm = LSM6DSOX(I2C(0, scl=Pin(13), sda=Pin(12)))
i=0
sample=[0]*100
val=["Rock","Paper","Scissors","Rock","Paper","Scissors","Rock","Paper","Scissors","Rock","Paper","Scissors",]

print("Ready")
def data():
    while  True:
        gc.collect()
        z = 1 - lsm.read_accel()[2]
        if (z>0.1):
            for i in range (100):
                z = 1 - lsm.read_accel()[2]
                sample[i]=z
                time.sleep(0.001)
            print(sample)
            break
        time.sleep(0.01)


def ready():
    global i
    if (i==6):
        time.sleep(5)
        i=0
    else:
        i=i+1

    
    time.sleep(2)
    print("*",val[i],"#")

