from machine import Pin, PWM
import utime
from machine import UART
import time
import json
import math

dataCount=0
data=[[-4, 37, 0, 143], [43, 36, 728, 1161]]
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


bark=Pin(18,Pin.OUT)
#pin numbers for Encoders
#15- D2
#25- D3
#16- D4
#17- D5

#pin numbers for PWMs 
#26 - A0
#27 - A1
#28 - A2
#29 - A3

duty = 0 #between 0-65000
pwm=[]
pos=[0]*4
PWMPins=[26,27,28,29]
EncoderPins=[16,17,15,25] 

for i in range(2):
    pos[i]=Count(Pin(EncoderPins[i*2], Pin.IN),Pin(EncoderPins[i*2+1], Pin.IN))
    pwm.append((PWM(Pin(PWMPins[i*2])), PWM(Pin(PWMPins[i*2+1]))))

    pwm[i][0].freq(100)
    pwm[i][1].freq(100)
    
    pwm[i][0].duty_u16(duty)
    pwm[i][1].duty_u16(duty)



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
    print("Distance is",currDist)
    if(currDist>10):
        bark.off()
        bark.on()
        return(-1)
    else:
        return givenArr[minDistIndex]

def calculateDist(x1, y1, x2, y2):
    xDiff = x2 - x1
    yDiff = y2 - y1
    xSquared = pow(xDiff, 2)
    ySquared = pow(yDiff, 2)
    diff = xSquared + ySquared
    return math.sqrt(diff)


def moveMotors(turnTo):

    while (abs(pos[0].value()-turnTo[2])>50 or abs(pos[1].value()-turnTo[3])>50 ):
        if(turnTo[2]-pos[0].value()>10):
            duty1_0=15000
            duty2_0=0
        elif(turnTo[2]-pos[0].value()<10):
            duty1_0=0
            duty2_0=15000
        if(turnTo[3]-pos[1].value()>10):
            duty1_1=15000
            duty2_1=0
        elif(turnTo[3]-pos[1].value()<10):
            duty1_1=0
            duty2_1=15000

        
        pwm[0][0].duty_u16(duty1_0)
        pwm[0][1].duty_u16(duty2_0)
        pwm[1][0].duty_u16(duty1_1)
        pwm[1][1].duty_u16(duty2_1)


    pwm[0][0].duty_u16(0)
    pwm[0][1].duty_u16(0)
    pwm[1][0].duty_u16(0)
    pwm[1][1].duty_u16(0)

bark.off()
bark.on()

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
            data.append([jsonStr["a"],jsonStr["b"],pos[0].value(),pos[1].value()])
            dataCount=dataCount+1
            print(data)
        elif(jsonStr["mode"]=='R'):
            turnTo=findPoints(int(jsonStr["a"]),int(jsonStr["b"]),data)
            if(turnTo==-1):
                pass
            else:
                print("I need to turn to this to angles :")
                print(turnTo)
                moveMotors(turnTo)
                f=open("data.txt","w")
                f.write(str(data))
                f.close()
        uart.write("Good")
    except:
        uart.write("err")
        print("there was some error ... don't worry")
