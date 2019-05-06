# Import standard python modules
import time
import sys

# Import Raspberry Hardware
import board
import busio

# Import ADS1115 module
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Import RPi.GPIO Module
import RPi.GPIO as GPIO

def main():
	# Create the I2C bus
	i2c = busio.I2C(board.SCL, board.SDA)

	# Create the ADC object using the I2C bus
	ads = ADS.ADS1115(i2c)

	# Create single-ended input on channel 0
	chan = AnalogIn(ads, ADS.P0)

	# Dict with some GPIO pin numbers
	pinList={"poca":14, "estable":15, "demasiado":16}

	# Setup GPIO setmode
	GPIO.setmode(GPIO.BCM)

	# Set GPIO pin signal OUT and initial value "shutdown"
	GPIO.setup(list(pinList.values()), GPIO.OUT, initial=GPIO.LOW)

	# Control vars
	rawValueMin=0
	rawValueMax=33000
	rawValueDeltaMax=rawValueMax-rawValueMin
	lastState=""

	while True:
		humidityPercentage=float(100-((chan.value-rawValueMin)/rawValueDeltaMax)*100)
		print("porcentaje de humedad {:.2f}%".format(humidityPercentage))
		if(humidityPercentage<40):
			state="poca"
		elif(humidityPercentage>75):
			state="demasiado"
		else:
			state="estable"

		if(state!=lastState):
			GPIO.output(list(pinList.values()), GPIO.LOW)
			GPIO.output(pinList.get(state), GPIO.HIGH)
			lastState=state
			print("cambio de estado a {}".format(state))
		
		time.sleep(0.5)

if __name__=="__main__":
	try:
		main()
	except:
		print("{} line {}".format(sys.exc_info()[0], sys.exc_info()[-1].tb_lineno))
		GPIO.cleanup()