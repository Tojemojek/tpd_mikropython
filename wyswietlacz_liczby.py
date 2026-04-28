from machine import Pin, PWM
from time import sleep_ms

s1 = Pin(0, Pin.OUT)
s2 = Pin(1, Pin.OUT)
s3 = Pin(2, Pin.OUT)
s4 = Pin(3, Pin.OUT)            
s5 = Pin(4, Pin.OUT)
s6 = Pin(5, Pin.OUT)
s7 = Pin(7, Pin.OUT)
s8 = Pin(6, Pin.OUT)    


def all_off():
    s1.off()
    s2.off()
    s3.off()
    s4.off()
    s5.off()
    s6.off()
    s7.off()
    s8.off()

def all_on():
    s1.on()
    s2.on()
    s3.on()
    s4.on()
    s5.on()
    s6.on()
    s7.on()
    s8.on()

def zero():
    all_off()
    s1.on()
    s3.on()
    s4.on()
    s5.on()
    s6.on()
    s7.on()

def jeden():
    all_off()
    s4.on()
    s7.on()

def dwa():
    all_off()
    s3.on()
    s2.on()
    s4.on()
    s5.on()
    s6.on()

def trzy():
    all_off()
    s2.on()
    s3.on()
    s4.on()
    s6.on()
    s7.on()

czas = 200

while True:
    zero()
    sleep_ms(czas)
    all_off()
    sleep_ms(czas)
    jeden()
    sleep_ms(czas)
    all_off()
    dwa()
    sleep_ms(czas)
    all_off()
    trzy()
    sleep_ms(czas)
    all_off()
    