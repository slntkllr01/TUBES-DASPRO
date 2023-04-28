from csvfunction import *
from function import *
from database import *

def role_count(arr : list, role : str) -> int :
    count = 0
    for i in range(len(arr) - array_kosong_count(arr)):
        if arr[i][2] == role:
            count += 1
    return count

role = 'bandung_bondowoso'

def batchkumpul():
    global user, role

    # Melakukan Validasi role
    if role != 'bandung_bondowoso':
        print("Ga punya akses!")
        return
    
    # Inisialisasi Jumlah Pasir, Batu, Air yang terkumpul untuk satu jin
    pasir = RandomNumber(0, 5, 1344567543)
    batu = RandomNumber(0, 5, 4765432345)
    air = RandomNumber(0, 5, 8765432344)

    # Inisialisasi Total Jumlah Pasir, Batu, Air yang terkumpul
    total_pasir = 0
    total_batu = 0
    total_air = 0

    pengumpul_count = role_count(user_csv, "Pengumpul")

    for i in range (pengumpul_count):
        total_pasir += pasir; total_batu += batu; total_air += air

    # Memasukkan ke Database
    bb[1][2] = int(bb[1][2]); bb[1][2] += total_pasir
    bb[2][2] = int(bb[2][2]); bb[2][2] += total_batu
    bb[3][2] = int(bb[3][2]); bb[3][2] += total_air

    print("Mengerahkan", pengumpul_count, "jin untuk mengumpulkan bahan.")
    print("Jin menemukan total", total_pasir, "pasir,", total_batu, "batu, dan", total_air, "air.")   

def batchbangun():
    # Melakukan Validasi role
    if role != 'bandung_bondowoso':
        print("Ga punya akses!")
        return
    
    pengumpul_count = role_count(user_csv, "Pembangun")

    if pengumpul_count == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        return
    else:    
        # Inisialisasi Jumlah Pasir, Batu, Air yang dibutuhkan untuk satu jin
        pasir = RandomNumber(0, 5, 234567889)
        batu = RandomNumber(0, 5, 678934569)
        air = RandomNumber(0, 5, 345678984)

        # Inisialisasi Total Jumlah Pasir, Batu, Air yang dibutuhkan
        total_pasir = 0
        total_batu = 0
        total_air = 0

        for i in range (pengumpul_count):
            total_pasir += pasir; total_batu += batu; total_air += air


        if total_pasir <= int(bb[1][2]) and total_batu <= int(bb[2][2]) and total_air <= int(bb[3][2]):
            print("Mengerahkan", pengumpul_count, "jin untuk membangun candi dengan total bahan", total_pasir, "pasir,", total_batu, "batu, dan", total_air, "air.")
            print("Jin berhasil membangun total", pengumpul_count, "candi.")
            bb[1][2] = int(bb[1][2]); bb[1][2] -= total_pasir
            bb[2][2] = int(bb[2][2]); bb[2][2] -= total_batu
            bb[3][2] = int(bb[3][2]); bb[3][2] -= total_air
            print(bb)
        else:
            pasir_needed = abs(int(bb[1][2]) - total_pasir)
            batu_needed = abs(int(bb[2][2]) - total_batu)
            air_needed = abs(int(bb[3][2]) - total_air)
            print("Bangun gagal. Kurang", pasir_needed, "pasir,", batu_needed, "batu, dan", air_needed, "air.")       

    



