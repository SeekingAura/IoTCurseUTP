# Adafruit Dashboard send and get data in feed
## Some about Adafruit
Adafruit is a Open Source Hardware Company, this company designs, manufactures and sells a number of electronics products, electronics components, tools and accessories. Also have a software Tools to develop and usage data analytic in Adafruit IO, here receive data in "Feeds" and store for several uses, this examples provides:

## Send and get data to simulated local system
The example code [send data to simulated feed with paho-mqtt publish.py](/Example&#32;code/Adafruit&#32;Dashboard/send&#32;data&#32;to&#32;simulated&#32;feed&#32;with&#32;paho-mqtt&#32;publish.py) take data from simulated sensor (keyboard) and make a publish every 10 seconds, the data published is received by example code [get data form simulated feed with paho-mqtt subscribe.py](/Example&#32;code/Adafruit&#32;Dashboard/get&#32;data&#32;from&#32;simulated&#32;feed&#32;with&#32;paho-mqtt&#32;subscribe.py). These example code use a Paho-mqtt library to publish and subscribe to a certain topic (to simulate feed sharing), designed for test data on local system.
### Run in terminal
#### Get data
```bash
python3 "get data form simulated feed with paho-mqtt subscribe.py" "$hostAddress"
```
#### Send data
```bash
python3 "send data to simulated feed with paho-mqtt publish.py" "$hostAddress"
```
Where *$hostAddress* is the Broker Server Addres, for test can use a local server or a public server.

### Run Preview
#### Terminal
![Execute preview - simulated topic](/Images/Example&#32;code/Execute&#32;preview&#32;simulated&#32;topic.png)

## Send and get data to Adafruit IO feeds with Paho-mqtt
The example code [send data to feed with paho-mqtt publish.py](/Example&#32;code/Adafruit&#32;Dashboard/send&#32;data&#32;to&#32;feed&#32;with&#32;paho-mqtt&#32;publish.py) take data from simulated sensor (keyboard) and make a publish every 10 seconds, the data published is received by Broker server **Adafruit IO** and stored in respective Feeds, the example code [get data from feed with paho-mqtt subscribe.py](/Example&#32;code/Adafruit&#32;Dashboard/get&#32;data&#32;from&#32;feed&#32;with&#32;paho-mqtt&#32;subscribe.py) get data from every publish data (only on the moment when this is publish). These example code use a Paho-mqtt library to publish and subscribe to topics that follow the Adafruit IO Group and Feed format *Username/feeds/GroupFeedKey.FeedKey* (Manually).

Connect to Broker require Authentication on server with Adafruit IO Username and Adafruit IO Secret Key, designed for test of send data to certain topics with paho-mqtt and receive data in adafruit feed.
### Run in terminal
#### Get data
```bash
python3 "get data from feed with paho-mqtt subscribe.py" "$AdafruitIOUsername" "$AdafruitIOKey" "$AdafruitIOGroupKey" "$AdafruitIOFeedKey"
```
#### Send data
```bash
python3 "send data to feed with paho-mqtt publish.py" "$AdafruitIOUsername" "$AdafruitIOKey" "$AdafruitIOFeedKey"
```

### Run preview
#### Terminal
![Execute preview - adafruit paho](/Images/Example&#32;code/Execute&#32;preview&#32;adafruit&#32;paho.png)
#### Adafruit IO - Feed Data
![Execute result - adafruit paho](/Images/Example&#32;code/Execute&#32;result&#32;dashboard&#32;adafruit&#32;paho.png)


## Send and get data to Adafruit IO feeds with Adafruit IO MQTT Library in Python
[send data to feed with AIO_LIB mqtt publish.py](/Example&#32;code/Adafruit&#32;Dashboard/send&#32;data&#32;to&#32;feed&#32;with&#32;AIO_LIB&#32;mqtt&#32;publish.py) take data from simulated sensor (keyboard) and make a publish every 10 seconds, the data published is received by Broker server **Adafruit IO** and stored in respective Feeds, the example code [get data from feed with AIO_LIB mqtt subscribe.py](/Example&#32;code/Adafruit&#32;Dashboard/get&#32;data&#32;from&#32;feed&#32;with&#32;AIO_LIB&#32;mqtt&#32;subscribe.py) get data from every publish (only on the moment when this is publish). These example code use a Adafruit IO MQTT client, to do publish is required Adafruit IO Username, Adafruit IO Secret Key, to specify the feed require Group Feed Key and Feed Key; the Username is the user in Adafruit IO, GropuFeedKey and FeedKey are in Feed Table of Adafruit IO Account.

Connect to Broker require Authentication on server with Adafruit IO Username and Adafruit IO Secret Key, the publish follow certain protocol (execute by library, same protocol to [Send and get data to Adafruit IO feeds with Paho-mqtt](#send-and-get-data-to-adafruit-io-feeds-with-paho-mqtt) but Automatically), designed for test of send data to Adafruit IO Feeds with properly mqtt Adafruit IO library.
### Run in Terminal
#### Get data
```bash
python3 "get data from feed with AIO_LIB mqtt subscribe.py" "$AdafruitIOUsername" "$AdafruitIOKey" "$AdafruitIOGroupKey" "$AdafruitIOFeedKey"
```
#### Send data
```bash
python3 "send data to feed with AIO_LIB mqtt publish.py" "$AdafruitIOUsername" "$AdafruitIOKey" "$AdafruitIOFeedKey"
```

### Run preview
#### Terminal
![Execute preview - adafruit AIO LIB](/Images/Example&#32;code/Execute&#32;preview&#32;adafruit&#32;AIO&#32;library.png)
#### Adafruit IO - Feed Data
![Execute result - adafruit AIO LIB](/Images/Example&#32;code/Execute&#32;result&#32;dashboard&#32;adafruit&#32;AIO&#32;library.png)

## Send data to Adafruit IO feeds with Adafruit IO Client Library in Python
[send data to feed with AIO_LIB Client.py](/Example&#32;code/Adafruit&#32;Dashboard/send&#32;data&#32;to&#32;feed&#32;with&#32;AIO_LIB&#32;Client.py) take data from simulated sensor (keyboard) and make a publish every 10 seconds, the data is send with properly method of Adafruit IO API is received by Broker server **Adafruit IO** and stored in respective Feeds, the last feed data is retreive with method *receive* on the example code [get data from feed with AIO_LIB Client.py](/Example&#32;code/Adafruit&#32;Dashboard/get&#32;data&#32;from&#32;fedd&#32;with&#32;AIO_LIB&#32;Client.py) take per iteration the last value, if feed is empty this generate error 404, the functions in these example code require Adafruit IO Username, Adafruit IO Secret Key, to specify the feed require Feed Key; the Username is your username in Adafruit IO, FeedKey are in Feed Table of Adafruit IO Account.

Connect to Broker require Authentication on server with Adafruit IO Username and Adafruit IO Secret Key, designed for test of send data to adafruit IO Feeds with Adafruit IO library properly methods.

### Run in terminal
#### Get data
```bash
python3 "get data from feed with AIO_LIB Client.py" "$AdafruitIOUsername" "$AdafruitIOKey" "$AdafruitIOFeedKey"
```

#### Send data
```bash
python3 "send data to feed with AIO_LIB Client.py" "$AdafruitIOUsername" "$AdafruitIOKey" "$AdafruitIOFeedKey"
```

### Run preview
#### Terminal
![Execute preview - adafruit AIO LIB Properly](/Images/Example&#32;code/Execute&#32;preview&#32;adafruit&#32;AIO&#32;library&#32;properly.png)
#### Adafruit IO - Feed Data
![Execute result - adafruit AIO LIB Properly](/Images/Example&#32;code/Execute&#32;result&#32;dashboard&#32;adafruit&#32;AIO&#32;library.png)


# References
* [Adafruit IO Library - MQTT API Documentation](https://learn.adafruit.com/welcome-to-adafruit-io/mqtt-api-documentation-2)
* [Adafruit IO Library - Usage Example](https://adafruit-io-python-client.readthedocs.io/en/latest/feed-sharing.html#usage-example)
* [Adafruit IO Groups, Feeds, and Proper MQTT Topics](https://io.adafruit.com/blog/notebook/2017/11/02/groups-feeds-and-fixing-mqtt-topics/))
* [Adafruit IO Home: Lights and Temperature - Learn all about home automation by building a cardboard's](https://learn.adafruit.com/adafruit-io-house-lights-and-temperature/python-code)