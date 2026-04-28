from machine import Pin, PWM
from time import sleep_ms

buzzer = PWM(Pin(15))
GLOSNOSC = 17000
TEMPO = 145

NUTY = {
    "C4": 262,
    "D4": 294,
    "E4": 330,
    "F4": 349,
    "G4": 392,
    "A4": 440,
    "B4": 494,
    "C5": 523,
    "D5": 587,
    "E5": 659,
    "F5": 698,
    "G5": 784,
    "A5": 880,
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
    sleep_ms(15)


def beat(n: float) -> int:
    return int((60000 / TEMPO) * n)


# Przyblizona linia melodyczna z glownego motywu "Techno Syndrome"
MORTAL_KOMBAT = [
    # Intro hook
    ("A4", beat(0.5)), ("A4", beat(0.5)), ("C5", beat(0.75)), ("A4", beat(0.5)),
    ("D5", beat(0.75)), ("A4", beat(0.5)), ("E5", beat(1.0)), ("P", beat(0.5)),

    ("A4", beat(0.5)), ("A4", beat(0.5)), ("C5", beat(0.75)), ("A4", beat(0.5)),
    ("D5", beat(0.75)), ("A4", beat(0.5)), ("F5", beat(1.0)), ("P", beat(0.5)),

    # Powtorzenie jak w refrenie
    ("A4", beat(0.5)), ("A4", beat(0.5)), ("C5", beat(0.75)), ("A4", beat(0.5)),
    ("D5", beat(0.75)), ("A4", beat(0.5)), ("E5", beat(1.0)), ("P", beat(0.5)),

    ("A4", beat(0.5)), ("A4", beat(0.5)), ("C5", beat(0.75)), ("A4", beat(0.5)),
    ("D5", beat(0.75)), ("A4", beat(0.5)), ("F5", beat(1.0)), ("P", beat(0.75)),

    # Sekcja "Mortal Kombat!" (wysokie akcenty)
    ("C5", beat(0.5)), ("E5", beat(0.5)), ("G5", beat(0.75)), ("E5", beat(0.5)),
    ("C5", beat(0.5)), ("E5", beat(0.5)), ("A5", beat(1.0)), ("P", beat(0.5)),

    ("C5", beat(0.5)), ("E5", beat(0.5)), ("G5", beat(0.75)), ("E5", beat(0.5)),
    ("C5", beat(0.5)), ("D5", beat(0.5)), ("E5", beat(1.0)), ("P", beat(1.0)),
]


buzzer.duty_u16(0)

while True:
    for nuta, czas in MORTAL_KOMBAT:
        zagraj(nuta, czas)
    sleep_ms(900)
