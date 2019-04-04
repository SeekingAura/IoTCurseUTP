# ADS1115 Ultra-Small Low-Power I2c Compatible
## Types of signals
On electronic cicuits and components, can work with 2 kind of signal, analog and digital

**Digital Signal:** Digital signal are discontinuous in time, give a certain discrete values

**Analog Signal:** Analog signal are a continue in time, for that reason gives data all time and is more precise

## Usage of device
The Raspberry pi can't read analog signals, for that reason is require use a ADS1115 Module, this take an analog signal and send information in digital signal.

This module works with any electronical device, such as [Hygrometer FC-28](/Example&#32;code/Hygrometer&#32;FC-28&#32;Sensor), [Hall sensor](/Example&#32;code/Hall&#32;Effect&#32;Sensor) (analog outputs). The example code *ADS1115* show how get data from the ADS1115 Decice to SDA pin in raspberry, the circuit to use this module is.
### Electronic components
* Raspberry Pi
* ADS1115
* Any device with Analog Output

To wire this sensor in raspberry pi is.
* ADS1115 VDD al Pin Raspberry Pi 3.3V
* ADS1115 GND to Raspberry Pi GND
* ADS1115 SCL to Raspberry Pi SCL
* ADS1115 SDA to Raspberry Pi SDA
* ADS1115 A0-A4 analog output from sensors
### Graphic circuit
![ADS Module](/Images/Circuits/ADS1115&#32;module_bb.png)

Raspberry receive an interpreted data of all inputs into SDA, the example code show how to get.

### Run in Terminal
```bash
python3 "ADS1115 get data.py"
```

# References
* [Basic tutorial of how to setup a soil moisture sensor with the Raspberry Pi - Digital Signal](https://www.instructables.com/id/Soil-Moisture-Sensor-Raspberry-Pi/)
* [Raspberry pi projects Analog Input - 3 Way switch | ADS1115 + ACS712](https://www.youtube.com/watch?v=pBxeHlvF4eQ)