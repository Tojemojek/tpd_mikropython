from machine import Pin
from utime import sleep_ms

zielone = Pin(0, Pin.OUT)
pomaranczowe = Pin(1, Pin.OUT)
czerwone = Pin(2, Pin.OUT)   
buzzer = Pin(15, Pin.OUT)   

def wszystkie_off():
    zielone.off()
    pomaranczowe.off()
    czerwone.off()

def wszystkie_on():
    zielone.on()
    pomaranczowe.on()
    czerwone.on()

print("Symulator świateł drogowych.")

while True:
    zielone.on()
    for _ in range(5):
        buzzer.on()
        sleep_ms(1000)
        buzzer.off()
        sleep_ms(1000)
    sleep_ms(1000)
    zielone.off()
    pomaranczowe.on()
    sleep_ms(1000)
    pomaranczowe.off()
    czerwone.on()
    sleep_ms(1000)
    pomaranczowe.on()
    sleep_ms(1000)
    wszystkie_off()