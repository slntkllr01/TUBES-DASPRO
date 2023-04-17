from function import RandomNumber
from database import bahan_bangunan 

def kumpul():
    pasir = RandomNumber(0, 5, 1344567543)
    batu = RandomNumber(0, 5, 4455224424)
    air = RandomNumber(0, 5, 8765432344)
    
    # Inisialisasi Nama
    bahan_bangunan[1][0] = 'pasir'
    bahan_bangunan[2][0] = 'batu'
    bahan_bangunan[3][0] = 'air'

    # Inisialisasi Deskripsi
    bahan_bangunan[1][1] = 'Jumlah dari bahan pasir yang tersedia saat ini.'
    bahan_bangunan[2][1] = 'Jumlah dari bahan batu yang tersedia saat ini.'
    bahan_bangunan[3][1] = 'Jumlah dari bahan air yang tersedia saat ini.'

    bahan_bangunan[1][2] += pasir
    bahan_bangunan[2][2] += batu
    bahan_bangunan[3][2] += air

    print("Selamat! Jin menemukan ", pasir, "pasir, ", batu ," batu, dan ", air, " air.")

kumpul()