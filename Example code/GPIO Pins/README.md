# GPIO Pins Raspberry Pi
## Raspberry Pi and interactions with eletronic devices
Raspberry Pi can interact with electronic Devices on general purpouse input/output (GPIO) Pins, those must been setup as input or output, in case of setup Output can assigned a signal value in LOW (0 or False) or HIGH (1 or True), or in the case setup input only get data from this Pin.

The Device have 26 GPIO pins, something of those have other functions such as SDA, SLI, I2c, SPI, GEN, TX, RX, etc. To get GPIO number check this table.

![GPIO Table](https://www.raspberrypi.org/documentation/usage/gpio/images/gpio-numbers-pi2.png)

#### Table with misc functions
|  →   |   →    |        →        |    ↓    |    ↓    |        ←        |    ←   |   ←  |
|:----:|:------:|:---------------:|:-------:|:-------:|:---------------:|:------:|:----:|
| Pin# |  NAME  |       Misc      |    ↓    |    ↓    |       Misc      |  NAME  | Pin# |
|  01  |  3.3v  |     DC Power    |&#x1F538;|&#x1F534;|     DC Power    |   5v   |  02  |
|  03  | GPIO02 |   (SDA1, I2C)   |&#x1F535;|&#x1F534;|     DC Power    |   5v   |  04  |
|  05  | GPIO03 |   (SCL1, I2C)   |&#x1F535;|&#x26AB; |                 | Ground |  06  |
|  07  | GPIO04 |   (GPIO_GCLK)   |&#x1F518;|&#x1F539;|      (TXD0)     | GPIO14 |  08  |
|  09  | Ground |                 |&#x26AB; |&#x1F539;|      (RXD0)     | GPIO15 |  10  |
|  11  | GPIO17 |   (GPIO_GEN0)   |&#x1F518;|&#x1F518;|   (GPIO_GEN1)   | GPIO18 |  12  |
|  13  | GPIO27 |   (GPIO_GEN2)   |&#x1F518;|&#x26AB; |                 | Ground |  14  |
|  15  | GPIO22 |   (GPIO_GEN3)   |&#x1F518;|&#x1F518;|   (GPIO_GEN4)   | GPIO23 |  16  |
|  17  |  3.3v  |     DC Power    |&#x1F538;|&#x1F518;|   (GPIO_GEN5)   | GPIO24 |  18  |
|  19  | GPIO10 |    (SPI_MOSI)   |&#x1F4A0;|&#x26AB; |                 | Ground |  20  |
|  21  | GPIO09 |    (SPI_MISO)   |&#x1F4A0;|&#x1F518;|   (GPIO_GEN6)   | GPIO25 |  22  |
|  23  | GPIO11 |    (SPI_CLK)    |&#x1F4A0;|&#x1F4A0;|   (SPI_CE0_N)   | GPIO08 |  24  |
|  25  | Ground |                 |&#x26AB; |&#x1F4A0;|   (SPI_CE1_N)   | GPIO07 |  26  |
|  27  |  ID_SD | (I2C ID EEPROM) |&#x1F532;|&#x1F532;| (I2C ID EEPROM) |  ID_SC |  28  |
|  29  | GPIO05 |                 |&#x1F518;|&#x26AB; |                 | Ground |  30  |
|  31  | GPIO06 |                 |&#x1F518;|&#x1F518;|                 | GPIO12 |  32  |
|  33  | GPIO13 |                 |&#x1F518;|&#x26AB; |                 | Ground |  34  |
|  35  | GPIO19 |                 |&#x1F518;|&#x1F518;|                 | GPIO16 |  36  |
|  37  | GPIO26 |                 |&#x1F518;|&#x1F518;|                 | GPIO20 |  38  |
|  39  | Ground |                 |&#x26AB; |&#x1F518;|                 | GPIO21 |  40  |
|  →   |   →    |        →        |    ↑    |    ↑    |         ←       |    ←   |   ←  |
To read this table the 5.0v are in rigth of raspberry (near to border)

## Testing GPIO Pins
GPIO Pins can use with system sentences or programing language such as python, the example code [LED on and off.py](/Example&#32;code/GPIO&#32;Pins/LED&#32;on&#32;and&#32;off.py) test all GPIO Pins with simple digital signals, on the execute turn on the ascendant of GPIO Pin Number and turn off the descendant GPIO Pin Number. This example use [RPi.GPIO](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/) Library (exist others for that), RPi.GPIO can use PWM technique, this is usefull for change ligth intensity, modulate motor speed and more, the example code [LED brightness.py](/Example&#32;code/GPIO&#32;Pins/LED&#32;brightness.py) turn on a LED in GPIO 21 with low brigtness, this increment 1% per 0.01 seconds and when it reaches 100% this decrease 1% until 0%.

### Electronical components
* Raspberry pi
* 26 Leds
* 26 resistor 220Ohms-1kOhms

### Graphic circuit
![GPIO pin Test LEDs](/Images/Circuits/LED&#32;on&#32;and&#32;off_bb.png)

### Run in termal
```bash
python3 "LED on and off.py"
```
```bash
python3 "LED brightness.py"
```
# References
* [GPIO Official Documentation](https://www.raspberrypi.org/documentation/usage/gpio/)
* [GPIO Zero Offical Documentation](https://www.raspberrypi.org/documentation/usage/gpio/python/README.md)
* [RPi.GPIO Wiki](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/)
* [RPi.GPIO PyPI](https://pypi.org/project/RPi.GPIO/)
* [Migration RPi.GPIO to GPIO Zerp](https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html)
* [GPIO Pin Numbering](https://www.raspberrypi.org/forums/viewtopic.php?t=196696)