from machine import Pin, PWM
from time import sleep_ms

buzzer = PWM(Pin(15))   # zmień pin, jeśli używasz innego GPIO

# buzzer.freq(440)  # ustaw częstotliwość na A4 (440 Hz)
# buzzer.duty_u16(10000)  # początkowo wyłącz dź
# sleep_ms(10000)  # poczekaj chwilę przed rozpoczęciem melodii
# buzzer.duty_u16(0)


# czestoliwosci = 10

# while czestoliwosci < 10000:
#     print(czestoliwosci)
#     buzzer.freq(czestoliwosci)
#     buzzer.duty_u16(10000)  # ustaw głośność (0-65535)
#     sleep_ms(100)  # czas trwania dźwięku
#     czestoliwosci += 50

# buzzer.duty_u16(0)  # wyłącz dźwięk po zakończeniu pętli




# NOTES = {
#     "C4": 262,
#     "D4": 294,
#     "E4": 330,
#     "F4": 349,
#     "G4": 392,
#     "A4": 440,
#     "P": 0
# }

glosnosc = 15000  # możesz dostosować głośność (0-65535)

def c(czas: int):
    buzzer.freq(262)
    buzzer.duty_u16(glosnosc)
    sleep_ms(czas)
    buzzer.duty_u16(0)

def pauza(czas: int):
    buzzer.duty_u16(0)
    sleep_ms(czas)



# c(500)
# pauza(500)
# c(250)
# pauza(250)
# c(125)





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



# freq = 0

# # while freq < 10000:
# #     buzzer.freq(freq)
# #     buzzer.duty_u16(glosnosc)
# #     sleep_ms(100)
# #     freq += 50

buzzer.duty_u16(0)

while True:
    pauza(1000)  # pauza przed rozpoczęciem melodii
    c(500)
    d(500)
    e(500)
    c(500)
    c(500)
    d(500)
    e(500)
    c(500)
    c(500)
    d(500)
    e(500)
    f(500)
    g(500)
    pauza(500)
    e(500)
    f(500)
    g(500)
    pauza(500)
    g(500)
    a(500)
    g(500)
    f(500)
    e(500)
    c(500)
    g(500)
    a(500)
    g(500)
    f(500)
    e(500)
    c(500)
    c(500)
    g(500)
    c(500)
    pauza(500)
    c(500)
    g(500)
    c(500)
    pauza(500)


