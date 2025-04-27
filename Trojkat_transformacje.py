
import pygame
import math

# Inicjalizacja
pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Transformacje trójkąta")

# Kolory
TLO = (255, 255, 0)  # Żółte tło
TROJKAT = (0, 0, 255)  # Niebieski trójkąt

# Funkcja do rysowania trójkąta
def rysuj_trojkat(punkty):
    pygame.draw.polygon(win, TROJKAT, punkty)

# Funkcja do przekształceń
def przeksztalc(punkty, operacja):
    nowe_punkty = []
    if operacja == 1:
        for x, y in punkty:
            nowe_punkty.append((300 + (x-300)*0.5, 300 + (y-300)*0.5))
    elif operacja == 2:
        for x, y in punkty:
            nowe_punkty.append((300 + (x-300)*1.5, 300 + (y-300)*1.5))
    elif operacja == 3:
        for x, y in punkty:
            nowe_punkty.append((300 + (y-300), 300 - (x-300)))
    elif operacja == 4:
        for x, y in punkty:
            nowe_punkty.append((300 + (x-300)*math.cos(math.pi/4) - (y-300)*math.sin(math.pi/4),
                                 300 + (x-300)*math.sin(math.pi/4) + (y-300)*math.cos(math.pi/4)))
    elif operacja == 5:
        for x, y in punkty:
            nowe_punkty.append((300 + (x-300)*2, y))
    elif operacja == 6:
        for x, y in punkty:
            nowe_punkty.append((x, 300 + (y-300)*2))
    elif operacja == 7:
        for x, y in punkty:
            nowe_punkty.append((600 - x, y))
    elif operacja == 8:
        for x, y in punkty:
            nowe_punkty.append((y, x))
    elif operacja == 9:
        for x, y in punkty:
            nowe_punkty.append((x, 600 - y))
    return nowe_punkty

# Początkowe wierzchołki trójkąta
punkty = [
    (300, 150),
    (150, 450),
    (450, 450)
]

run = True
while run:
    win.fill(TLO)
    rysuj_trojkat(punkty)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                operacja = event.key - pygame.K_0
                punkty = przeksztalc(punkty, operacja)

pygame.quit()
