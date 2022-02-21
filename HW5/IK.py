from math import *
def invK(x,y,l1=5,l2=5):
	num1=x*x + y*y - l1*l1 -l2*l2
	denum1=2*l1*l2

	q2=degrees(acos(num1/denum1))

	num2=l2*sin(radians(q2))
	denum2= l1+l2*cos(radians(q2))

	A=degrees(atan(y/x))
	B=degrees(atan(num2/ denum2))

	q1= A - B

	print(q1,q2)
	
	return (q1,q2)