from machine import Pin, PWM
from utime import sleep_ms, ticks_ms, ticks_diff

zielone = Pin(0, Pin.OUT)
pomaranczowe = Pin(1, Pin.OUT)
czerwone = Pin(2, Pin.OUT)
przycisk = Pin(3, Pin.IN, Pin.PULL_UP)


def wszystkie_off():
    zielone.off()
    pomaranczowe.off()
    czerwone.off()


def sekwencja_startowa():
    czerwone.on()
    sleep_ms(1000)
    pomaranczowe.on()
    sleep_ms(1000)
    zielone.on()
    sleep_ms(1000)
    wszystkie_off()


print("Gra refleksowa.")
print("Po zgaśnięciu wszystkich diod naciśnij i puść przycisk.")

while True:
    wszystkie_off()
    sekwencja_startowa()

    if przycisk.value() == 0:
        print("NIE OSZUKUJ!")
        print("Naciśnięty przycisk przed startem!")
    
    # Zaczynamy mierzyć czas od momentu zgaśnięcia wszystkich diod
    start = ticks_ms()
    
    # Czekamy na naciśnięcie przycisku
    # Co milisekundę sprawdzamy, czy przycisk został naciśnięty
    while przycisk.value() == 1:
        sleep_ms(1)
    
    # Wyszliśmy z pętli - czyli przycisk został naciśnięty
    koniec = ticks_ms()

    # Obliczamy różnicę między czasem naciśnięcia a czasem startu
    czas_do_nacisniecia = ticks_diff(koniec, start)

    # Piszemy wynik
    print("Czas do naciśnięcia:", czas_do_nacisniecia, "ms")
    print("---")

    sleep_ms(5000)
