# Pyroelectric sensor HC-SR501
## How sensor works
PIR, "Passive Infrared", "Pyroelectric", or "IR motion" is made basically with Pyroelectricity, this can be described as the ability of certain materials to generate a temporary voltage when they are heated or cooled. This sensor can detect levels of infrared radiation. 

The sensor detect a motion in IR levels of enviroment, have two usage mode retriggering (jumper placed in H), this mode output HIGH while detect motion and non-retriggering (jumper placed in L), this mode output HIGH for some time (depend of sensivity pulse time) and set output in LOW, if motion is still set HIGH again (for the same last time), the sensivity pulse time and tiemout length can change turn the screws right for increase left to decrease

## Get data from sensor
PIR sensor have a 1 output signal type, digital, this signal output 0 if not are motion in IR levels of enviroment and 1 if are motion, to program this sensor depend the mode are activated, in retriggering mode output are 1 indicate while motion in area, 0 indicate no motion (get 1 to 0 when pulse time is reached), this is usefull to measure motion time or event only then motion start and stop, in non-retriggering mode 0 to 1 indicate motion and when pulse time is reached the output if are in 1 change to 0, even if motion still continue, this is usefull to generate event for motion detection every pulse time.

The example code [PIR get data.py](/Example&#32;code/Pyroelectric&#32;HC-SR501&#32;Sensor) use PIR retriggering mode, this show event when started to detect a motion and event when are not more motion with the time stamp, to interact only require a [GPIO Pins](/Example&#32;code/GPIO#32;Pins).

### Electronic Devices
* Raspberry Pi
* PIR Sensor

### Graphic circuit
![PIR sensor circuit](/Images/Circuits/Pyroelectric&#32;HC-SR501&#32;Sensor_bb.png)

### Run in Terminal
```bash
python3 "PIR get data.py"
```

# References
* [Adafruit PIR Motion Sensor - Overview](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/overview)
* [InfraTec - FAQ](https://www.infratec-infrared.com/sensor-division/service-support/faq/)
* [Adafruit learning system - PIR Motion Sensor](https://cdn-learn.adafruit.com/downloads/pdf/pir-passive-infrared-proximity-motion-sensor.pdf)