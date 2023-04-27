from function import *
from database import *
from csvfunction import *
import os

clear_terminal =lambda:os.system('cls')

user_csv = csv_to_array('user.csv')
user_array = add_to_database(user, user_csv)
print(user_array)

def validasi_username(variable):
    valid = True
    for i in range (len(user_array) - array_kosong_count(user_array)):
        if variable == user_array[i][0]:
            valid  = False
            break
        else:
            valid = True
    return valid

def validasi_jin(role):
    while True:
        username_jin = input("Masukkan username jin: ")
        if not validasi_username(username_jin):
            print("\nMohon Maaf, Username", username_jin, "sudah diambil\nSilakan pilih username lain!\n")
            continue
        while True:
            password_jin = input("Masukkan password jin: ")
            if len(password_jin) < 5 or len(password_jin) > 25:
                print("\nMaaf, password harus memiliki panjang 5-25 karakter!\n")
                continue
            else:
                add_to_database(user_array, [[username_jin, password_jin, role]])
                print("Mengumpulkan sesajen...")
                print("Menyerahkan sesajen...")
                print("Membacakan mantra...")
                print("\nJin", username_jin, "berhasil dipanggil!")
                return


role = 'Bandung_bondowoso'

def summonjin():
    if role == 'Bandung_bondowoso':
        if array_length(candi) - array_kosong_count(user_array) >= 100:
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu.")
            return
        
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - bertugas membangun candi")

        while True:
            jenis_jin = int(input("Masukkan nomor jenis jin yang dipanggil: "))

            if jenis_jin == 1:
                print("\nMemilih jin “Pengumpul”.\n")
                validasi_jin("Pengumpul")
                break
            elif jenis_jin == 2:
                print("\nMemilih jin “Pembangun”.\n")
                validasi_jin("Pembangun")
                break
            else:
                print("Sorry banget, tapi lu siapa?")
    else:
        print("Lu ga punya akses!")



    

