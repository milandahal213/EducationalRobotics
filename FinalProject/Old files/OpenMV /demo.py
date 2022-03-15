
from pyb import UART
import sensor, image, time
uart = UART(1, 9600, timeout_char=1000)
uart.init(9600, bits=8, parity=None, stop=1, timeout_char=1000)
from pyb import Pin
import OLED,LOGO
pin0 = Pin('P3', Pin.IN, Pin.PULL_UP)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()

color = "Undetected"

# Capturing color thresholds center of the image.
r = [(320//2)-(50//2), (240//2)-(50//2), 10, 10]

# Color Tracking:
    # thresholds[L Min, L Max, A Min, A Max, B Min, B Max]
    # L - lightness
    # A - /green/red value
    # B - blue/yellow value

    # Generic thresholds:
    # thresholds = (30, 100, 15, 127, 15, 127) = red
                 # (1, 49, -14, 9, -11, 22) = black
                 # (40, 79, -21, 5, -18, 67) = yellow
                 # Can add more color thresholds here.

print(" ")
print("Hold OpenMV infront of objects to detect their color.")

for i in range(60):
    img = sensor.snapshot()
    img.draw_rectangle(r)

threshold = [50, 50, 0, 0, 0, 0] # Middle L, A, B values to inilialize.

while True:

    #mode=based on the QR code it can be either T or R
    mode='T'
    if(not pin0.value()):
        enteredTime=time.ticks_ms()
        while(not pin0.value()):
            if((time.ticks_ms()-enteredTime)>2000):
                img = sensor.snapshot()
                hist = img.get_histogram(roi=r)
                mid = hist.get_percentile(0.5)
                print(mid.a_value(),mid.b_value())
                OLED.drawBitmap(0,0,LOGO.eye,64,0)
                time.sleep(0.5)
                OLED.clear()
                print(type(mid.a_value()))
                uart.write(str({'mode':mode,'a':mid.a_value(),'b':mid.b_value()}))
                break
        while(pin0.value()):
            pass

