
from pyb import UART
import sensor, image, time
uart = UART(1, 9600, timeout_char=1000)
uart.init(9600, bits=8, parity=None, stop=1, timeout_char=1000)
from pyb import Pin
import OLED,LOGO
pin0 = Pin('P3', Pin.IN, Pin.PULL_UP)
buzz = Pin('P2', Pin.OUT, Pin.PULL_DOWN)





def buzzer(num):
    for i in range(num):
        buzz.on()
        time.sleep(0.15)
        buzz.off()
        time.sleep(0.1)


buzzer(5)
# Capturing color thresholds center of the image.
r = [(320//2)-(50//2), (240//2)-(50//2), 10, 10]

for i in range(60):
    img = sensor.snapshot()
    img.draw_rectangle(r)

threshold = [50, 50, 0, 0, 0, 0] # Middle L, A, B values to inilialize.

#mode=based on the QR code it can be either T or R
mode='R'


sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()

color = "Undetected"


#draw the eyeballs
OLED.drawBitmap(0,0,LOGO.eyeball,128,0)
OLED.drawBitmap(8,0,LOGO.eyeball,128,0)
while True:

    clock.tick()
    img = sensor.snapshot()
    codes = img.find_qrcodes()
    for code in codes:
        print(code.payload())
        if(code.payload()=='1'):
            mode='R'
            buzzer(3)
            print("R")
        else:
            mode='T'
            buzzer(2)
            print("?T")
    
    #draw the eye looking straight at user   
    OLED.drawBitmap(3,6,LOGO.iris,16,0)
    OLED.drawBitmap(12,6,LOGO.iris,16,0)  
    OLED.drawBitmap(3,1,LOGO.iris_r,16,0)
    OLED.drawBitmap(12,1,LOGO.iris_r,16,0)

    if(not pin0.value()):
        OLED.drawBitmap(3,6,LOGO.iris_r,16,0)
        OLED.drawBitmap(12,6,LOGO.iris_r,16,0)
        OLED.drawBitmap(3,1,LOGO.iris,16,0)
        OLED.drawBitmap(12,1,LOGO.iris,16,0)
        enteredTime=time.ticks_ms()
        while(not pin0.value()):
            if((time.ticks_ms()-enteredTime)>2000):
                img = sensor.snapshot()
                hist = img.get_histogram(roi=r)
                mid = hist.get_percentile(0.5)
                print(mid.a_value(),mid.b_value())
                OLED.drawBitmap(3,1,LOGO.iris_r,16,0)
                OLED.drawBitmap(12,1,LOGO.iris_r,16,0)
                OLED.drawBitmap(3,6,LOGO.iris_d,32,0)
                OLED.drawBitmap(11,6,LOGO.iris_d,32,0)
                time.sleep(0.5)
                OLED.drawBitmap(3,6,LOGO.iris_dr,32,0)
                OLED.drawBitmap(11,6,LOGO.iris_dr,32,0)
                #animate something here    

                if((abs(mid.a_value())+abs(mid.b_value()))>10):
                    uart.write(str({'mode':mode,'a':mid.a_value(),'b':mid.b_value()}))
                    #checking for error'
                    error=1
                    while(error==1):
                        from2040=uart.readline()
                        while(not from2040 or uart.any()):
                            time.sleep(0.1)
                            from2040=uart.readline()
                        strFrom2040=from2040.decode()
                        if(strFrom2040.find("err")>-1):
                            print("received an error... sending again")
                            uart.write(str({'mode':mode,'a':mid.a_value(),'b':mid.b_value()}))
                        else:
                            error=0

                    break
            else:
                img = sensor.snapshot()
                codes = img.find_qrcodes()
                for code in codes:
                    print(code.payload())
                    if(code.payload()=='1'):
                        mode='R'
                        print("R")
                    else:
                        mode='T'
                        print("1T")
    time.sleep(0.1)
