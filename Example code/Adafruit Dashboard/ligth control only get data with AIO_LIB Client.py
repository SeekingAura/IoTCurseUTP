# Import standard python modules
import time
import os
import sys

# Import Adafruit IO MQTT client.
from Adafruit_IO import Client

if __name__ == "__main__":
	if(len(sys.argv)!=3):
		sys.stderr.write('Usage: "{0}" $AdafruitIOUsername $AdafruitIOKey $AdafruitIOFeedForStateKey $AdafruitIOFeedForIntensityKey \n'.format(sys.argv[0]))
		os._exit(1)
	
	AdafruitIOFeedUsername=sys.argv[1]
	AdafruitIOKey=sys.argv[2]# Beware, your Key is Secret!
	incubatorLigthStateFeedKey=sys.argv[3] # Feed key where data is received
	incubatorLigthIntensityFeedKey=sys.argv[4] # Feed key where data is received

	# Connect to Adafruit IO Server
	aio=Client(username=AdafruitIOFeedUsername, key=AdafruitIOKey)

	# feeds instance
	incubatorLigthStateFeed=aio.feeds(incubatorLigthStateFeedKey)
	incubatorLigthIntensityFeed=aio.feeds(incubatorLigthIntensityFeedKey)

	while True:
		# get feeds data from Adafruit IO
		incubatorLigthStateData=aio.receive(incubatorLigthStateFeed.key)
		incubatorLigthIntensityData=aio.receive(incubatorLigthIntensityFeed.key)
		
		print("Estado de luz {}, última actualización {}".format(incubatorLigthStateData.value, incubatorLigthStateData.updated_at))
		print("Intensidad de luz {}, última actualización {}".format(incubatorLigthIntensityData.value, incubatorLigthIntensityData.updated_at))