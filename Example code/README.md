# Test circuits and modules
Example codes show basic usage about modules and circuits, this can combinate to build projects, here is neccesary modules and circuits for IoT Curse projects, all using a programing languague python.

## Content
### Adafruit Dashboard
Tools for receive and store data (1 month), data analytic, generate and use triggers, alerts, conectivity IoT Projects, this give a Broker server (MQTT Protocol) but is only for feed sharing data and actions for triggers. Supply tools for build Dashboard to show data and then does data analytic, here can use int, float, position values and more.  
[Adafruit Dashboard - Folder](/Example&#32;code/Adafruit&#32;Dashboard)

### ADS1115 Module
Convert analog signal to digital signal, this is a helpfull tool for raspberry pi, because raspberry can't read analog signals, this is a necesary module to get float and precision data.

[ADS1115 - Folder](/Example&#32;code/ADS1115&#32;Module)

### DHT11 Sensor
Sensor to read temperature and humidity enviroment, this module give digital output signal, the data received is high precision because send data with a MUC protocol, useful for activate air conditioner.

[DHT11 Sensor - Folder](/Example&#32;code/ADS1115&#32;Module)

### GPIO Pins
Raspberry Pi can interface to electronical devices with GPIO Pins, this can send output signals, read input signals from the sensors and more configurations about event control.

[GPIO Pins - Folder](/Example&#32;code/GPIO&#32;Pins)

### Hall Effect Sensor
Detect magnetive presence, have digital and analog output, digital output only show if are magnetive presence or no, analog output gives magnitive measurement, for analog signal is required [ADS1115 Module](#ads1115-module).

[Hall Effect Sensor- Folder]()

### Hygrometer FC-28 Sensor
Soil moisture is calculate with Hygrometer FC-28 Sensor, the value about humidity is conductivity between electrodes of the sensor, sensor hve analog and digital output, where digital output indicate if are or not humidity, analog output can indicate percentage of humidity but is required [ADS1115 Module](#ads1115-module).

[Hygrometer FC-28 Sensor - Folder](/Example&#32;code/Hygrometer&#32;FC-28&#32;Sensor)

### MQTT Protocol
Comunication with publish and subscribe adminsitrative by a Broker server (can be local, public, private) usage with python library Paho-mqtt, this used for feed sharing in [Adafruit IO Library](#adafruit-dashboard), comunication process is very important on IoT projects.

[MQtt Protocol - Folder](/Example&#32;code/MQTT&#32;Protocol)

### Piroelectric Sensor
PIR sensor reacts


### Ultrasonic Sensor HC-sr04
Ultrasonic Sensor works with ultra sonic pulses, this sensor can generate ultra sonic pulse and detect when this pulse is received on the sensor generate a output digital signal, this sensor have some applications how: measure object distance, check if something is near, measurement liquid on a deposit. 

To work on raspberry pi requires do the measurement manually, the process is trigger ultra sonic pulse, start measure time, wait for receive pulse, stop measure time, multiply by sound spped, divide by 2, all signals are digital.

[Ultrasonic Sensor - Folder](/Example&#32;code/Ultrasonic&#32;Sensor&#32;HC-sr04)




