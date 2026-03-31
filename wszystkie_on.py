from machine import Pin
from utime import sleep_ms

zielone = Pin(0, Pin.OUT)
pomaranczowe = Pin(1, Pin.OUT)
czerwone = Pin(2, Pin.OUT)   


def wszystkie_off():
    zielone.off()
    pomaranczowe.off()
    czerwone.off()

def wszystkie_on():
    zielone.on()
    pomaranczowe.on()
    czerwone.on()

print("Na zmianę zapalają się wszystkie diody, a potem gasną.")

while True:
    wszystkie_on()
    sleep_ms(1000)
    wszystkie_off()
    sleep_ms(1000)
