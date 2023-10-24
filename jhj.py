import os
import time
import random

# Dimansyon konsòl la
largeur_konsol = 30
longè_konsol = 20

def netwaye_konsol():
    os.system('cls' if os.name == 'nt' else 'clear')

class Obstak:
    def __init__(self, largeur_konsol):
        self.largeur = random.randint(1, largeur_konsol)
        self.pozisyon = 0

    def move(self):
        self.pozisyon += 1

    def estwazini(self):
        return self.pozisyon == longè_konsol - 1

def jwe_tetris():
    obstak = Obstak(largeur_konsol)
    jwèt_fini = False
    score = 0

    while not jwèt_fini:
        netwaye_konsol()

        # Afiche obstak la
        konsol = [' ' * largeur_konsol for _ in range(longè_konsol)]
        konsol[obstak.pozisyon] = '✨✨' * obstak.largeur

        for line in konsol:
            print(line)

        if obstak.estwazini():
            jwèt_fini = True
            print("Jwèt la fini. Score ou se:", score)

        obstak.move()
        time.sleep(0.33)  # Delè 1/3 segonn

        score += 1

if __name__ == "__main__":
    jwe_tetris()
