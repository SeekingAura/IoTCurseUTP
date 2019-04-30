# Import standard Python Modules
import sys
import os
import datetime

# Import paho MQTT Client
import paho.mqtt.client as mqtt


# Define callback functions which will be called when certain events happen.
def on_connect(client, userdata, flags, rc):
	# Connected function will be called when the client connects.
	print("Conectado con codigo resultante:  "+str(rc))

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	print("Suscribiendose al topic ->{0}".format("edificio1/#"))
	client.subscribe("edificio1/#")

def on_message(client, userdata, message):
	# Message function will be called when a subscribed feed has a new value.
	messageStr=str(message.payload.decode("utf-8"))
	print("topic del mensaje →", message.topic)
	print("mensaje recibido →" , messageStr)

	fileControl=open("log subscribe.txt", "a", encoding='utf8')
	try:# handle format topic, should be "edificio#/piso#/habitacion#" # is a number
		if("/" in message.topic):
			edificio, piso, habitacion=message.topic.split("/")[:3]
			edificio=edificio.split("edificio")[1]
			piso=piso.split("piso")[1]
			habitacion=habitacion.split("habitacion")[1]
			elementAction=message.topic.split("/")[3:]# where aplicate actions
	except:
		print("el topic dado no es adecuado para las acciones del caso")
		edificio=piso=habitacion=None
		fileControl.write("{}|{}|{}|{}\n".format(datetime.datetime.now(), messageStr, message.topic, "no acción - Topic no configurado"))

	if(edificio is not None):# only if format success
		try:
			action, number=messageStr.split(" ~ ")
			if(elementAction[0]=="luces"):
				if(action=="encender" and number.isdigit()):
					print("edificio #{}, piso #{}, habitación #{}".format(edificio, piso, habitacion))
					print("{}=ON".format(number))
					fileControl.write("{}|{}|{}|{}\n".format(datetime.datetime.now(), messageStr, message.topic, "acción encender - en edificio #{}, piso #{}, habitación #{}".format(edificio, piso, habitacion)))
				elif(action=="apagar" and number.isdigit()):
					print("{}=OFF".format(number))
					fileControl.write("{}|{}|{}|{}\n".format(datetime.datetime.now(), messageStr, message.topic, "acción apagar - en edificio #{}, piso #{}, habitación #{}".format(edificio, piso, habitacion)))
				else:
					print("No se reconoce la acción para las luces")
					fileControl.write("{}|{}|{}|{}\n".format(datetime.datetime.now(), messageStr, message.topic, "no acción - Acción no reconocida "))
			else:
				print("El elemento a accionar no está en la configuración")
				fileControl.write("{}|{}|{}|{}\n".format(datetime.datetime.now(), messageStr, message.topic, "no acción - Elemento no configurado"))
		except:
			print("Mal formato del mensaje recibido")
			fileControl.write("{}|{}|{}|{}\n".format(datetime.datetime.now(), messageStr, message.topic, "no acción - Mal forma del mensaje"))
	fileControl.close()


if __name__ == "__main__":
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $hostAddress\n'.format(sys.argv[0]))
		os._exit(1)

	# Write on log
	fileControl=open("log publish.txt", "a", encoding='utf8')
	fileControl.write("{}|{}|{}|{}\n".format(datetime.datetime.now(), "Nulo", "Nulo", "Aplicación iniciada"))
	fileControl.close()
	
	# Create an MQTT client instance.
	print("Creando instancia MQTT")
	client = mqtt.Client()

	# Setup the callback functions
	client.on_message = on_message
	client.on_connect = on_connect

	print("conectando al broker")
	client.connect(host=sys.argv[1], port=1883, keepalive=60)
	
	client.loop_forever()
