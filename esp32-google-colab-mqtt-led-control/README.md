# ESP32 Google Colab MQTT LED Control

## Objective

Develop an IoT-based LED control system where Google Colab publishes MQTT messages and an ESP32 subscribes to those messages to control an LED wirelessly.

## Components

* ESP32
* LED
* Wi-Fi Network
* Google Colab
* MQTT Broker

## Topics Covered

* ESP32
* MicroPython
* Google Colab
* MQTT Protocol
* Publisher-Subscriber Model
* Wi-Fi Communication
* IoT Applications

## Files

* esp32_subscriber.py
* google_colab_mqtt_publisher.ipynb
* diagram.json
* circuit.png
* serial-monitor.png

## Description

This project demonstrates an IoT-based LED control system using the MQTT publish-subscribe communication model. Google Colab acts as the MQTT publisher by sending LED ON and OFF commands to an MQTT broker, while the ESP32 subscribes to the same topic and controls the LED based on the received messages. The project illustrates cloud-to-device communication, wireless control, MQTT messaging, and embedded IoT development using ESP32 and MicroPython.

