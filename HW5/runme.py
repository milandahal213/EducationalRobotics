import servoM
import IK
import time
import math
import RGB

s1=servoM.Servo(15)
s2=servoM.Servo(17)
s1.move(90)
s2.move(0)

delay=0.3
l1=11
l2=10

def GoTo(x,y):
	if (math.sqrt(x*x + y*y)<(l1+l2)):
		a,b=IK.invK(x,y,l1,l2)
		s1.move(a+90)
		s2.move(b)
		RGB.GREEN(1)
		RGB.RED(0)
	else:
		RGB.GREEN(0)
		RGB.RED(1)


def run(positions):
	for i in positions:
		GoTo(i[0],i[1])
		time.sleep(delay)




def drawRect(startPointX=4,startPointY=4,length=6):
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