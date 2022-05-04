from machine import Pin, PWM
import utime
from machine import UART
import time
import json
dataCount=0
data=[]
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

class Count(object):
    def __init__(self,A,B):
        self.A = A
        self.B = B
        self.counter = 0
        A.irq(self.cb,self.A.IRQ_FALLING|self.A.IRQ_RISING) #interrupt on line A
        B.irq(self.cb,self.B.IRQ_FALLING|self.B.IRQ_RISING) #interrupt on line B

    def cb(self,msg):
        other,inc = (self.B,1) if msg == self.A else (self.A,-1) #define other line and increment
        self.counter += -inc if msg.value()!=other.value() else  inc #XOR the two lines and increment
        
    def value(self):
        return self.counter


pos1 = Count(Pin(15, Pin.IN),Pin(25, Pin.IN))
pos2 = Count(Pin(16, Pin.IN),Pin(17, Pin.IN))
pos3 = Count(Pin(18, Pin.IN),Pin(19, Pin.IN))
pos4 = Count(Pin(27, Pin.IN),Pin(26, Pin.IN))

old1 = -1
old2 = -1
old3 = -1
old4 = -1

while True:
    fromCamera=uart.readline()
    time.sleep(0.1)
    while(not fromCamera or uart.any()):
        time.sleep(0.1)
        fromCamera=uart.readline()

    try:    
        strFromCamera=fromCamera.decode()
        newstr=strFromCamera.replace('\'','\"')
        jsonStr=json.loads(newstr)
        print(jsonStr)
        #look for signal from OpenMV to store data
        #find the positions of all the values and create an array along with the "data" from OpenMV
        #save data in format OpenMV 
        utime.sleep(0.5)  #no need to update too fast
        print(jsonStr["mode"])

        if (jsonStr["mode"]=='T'):

            counter1 = pos1.value()
            counter2 = pos2.value()
            counter3 = pos3.value()
            counter4 = pos4.value()
            data.append([jsonStr["a"],jsonStr["b"],counter1,counter2,counter3,counter4])
            dataCount=dataCount+1
            print(data)
        elif(jsonStr["mode"]=='R'):
            pass
    except:
        print("there was some error ... don't worry                                                                                                                           ")
