from machine import Pin, PWM, ADC
import time

led = PWM(Pin(19))
led.freq(1000)

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)

while True:
    value = pot.read()    

    brightness = value // 4   

    led.duty(brightness)

    print("ADC =", value,
          "Brightness =", brightness)

    time.sleep(1)