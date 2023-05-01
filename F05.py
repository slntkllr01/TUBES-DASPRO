from function import *

def ubahjin(role, user):
    if role != 'bandung_bondowoso':
        print("Maaf, Command ini hanya bisa diakses oleh Bandung Bondowoso!")
    else:
        print()
        database_tabel = filter_array(user)
        tabel_maker(database_tabel)
        print()
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
                    print()
                    database_tabel = filter_array(user)
                    tabel_maker(database_tabel)
                    print("\nJin telah berhasil diubah.")
                    found = True
                    break
                else:
                    found = True 
                    break
        if not found:
            print("\nTidak ada jin dengan username tersebut.")     

def filter_array(arr):
    # Inisialisasi array hasil dengan header
    result = [['username', 'role']]
    
    # Iterasi elemen di arr mulai dari indeks 1
    for i in range(1, len(arr)):
        # Jika panjang elemen ke-i sama dengan 3
        if len(arr[i]) == 3:
            # Jika role-nya adalah Pengumpul atau Pembangun
            if arr[i][2] == 'Pengumpul' or arr[i][2] == 'Pembangun':
                # Tambahkan username dan role-nya ke dalam array hasil
                result = arr_append(result, [arr[i][0], arr[i][2]])
        else:
            # Jika elemen ke-i bukan berupa list dengan panjang 3, tambahkan list kosong ke dalam array hasil
            result = arr_append(result, [])

    return result



