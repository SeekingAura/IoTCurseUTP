# Import standard Python Modules
import time
import sys
import os

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

	print("Ejecución de publicación activado, para salir escriba 'x'")
	while True:
		message=str(input("Ingrese el mensaje a enviar:\n"))
		success=False# Var for format check
		# The next checks is better do with regex, but can do with you whatever prefer
		if("encender" in message or "apagar" in message):# check if are respective action in message
			if(" ~ " in message):# check if are correct format separator
				try:#handle format error
					if(message.split(" ~ ")[1].isdigit()):# check if second value is number
						success=True
						print("Publicando al topic -> '{0}'".format("edificio1/piso1/habitacion1/luces"))
						client.publish("edificio1/piso1/habitacion1/luces", message)
				except:
					print("Error en el formato")
		if(not success):
			print("Se desconoce a que topic enviar el mensaje dado")
