from machine import Pin, PWM
import utime

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
pos4 = Count(Pin(29, Pin.IN),Pin(28, Pin.IN))

old1 = -1
old2 = -1
old3 = -1
old4 = -1

while True:
    utime.sleep(0.1)  #no need to update too fast
    counter1 = pos1.value()
    counter2 = pos2.value()
    counter3 = pos3.value()
    counter4 = pos4.value()
    if counter1 != old1:  # only print if the counter has changed
        print("Motor1 ",counter1)
    if counter2 != old2:  # only print if the counter has changed
        print("Motor2 ",counter2)
    if counter3 != old3:  # only print if the counter has changed
        print("Motor3 ",counter3)
    if counter4 != old4:  # only print if the counter has changed
        print("Motor4 ",counter4)
    old1 = counter1
    old2 = counter2
    old3 = counter3
    old4 = counter4