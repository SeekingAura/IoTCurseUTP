# Import standard python modules
import time
import os
import sys

# Import RPi.GPIO library
try:
   import RPi.GPIO as GPIO
except RuntimeError:
   print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

# Import Adafruit IO MQTT client.
from Adafruit_IO import Client

def main():
	if(len(sys.argv)!=3):
		sys.stderr.write('Usage: "{0}" $AdafruitIOUsername $AdafruitIOKey\n'.format(sys.argv[0]))
		os._exit(1)
	# var GPIO pin to show output
	led_pin = 21
	
	# Set GPIO pin mode
	GPIO.setmode(GPIO.BCM)

	# Set GPIO pin direction
	GPIO.setup(led_pin, GPIO.OUT)
	
	# Setup PWM instance to led_pin with 60 Hz
	pwm = GPIO.PWM(led_pin, 60)
	
	# Connect to Adafruit IO Server
	aio=Client(username=sys.argv[1], key=sys.argv[2])

	# Link to feeds
	incubatorLigthState=aio.feeds("incubadura0.estado-de-luz")
	incubatorLigthIntensity=aio.feeds("incubadura0.intensidad-luminica")
	
	# Control vars
	dutyValue=0
	incubatorLigthStateLastUpdate=""
	incubatorLigthIntensityLastUpdate=""

	try:
		while True:
			# get feeds data from Adafruit IO
			incubatorLigthStateData=aio.receive(incubatorLigthState.key)
			incubatorLigthIntensityData=aio.receive(incubatorLigthIntensity.key)
		   
			# check if the received data is new
			if(incubatorLigthStateData.updated_at!=incubatorLigthStateLastUpdate):
				# Update datetime update, for execute only one time
				incubatorLigthStateLastUpdate=incubatorLigthStateData.updated_at
				if(incubatorLigthStateData.value=="ON"):
					print("encendido")
					pwm.start(dutyValue)
				elif(incubatorLigthStateData.value=="OFF"):
					print("apagado")
					pwm.ChangeDutyCycle(0)
					pwm.stop()
					
					# Set on dashboard (publish) ligth intensity in 0
					aio.send(incubatorLigthIntensity.key, 0)
			
			# check if the received data is new
			if(incubatorLigthIntensityData.updated_at!=incubatorLigthIntensityLastUpdate):
				# Update datetime update, for execute only one time
				incubatorLigthIntensityLastUpdate=incubatorLigthIntensityData.updated_at

				# Check value is a number, manage errors
				if(incubatorLigthIntensityData.value.isdigit()):
					dutyValue=int(incubatorLigthIntensityData.value)
					print("cambio de intensidad a {}%".format(dutyValue))
				else:
					print("Error en el Duty value, valor recibido -> {}".format(incubatorLigthIntensityData.value))
					
				# check if the actual state for LED is ON
				if(incubatorLigthStateData.value=="ON"):
					# change LED ilumination intensity
					pwm.ChangeDutyCycle(dutyValue)
							
	except KeyboardInterrupt:
		# Set default values in dashboard (publish)
		aio.send(incubatorLigthState.key, "OFF")
		aio.send(incubatorLigthIntensity.key, 0)
		
		# Stop PWM
		pwm.stop()
		
		# Clean
		GPIO.cleanup()
	

if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(e)
		GPIO.cleanup()
