
_COMMAND_MODE = 0x80
_DATA_MODE = 0x40
_NORMAL_DISPLAY = 0xA6
_DISPLAY_OFF = 0xAE
_DISPLAY_ON = 0xAF
_INVERSE_DISPLAY = 0xA7
_SET_BRIGHTNESS = 0x81
SET_COMMAND_LOCK = const(0xFD)
HORIZONTAL = 0x00
VERTICAL = 0x01
PAGE = 0x02

SET_DISP = const(0xAD)
SET_DISP_START_LINE = const(0xA1)


# Create I2C object
from pyb import I2C
i2c = I2C(2, I2C.MASTER)  
devices = i2c.scan()
import LOGO


address=60

def send_data(data):
	i2c.send(bytearray([_DATA_MODE ,data]),address)
	

def send_command(cmd):
	i2c.send(bytearray([_COMMAND_MODE ,cmd]),address)


def set_cursor(row, column):
    send_command(0xB0 + row)
    send_command(0x00 + (8*column & 0x0F))
    send_command(0x10 + ((8*column>>4)&0x0F))

def clear():
    send_command(_DISPLAY_OFF)
    for i in range(16):
    	set_cursor(i, 0)
        puts(' ' * 16)
 
    send_command(_DISPLAY_ON)
    set_cursor(0, 0)

def puts(text):
    for c in text:
        putc(c)

def putc(c):
    C_add = ord(c)
    if C_add < 32 or C_add > 127:     # Ignore non-printable ASCII characters
        c = ' '
        C_add = ord(c)

    for i in range(0, 8):
        send_data( LOGO.BasicFont[C_add-32][i])

import time
def drawBitmap(x,y,data,width,delay=0.1):
    set_cursor(x,y)
    count=0
    for i in range(len(data)):
        time.sleep(delay)
        if(i%width==0):
            set_cursor(x+count,y)
            count=count+1
        send_data(data[i])
        

send_command(_DISPLAY_OFF)
send_command(_NORMAL_DISPLAY)
send_command(0x20)
send_command(HORIZONTAL)
clear()
send_command(_DISPLAY_ON)

set_cursor(0,0)
