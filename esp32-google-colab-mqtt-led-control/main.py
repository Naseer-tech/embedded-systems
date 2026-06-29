import network
import time
from machine import Pin
from umqtt.simple import MQTTClient


WIFI_SSID = "Wokwi-GUEST"
WIFI_PASSWORD = ""


MQTT_BROKER = "broker.hivemq.com"
CLIENT_ID = "esp32-led"
TOPIC = b"home/led"


led = Pin(2, Pin.OUT)
led.off()


wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

print("Connecting to WiFi...")

while not wifi.isconnected():
    time.sleep(0.5)

print("WiFi Connected!")
print(wifi.ifconfig())


def message_callback(topic, msg):
    print("Received:", topic, msg)

    if msg == b"ON":
        led.on()
        print("LED ON")

    elif msg == b"OFF":
        led.off()
        print("LED OFF")


client = MQTTClient(CLIENT_ID, MQTT_BROKER)

client.set_callback(message_callback)

client.connect()

print("Connected to MQTT")

client.subscribe(TOPIC)

print("Subscribed to:", TOPIC)


while True:
    client.check_msg()
    time.sleep(0.1)
