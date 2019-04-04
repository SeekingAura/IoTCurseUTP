# Hygrometer FC-28
## How sensor Works
Soils moisture sensors get's data from the floor, uses on farming activities, this get value from conductivity between electrodes, if this nodes have full conductivity voltage value an raw value is cero.

## Get data from sensor
Hygrometer give 2 output signal type, Analog and Digital, Raspberry pi only can read digital signals, for that reason is required a [ADS1115 module](Example&#32;code/ADS1115&#32;Module), this convert an analog signal to Digital, the circut to get analog data from sensor FC-28 is.

### Electronic components
* Raspberry Pi
* Hygrometer Fc-28 Module
* ADS1115 Module

### Graphic Circuit.
![Hygrometer sensor](/Images/Circuits/Hygrometer&#32;FC-28&#32;Sensor_bb.png)

### Run in Terminal
```bash
python3 "Hygrometer get data.py"
```

# References
* [Build a Raspberry Pi Moisture Sensor to Monitor Your Plants](https://computers.tutsplus.com/tutorials/build-a-raspberry-pi-moisture-sensor-to-monitor-your-plants--mac-52875)
* [Raspberry pi projects Analog Input - 3 Way switch | ADS1115 ](https://www.youtube.com/watch?v=pBxeHlvF4eQ)
* [Basic tutorial of how to setup a soil moisture sensor with the Raspberry Pi. - Digital Signal](https://www.instructables.com/id/Soil-Moisture-Sensor-Raspberry-Pi/)