# Hall effect sensor - KY-024 Linear magnetic sensor
## How sensor works
Effect hall is current-carrying conductor is placed into magnetic field, a voltage will be generated perpendicular to both the current and the field, this current-carrying change about magnetic field, is usefull to detect if a certain element is near o far, for example door closing, liquid level, triger limit and more.

## Get data from the sensor
KY-024 Linear magnetic sensor, give 2 output signal type, analog and digital signal, with digital signal sensor output only 0 when not are an magnetic element and 1 when is magnetic element near, the sensivity about this detection can change with potenciometer (screw on the module), turn rigth to increase, turn left to decrease. But analog signal get how much magnetic field are near to the sensor. The example code [Hall Effect get data.py](Hall&#32;Effect#32;get#32;data.py) get data from analog output, because with a precision magnetic value can implement a better trigger (discard middle values), Raspberry pi only can read digital signals, for that reason is required a [ADS1115 module](Example&#32;code/ADS1115&#32;Module).

Depend about magnet side (South North) is change about this sensor (positive or negative), each material have a diferent magnet field force, this is important to know how close it must magnet be for detect some are there or not.

### Electronic componentes
* Raspberry Pi
* KY-024 Linear magnetic Hall Sensor
* ADS1115 Module

### Graphic circuit
![KY-024 Linear magnetic Hall Sensor circuit](/Images/Circuits/KY-024&#32;Linear&#32;magnetic&#32;Hall&#32;Sensor_bb.png)

### Run in Terminal
```bash
python3 "Hall Effect get data.py"
```

# References
* [HALL EFFECT SENSING AND APPLICATION - Honeywell](https://sensing.honeywell.com/hallbook.pdf)
* [KY-024 Linear magnetic Hall Sensor](http://sensorkit.en.joy-it.net/index.php?title=KY-024_Linear_magnetic_Hall_Sensor)
* [Keyes KY 024 Hall Sensor](https://github.com/R2D2-2017/R2D2-2017/wiki/Keyes-KY-024-Hall-Sensor)
* [Arduino Modules - KY-024 Linear Magnetic Hall Module.fzpz](https://arduinomodules.info/download/ky-024-linear-magnetic-hall-module-zip-file/)