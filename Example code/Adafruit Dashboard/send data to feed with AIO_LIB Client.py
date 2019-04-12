# Import standard python modules
import time
import os
import sys

# Import Adafruit IO Client.
from Adafruit_IO import Client

# Define Functions for Threading
def send_message(aioClient, feedObj, message):
	while True:
		if(message!=""):
			if(message.isdigit()):
				aioClient.send(feedObj.key, int(message))
			else:
				aioClient.send(feedObj.key, message)
			time.sleep(10)

if __name__ == "__main__":
	if(len(sys.argv)!=4):
		sys.stderr.write('Usage: "{0}" $AdafruitIOUsername $AdafruitIOKey $AdafruitIOFeedKey\n'.format(sys.argv[0]))
		os._exit(1)

	AdafruitIOFeedUsername=sys.argv[1]
	AdafruitIOKey=sys.argv[2]# Beware, your Key is Secret!
	AdafruitIOFeedKey=sys.argv[3] # Feed key where data is received

	# Connect to Adafruit IO Server
	aio=Client(username=AdafruitIOFeedUsername, key=AdafruitIOKey)

	# Link to feeds
	feedInstance=aio.feeds(AdafruitIOFeedKey)

	# message
	messageSend=""
	
	# Setup Threading, to publish message every 10 seconds
	hilo0=threading.Thread(target=send_message, args=(feedInstance, messageSend,))
	hilo0.start()

	# Mod publish value
	while messageSend!="x": # char 'x' to exit
		messageSend=input("Ingrese nuevo valor para el tanque\n")