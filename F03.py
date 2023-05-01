from function import *
from csvfunction import *

def summonjin(role, user, candi):
    if role == 'bandung_bondowoso':
        if array_length(candi) - array_kosong_count(user) >= 100:
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu.")
            return
        
        print("\nJenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - bertugas membangun candi")

        while True:
            jenis_jin = int(input("\nMasukkan nomor jenis jin yang dipanggil: "))

            if jenis_jin == 1:
                print("\nMemilih jin “Pengumpul”.\n")
                validasi_jin("Pengumpul", user)
                break
            elif jenis_jin == 2:
                print("\nMemilih jin “Pembangun”.\n")
                validasi_jin("Pembangun", user)
                break
            else:
                print("\nTidak ada jenis jin bernomor " + str(jenis_jin) + "!")
    else:
        print("\nMaaf, Command ini hanya bisa diakses oleh Bandung Bondowoso!\n")

def validasi_username(variable, user):
    valid = True
    for i in range (array_length(user) - array_kosong_count(user)):
        if variable == user[i][0]:
            valid  = False
            break
        else:
            valid = True
    return valid

def validasi_jin(role, user):
    while True:
        username_jin = input("Masukkan username jin: ")
        if not validasi_username(username_jin, user):
            print("\nMohon Maaf, Username", username_jin, "sudah diambil\nSilakan pilih username lain!\n")
            continue
        while True:
            password_jin = input("Masukkan password jin: ")
            if len(password_jin) < 5 or len(password_jin) > 25:
                print("\nMaaf, password harus memiliki panjang 5-25 karakter!\n")
                continue
            else:
                user = add_to_database(user, [[username_jin, password_jin, role]])
                print("\nMengumpulkan sesajen...")
                print("Menyerahkan sesajen...")
                print("Membacakan mantra...")
                print("\nJin", username_jin, "berhasil dipanggil!\n")
                return



    

