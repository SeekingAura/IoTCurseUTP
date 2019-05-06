# Import standard Python Modules
import time
import sys
import os

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
		
	# Setup an MQTT Client Instance
	client = mqtt.Client()

	# Setup Callbacks
	client.on_connect = on_connect
	client.on_disconnect=on_disconnect

	client.connectedFlag=False

	# Connect to the Broker server.
	print("Conectando al broker")
	client.connect(host=sys.argv[1], port=1883, keepalive=60)
	client.loop_start()
	while not client.connectedFlag:
		print("Esperando conexión")
		time.sleep(1)

	while True:
		# Retreive data from DHT11 sensor
		humidity, temperature = Adafruit_DHT.read_retry(sensor=Adafruit_DHT.DHT11, pin=4, retries=15, delay_seconds=2)
		
		# Check Retreive Data
		if humidity is not None and temperature is not None:
			print('Temp={0:0.1f}° Humidity={1:0.1f}%'.format(temperature, humidity))
			client.publish("area0/plant0/HumedadAmbiente", humidity)
			client.publish("area0/plant0/TemperaturaAmbiente", humidity)
		else:
			print('Failed to get reading. Try again!')
