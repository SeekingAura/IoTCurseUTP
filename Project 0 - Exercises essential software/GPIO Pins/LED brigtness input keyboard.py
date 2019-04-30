# Import standard python modules
import time
import sys

# Import RPi.GPIO library
try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO!  This is probably because you need \
	superuser privileges.  You can achieve \
	this by using 'sudo' to run your script")

# Define Function "main", way to manage errors
def main():
	# List with all GPIO pin numbers
	pinList=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
	
	# Set GPIO pin mode
	GPIO.setmode(GPIO.BCM)
	
	# Set GPIO pin direction and initial in Off
	GPIO.setup(pinList, GPIO.OUT, initial=GPIO.LOW)
	
	# create a list for pwm instances
	pwmList=[]
	for i in pinList:
		# Setup PWM instance to led_pin with 60 Hz
		pwm = GPIO.PWM(i, 60)

		# add pwm instance to pwm list
		pwmList.append(pwm)
	
		# start PWM at 0% duty cycle 
		pwm.start(0)
	
	while True:
		# Catch errors
		try:
			pinNums=str(input("Ingrese los pines a interactuar, con el formato #, #, #\n"))
			pinNums="["+pinNums+"]"

			# convert string to integer list
			pinNums=eval(pinNums)

			percentage=str(input("Indique el porcentaje a asignar a los pines\n"))
			percentage=float(percentage)
			
			for i in pinNums:
				pwmList[i-2].ChangeDutyCycle(percentage)
				
		except Exception as e:
			print("Error al ejecutar lo ingresado:\n{} line".format(e, sys.exc_info()[-1].tb_lineno))


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(e, "line", sys.exc_info()[-1].tb_lineno)
		GPIO.cleanup()
