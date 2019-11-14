# Import standard python modules
import time
import os
import sys

# Import Adafruit IO Client.
from Adafruit_IO import Client


if __name__ == "__main__":
	if(len(sys.argv)!=4):
		sys.stderr.write('Usage: "{0}" $AIOUsername $AIOKey $PotenFeedKeyData\n'.format(sys.argv[0]))
		os._exit(1)

	## Adafruit config
	AIOUsername=sys.argv[1]
	AIOKey=sys.argv[2]# Beware, your Key is Secret! - c0354363dc384523bc1022b5fb66d6b7
	potenFeedKey=sys.argv[3] # Feed key where tank measure data is received
	# Connect to Adafruit IO Server
	aio=Client(username=AIOUsername, key=AIOKey)

	# Link to feeds
	PotenFeedInstance=aio.feeds(potenFeedKey)

	## Potenciometer get data
	# Create the I2C bus
	i2c = busio.I2C(board.SCL, board.SDA)

	# Create the ADC object using the I2C bus
	ads = ADS.ADS1115(i2c)

	# Create single-ended input on channel 0
	chan = AnalogIn(ads, ADS.P0)

	# Mod publish value
	while True: # char 'x' to exit
		aio.send(PotenFeedInstance.key, chan.value)
		time.sleep(5)
	
