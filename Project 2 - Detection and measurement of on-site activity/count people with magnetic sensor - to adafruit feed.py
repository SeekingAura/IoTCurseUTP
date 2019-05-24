# Import standard python modules
import time
import sys
import threading
import datetime

# Import Raspberry Hardware
import board
import busio

# Import ADS1115 module
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Import RPi.GPIO Module
import RPi.GPIO as GPIO

# Import Adafruit IO Client.
from Adafruit_IO import Client


# Define global vars #
# Control of sincronization in Threads
lock = threading.RLock()

# Setup show data time
showDataTime=20


# Define Classes #
# Define class for instance objects in threading
class DataCount():
	def __init__(self, aioClient, sensorDataFeed):
		self.countTimes=0
		self.client=aioClient
		self.sensorDataFeed=sensorDataFeed


# Define functions #
# Define functions for paralelism
def show_data(peopleCount):
	counted=False
	while True:
		"""show data every 20 seconds and reset countTimes"""		
		if(int(time.time())%showDataTime==0):
			if(not counted):
				lock.acquire()
				peopleCount.aioClient.send(peopleCount.sensorDataFeed.key, 
					peopleCount.countTimes)
				peopleCount.countTimes=0
				lock.release()
				counted=True
		else:
			counted=False


def main():
	if(len(sys.argv)!=4):
		sys.stderr.write('Usage: "{0}" $aIOUsername $aIOKey \
			$aIOFeedKeyPersonsUltrasonic \n'.format(sys.argv[0]))
		os._exit(1)

	# Create the I2C bus
	i2c = busio.I2C(board.SCL, board.SDA)

	# Create the ADC object using the I2C bus
	ads = ADS.ADS1115(i2c)

	# Create single-ended input on channel 0
	chan = AnalogIn(ads, ADS.P0)

	# Dict with some GPIO pin numbers
	pinList={"countState":7, "count":8}

	# Setup GPIO setmode
	GPIO.setmode(GPIO.BCM)

	# Set GPIO pin signal OUT and initial value "shutdown"
	GPIO.setup(list(pinList.values()), GPIO.OUT, initial=GPIO.LOW)

	aIOUsername=sys.argv[1]
	aIOKey=sys.argv[2]		# Beware, your Key is Secret!

	# Feed key's where data is management
	aIOFeedKeyPersonsMagnetic=sys.argv[3]

	# Connect to Adafruit IO Server
	aioClient=Client(username=aIOUsername, key=aIOKey)

	# Link to feeds
	personsMagneticFeed=aioClient.feeds(aIOFeedKeyPersonsMagnetic)
	 	
	# Control of count system
	peopleCount=DataCount(aioClient, personsMagneticFeed)

	# When magnetic element is far the min value is reached
	sensorValueMin=6900
	# When magnetic element is near the max value is reached
	sensorValueMax=10300
	"""When magnectic element are middle of distances between min and
	max
	"""
	sensorValueMedium=(int((sensorValueMax-sensorValueMin)/2)
						+ sensorValueMin)

	baseTime=time.time()
	countTemp=0		# Count value while state count and doesn't show
	countTempLast=0		# For toggle LED alert count +1

	# Flags for execute only one time (turn off, turn on)
	counted=False
	countState=False
	countTempLastState=True

	countRate=0.6



	# Setup Threading, to show data every 20 seconds
	hilo0=threading.Thread(target=show_data, args=[peopleCount,])
	hilo0.start()
	while True:
		sensorValue = chan.value		# Distance of magnetic sensor
		# Case if are plaque in high position
		
		if(sensorValue>=sensorValueMedium):
			baseTime=time.time()
			if(countTemp!=0):
				lock.acquire()
				peopleCount.countTimes+=countTemp
				lock.release()
				countTemp=0

			# Turn off LED to alert plaque in high position
			if(countState):
				countState=False
				GPIO.output(pinList.get("countState"), GPIO.LOW)

		else:		# Case if are plaque in low position
			"""Triggered every showDataTime-1 seconds for update 
			counTimes
			"""
			# print("is",sensorValue,  sensorValueMedium)
			if(int(time.time())%(showDataTime-1)==0):
				# Do only one time per showDataTime-1
				if(not counted):		
					lock.acquire()
					peopleCount.countTimes+=countTemp
					lock.release()

					# Update base time with rate residue
					baseTime=time.time()-(time.time()%countRate)
					# Update countTempLast for LED count alert
					continueTime=time.time()-baseTime
					countTempLast=int(continueTime/countRate)+1
					counted=True
					
			else:
				counted=False

			continueTime=time.time()-baseTime
			# Count rate + 1 more (case 0 to 0.6)
			countTemp=int(continueTime/countRate)+1
			
			# Turn on LED to alert plaque in low position
			if(not countState):
				countState=True
				GPIO.output(pinList.get("countState"), GPIO.HIGH)
		
		# Turn on LED to alert every counted +1 for 1 cycle time
		if(countTempLast!=countTemp):
			countTempLast=countTemp
			countTempLastState=False
			GPIO.output(pinList.get("count"), GPIO.HIGH)
		elif(not countTempLastState):
			countTempLastState=True
			GPIO.output(pinList.get("count"), GPIO.LOW)
			


		time.sleep(0.1)		# Cycle time

if __name__=="__main__":
	try:
		main()
	except:
		print("{} line {}".format(sys.exc_info()[0], 
			sys.exc_info()[-1].tb_lineno))
		GPIO.cleanup()