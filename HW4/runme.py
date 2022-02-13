import servoM
import IK
import time

time.sleep(3)

s1=servoM.Servo(15)
s2=servoM.Servo(17)
s1.move(0)
s2.move(0)

length=6
startPointX=4
startPointY=4
delay=0.05

for i in range(length):
	a,b = IK.invK(startPointX,startPointY + i,10,11)
	s1.move(90+a)
	s2.move(b)
	time.sleep(delay)

for i in range(length):
	a,b = IK.invK(startPointX + i, startPointY + length,10,11)
	s1.move(90+a)
	s2.move(b)
	time.sleep(delay)

for i in range(length):
	a,b = IK.invK(startPointX + length, startPointY + length -i,10,11)
	s1.move(90+a)
	s2.move(b)
	time.sleep(delay)

for i in range(length):
	a,b = IK.invK(startPointX + length - i ,startPointY,10,11)
	s1.move(90+a)
	s2.move(b)
	time.sleep(delay)