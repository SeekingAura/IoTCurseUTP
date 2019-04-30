# Import standard Python Modules
import sys
import os

# Import paho MQTT Client
import paho.mqtt.client as mqtt

# Import RPi.GPIO Module
try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO!  This is probably because you need \
	superuser privileges.  You can achieve \
	this by using 'sudo' to run your script")

# Define callback functions which will be called when certain events happen.
def on_connect(client, userdata, flags, rc):
	# Connected function will be called when the client connects.
	print("Conectado con codigo resultante:  "+str(rc))

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	print("Suscribiendose al topic ->{0}".format("area0/luces"))
	client.subscribe("area0/luces")

def on_message(client, userdata, message):
	# Message function will be called when a subscribed feed has a new value.
	messageStr=str(message.payload.decode("utf-8"))
	print("message received " ,str(message.payload.decode("utf-8")))
	print("message topic=",message.topic)

	# Catch errors
	try:
		if("| " in messageStr):
			pinNums, newStatePin =messageStr.split("| ")
			# Convert string to integer list
			pinNums=eval(pinNums)

			if(newStatePin=="OFF"):
				GPIO.output(pinNums, GPIO.LOW)
			elif(newStatePin=="ON"):
				GPIO.output(pinNums, GPIO.HIGH)
			else:
				print("Estado recibido incorrecto")
	except Exception as e:
		print("Error al ejecutar el mensaje recibido:\n{} line {}".format(e, sys.exc_info()[-1].tb_lineno))

def main():
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $hostAddress\n'.format(sys.argv[0]))
		os._exit(1)

	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	# List with all GPIO pin numbers
	pinList=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
	
	# Set GPIO pin signal OUT and initial value "shutdown"
	GPIO.setup(pinList, GPIO.OUT, initial=GPIO.LOW)

	# Create an MQTT client instance.
	print("Creando instancia MQTT")
	client = mqtt.Client()

	# Setup the callback functions
	client.on_message = on_message
	client.on_connect = on_connect

	print("conectando al broker")
	client.connect(host=sys.argv[1], port=1883, keepalive=60)
	
	client.loop_forever()

if __name__ == "__main__":
	try:
		main()
	except:
		GPIO.cleanup()