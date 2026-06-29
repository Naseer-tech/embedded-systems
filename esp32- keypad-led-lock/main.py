from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)


rows = [Pin(19, Pin.OUT), Pin(18, Pin.OUT), Pin(5, Pin.OUT), Pin(17, Pin.OUT)]
cols = [Pin(16, Pin.IN, Pin.PULL_DOWN),
        Pin(4, Pin.IN, Pin.PULL_DOWN),
        Pin(2, Pin.IN, Pin.PULL_DOWN),
        Pin(21, Pin.IN, Pin.PULL_DOWN)]

keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

password = "1234"
entered = ""

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

while True:
    key = get_key()

    if key:

        if key == '*':
            entered = ""
            led.off()

        else:
            entered += key

            
            if len(entered) == 4:
                if entered == password:
                    print("Correct Password")
                    led.on()
                else:
                    print("Wrong Password")
                    led.off()

                entered = ""

    sleep(0.05)