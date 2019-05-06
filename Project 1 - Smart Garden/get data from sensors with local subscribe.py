# Import standard python modules
import time
import sys
import os

# Import paho MQTT client.
import paho.mqtt.client as mqtt

# Import RPi.GPIO Module
import RPi.GPIO as GPIO

# Define callback functions which will be called when certain events happen.
def on_connect(client, userdata, flags, rc):
	# Connected function will be called when the client connects.
	print("Conectado con codigo resultante:  "+str(rc))
	print("Suscribiendose al topic ->{0}".format("area0/#"))
	client.subscribe("area0/#")

def on_disconnect(client):
	# Disconnected function will be called when the client disconnects.
	print("¡Se ha Desconectado!")
	os._exit(1)

def on_message(client, userdata, message):
	# Message function will be called when a subscribed feed has a new value.
	messageStr=str(message.payload.decode("utf-8"))
	print("message received " ,str(message.payload.decode("utf-8")))
	print("message topic=",message.topic)
	
	area, plant, action=message.topic.split("/")

	if(action=="HumedadSuelo"):	
		valueSensor=float(messageStr)
		print("porcentaje de humedad del suelo {:.2f}%".format(valueSensor))
		
		if(valueSensor<40):
			state="baja"
		elif(valueSensor>75):
			state="alta"
		else:
			state="normal"

		if(state!=client.lastSoilMoistureState):
			GPIO.output(list(client.pinSoilMoisture.values()), GPIO.LOW)
			GPIO.output(client.pinSoilMoisture.get(state), GPIO.HIGH)
			client.lastSoilMoistureState=state
			print("cambio de estado humedad del suelo a {}".format(state))

	elif(action=="TemperaturaAmbiente"):
		valueSensor=float(messageStr)
		print("Temperatura ambiental")
		if(valueSensor<35):
			state="baja"
		elif(valueSensor>40):
			state="alta"
		else:
			state="normal"

		if(state!=client.lastTemperatureState):
			GPIO.output(list(client.pinTemperature.values()), GPIO.LOW)
			GPIO.output(client.pinTemperature.get(state), GPIO.HIGH)
			client.lastTemperatureState=state
			print("cambio de estado temperatura del ambiente a {}".format(state))

	elif(action=="HumedadAmbiente"):
		valueSensor=float(valueSensor)
		print("porcentaje de humedad ambiental {:.2f}%".format(valueSensor))
		if(valueSensor<50):
			state="baja"
		elif(valueSensor>80):
			state="alta"
		else:
			state="normal"

		if(state!=client.lastHumidityState):
			GPIO.output(list(client.pinHumidity.values()), GPIO.LOW)
			GPIO.output(client.pinHumidity.get(state), GPIO.HIGH)
			client.lastHumidityState=state
			print("cambio de estado humedad del ambiente a {}".format(state))

def main():
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $hostAddress\n'.format(sys.argv[0]))
		os._exit(1)
	# Dict with GPIO pin numbers for humidty alert
	pinSoilMoisture={"baja":6, "normal":7, "alta":8}

	# Dict with GPIO pin numbers for temperature alert
	pinTemperature={"baja":12, "normal":13, "alta":14}

	# Dict with GPIO pin numbers for humidty alert
	pinHumidity={"baja":20, "normal":21, "alta":22}

	# Setup GPIO setmode
	GPIO.setmode(GPIO.BCM)

	# Set GPIO pin signal OUT and initial value "shutdown"
	GPIO.setup(list(pinTemperature.values())+list(pinHumidity.values())+list(pinSoilMoisture.values()), GPIO.OUT, initial=GPIO.LOW)

	# Setup an MQTT Client Instance
	client = mqtt.Client()

	# Setup Callbacks
	client.on_connect = on_connect
	client.on_disconnect=on_disconnect
	client.on_message=on_message

	# set params in client object
	client.lastHumidityState=""
	client.lastTemperatureState=""
	client.lastSoilMoistureState=""

	client.pinHumidity=pinHumidity
	client.pinTemperature=pinTemperature
	client.pinSoilMoisture=pinSoilMoisture

	# Connect to the Broker server.
	print("Conectando al broker")
	client.connect(host=sys.argv[1], port=1883, keepalive=60)
	client.loop_forever()

if __name__=="__main__":
	try:
		main()
	except:
		print("{} line {}".format(sys.exc_info()[0], sys.exc_info()[-1].tb_lineno))
		GPIO.cleanup()