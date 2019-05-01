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

	print("Ejecución de publicación activado")
	while True:
		homeZone=str(input("Ingrese la parte del hogar a controlar\n"))

		if(homeZone!="cocina0" and homeZone!="habitacion0" and homeZone!="garaje0"):
			print("El area indicada no es valida")
			continue

		action=str(input("Indique la acción a aplicar (ON o OFF)\n"))

		
		if(action!="ON" and action!="OFF"):
			print("La acción dada no es valida")
			continue
		
		print("Publicando al topic -> '{0}'".format("casa0/"+homeZone+"/luces"))
		client.publish("casa0/"+homeZone+"/luces", action)
