# MQTT Protocol with Paho-mqtt
## About MQTT
The Eclipse Paho project provides open-source client implementations of MQTT and MQTT-SN messaging protocols aimed at new, existing. In Internet of Things (IoT) is very important communication between devices for send data and generate alerts.

MQTT Protocol for comunication use a intermediate device known as "Broker", the broker can configurate with [mosquitto](https://mosquitto.org/) (C library for implementing MQTT), this receive messages with a "topic", the topic works how a "address" to where send data, but more 1 devices can have the same "topic" or topic how "regular expresion", to send message is *Publish*, to receive message is *Subscribe*.

## Simple protocol usage
The example code [publish&#46;py](/Example&#32;code/MQTT&#32;Protocol/publish.py) does a publish to topic *area0/plant0/temp*, the message data *{temp: 30}*, and the example code [subscribe.py](/Example&#32;code/MQTT&#32;Protocol/subscribe.py) subscribe to topic *area0/plant0/temp*, this receive all publish messages from anywhere for mentioned topic.
### Run in Terminal
#### Subscribe
```bash
python3 subscribe.py "$hostAddress"
```
#### Publish
```bash
python3 publish.py "$hostAddress"
```
Where *$hostAddress* is the Broker Server Addres, for test can use a local server or a public server.

# References
* [Tutorial Raspberry Pi - GPIO y MQTT (Parte 1)](https://geekytheory.com/tutorial-raspberry-pi-gpio-y-mqtt-parte-1/ )
* [Paho-mqtt PyPi](https://pypi.org/project/paho-mqtt/)
* [Eclipse Paho](https://www.eclipse.org/paho/)
* [Beginners Guide To The Paho MQTT Python Client](http://www.steves-internet-guide.com/into-mqtt-python-client/)
* [Quick Guide to The Mosquitto.conf File With Examples](http://www.steves-internet-guide.com/mossquitto-conf-file/ )