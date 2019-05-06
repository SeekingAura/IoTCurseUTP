# Import standard Python Modules
import time
import sys

# Import Adafruit_DHT Module
import Adafruit_DHT

# Import RPi.GPIO Module
import RPi.GPIO as GPIO

def main():
	# Setup GPIO setmode
	GPIO.setmode(GPIO.BCM)

	# Dict with GPIO pin numbers for temperature alert
	pinTemperature={"temperatura baja":8, "temperatura normal":9, "temperatura alta":10}

	# Dict with GPIO pin numbers for humidty alert
	pinHumidity={"humedad baja":21, "humedad normal":22, "humedad alta":23}

	# Set GPIO pin signal OUT and initial value "shutdown"
	GPIO.setup(list(pinTemperature.values())+list(pinHumidity.values()), GPIO.OUT, initial=GPIO.LOW)
	
	# Control vars
	lastStateTemperature=""
	lastStateHumidity=""

	while True:
		# Retreive data from DHT11 sensor
		humidity, temperature = Adafruit_DHT.read_retry(sensor=Adafruit_DHT.DHT11, pin=4, retries=15, delay_seconds=2)
		
		# Check Retreive Data
		if humidity is not None and temperature is not None:
			print('Temp={}°  Humidity={}%'.format(temperature, humidity))
			
			if(temperature<35):
				stateTemperature="temperatura baja"
			elif(temperature>40):
				stateTemperature="temperatura alta"
			else:
				stateTemperature="temperatura normal"

			if(humidity<50):
				stateHumidity="humedad baja"
			elif(humidity>90):
				stateHumidity="humedad alta"
			else:
				stateHumidity="humedad normal"

			if(lastStateTemperature!=stateTemperature):
				GPIO.output(list(pinTemperature.values()), GPIO.LOW)
				GPIO.output(pinTemperature.get(stateTemperature), GPIO.HIGH)
				lastStateTemperature=stateTemperature
				print("cambio de estado a {}".format(stateTemperature))
			
			if(lastStateHumidity!=stateHumidity):
				GPIO.output(list(pinHumidity.values()), GPIO.LOW)
				GPIO.output(pinHumidity.get(stateHumidity), GPIO.HIGH)
				lastStateHumidity=stateHumidity
				print("cambio de estado a {}".format(stateHumidity))
			
		else:
			print('Failed to get reading. Try again!')

if __name__=="__main__":
	try:
		main()
	except:
		print("{} line {}".format(sys.exc_info()[0], sys.exc_info()[-1].tb_lineno))
		GPIO.cleanup()