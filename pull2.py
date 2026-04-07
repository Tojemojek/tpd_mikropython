from utime import sleep_ms, ticks_ms

from machine import Pin

przycisk = Pin(15, Pin.IN, Pin.PULL_UP)

ile_razy = 0
ile_czekac = 300

while True:
    ile_razy = ile_razy + 1
    print("stan: " + str(przycisk.value()))
    print(ile_razy)
    sleep_ms(ile_czekac)