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

# Import paho MQTT client.
import paho.mqtt.client as mqtt

# Define callback functions which will be called when certain events happen.
def on_connect(client, userdata, flags, rc):
	# Connected function will be called when the client connects.
	print("Conectado con codigo resultante:  "+str(rc))
	client.connectedFlag=True

def on_disconnect(client):
	# Disconnected function will be called when the client disconnects.
	print("¡Se ha Desconectado!")
	os._exit(1)

if __name__=="__main__":
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $hostAddress\n'.format(sys.argv[0]))
		os._exit(1)
	
	# Create the I2C bus
	i2c = busio.I2C(board.SCL, board.SDA)

	# Create the ADC object using the I2C bus
	ads = ADS.ADS1115(i2c)

	# Create single-ended input on channel 0
	chan = AnalogIn(ads, ADS.P0)

	# Setup an MQTT Client Instance
	client = mqtt.Client()

	# Setup Callbacks
	client.on_connect = on_connect
	client.on_disconnect=on_disconnect

	# set params in client object
	rawValueMin=0
	rawValueMax=33000
	rawValueDeltaMax=rawValueMax-rawValueMin

	client.connectedFlag=False

	# Connect to the Broker server.
	print("Conectando al broker")
	client.connect(host=sys.argv[1], port=1883, keepalive=60)
	client.loop_start()
	while not client.connectedFlag:
		print("Esperando conexión")
		time.sleep(1)
	
	while True:
		humidityPercentage=float(100-((chan.value-rawValueMin)/rawValueDeltaMax)*100)
		print("porcentaje de humedad del suelo {:.2f}%".format(humidityPercentage))
		client.publish("area0/plant0/HumedadSuelo", humidityPercentage)

		# Retreive data from DHT11 sensor
		humidity, temperature = Adafruit_DHT.read_retry(sensor=Adafruit_DHT.DHT11, pin=4, retries=15, delay_seconds=2)
		
		# Check Retreive Data
		if humidity is not None and temperature is not None:
			print('Temperatura ambiental {:0.1f}°'.format(temperature))
			print('Humedad ambiental {:0.1f}%'.format(humidity))

			client.publish("area0/plant0/HumedadAmbiente", humidity)
			client.publish("area0/plant0/TemperaturaAmbiente", temperature)
		else:
			print('Failed to get reading. Try again!')

		time.sleep(10)
