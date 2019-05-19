# Import standard Python Modules
import time
import sys

# Import RPi.GPIO Module
try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO!  This is probably because you need \
	superuser privileges.  You can achieve \
	this by using 'sudo' to run your script")
	
# Define Function "main", way to manage errors
def main():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	# List with all GPIO pin numbers
	pinList=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

	# Set GPIO pin signal OUT and initial value "shutdown"
	GPIO.setup(pinList, GPIO.OUT, initial=GPIO.LOW)
	
	while True:
		try:
			pinNums=str(input("Ingrese los pines a interactuar, con el formato #, #, #\n"))
			pinNums="["+pinNums+"]"
			pinNums=eval(pinNums)
			newState=str(input("Indique el nuevo estado para los pines (ON o OFF)\n"))

			if(newState=="ON"):
				GPIO.output(pinNums, GPIO.HIGH)
			elif(newState=="OFF"):
				GPIO.output(pinNums, GPIO.LOW)
			else:
				print("estado invalido")
		except:
			print("Error al ejecutar lo ingresado:\n{} line {}".format(e, sys.exc_info()[-1].tb_lineno))

if __name__ == '__main__':
	try:
		main()
	except:
		print("{} line {}".format(sys.exc_info()[0], sys.exc_info()[-1].tb_lineno))
		GPIO.cleanup()

