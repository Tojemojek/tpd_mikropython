from machine import Pin, PWM
from time import sleep_ms

buzzer = PWM(Pin(15))
GLOSNOSC = 16000

NUTY = {
    "C4": 262,
    "D4": 294,
    "E4": 330,
    "F4": 349,
    "G4": 392,
    "A4": 440,
    "B4": 494,
    "C5": 523,
    "P": 0,
}


def zagraj(nuta: str, czas_ms: int):
    freq = NUTY[nuta]
    if freq == 0:
        buzzer.duty_u16(0)
        sleep_ms(czas_ms)
        return

    buzzer.freq(freq)
    buzzer.duty_u16(GLOSNOSC)
    sleep_ms(czas_ms)
    buzzer.duty_u16(0)
    sleep_ms(25)


BELLA_CIAO = [
    # Intro / fraza glowna
    ("E4", 260), ("A4", 260), ("B4", 260), ("C5", 260), ("A4", 260), ("P", 120),
    ("E4", 260), ("A4", 260), ("B4", 260), ("C5", 260), ("A4", 260), ("P", 120),

    # Pierwsze rozwiniecie
    ("E4", 260), ("A4", 260), ("B4", 260), ("C5", 260), ("B4", 260), ("A4", 260),
    ("G4", 260), ("E4", 260), ("G4", 260), ("A4", 380), ("P", 160),

    # Refrain (styl z serialu - bardziej marszowy)
    ("A4", 260), ("B4", 260), ("C5", 260), ("B4", 260), ("A4", 260), ("G4", 260),
    ("E4", 260), ("P", 120),
    ("A4", 260), ("B4", 260), ("C5", 260), ("B4", 260), ("A4", 260), ("G4", 260),
    ("E4", 380), ("P", 180),

    # Powtorzenie glownej linii
    ("E4", 260), ("A4", 260), ("B4", 260), ("C5", 260), ("A4", 260), ("P", 120),
    ("E4", 260), ("A4", 260), ("B4", 260), ("C5", 260), ("A4", 260), ("P", 120),

    # Zakonczenie dluzsze
    ("E4", 260), ("A4", 260), ("B4", 260), ("C5", 260), ("B4", 260), ("A4", 260),
    ("G4", 260), ("F4", 260), ("E4", 260), ("D4", 260), ("E4", 520),
    ("P", 700),
]


buzzer.duty_u16(0)

while True:
    for nuta, czas in BELLA_CIAO:
        zagraj(nuta, czas)
    sleep_ms(1200)
