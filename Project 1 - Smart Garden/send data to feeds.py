# Import standard python modules
import time
import sys
import os

# Import Raspberry Hardware
import board
import busio

# Import ADS1115 module
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Import Adafruit_DHT Module
import Adafruit_DHT

# Import Adafruit IO Client.
from Adafruit_IO import Client

if __name__=="__main__":
	if(len(sys.argv)!=6):
		sys.stderr.write('Usage: "{0}" $AIOUsername $AIOKey $AIOFeedKeySoilMoisture $AIOFeedKeyAmbientHumidity $AIOFeedKeyAmbientTemperature\n'.format(sys.argv[0]))
		os._exit(1)

	AIOUsername=sys.argv[1]
	AIOKey=sys.argv[2]# Beware, your Key is Secret!
	AIOFeedKeySoilMoisture=sys.argv[3] # Feed key where data is received
	AIOFeedKeyAmbientHumidity=sys.argv[4] # Feed key where data is received
	AIOFeedKeyAmbientTemperature=sys.argv[5] # Feed key where data is received

	# Connect to Adafruit IO Server
	aio=Client(username=AIOUsername, key=AIOKey)

	# Link to feeds
	soilMoistureFeed=aio.feeds(AIOFeedKeySoilMoisture)
	ambientHumidityFeed=aio.feeds(AIOFeedKeyAmbientHumidity)
	ambientTemperatureFeed=aio.feeds(AIOFeedKeyAmbientTemperature)

	# get feeds data from Adafruit IO
	# feedSoilMoistureData=aio.receive(feedSoilMoisture.key)
	# feedSAmbientHumidityData=aio.receive(feedAmbientHumidity.key)
	# feedSAmbientTemperatureData=aio.receive(feedAmbientTemperature.key)

	# Create the I2C bus
	i2c = busio.I2C(board.SCL, board.SDA)

	# Create the ADC object using the I2C bus
	ads = ADS.ADS1115(i2c)

	# Create single-ended input on channel 0
	chan = AnalogIn(ads, ADS.P0)

	# Control vars
	rawValueMin=0
	rawValueMax=33000
	rawValueDeltaMax=rawValueMax-rawValueMin

	while True:
		soilMoisturePercentage=float(100-((chan.value-rawValueMin)/rawValueDeltaMax)*100)
		print("porcentaje de humedad {:.2f}%".format(soilMoisturePercentage))
		
		aio.send(soilMoistureFeed.key, float(soilMoisturePercentage))

		# Retreive data from DHT11 sensor
		humidity, temperature = Adafruit_DHT.read_retry(sensor=Adafruit_DHT.DHT11, pin=4, retries=15, delay_seconds=2)
		
		# Check Retreive Data
		if humidity is not None and temperature is not None:
			print('Temp={}°  Humidity={}%'.format(temperature, humidity))
			aio.send(ambientHumidityFeed.key, float(humidity))
			aio.send(ambientTemperatureFeed.key, float(temperature))
		
		time.sleep(10)