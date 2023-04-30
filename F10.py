from csvfunction import *
from function import *
from database import *

def laporancandi():
    global role
    if role == 'bandung_bondowoso':

        # mencari Total Candi dan Bahan Bangunan
        total_candi = (array_length(candi) - array_kosong_count(candi) - 1)
        total_pasir = totalharga(2)
        total_batu = totalharga(3)
        total_air = totalharga(4)

        # Mencari ID Candi Termurah dan Termahal beserta Harganya (dalam Rupiah)
        harga_termurah = float('inf')
        harga_termahal = float('-inf')
        id_termurah = ''
        id_termahal = ''

        length_candi = (array_length(candi) - array_kosong_count(candi))

        for i in range(1, (length_candi)):

            pasir = int(candi[i][2])
            batu = int(candi[i][3])
            air = int(candi[i][4])
            harga = hargacandi(pasir, batu, air)
            
            if harga < harga_termurah:
                harga_termurah = harga
                id_termurah = candi[i][0]
                
            if harga > harga_termahal:
                harga_termahal = harga
                id_termahal = candi[i][0]

        print("Total Candi:", total_candi)
        print("Total Pasir yang digunakan:", total_pasir)
        print("Total Batu yang digunakan:", total_batu)
        print("Total Air yang digunakan:", total_air)

        if length_candi == 1:
            print("ID Candi Termahal: -")
            print("ID Candi Termurah: -")
        else:
            print("ID Candi Termahal:", id_termahal, "(Rp " + formatting_harga(harga_termahal) + ")")
            print("ID Candi Termurah:", id_termurah, "(Rp " + formatting_harga(harga_termurah) + ")")
        
    else:
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")    

def totalharga(indeks : int) -> int:

    total_harga = 0

    for i in range (1, array_length(candi) - array_kosong_count(candi)):
        total_harga += int(candi[i][indeks])

    return total_harga

def hargacandi(pasir : int, batu : int, air : int) -> int:
    harga = 1000 * pasir + 15000 * batu + 7500 * air
    return harga

def formatting_harga(nominal : int) -> str:
    angka_str = str(nominal)
    new_str = ''

    for i in range(len(angka_str)):
        digit = angka_str[i]
        if (len(angka_str) - i) % 3 == 0 and i != 0:
            new_str += '.'
        new_str += digit

    return new_str

def hargacandi(pasir, batu, air):
    harga = 1000 * pasir + 15000 * batu + 7500 * air
    return harga