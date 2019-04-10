# Import standard python modules
import time

# Import RPi.GPIO library
import RPi.GPIO as GPIO     

# Import Adafruit IO MQTT client.
from Adafruit_IO import Client


def main():
    # var GPIO pin to show output
    led_pin = 21
    
    # Set GPIO pin mode
    GPIO.setmode(GPIO.BCM)
    # Set GPIO pin direction
    GPIO.setup(led_pin, GPIO.OUT)   # Declaring pin 21 as output pin
    
    # Setup PWM instance to led_pin with 100 Hz
    pwm = GPIO.PWM(led_pin, 60)
    
    aio=Client(username="carlosmore", key="c0354363dc384523bc1022b5fb66d6b7")
    incubatorLigthState=aio.feeds("incubadura0.estado-de-luz")
    incubatorLigthIntensity=aio.feeds("incubadura0.intensidad-luminica")
    dutyValue=0
    
    incubatorLigthStateLastUpdate=""
    incubatorLigthIntensityLastUpdate=""

    try:
        while True:
            # get data from Adafruit IO
            incubatorLigthStateData=aio.receive(incubatorLigthState.key)
            incubatorLigthIntensityData=aio.receive(incubatorLigthIntensity.key)
           
            if(incubatorLigthStateData.updated_at!=incubatorLigthStateLastUpdate):
                incubatorLigthStateLastUpdate=incubatorLigthStateData.updated_at
                if(incubatorLigthStateData.value=="ON"):
                    print("encendido")
                    pwm.start(dutyValue)
                elif(incubatorLigthStateData.value=="OFF"):
                    print("apagado")
                    pwm.ChangeDutyCycle(0)
                    pwm.stop()
                    # Set on dashboard ligth intensity in 0
                    aio.send(incubatorLigthIntensity.key, 0)
            
            if(incubatorLigthIntensityData.updated_at!=incubatorLigthIntensityLastUpdate):
                incubatorLigthIntensityLastUpdate=incubatorLigthIntensityData.updated_at
                if(incubatorLigthIntensityData.value.isdigit()):
                    dutyValue=int(incubatorLigthIntensityData.value)
                    
                if(incubatorLigthStateData.value=="ON"):
                    print("cambio de intensidad a {}%".format(dutyValue))
                    pwm.ChangeDutyCycle(dutyValue)
                            
    except KeyboardInterrupt:
        # set default values in dashboard
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
