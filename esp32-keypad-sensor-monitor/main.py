from machine import Pin, I2C
from time import sleep
from i2c_lcd import I2cLcd
from bmp180 import BMP180
import dht


i2c = I2C(0, scl=Pin(23), sda=Pin(22), freq=100000)

lcd = I2cLcd(i2c, 0x27, 2, 16)

bmp = BMP180(i2c)

dht_sensor = dht.DHT22(Pin(15))


rows = [
    Pin(19, Pin.OUT),
    Pin(18, Pin.OUT),
    Pin(5, Pin.OUT),
    Pin(17, Pin.OUT)
]

cols = [
    Pin(16, Pin.IN, Pin.PULL_DOWN),
    Pin(4, Pin.IN, Pin.PULL_DOWN),
    Pin(2, Pin.IN, Pin.PULL_DOWN),
    Pin(21, Pin.IN, Pin.PULL_DOWN)
]

keys = [
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*','0','#','D']
]


def get_key():

    for r in range(4):

        for row in rows:
            row.value(0)

        rows[r].value(1)

        for c in range(4):

            if cols[c].value():

                while cols[c].value():
                    pass

                return keys[r][c]

    return None


lcd.clear()
lcd.putstr("1:Temp2:Pressure")
lcd.move_to(0,1)
lcd.putstr("3:Humidity")


while True:

    key = get_key()

    if key == '1':

        dht_sensor.measure()

        temperature = dht_sensor.temperature()

        lcd.clear()
        lcd.putstr("Temperature")
        lcd.move_to(0,1)
        lcd.putstr(str(temperature) + " C")

    elif key == '2':

        pressure = bmp.pressure()

        lcd.clear()
        lcd.putstr("Pressure")
        lcd.move_to(0,1)
        lcd.putstr("{:.1f} hPa".format(pressure/100))

    elif key == '3':

        dht_sensor.measure()

        humidity = dht_sensor.humidity()

        lcd.clear()
        lcd.putstr("Humidity")
        lcd.move_to(0,1)
        lcd.putstr(str(humidity) + " %")

    elif key == '*':

        lcd.clear()
        lcd.putstr("1:T 2:P")
        lcd.move_to(0,1)
        lcd.putstr("3:H")

    sleep(0.1)