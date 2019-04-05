# Import standard python modules
import time

# Import Raspberry Hardware
import board
import busio

# Import ADS1115 module
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


if __name__=="__main__":
	# Create the I2C bus
	i2c = busio.I2C(board.SCL, board.SDA)

	# Create the ADC object using the I2C bus
	ads = ADS.ADS1115(i2c)

	# Create single-ended input on channel 0
	chan = AnalogIn(ads, ADS.P0)

	# Create differential input between channel 0 and 1
	#chan = AnalogIn(ads, ADS.P0, ADS.P1)
	
	print("{:>5}\t{:>5}".format('raw', 'v'))

	while True:
		print("{0:>5}, {1:>5}".format(chan.value,chan.voltage))
		time.sleep(0.5)
