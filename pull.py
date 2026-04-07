from utime import sleep_ms, ticks_ms

from machine import Pin

przycisk = Pin(15, Pin.IN, Pin.PULL_UP)

ile_razy = 0
ile_czekac = 1000

while True:
    if przycisk.value() == 1:
        print("Przycisk nie naciśnięty")
        print(ile_razy)
        sleep_ms(ile_czekac)
    else:
        print("Przycisk jest naciśnięty")
        print(ile_razy)
        sleep_ms(ile_czekac)