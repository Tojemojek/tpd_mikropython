from machine import Pin, PWM
from time import sleep_ms

buzzer = PWM(Pin(15))   # zmień pin, jeśli używasz innego GPIO

NOTES = {
    "C4": 262,
    "D4": 294,
    "E4": 330,
    "F4": 349,
    "G4": 392,
    "A4": 440,
    "P": 0
}

glosnosc = 15000  # możesz dostosować głośność (0-65535)

def c(czas: int):
    buzzer.freq(600)
    buzzer.duty_u16(glosnosc)
    sleep_ms(czas)
    buzzer.duty_u16(0)

def d(czas: int):
    buzzer.freq(294)
    buzzer.duty_u16(glosnosc)
    sleep_ms(czas)
    buzzer.duty_u16(0)

def e(czas: int):
    buzzer.freq(330)
    buzzer.duty_u16(glosnosc)
    sleep_ms(czas)
    buzzer.duty_u16(0)

def f(czas: int):
    buzzer.freq(349)
    buzzer.duty_u16(glosnosc)
    sleep_ms(czas)
    buzzer.duty_u16(0)

def g(czas: int):
    buzzer.freq(392)
    buzzer.duty_u16(glosnosc)
    sleep_ms(czas)
    buzzer.duty_u16(0)

def a(czas: int):
    buzzer.freq(440)
    buzzer.duty_u16(glosnosc)
    sleep_ms(czas)
    buzzer.duty_u16(0)

def pauza(czas: int):
    buzzer.duty_u16(0)
    sleep_ms(czas)


freq = 0

while freq < 10000:
    buzzer.freq(freq)
    buzzer.duty_u16(glosnosc)
    sleep_ms(100)
    freq += 50

buzzer.duty_u16(0)

# while True:
#     pauza(1000)  # pauza przed rozpoczęciem melodii
#     c(500)
#     d(500)
#     e(500)
#     c(500)
#     c(500)
#     d(500)
#     e(500)
#     c(500)
#     c(500)
#     d(500)
#     e(500)
#     f(500)
#     g(500)
#     pauza(500)
#     e(500)
#     f(500)
#     g(500)
#     pauza(500)
#     g(500)
#     a(500)
#     g(500)
#     f(500)
#     e(500)
#     c(500)
#     g(500)
#     a(500)
#     g(500)
#     f(500)
#     e(500)
#     c(500)
#     c(500)
#     g(500)
#     c(500)
#     pauza(500)
#     c(500)
#     g(500)
#     c(500)
#     pauza(500)


