from machine import Pin
from utime import sleep_ms

zielone = Pin(0, Pin.OUT)
pomaranczowe = Pin(1, Pin.OUT)
czerwone = Pin(2, Pin.OUT)   
przycisk = Pin(3, Pin.IN, Pin.PULL_UP)

def wszystkie_off():
    zielone.off()
    pomaranczowe.off()
    czerwone.off()

def wszystkie_on():
    zielone.on()
    pomaranczowe.on()
    czerwone.on()

print("Naciśnij przycisk, aby zapalić wszystkie diody.")
print("Zwolnij przycisk, aby zgasić wszystkie diody.")
while True:
    wszystkie_off()
   
    if przycisk.value() == 1:
        wszystkie_off()
    else:
        wszystkie_on()
        sleep_ms(10000)
