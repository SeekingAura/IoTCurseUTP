# Import standard python modules
import time
import os
import sys
import threading

# Import Adafruit IO Client.
from Adafruit_IO import Client

# Import RPi.GPIO Module
try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO!  This is probably because you need \
	superuser privileges.  You can achieve \
	this by using 'sudo' to run your script")

# Class for params into object for Threading call
class MessageSendControl():
	def __init__(self, message):
		self.message=message

# Define Functions for Threading
def send_message(aioClient, tankMeasureFeedInstance, tankStatusFeedInstance, messageInstance, pinList):
	while True:
		if(messageInstance.message!=""):
			if(messageInstance.message.isdigit()):
				aioClient.send(tankMeasureFeedInstance.key, int(messageInstance.message))
				# Case for trigger a normal status
				if(int(messageInstance.message)>=10 and int(messageInstance.message)<=90):
					aioClient.send(tankStatusFeedInstance.key, "normal")
				
				# LED control
				tankStatusFeedData=aio.receive(tankStatusFeedInstance.key)
				for i in pinList:
					if(i==tankStatusFeedData.value):
						GPIO.output(pinList.get(i), GPIO.HIGH)
					else:
						GPIO.output(pinList.get(i), GPIO.LOW)

				print("Capacidad en el tanque {}%".format(messageInstance.message))
			else:
				print("El dato '{}' no es apto para el envio".format(messageInstance.message))
			time.sleep(10)

if __name__ == "__main__":
	if(len(sys.argv)!=5):
		sys.stderr.write('Usage: "{0}" $AIOUsername $AIOKey $TankMeasureFeedKey $TankStatusFeedKey\n'.format(sys.argv[0]))
		os._exit(1)

	AIOUsername=sys.argv[1]
	AIOKey=sys.argv[2]# Beware, your Key is Secret! - c0354363dc384523bc1022b5fb66d6b7
	TankMeasureFeedKey=sys.argv[3] # Feed key where tank measure data is received
	TankStatusFeedKey=sys.argv[4] # Feed key where tank status data is received
	# Connect to Adafruit IO Server
	aio=Client(username=AIOUsername, key=AIOKey)

	# Link to feeds
	tankMeasureFeedInstance=aio.feeds(TankMeasureFeedKey)
	tankStatusFeedInstance=aio.feeds(TankStatusFeedKey)
	
	# Create messageSendControl instance
	messageInstance=MessageSendControl("")
	
	# Setup GPIO mode
	GPIO.setmode(GPIO.BCM)
	
	# List with all GPIO pin numbers
	pinList={"bajo":10, "normal":11, "alto":12}
	
	# Set GPIO pin signal OUT and initial value "shutdown"
	GPIO.setup(pinList, GPIO.OUT, initial=GPIO.LOW)
	
	# Setup Threading, to publish message every 10 seconds
	hilo0=threading.Thread(target=send_message, args=(aio, tankMeasureFeedInstance, tankStatusFeedInstance, messageInstance, pinList))
	hilo0.start()

	# Mod publish value
	while messageInstance.message!="x": # char 'x' to exit
		messageInstance.message=input("Ingrese nuevo valor para el tanque\n")
	os._exit(1)
