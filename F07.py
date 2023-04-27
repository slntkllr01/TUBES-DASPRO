from function import *
from database import *
from csvfunction import *

bb_csv = csv_to_array('bahan_bangunan.csv')
bb_array = add_to_database(bahan_bangunan, bb_csv)

def kumpul():
    pasir = RandomNumber(0, 5, 1344567543)
    batu = RandomNumber(0, 5, 4455224424)
    air = RandomNumber(0, 5, 8765432344)

    bahan_bangunan[1][2] = int(bahan_bangunan[1][2]); bahan_bangunan[1][2] += pasir
    bahan_bangunan[2][2] = int(bahan_bangunan[2][2]); bahan_bangunan[2][2] += batu
    bahan_bangunan[3][2] = int(bahan_bangunan[3][2]); bahan_bangunan[3][2] += air

    print("Selamat! Jin menemukan", pasir, "pasir,", batu ," batu, dan", air, "air.") 

kumpul()