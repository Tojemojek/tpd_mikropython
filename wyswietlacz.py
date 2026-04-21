from machine import Pin, PWM
from time import sleep_ms

# Pin 3 lub 8 do GND

segment = Pin(15, Pin.OUT) 
segment2 = Pin(14, Pin.OUT) 

while True:
    segment.on()
    sleep_ms(500)
    segment.off()
    sleep_ms(500)
    segment2.on()
    sleep_ms(500)
    segment2.off()
    sleep_ms(500)