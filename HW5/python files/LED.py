from machine import SPI, Pin
import machine
import time

LEDR=26
LEDB=27
LEDG=25

INPUT=1
OUTPUT=0

START_CMD = 224 #'\xE0'
SET_PIN_MODE = 80 #'\x50'
SET_DIGITAL_WRITE     = 81 #'\x51'
SET_DIGITAL_READ     = 83 #'\x53'
END_CMD    = 238 #'\xEE'
DUMMY_DATA = 255 #'\xFF'
NO_LAST_PARAM  = 0
LAST_PARAM     = 1

REPLY_FLAG= 127 #~(1<<7)

SlaveSelect=machine.Pin(9, Pin.OUT)
SlaveReady=machine.Pin(10,Pin.IN)
SlaveReset=machine.Pin(3, Pin.OUT)
NinaGPIO0=machine.Pin(2,Pin.OUT)

spi = machine.SPI(1,
                baudrate=8000000,
                polarity=0,
                phase=0,
                bits=8,
                firstbit=machine.SPI.MSB,
                sck=machine.Pin(14),
                mosi=machine.Pin(11),
                miso=machine.Pin(8))

'''
bytearray(b'\xe0')
bytearray(b'P')
bytearray(b'\x02')
bytearray(b'\x01')
bytearray(b'\x1a')
bytearray(b'\x01')
bytearray(b'\x00')
bytearray(b'\xee')
bytearray(b'\xff')
'''

def setPin(pin,value):
    Reset()
    spi.init()
    fred = [0xE0,0x50,0x02,0x01,pin,0x01,value,0xEE,0xFF]
    SlaveSelect(0)
    while(not SlaveReady()):
        pass
    spi.write(bytearray(fred))

    SlaveSelect(1)
    spi.deinit()

'''
bytearray(b'\xe0')
bytearray(b'Q')
bytearray(b'\x02')
bytearray(b'\x01')
bytearray(b'\x1a')
bytearray(b'\x01')
bytearray(b'\x00')
bytearray(b'\xee')
bytearray(b'\xff')
'''
def digitalWrite(pin,value):
    spi.init()
    fred = [0xE0,0x51,0x02,0x01,pin,0x01,value,0xEE,0xFF]
    SlaveSelect(0)
    while(not SlaveReady()):
        pass
    spi.write(bytearray(fred))
    SlaveSelect(1)
    spi.deinit()

def Reset():
    NinaGPIO0(1)
    SlaveSelect(1)
    SlaveReset(0)
    time.sleep(0.010)
    SlaveReset(1)
    time.sleep(0.750)
    NinaGPIO0(0)

