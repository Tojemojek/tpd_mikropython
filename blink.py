from machine import Pin
from utime import sleep

zielone = Pin("LED", Pin.OUT)

while True:
    zielone.toggle()
    sleep(1000)