from csvfunction import *
from function import *
from database import *

user_csv = csv_to_array('user.csv')
user = add_to_database(user, user_csv)

role = 'bandung_bondowoso'

def ubahjin():
    global role
    if role != 'bandung_bondowoso':
        print("Maaf, Command ini hanya bisa diakses oleh Bandung Bondowoso!")
    else:    
        username_jin = input('Masukkan username jin : ')
        found = False
        for i in range(array_length(user) - array_kosong_count(user)):
            if username_jin == user[i][0]:
                if user[i][2] == 'Pengumpul':
                    konfirmasi = input(f"Jin ini bertipe {user[i][2]}. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
                else: # Role : Pembangun
                    konfirmasi = input(f"Jin ini bertipe {user[i][2]}. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")

                if konfirmasi == 'y' or konfirmasi == 'Y':
                    user[i][2] = 'Pembangun' if user[i][2] == 'Pengumpul' else 'Pengumpul'
                    print(user)
                    print("\nJin telah berhasil diubah.")
                    found = True
                    break
                else:
                    found = True # user found, but not updated
                    break
        if not found:
            print("\nTidak ada jin dengan username tersebut.")       





