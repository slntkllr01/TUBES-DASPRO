from function import *
from Bonus import *

def kumpul(role, bb):
    if role != 'Pengumpul':
        print("\nMaaf, Command ini hanya bisa diakses oleh Jin Pengumpul!\n")
    else:
        pasir = lcg(0, 5, 1344567543)
        batu = lcg(0, 5, 4455224424)
        air = lcg(0, 5, 8765432344)

        bb[1][2] = int(bb[1][2]); bb[1][2] += pasir
        bb[2][2] = int(bb[2][2]); bb[2][2] += batu
        bb[3][2] = int(bb[3][2]); bb[3][2] += air

        print("\nSelamat! Jin menemukan", pasir, "pasir,", batu ," batu, dan", air, "air.\n")