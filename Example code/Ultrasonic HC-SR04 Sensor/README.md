# Ultra sonic sensor HC-sr04
## How sensor works
An ultrasonic sensor when trigger are activate send a ultrasonic pulses, this pulse reflect with any object and when received for ultrasonic sensor this send data to "echo" pin, the time to triggered ultrasonic pulse and received by ultrasonic sensor can get an approximate distance.

At 20 °C the speed of sound on air is 343 meters/second, therefore time in seconds since trigered and until receives by ultrasonic sensor divided with 2 (because the pulse goes and back), is the distance between ultrasonic sensor and the object.

## Get data from sensor
The Ultra sonic sensor HC-sr04 have a pin for Trigger and pin for receive echo, on raspberry pi the easy way to use sensor is manually get distance, the example code [ultrasonic hc-sr04 get data.py](/Example&#32;code/Ultrasonic&#32;HC-SR04&#32;Sensor/ultrasonic&#32;get&#32;data.py), interact to this sensor with [GPIO Pins](/Example&#32;code/GPIO&#32;Pins), the process to get data is activate a trigger, measure time since sensor is triggered until echo receive a signal from ultrasonic pulse.

The time in python is measured in seconds(default) to get distance should be multiplied with speed value for sound in air and divide with 2, the value sensor change for several factors, depend about use with this data should be take some considerations and extra operations. The circuit have a Pull Down on the ECHO pin with this make a sure signal 0 on ECHO pin and discard *noises* on the signal.

### Eletronic devices
* Raspberry Pi
* 1 Resistor 330Ohms
* 1 Resistor 470Ohms
* Ultrasonic HC-SR04 sensor

### Graphic Circuit
![HC-SR04 sensor](/Images/Circuits/UltraSonic&#32;HC-sr04&#32;Sensor_bb.png)
UltraSonic HC-SR04 Sensor_bb.png
### Run in Terminal
```bash
python3 "ultrasonic hc-sr04 get data.py"
```

# References
* [Velocidad del Sonido en el Aire](http://hyperphysics.phy-astr.gsu.edu/hbasees/Sound/souspe.html)
* [Física/Acústica/Velocidad del sonido](https://es.wikibooks.org/wiki/F%C3%ADsica/Ac%C3%BAstica/Velocidad_del_sonido)
* [Ultrasonic Sensors: How They Work (and How to Use Them with Arduino)](https://www.arrow.com/en/research-and-events/articles/ultrasonic-sensors-how-they-work-and-how-to-use-them-with-arduino)
* [Using a Raspberry Pi distance sensor (ultrasonic sensor HC-SR04)](https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/)
* [Resistencia pull up y pull down - Programar facil](https://programarfacil.com/blog/arduino-blog/resistencia-pull-up-y-pull-down/)