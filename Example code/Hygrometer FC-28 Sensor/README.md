# Hygrometer FC-28
## How sensor Works
Soils moisture sensors get's data from the soil, uses on farming activities, this get value from conductivity between electrodes, if is wet soil these electrodes have full conductivity then voltage value an raw value is near to zero, if is dry soil the electrodes have few conductivity the voltage value and raw value is higer than zero.

## Get data from sensor
Hygrometer have 2 output signal type, Analog and Digital, with digital signal the sensor only output 0 when is dry and 1 when is wet, the sensivity about detection can change with potenciometer (screw inside module), turn rigth to increase, turn left to decrease. But with analog signal sensor output a range of values (depend about protocol read). The example code [Hygrimeter get data.py](/Example&#32;code/Hygrometer&#32;FC-28&#32;Sensor/Hygrometer&#32;get&#32;data.py) get data from analog output, a precision data is useful for a better data analytic, because analog signal give a continuos data, raspberry pi only can read digital signals, for that reason is required a [ADS1115 module](/Example&#32;code/ADS1115&#32;Module), this convert an analog signal to digital (where is the data with certain protocol).

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
* [Guide for Soil Moisture Sensor YL-69 or HL-69 with Arduino](https://randomnerdtutorials.com/guide-for-soil-moisture-sensor-yl-69-or-hl-69-with-the-arduino/)