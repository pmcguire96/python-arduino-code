# tempScript.py
# Author: Patrick Michael McGuire III
# Created: 07 May 2018
# Purpose: Read temperature every 60 seconds 
# 	using Adafruit DHT22 sensor on Raspberry Pi

import Adafruit_DHT
import datetime

int i = 0;

# runs for 24 hours
while i < 1440:
	sensor = Adafruit_DHT.DHT11
	pin = 4
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

	print 'Temperature: ', temperature, 'Celsius  ||  Time: ', datetime.datetime.now().time()
	time.sleep(60)
	i++
	
