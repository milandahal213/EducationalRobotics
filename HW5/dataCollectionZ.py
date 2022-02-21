import time, math, array
from lsm6dsox import LSM6DSOX
from machine import Pin, I2C

lsm = LSM6DSOX(I2C(0, scl=Pin(13), sda=Pin(12)))
file = open("testData.csv","w")
n = 100
testArry = [0]*n
targetTime = 1000
def read_accel():
    start = time.ticks_ms()
    while(lsm.read_accel()[2]>0.9):
        current = time.ticks_ms()
        if((current-start)>2000):
            break
        pass
    #start = time.ticks_ms()
    for i in range(len(testArry)):
        accel = lsm.read_accel()
        zaccel = accel[2]
        testArry[i] = zaccel
        time.sleep_ms(targetTime//n)
    #end = time.ticks_ms()
    #print(end-start)
    #print("ool")
        
def find_std():
    mean = sum(testArry) / len(testArry)   # mean
    var  = sum(pow(x-mean,2) for x in testArry) / len(testArry)  # variance
    std  = math.sqrt(var)  # standard deviation
    print('mean: '+str(mean))
    print('var: '+str(var))
    print('std: '+str(std))
    return std

def write_to_file(std):
    catagory = int(input("Was that 1 tap [1] 2 taps [2] or 3 taps[3]? Or no taps [0]? ")) - 1
    if catagory == -1:
        catagory=4

    print(std)
    print(catagory)
    file.write(str(std) + "," + str(catagory)+'\n')

def main():
    run = True
    while run:
        ans = input("test? (y/n)\n")
        if ans == 'y':

            read_accel()
            std = find_std()
            write_to_file(std)
        elif ans == 'n':
            run = False
    file.close()
    #
#ain()
