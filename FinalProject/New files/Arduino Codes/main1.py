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
pos=[0]*4
EncoderPins=[15,25,16,17,18,19,27,26]
for i in range (4):
    print(i)
    print(EncoderPins[i*2])
    print(EncoderPins[i*2+1])
    pos[i]=Count(Pin(EncoderPins[i*2], Pin.IN),Pin(EncoderPins[i*2+1], Pin.IN))


'''   
pos1 = Count(Pin(15, Pin.IN),Pin(25, Pin.IN))
pos2 = Count(Pin(16, Pin.IN),Pin(17, Pin.IN))
pos3 = Count(Pin(18, Pin.IN),Pin(19, Pin.IN))
pos4 = Count(Pin(27, Pin.IN),Pin(26, Pin.IN))
'''

old1 = -1
old2 = -1
old3 = -1
old4 = -1

pwm1 = PWM(Pin(7))
pwm2 = PWM(Pin(4))
pwm3 = PWM(Pin(21))
pwm4 = PWM(Pin(5))
duty = 63000 #between 0-65000

pwm1.freq(100)
pwm2.freq(100)
pwm3.freq(100)
pwm4.freq(100)
import math
pwm1.duty_u16(0)
pwm2.duty_u16(0)

def findPoints(x, y, givenArr):
    minDistIndex = 0
    currDist = calculateDist(x, y, givenArr[0][0], givenArr[0][1])
    for i in range(len(givenArr)):
        currList = givenArr[i]
        currx = currList[0]
        curry = currList[1]
        dist = calculateDist(currx, curry, x, y)
        if (dist < currDist):
            currDist = dist
            minDistIndex = i
    return givenArr[minDistIndex]

def calculateDist(x1, y1, x2, y2):
    xDiff = x2 - x1
    yDiff = y2 - y1
    xSquared = pow(xDiff, 2)
    ySquared = pow(yDiff, 2)
    diff = xSquared + ySquared
    return math.sqrt(diff)


def moveMotors(turnTo):
    while (abs(pos[0].value()-turnTo[2])>50):
        if(turnTo[2]>pos[0].value()):
            duty1=10000
            duty2=0

        else:
            duty1=0
            duty2=10000

        
        pwm1.duty_u16(duty1)
        pwm2.duty_u16(duty2)

        print(pos[0].value(),turnTo[2])

    pwm1.duty_u16(0)
    pwm2.duty_u16(0)

while True:
    fromCamera=''
    fromCamera=uart.readline()
    time.sleep(0.5)
    print(fromCamera)
    while((not fromCamera) or uart.any()):
        time.sleep(0.5)
        fromCamera=uart.readline()


    try:   
        print(fromCamera) 
        strFromCamera=fromCamera.decode()
        newstr=strFromCamera.replace('\'','\"')
        jsonStr=json.loads(newstr)
        print(jsonStr)
        utime.sleep(0.5)
        print(jsonStr["mode"])

        if (jsonStr["mode"]=='T'):
            data.append([jsonStr["a"],jsonStr["b"],pos[0].value(),pos[1].value(),pos[2].value(),pos[3].value()])
            dataCount=dataCount+1
            print(data)
        elif(jsonStr["mode"]=='R'):
            turnTo=findPoints(int(jsonStr["a"]),int(jsonStr["b"]),data)
            print("I need to turn to this")
            moveMotors(turnTo)
    except:
        print("there was some error ... don't worry")
