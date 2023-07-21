import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2

TRIG = 22
ECHO = 27

Ab = AlphaBot2()
repeat_distance = []

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ECHO,GPIO.IN)

def Distance():
	GPIO.output(TRIG,GPIO.HIGH)
	time.sleep(0.000015)
	GPIO.output(TRIG,GPIO.LOW)
	while not GPIO.input(ECHO):
		pass
	t1 = time.time()
	while GPIO.input(ECHO):
		pass
	t2 = time.time()
	return (t2-t1)*34000/2
	
print("Ultrasonic_Obstacle_Avoidance")
try:
	while True:
		repeat_distance = Distance()
		Dist = Distance()
		print("Distance = %0.2f cm"%Dist)
		if Dist < 5:
			Ab.stop()
			Ab.backward()
			#Ab.right()
			Ab.left()
		elif repeat_distance == Dist:
			Ab.backward()
		
		else:
			Ab.forward()
		#time.sleep(0.02)

except KeyboardInterrupt:
	GPIO.cleanup();
