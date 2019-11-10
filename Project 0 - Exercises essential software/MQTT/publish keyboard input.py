# Import standard Python Modules
import time
import sys
import os

# Control of errors with regular expressions
import re

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
	while True:
		## Start Build topic
		IdsString=str(input("Ingrese el número de edificio, piso y habitación a \
controlar luces con el formato en el orden respectivo '#, #, #'\n")
		)
		
		### Start Format Check
		# Regex for respective format
		regexCheck=re.match("[0-9]+(\s*,\s*[0-9]+)*", IdsString)

		# Check if regex are not none, if not match makes None Object
		if(regexCheck is not None):
			# check matched string are same if not is error
			if(IdsString!=regexCheck.group()):
				print("error en el formato")
				continue # Force while loop to next iteration
		else:
			print("error en el formato")
			continue # Force while loop to next iteration
		### End Format Check
		#  Format Check

		IdsList=eval("["+IdsString+"]") # Convert ID numbers to python list
		
		### Start Check quantity of IDs
		# Check quantity of ID's, must be only 3
		if(len(IdsList)!=3):
			print("la cantidad de IDs no corresponde a 3, es edificio, piso, \
habitación")
			continue # Force while loop to next iteration
		### End Check quantity of IDs

		action=str(input("Indique a que va accionar el mensaje (por defecto \
solo hay 'luces')\n"))

		actions=["luces"] # List with possible actions

		### Start Check action
		# Check if are avalible and correct action
		if(not action in actions):
			print("acción {} no está disponible o no es valida".format(action))
			continue # Force while loop to next iteration
		### End Check action

		# Get ID's in respective order
		buildID, floorID, roomID=IdsList

		# Make topic with ids and action for publish
		topic="edificio{}/piso{}/habitacion{}/{}".format(buildID, floorID, roomID, action)
		## End Build topic

		## Start Message creation
		# Message format "Action | #, #, #", example "ON | 1, 4, 6"
		# Method upper makes full caps
		message=str(input("Ingrese el mensaje a enviar (formato 'Action | #, \
#, #', example 'ON | 1, 4, 6'):\n")
		).upper()
		
		

		regexCheck=re.match("(ON|OFF)\s[|]\s[0-9]+(\s*,\s*[0-9]+)*", message)

		# Check if regex are not none, if not match makes None Object
		if(regexCheck is not None):
			# check matched string are same if not is error
			if(message!=regexCheck.group()):
				print("error en el formato")
				continue # Force while loop to next iteration
		else:
			print("error en el formato")
			continue # Force while loop to next iteration
		
		## End Message creation
			
		# publish message
		print("Publicando al topic -> '{0}'".format(topic))
		print("mensaje -> '{0}'".format(message))
		client.publish(topic, message)

		# Exit program
		programAction=input("¿Salir? y/n\n")
		if(programAction=="y"):
			print("Cerrando...")
			break # Force loop close
	client.disconnect()
	client.loop_stop()