# Import standard python modules
import time
import datetime
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

# Control of sincronization Thread
lock = threading.RLock()

# Class for params into object for Threading call
class MessageSendControl():
	def __init__(self, message):
		self.message=message

# Define Functions for Threading
def send_message(aioClient, tankMeasureFeedInstance, tankStatusFeedInstance, messageInstance, pinList):
	lastState=""
	while True:
		if(messageInstance.message!=""):
			lock.acquire()
			logFile=open("log fuel.txt", "a", encoding="utf8")
		
			if(messageInstance.message.isdigit()):
				aioClient.send(tankMeasureFeedInstance.key, int(messageInstance.message))
				logFile.write("{}~{}~{}~{}\n".format(datetime.datetime.now(), tankMeasureFeedInstance.key, messageInstance.message, "Valor de temperatura enviado"))

				# Case for trigger a normal status, 
				if(int(messageInstance.message)>=10 and int(messageInstance.message)<=90):
					aioClient.send(tankStatusFeedInstance.key, "normal")
					logFile.write("{}~{}~{}~{}\n".format(datetime.datetime.now(), tankStatusFeedInstance.key, "normal", "Estado de temperatura enviado"))

				# LED control
				tankStatusFeedData=aio.receive(tankStatusFeedInstance.key)
				if(lastState!=tankStatusFeedData.value):
					GPIO.output(list(pinList), GPIO.LOW)
					GPIO.output(pinList.get(i), GPIO.HIGH)
					logFile.write("{}~{}~{}~{}\n".format(datetime.datetime.now(), tankStatusFeedInstance.key, tankStatusFeedData, "Encendiendo LED {} - Estado recibido {}".format(pinList.get(i), tankStatusFeedData.value)))
					lastState=tankStatusFeedData.value
				
				
			else:
				print("El dato '{}' no es apto para el envio".format(messageInstance.message))

			logFile.close()
			lock.release()
			time.sleep(10)

if __name__ == "__main__":
	if(len(sys.argv)!=5):
		sys.stderr.write('Usage: "{0}" $AIOUsername $AIOKey $tankMeasureFeedKey $tankStatusFeedKey\n'.format(sys.argv[0]))
		os._exit(1)

	AIOUsername=sys.argv[1]
	AIOKey=sys.argv[2]# Beware, your Key is Secret!
	tankMeasureFeedKey=sys.argv[3] # Feed key where tank measure data is received
	tankStatusFeedKey=sys.argv[4] # Feed key where tank status data is received

		# Connect to Adafruit IO Server
	aio=Client(username=AIOUsername, key=AIOKey)

	# Link to feeds
	tankMeasureFeedInstance=aio.feeds(tankMeasureFeedKey)
	tankStatusFeedInstance=aio.feeds(tankStatusFeedKey)
	
	# Create messageSendControl instance
	messageInstance=MessageSendControl("")

	# Setup GPIO mode
	GPIO.setmode(GPIO.BCM)
	
	# List with all GPIO pin numbers
	pinList={"bajo":10, "normal":11, "alto":12}
	
	# write on log file
	logFile=open("log fuel.txt", "a", encoding="utf8")
	logFile.write("{}~{}~{}~{}\n".format(datetime.datetime.now(), "Nulo", "Nulo", "Aplicación iniciada"))
	logFile.close()
	
	# Setup Threading, to publish message every 10 seconds
	hilo0=threading.Thread(target=send_message, args=(aio, tankMeasureFeedInstance, tankStatusFeedInstance, messageInstance, pinList))
	hilo0.start()

	# Mod publish value
	while messageInstance.message!="x": # char 'x' to exit
		messageInstance.message=input("Ingrese nuevo valor para el tanque\n")
		
		# Sincronization threads
		lock.acquire()
		# write on log file
		logFile=open("log fuel.txt", "a", encoding="utf8")
		logFile.write("{}~{}~{}~{}\n".format(datetime.datetime.now(), "Nulo", "Nulo", "Valor de temperatura modificado a {}".format(messageInstance.message)))
		logFile.close()
		lock.release()
	os._exit(1)
 