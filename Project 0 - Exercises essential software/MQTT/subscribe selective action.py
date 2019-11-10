# Import standard Python Modules
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

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	print("Suscribiendose al topic ->{0}".format("edificio#"))
	
	buildingsID=[0, 1]
	for buildingID in buildingsID:
		client.subscribe("edificio{}/#".format(buildingID))

def on_message(client, userdata, message):
	try: # Catch errors, callback dont show by default
		# Message function will be called when a subscribed feed has a new value.

		# message content are codified in bytes, must be decodificated for read
		messageStr=str(message.payload.decode("utf-8"))
		print("topic del mensaje → {}".format(message.topic))
		print("mensaje recibido → {}".format(messageStr))
		print(type(message.topic))
		### Start Check topic
		regexCheck=re.match("edificio[0-9]+/piso[0-9]+/habitacion[0-9]+/[a-zA-Z]+",  
			message.topic
		)

		# Check if regex are not none, if not match makes None Object
		if(regexCheck is not None):
			# check matched string are same if not is error
			if(message.topic!=regexCheck.group()):
				print("error, topic '{}' no reconocido",format(message.topic))
				return # Force function exit
		else:
			print("error, topic '{}' no reconocido",format(message.topic))
			return # Force function exit
		### End Check topic


		### Start Check message
		regexCheck=re.match("(ON|OFF)\s[|]\s[0-9]+(\s*,\s*[0-9]+)*", messageStr)
		
		# Check if regex are not none, if not match makes None Object
		if(regexCheck is not None):
			# check matched string are same if not is error
			if(messageStr!=regexCheck.group()):
				print("error, mensaje '{}' no reconocido".format(messageStr))
				return # Force function exit
		else:
			print("error, mensaje '{}' no reconocido".format(messageStr))
			return # Force function exit
		### End Check message

		## Start Get ID's of building, floor, room and element action
		# Slice topic string with char '/'
		
		edificio, piso, habitacion, action=message.topic.split("/")
		
		# slice word edificio for take only number, split stores in a list on index 1
		edificio=edificio.split("edificio")[1]

		# slice word piso for take only number, split stores in a list on index 1
		piso=piso.split("piso")[1]

		# slice word habitacion for take only number, split stores in a list on index 1
		habitacion=habitacion.split("habitacion")[1]
		
		# Take element to applicate action with message 
		elementAction=message.topic.split("/")[3]
		## End Get ID's of building, floor, room and element action

		## Start Get action to apply and ID of elements
		action, ligthsNumber=messageStr.split(" | ")

		ligthsNumber=eval(ligthsNumber)
		## End Get action to apply and ID of elements


		# Apply actions to respective room and ligths
		# Check action
		if(elementAction=="luces"): # Action for ligths
			print("Aplicando acciones al edificio {}, piso {}, habitación {}".format(edificio, piso, habitacion))
			print("-"*30)# A Line in command line
			
			if(action=="ON"):
				for ligthNumber in ligthsNumber:
					print("encendiendo la luz {}".format(ligthNumber))
			elif(action=="OFF"):
				for ligthNumber in ligthsNumber:
					print("apagando la luz {}".format(ligthNumber))

			print("-"*30)# A Line in command line
	except:
		print("Surgió un error")

	


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

	print("conectando al broker")
	client.connect(host=sys.argv[1], port=1883, keepalive=60)
	
	client.loop_forever()
