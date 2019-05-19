# Import standard python modules
import time
import sys
import os

# Import RPi.GPIO Module
import RPi.GPIO as GPIO

# Import Adafruit IO MQTT client.
from Adafruit_IO import Client

def main():
	if(len(sys.argv)!=7):
		sys.stderr.write('Usage: "{0}" $AIOUsername $AIOKey $AIOFeedKeySoilMoisture $AIOFeedKeyAmbientTemperature $AIOFeedKeyAmbientHumidity $AIOFeedKeyState\n'.format(sys.argv[0]))
		os._exit(1)

	AIOUsername=sys.argv[1]
	AIOKey=sys.argv[2]# Beware, your Key is Secret!
	AIOFeedKeySoilMoisture=sys.argv[3] # Feed key where data is received
	AIOFeedKeyAmbientTemperature=sys.argv[4] # Feed key where data is received
	AIOFeedKeyAmbientHumidity=sys.argv[5] # Feed key where data is received
	AIOFeedKeyState=sys.argv[6] # Feed key where data is received

	# Connect to Adafruit IO Server
	aio=Client(username=AIOUsername, key=AIOKey)

	# Link to feeds
	soilMoistureFeed=aio.feeds(AIOFeedKeySoilMoisture)
	ambientTemperatureFeed=aio.feeds(AIOFeedKeyAmbientTemperature)
	ambientHumidityFeed=aio.feeds(AIOFeedKeyAmbientHumidity)
	stateFeed=aio.feeds(AIOFeedKeyState)

	# Dict with some GPIO pin numbers
	pinSoilMoisture={"humedad suelo baja":14, "humedad suelo normal":15, "humedad suelo alta":16}

	# Dict with GPIO pin numbers for temperature alert
	pinTemperature={"temperatura ambiente baja":8, "temperatura ambiente normal":9, "temperatura ambiente alta":10}

	# Dict with GPIO pin numbers for humidty alert
	pinHumidity={"humedad ambiente baja":21, "humedad ambiente normal":22, "humedad ambiente alta":23}

	# Setup GPIO setmode
	GPIO.setmode(GPIO.BCM)

	# Set GPIO pin signal OUT and initial value "shutdown"
	GPIO.setup(list(pinTemperature.values())+list(pinSoilMoisture.values())+list(pinHumidity.values()), GPIO.OUT, initial=GPIO.LOW)

	# set control state var
	humidityLastState=""
	temperatureLastState=""
	soilMoistureLastState=""

	humidityLastUpdate=""
	temperatureLastUpdate=""
	soilMoistureLastUpdate=""

	while True:
		soilMoistureData=aio.receive(soilMoistureFeed.key)
		
		ambientTemperatureData=aio.receive(ambientTemperatureFeed.key)

		ambientHumidityData=aio.receive(ambientHumidityFeed.key)
		
		if(soilMoistureData.updated_at!=soilMoistureLastUpdate):	
			valueSensor=float(soilMoistureData.value)
			print("porcentaje de humedad del suelo {:.2f}%".format(valueSensor))
			
			if(valueSensor<40):
				state="humedad suelo baja"
			elif(valueSensor>75):
				state="humedad suelo alta"
			else:
				state="humedad suelo normal"

			if(state!=soilMoistureLastState):
				GPIO.output(list(pinSoilMoisture.values()), GPIO.LOW)
				GPIO.output(pinSoilMoisture.get(state), GPIO.HIGH)
				soilMoistureLastState=state
				print("cambio de estado humedad del suelo a {}".format(state))
			
			soilMoistureLastUpdate=soilMoistureData.updated_at

		if(ambientTemperatureData.updated_at!=temperatureLastUpdate):
			valueSensor=float(ambientTemperatureData.value)
			print("Temperatura ambiental {}°".format(valueSensor))
			if(valueSensor<35):
				state="temperatura ambiente baja"
			elif(valueSensor>40):
				state="temperatura ambiente alta"
			else:
				state="temperatura ambiente normal"

			if(state!=temperatureLastState):
				GPIO.output(list(pinTemperature.values()), GPIO.LOW)
				GPIO.output(pinTemperature.get(state), GPIO.HIGH)
				temperatureLastState=state
				print("cambio de estado temperatura del ambiente a {}".format(state))
			temperatureLastUpdate=ambientTemperatureData.updated_at

		if(ambientHumidityData.updated_at!=humidityLastUpdate):
			valueSensor=float(ambientHumidityData.value)
			print("porcentaje de humedad ambiental {:.2f}%".format(valueSensor))
			if(valueSensor<50):
				state="humedad ambiente baja"
			elif(valueSensor>80):
				state="humedad ambiente alta"
			else:
				state="humedad ambiente normal"

			if(state!=humidityLastState):
				GPIO.output(list(pinHumidity.values()), GPIO.LOW)
				GPIO.output(pinHumidity.get(state), GPIO.HIGH)
				humidityLastState=state
				print("cambio de estado humedad del ambiente a {}".format(state))
			
			humidityLastUpdate=ambientHumidityData.updated_at

if __name__=="__main__":
	try:
		main()
	except:
		print("{} line {}".format(sys.exc_info()[0], sys.exc_info()[-1].tb_lineno))
		GPIO.cleanup()

