# Import standard python modules
import time
import datetime
import sys
import threading

# Import GPIO Module
import RPi.GPIO as GPIO

# Import paho MQTT Client
import paho.mqtt.client as mqtt


# Control of sincronization in Threads
lock = threading.RLock()

# Setup Sensor pin var
SENSOR_PIN = 5

# Setup var controls
showDataTime=5


# Define class for instance objects in threading
class MeasureData():
	def __init__(self, mqttClient):
		self.measureTime=0
		self.isMovement=False
		self.client=mqttClient


# Define functions for paralelism
def show_data(motionMeasure):
	counted=False
	while True:
		# show data every 20 seconds and reset countTimes
		if(int(time.time())%showDataTime==0): 
			if(not counted):
				lock.acquire()
				motionMeasure.client.publish("piso0/local0/tiempo", 
					motionMeasure.measureTime)
				motionMeasure.measureTime=0
				lock.release()
				counted=True
		else:
			counted=False


# Define callback functions which will be called when certain events happen.#
def on_connect(client, userdata, flags, rc):
	# Connected function will be called when the client connects.
	print("Conectado con codigo resultante:  "+str(rc))
	client.connectedFlag=True


def on_disconnect(client):
	# Disconnected function will be called when the client disconnects.
	print("¡Se ha Desconectado!")
	os._exit(1)


if(len(sys.argv)!=2):
	sys.stderr.write('Usage: "{0}" $hostAddress\n'.format(sys.argv[0]))
	os._exit(1)

## Global vars for function motion_pir ##
# Setup MQTT instance
client = mqtt.Client()

# Setup the callback functions
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# Setup Control vars
client.connectedFlag=False

# Connect to the Broker server.
print("conectando al broker")
client.connect(sys.argv[1], 1883, 60)
client.loop_start()

while not client.connectedFlag:
	print("Esperando conexión")
	time.sleep(1)

# object instance for global data in events (is handle with events)
totalMotionTime=MeasureData(client)

# Setup Threading, to show data every 20 seconds
hilo0=threading.Thread(target=show_data, args=[totalMotionTime,])
hilo0.start()


# Define callback functions which will be called when certain events happen.
def motion_pir(channel):
	# motion_pir function will be called when event
	# RISING and FALLING is detected (GPIO event)
	# In retriggering mode (jumper placed in H) 
	# The event detection can works of the next form:
	# with RISING event (LOW to HIGH) while detect movement
	# with FALLING event (HIGH to LOW) when movement are 
	# stoped (some seconds, depend sensivity value)
	timestamp = time.time()
	stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
	sense=GPIO.input(SENSOR_PIN)
	if(sense==GPIO.HIGH):
		# print('Se ha detectado movimiento: {}'.format(stamp))
		totalMotionTime.isMovement=True
	elif(sense==GPIO.LOW):
		# print('No hay mas movimiento: {}'.format(stamp))
		totalMotionTime.isMovement=False


# Define Function "main", way to manage errors
def main():
	# Setup GPIO mode
	GPIO.setmode(GPIO.BCM)
	# Set GPIO pin direction
	GPIO.setup(SENSOR_PIN, GPIO.IN)

	# add event for detection
	GPIO.add_event_detect(SENSOR_PIN , GPIO.BOTH, callback=motion_pir, 
		bouncetime=150)

	# measurement vars
	motionTimeTemp=0
	baseTime=0
	measured=False # Control about get baseTime only one time

	while True:
		if(totalMotionTime.isMovement):
			if(not measured):
				baseTime=time.time()
				measured=True
		else:
			if(measured):
				motionTimeTemp+=time.time()-baseTime
				measured=False

		if(int(time.time())%(showDataTime-1)==0):
			if(totalMotionTime.isMovement):# Case if motion stills
				lock.acquire()
				totalMotionTime.measureTime+=(motionTimeTemp+time.time()
					-baseTime)
				lock.release()
			else:# case are not motion
				lock.acquire()
				totalMotionTime.measureTime+=motionTimeTemp
				lock.release()
			motionTimeTemp=0
		time.sleep(0.5)
		

if __name__=="__main__":
	try:
		main()
	except:
		print("{} line {}".format(sys.exc_info()[0], 
			sys.exc_info()[-1].tb_lineno))
		GPIO.cleanup()