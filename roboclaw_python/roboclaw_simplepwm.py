import time
from roboclaw_3 import Roboclaw

#Windows comport name
rc = Roboclaw("/dev/ttyS0",38400)
#Linux comport name
#rc = Roboclaw("/dev/ttyACM0",115200)

if(rc):
	print("Roboclaw connected")

rc.Open()
address = 0x80

while(1):
	rc.ForwardM1(address,64)	#1/4 power forward
	rc.BackwardM2(address,64)
	print("Backward")	#1/4 power backward
	time.sleep(2)
	
	rc.BackwardM1(address,64)	#1/4 power backward
	rc.ForwardM2(address,64)
	print("Forward")	#1/4 power forward
	time.sleep(2)

	rc.BackwardM1(address,0)	#Stopped
	rc.ForwardM2(address,0)	
	print("Stop")	#Stopped
	time.sleep(2)

	m1duty = 16
	m2duty = -16
	rc.ForwardBackwardM1(address,64+m1duty)	#1/4 power forward
	rc.ForwardBackwardM2(address,64+m2duty)	#1/4 power backward
	time.sleep(2)
	
	m1duty = -16
	m2duty = 16
	rc.ForwardBackwardM1(address,64+m1duty)	#1/4 power backward
	rc.ForwardBackwardM2(address,64+m2duty)	#1/4 power forward
	time.sleep(2)

	rc.ForwardBackwardM1(address,64)	#Stopped
	rc.ForwardBackwardM2(address,64)	#Stopped
	time.sleep(2)
	