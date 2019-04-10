# Import standard python modules
import time

# Import Adafruit IO MQTT client.
from Adafruit_IO import Client

if __name__ == "__main__":
    if(len(sys.argv)!=5):
		sys.stderr.write('Usage: "{0}" $AdafruitIOUsername $AdafruitIOKey\n'.format(sys.argv[0]))
		os._exit(1)
    # Connect to Adafruit IO Server
    aio=Client(username=sys.argv[1], key=sys.argv[2])

    # Create feed objects
    incubatorLigthState=aio.feeds("incubadura0.estado-de-luz")
    incubatorLigthIntensity=aio.feeds("incubadura0.intensidad-luminica")
    while True:
        # get last data from the feeds, Warning should be have any data, not empty
        incubatorLigthStateData=aio.receive(incubatorLigthState.key)
        incubatorLigthIntensityData=aio.receive(incubatorLigthIntensity.key)

        print("Estado del LED {}".format(incubatorLigthStateData.value))
        print("Intensidad del LED".format(incubatorLigthIntensityData.value))