# Import standard Python Modules
import time
import sys
import os
import datetime

# Import paho MQTT Client
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

if __name__ == "__main__":
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $hostAddress\n'.format(sys.argv[0]))
		os._exit(1)

	# Setup the callback functions
	client = mqtt.Client()

	# Setup the callback functions
	client.on_connect = on_connect
	client.on_disconnect = on_disconnect

	# Setup Control vars
	client.connectedFlag=False

	# Connect to the Broker server.
	print("conectando al broker")
	client.connect(sys.argv[1], 1883, 60)
	client.loop_start()

	while not client.connectedFlag:
		print("Esperando conexión")
		time.sleep(1)

	print("Ejecución de publicación activado")

	# write on log file
	logFile=open("log publish.txt", "a", encoding="utf8")
	logFile.write("{}~{}~{}~{}\n".format(datetime.datetime.now(), "Nulo", "Nulo", "Aplicación iniciada"))
	logFile.close()

	while True:
		# Get data for publish
		pinNums=str(input("Ingrese los pines a interactuar, con el formato #, #, #\n"))
		percentage=str(input("Indique el nuevo valor porcentual para el brillo\n"))
		logFile=open("log publish.txt", "a", encoding="utf8")

		message="["+pinNums+"]"+"| "+percentage
		topic="area0/luminosidad"

		print("Publicando al topic -> '{0}'".format(topic))
		client.publish(topic, message)
		logFile.write("{}~{}~{}~{}\n".format(datetime.datetime.now(), message, topic, "Mensaje enviado"))
		logFile.close()
