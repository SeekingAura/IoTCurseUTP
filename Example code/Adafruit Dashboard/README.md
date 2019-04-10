# Adafruit Dashboard feed sharing
## Some about Adafruit
Adafruit is a Open Source Hardware Company, this company designs, manufactures and sells a number of electronics products, electronics components, tools and accessories. Also have a software Tools to develop and usage data analytic in Adafruit IO, here receive data in "Feeds" and store for several uses, this examples provides:

## Get and send data local system
The example code [mqtt to simulated topic publish.py](/Example&#32;code/Adafruit&#32;Dashboard/mqtt&#32;to&#32;simulated&#32;topic&#32;publish.py) take data from simulated sensor (keyboard) and make a publish every 10 seconds, the data published is received by example code [mqtt to simulated topic subscribe.py](/Example&#32;code/Adafruit&#32;Dashboard/mqtt&#32;to&#32;simulated&#32;topic&#32;subscribe.py). These example code use a Paho-mqtt library to publish and subscribe to a certain topic (to simulate feed sharing), designed for test data on local system.
### Run in terminal
#### Subscribe
```bash
python3 mqtt to simulated topic subscribe.py "$hostAddress"
```
#### Publish
```bash
python3 mqtt to simulated topic subscribe.py "$hostAddress"
```
Where *$hostAddress* is the Broker Server Addres, for test can use a local server or a public server.

### Run Preview
#### Terminal
![Execute preview - simulated topic](/Images/Example&#32;code/Execute&#32;preview&#32;simulated&#32;topic.png)

## Feed sharing to Adafruit IO Server using Paho-mqtt
The example code [mqtt to adafruit publish.py](/Example&#32;code/Adafruit&#32;Dashboard/mqtt&#32;to&#32;adafruit&#32;publish.py) take data from simulated sensor (keyboard) and make a publish every 10 seconds, the data published is received by Broker server **Adafruit IO** and stored in respective Feeds, the example code [mqtt to adafruit subscribe.py](/Example&#32;code/Adafruit&#32;Dashboard/mqtt&#32;to&#32;adafruit&#32;subscribe.py) can catch every publish data. These example code use a Paho-mqtt library to publish and subscribe to topics that follow the Adafruit IO Group and Feed format *Username/feeds/GroupFeedKey.FeedKey* (Manually).

To do the publish require Authentication on Broker server with Adafruit IO Username and Adafruit IO Secret Key, designed for test of feed sharing in Adafruit IO Feeds.
### Run in terminal
#### Subscribe
```bash
python3 mqtt to simulated topic subscribe.py "$AdafruitIOUsername" "$AdafruitIOKey" "$AdafruitIOGroupKey" "$AdafruitIOFeedKey"
```
#### Publish
```bash
python3 mqtt to simulated topic subscribe.py "$AdafruitIOUsername" "$AdafruitIOKey" "$AdafruitIOFeedKey"
```
Where *$AdafruitIOUsername* is the user in Adafruit IO, *$AdafruitIOKey* is the Secret Key (this can get in Adafruit IO Dashboard on link *View AIO Key*), *AdafruitIOGroupKey* and *AdafruitIOFeedKey* are in Feed Table in Adafruit IO Account

### Run preview
#### Terminal
![Execute preview - adafruit paho](/Images/Example&#32;code/Execute&#32;preview&#32;adafruit&#32;paho.png)
#### Adafruit IO - Feed Data
![Execute result - adafruit paho](/Images/Example&#32;code/Execute&#32;result&#32;dashboard&#32;adafruit&#32;paho.png)


## Feed sharing to Adafruit IO Server using Adafruit IO Library in Python
[mqtt to adafruit with AIO_LIB publish.py](/Example&#32;code/Adafruit&#32;Dashboard/mqtt&#32;to&#32;adafruit&#32;with&#32;AIO_LIB&#32;publish.py) take data from simulated sensor (keyboard) and make a publish every 10 seconds, the data published is received by Broker server **Adafruit IO** and stored in respective Feeds, the example code [mqtt to adafruit with AIO_LIB subscribe.py](/Example&#32;code/Adafruit&#32;Dashboard/mqtt&#32;to&#32;adafruit&#32;&#32;with&#32;AIO_LIB&#32;subscribe.py) can catch every publish data. These example code use a Adafruit IO MQTT client, to do publish is required Adafruit IO Username, Adafruit IO, Adafruit IO Secret Key, to specify the feed require Group Feed Key and Feed Key; the Username is the user in Adafruit IO, GropuFeedKey and FeedKey are in Feed Table in Adafruit IO Account.

The publish follow certain protocol (execute by library, same protocol to [Adafruit IO Server using Paho-mqtt](#feed-sharing-to-adafruit-io-server-using-paho-mqtt) but Automatically), designed for test of feed sharing in Adafruit IO Feeds.
### Run in Terminal
#### Subscribe
```bash
python3 mqtt to simulated topic subscribe.py "$AdafruitIOUsername" "$AdafruitIOKey" "$AdafruitIOGroupKey" "$AdafruitIOFeedKey"
```
#### Publish
```bash
python3 mqtt to simulated topic subscribe.py "$AdafruitIOUsername" "$AdafruitIOKey" "$AdafruitIOFeedKey"
```
Where *$AdafruitIOUsername* is the user in Adafruit IO, *$AdafruitIOKey* is the Secret Key (this can get in Adafruit IO Dashboard on link *View AIO Key*), *AdafruitIOGroupKey* and *AdafruitIOFeedKey* are in Feed Table in Adafruit IO Account

### Run preview
#### Terminal
![Execute preview - adafruit AIO LIB](/Images/Example&#32;code/Execute&#32;preview&#32;adafruit&#32;AIO&#32;library.png)
#### Adafruit IO - Feed Data
![Execute result - adafruit AIO LIB](/Images/Example&#32;code/Execute&#32;result&#32;dashboard&#32;adafruit&#32;AIO&#32;library.png)

# References
* [Adafruit IO Library - MQTT API Documentation](https://learn.adafruit.com/welcome-to-adafruit-io/mqtt-api-documentation-2)
* [Adafruit IO Library - Usage Example](https://adafruit-io-python-client.readthedocs.io/en/latest/feed-sharing.html#usage-example)
* [Adafruit IO Groups, Feeds, and Proper MQTT Topics](https://io.adafruit.com/blog/notebook/2017/11/02/groups-feeds-and-fixing-mqtt-topics/))