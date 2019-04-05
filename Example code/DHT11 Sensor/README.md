# Relative Humidity and temperature Sensor DHT11 Module
## How sensor works
This sensor measures relative humidity with conductivity between 2 electrodes, the conductivity change resistence and then voltage value (at more resistence, more humidity value), and temperature measures with thermistor, this component resistor change about a temperature (because is a material semiconductive such ceramics).

Sensor DHT11 module give a digital signal output with certain protocol MUC(Micro-computer Unite or single chip Computer, see also on [Datasheet](https://www.mouser.com/ds/2/758/DHT11-Technical-Data-Sheet-Translated-Version-1143054.pdf))

## Get data from sensor
On protocol MUC, to make sure the signal level stays high by default is required make pull-up resistor (5KOhms minimum, with shorter cable) on the circuit, the pull-up resistor discarts *noises* in the signal. 

A raspberry pi can get a percentage of humidity and temperature Celcius from Adafruit DHT library, this library is designed for [Adafruit DHT sensor](https://www.adafruit.com/product/385), but can works with this [DHT11 Sensor](https://dualtronica.com/sensores/25-sensor-de-temperatura-y-humedad-relativa-dht11.html), the example code [DHT11 get data.py](/Example&#32;code/DHT11&#32;Sensor/DHT11&#32;get&#32;data.py) get data with Adafruit DHT library.

### Electronic components
* Raspberry Pi
* DHT11 Module
* 5kOhms-10kOhms Resistor

### Graphic Circuit.
![DHT11 circuit - Test](/Images/Circuits/DHT11&#32;Sensor_bb.png)

### Run in Terminal
```bash
python3 "DHT11 get data.py"
```

# References
* [Resistencia pull up y pull down - Programar facil](https://programarfacil.com/blog/arduino-blog/resistencia-pull-up-y-pull-down/)
* [HOW TO SET UP THE DHT11 HUMIDITY SENSOR ON THE RASPBERRY PI](http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/)
* [Raspberry Pi: Measure Humidity and Temperature with DHT11/DHT22](https://tutorials-raspberrypi.com/raspberry-pi-measure-humidity-temperature-dht11-dht22/)
* [DHT11-module-fritzing-part](https://github.com/HuangYuTse/DHT11-module-fritzing-part)