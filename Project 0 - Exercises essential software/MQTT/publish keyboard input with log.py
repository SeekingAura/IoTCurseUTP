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
	fileControl=open("log publish.txt", "a", encoding='utf8')
	fileControl.write("{}|{}|{}|{}\n".format(datetime.datetime.now(), "Nulo", "Nulo", "Conectado al Broker"))
	fileControl.close()

def on_disconnect(client):
	# Disconnected function will be called when the client disconnects.
	print("¡Se ha Desconectado!")
	client.connectedFlag=False
	os._exit(1)

if __name__ == "__main__":
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $hostAddress\n'.format(sys.argv[0]))
		os._exit(1)

	# Write on log
	fileControl=open("log publish.txt", "a", encoding='utf8')
	fileControl.write("{}|{}|{}|{}\n".format(datetime.datetime.now(), "Nulo", "Nulo", "Aplicación iniciada"))
	fileControl.close()

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
	try:
		while True:
			# receive input for publish
			message=str(input("Ingrese el mensaje a enviar:\n"))
			
			# Open a log file
			fileControl=open("log publish.txt", "a", encoding='utf8')

			# Var for format check
			success=False
			
			# The next checks is better do with regex, but can do with you whatever prefer
			if("encender" in message or "apagar" in message):# check if are respective action in message
				if(" ~ " in message):# check if are correct format separator
					try:#handle format error
						if(message.split(" ~ ")[1].isdigit()):# check if second value is number
							# Set control var
							success=True

							print("Publicando al topic -> '{0}'".format("edificio1/piso1/habitacion1/luces"))

							# Write on log file
							fileControl.write("{}|{}|{}|{}\n".format(datetime.datetime.now(), message, "edificio1/piso1/habitacion1/luces", "enviado"))

							# Publish message
							client.publish("edificio1/piso1/habitacion1/luces", message)
					except:
						print("Error en el formato")

						# Write on log file
						fileControl.write("{}|{}|{}|{}\n".format(datetime.datetime.now(), message, "edificio1/piso1/habitacion1/luces", "no enviado - Error en el formato"))
			if(not success):
				print("Se desconoce a que topic enviar el mensaje dado")
				
				# Write on log file
				fileControl.write("{}|{}|{}|{}\n".format(datetime.datetime.now(), message, "Nulo", "no enviado - Mensaje sin topic"))
			
			# Close file for realse memory and update in system
			fileControl.close()
	except:
		# Write on log file
		fileControl=open("log publish.txt", "a", encoding='utf8')
		fileControl.write("{}|{}|{}|{}\n".format(datetime.datetime.now(), "Nulo", "Nulo", "Terminado"))
		fileControl.close()