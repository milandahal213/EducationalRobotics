from machine import Pin, PWM
from time import sleep
import time

class Servo:

      def __init__(self, pin):
            self.pin = pin
            self.servo = PWM(Pin(pin))
            self.servo.freq(50)

      def move(self, angle):
            if (angle>=0 and angle<=180):
                  temp=1613 + 37.411 * angle
                  self.servo.duty_u16(int(temp))
            else:
                  pass
