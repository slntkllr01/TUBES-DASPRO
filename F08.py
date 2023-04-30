from csvfunction import *
from function import *
from database import *

def role_count(arr : list, role : str) -> int :
    count = 0
    for i in range(len(arr) - array_kosong_count(arr)):
        if arr[i][2] == role:
            count += 1
    return count

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

    if pengumpul_count == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        return

    print("Mengerahkan", pengumpul_count, "jin untuk mengumpulkan bahan.")
    print("Jin menemukan total", total_pasir, "pasir,", total_batu, "batu, dan", total_air, "air.")   

def batchbangun():
    global user, candi
    # Melakukan Validasi role
    if role != 'bandung_bondowoso':
        print("Ga punya akses!")
        return
    
    pembangun_count = role_count(user, "Pembangun")

    if pembangun_count == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        return
    else:
        # Inisialisasi Total Jumlah Pasir, Batu, Air yang dibutuhkan
        total_pasir = 0
        total_batu = 0
        total_air = 0

        # Memasukkan riwayat Jumlah Pasir, Batu, dan Air yang dibutuhkan untuk membangun candi sejumlah banyak pembangun

        riwayat_total = [[] for i in range(pembangun_count)]
        
        for i in range (pembangun_count):

            # Inisialisasi Jumlah Pasir, Batu, Air yang dibutuhkan untuk satu jin
            pasir = RandomNumber(0, 5, 234567889)
            batu = RandomNumber(0, 5, 678934569)
            air = RandomNumber(0, 5, 345678984)

            total_pasir += pasir; total_batu += batu; total_air += air
            riwayat_total[i] = [pasir, batu, air]

        if total_pasir <= int(bb[1][2]) and total_batu <= int(bb[2][2]) and total_air <= int(bb[3][2]):
            print("Mengerahkan", pembangun_count, "jin untuk membangun candi dengan total bahan", total_pasir, "pasir,", total_batu, "batu, dan", total_air, "air.")
            print("Jin berhasil membangun total", pembangun_count, "candi.")

            # Meng-update sisa bahan bangunan ke database bahan bangunan
            bb[1][2] = int(bb[1][2]); bb[1][2] -= total_pasir
            bb[2][2] = int(bb[2][2]); bb[2][2] -= total_batu
            bb[3][2] = int(bb[3][2]); bb[3][2] -= total_air

            # Meng-update candi yang telah dibangun ke database candi
            database_jin = database_username_jin(user, 'Pembangun')
            for i in range (pembangun_count):
                candi = add_to_database(candi, [[str(array_length(candi_csv)+i), database_jin[i], str(riwayat_total[i][0]), str(riwayat_total[i][1]), str(riwayat_total[i][2])]])
                print(candi)
        else:
            pasir_needed = abs(int(bb[1][2]) - total_pasir)
            batu_needed = abs(int(bb[2][2]) - total_batu)
            air_needed = abs(int(bb[3][2]) - total_air)
            print("Bangun gagal. Kurang", pasir_needed, "pasir,", batu_needed, "batu, dan", air_needed, "air.")

def database_username_jin(arr, role):
    result = []  # list kosong untuk menampung hasil
    for i in range(array_length(arr)):
        if array_length(arr[i]) >= 3 and arr[i][2] == role:  # Tujuannya agar tidak indexerror karena terdapat array kosong
            result = arr_append(result, arr[i][0])  # menambahkan nilai index[i][0] ke dalam result
    return result

batchbangun()
