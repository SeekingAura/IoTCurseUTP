# Import standard Python Modules
import sys
import os

# Import paho MQTT Client
import paho.mqtt.client as mqtt

# Define callback functions which will be called when certain events happen.
def on_connect(client, userdata, flags, rc):
	# Connected function will be called when the client connects.
	print("Conectado con codigo resultante:  "+str(rc))

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	print("Suscribiendose al topic ->{0}".format("area0/#"))
	client.subscribe("area0/#")

def on_message(client, userdata, message):
	# Message function will be called when a subscribed feed has a new value.
	print("message received " ,str(message.payload.decode("utf-8")))
	print("message topic=",message.topic)

if __name__ == "__main__":
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $hostAddress\n'.format(sys.argv[0]))
		os._exit(1)

	# Create an MQTT client instance.
	print("Creando instancia MQTT")
	client = mqtt.Client()

	# Setup the callback functions
	client.on_message = on_message
	client.on_connect = on_connect

	# Connect to the Broker server.
	print("conectando al broker")
	client.connect(host=sys.argv[1], port=1883, keepalive=60)

	client.loop_forever()
