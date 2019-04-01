# Adafruit Dashboard feed sharing
Adafruit is a Open Source Hardware Company, this company designs, manufactures and sells a number of electronics products, electronics components, tools and accessories. Also have a software Tools to develop and usage data analytic in Adafruit IO, here receive data in "Feeds" and store for several uses, this examples provides:

## To Supposed Topic
[Publish](/Example&#32;code/Adafruit&#32;Dashboard/mqtt&#32;to&#32;simulated&#32;topic&#32;publish.py "mqtt to supposed topic publish.py") and [Subscribe](/Example&#32;code/Adafruit&#32;Dashboard/mqtt&#32;to&#32;simulated&#32;topic&#32;subscribe.py "mqtt to simulated topic subscribe.py") codes, a publisher take data from simulated sensor (keyboard) and sends every 10 seconds, where data is received only by the subscriber, designed for test data on local system.
![Execute preview - simulated topic](/Images/Example&#32;code/Execute&#32;preview&#32;simulated&#32;topic.png)

## To Adafruit IO Server using Paho-mqtt
[Publish](/Example&#32;code/Adafruit&#32;Dashboard/mqtt&#32;to&#32;adafruit&#32;publish.py "mqtt to adafruit publish.py") and [Subscribe](/Example&#32;code/Adafruit&#32;Dashboard/mqtt&#32;to&#32;adafruit&#32;subscribe.py "mqtt to adafruit subscribe.py") codes, a publisher take data from simulated sensor (keyboard) and sends every 10 seconds, to certain topic such as *Username/feeds/GroupFeedKey.FeedKey* (Manually), to do the publish requeire Authenticate to Broker server with Adafruit IO Username and Adafruit IO Secret Key; the Username is the user in Adafruit IO, GropuFeedKey and FeedKey are in Feed Table in Adafruit IO Account.

The Data is published to topic *Username/feeds/GroupFeedKey.FeedKey* is received by Broker server **Adafruit IO** and stored in Feeds, the subscriber can catch same data, designed for test of feed sharing in Adafruit IO Feeds.
![Execute preview - adafruit paho](/Images/Example&#32;code/Execute&#32;preview&#32;adafruit&#32;paho.png)
![Execute result - adafruit paho](/Images/Example&#32;code/Execute&#32;result&#32;dashboard&#32;adafruit&#32;paho.png)


## To Adafruit IO Server using Adafruit IO Library in Python
[Publish](/Example&#32;code/Adafruit&#32;Dashboard/mqtt&#32;to&#32;adafruit&#32;with&#32;AIO_LIB&#32;publish.py "mqtt to adafruit with AIO_LIB publish.py") and [Subscribe](/Example&#32;code/Adafruit&#32;Dashboard/mqtt&#32;to&#32;adafruit&#32;&#32;with&#32;AIO_LIB&#32;subscribe.py "mqtt to adafruit with AIO_LIB subscribe.py") codes, a publisher take data from simulated sensor (keyboard) and sends every 10 seconds to the feed that is specified in the code, to do publish is required Adafruit IO Username, Adafruit IO, Adafruit IO Secret Key, to specify the feed require Group Feed Key and Feed Key; the Username is the user in Adafruit IO, GropuFeedKey and FeedKey are in Feed Table in Adafruit IO Account.

The Data publish follow certain protocol (execute by library, same protocol to [Adafruit IO Server using Paho-mqtt](#to-adafruit-io-server-using-paho-mqtt "Adafruit Server using paho") but Automatically), received by Broker server **Adafruit IO** and stored in Feeds, the subscriber can catch same data, designed for test of feed sharing in Adafruit IO Feeds.
![Execute preview - adafruit AIO LIB](/Images/Example&#32;code/Execute&#32;preview&#32;adafruit&#32;AIO&#32;library.png)
![Execute result - adafruit AIO LIB](/Images/Example&#32;code/Execute&#32;result&#32;dashboard&#32;adafruit&#32;AIO&#32;library.png)

# References
* [Adafruit IO Library - MQTT API Documentation](https://learn.adafruit.com/welcome-to-adafruit-io/mqtt-api-documentation-2)
* [Adafruit IO Library - Usage Example](https://adafruit-io-python-client.readthedocs.io/en/latest/feed-sharing.html#usage-example)
* [Adafruit Groups, Feeds, and Proper MQTT Topics](https://io.adafruit.com/blog/notebook/2017/11/02/groups-feeds-and-fixing-mqtt-topics/)
