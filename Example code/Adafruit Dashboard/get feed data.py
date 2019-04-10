# Import standard python modules
import time

# Import Adafruit IO MQTT client.
from Adafruit_IO import Client

if __name__ == "__main__":
    # Connect to Adafruit IO Server
    aio=Client(username="carlosmore", key="c0354363dc384523bc1022b5fb66d6b7")

    # Create feed objects
    incubatorLigthState=aio.feeds("incubadura0.estado-de-luz")
    incubatorLigthIntensity=aio.feeds("incubadura0.intensidad-luminica")
    while True:
        # get last data from the feeds, Warning should be have any data, not empty
        incubatorLigthStateData=aio.receive(incubatorLigthState.key)
        incubatorLigthIntensityData=aio.receive(incubatorLigthIntensity.key)

        print("Estado del LED {}".format(incubatorLigthStateData.value))
        print("Intensidad del LED".format(incubatorLigthIntensityData.value))