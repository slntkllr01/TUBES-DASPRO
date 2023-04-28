from function import *
from database import *
from csvfunction import *

def kumpul():
    pasir = RandomNumber(0, 5, 1344567543)
    batu = RandomNumber(0, 5, 4455224424)
    air = RandomNumber(0, 5, 8765432344)

    bb[1][2] = int(bb[1][2]); bb[1][2] += pasir
    bb[2][2] = int(bb[2][2]); bb[2][2] += batu
    bb[3][2] = int(bb[3][2]); bb[3][2] += air

    print("Selamat! Jin menemukan", pasir, "pasir,", batu ," batu, dan", air, "air.") 

kumpul()