from function import *

def hapusjin(role, user, candi):
    if role != "bandung_bondowoso":
        print("Anda tidak memiliki wewenang untuk menghapus jin!")
        return
    else:
        print()
        database_tabel = filter_array(user)
        tabel_maker(database_tabel)
        print()
        jin_username = input("Masukkan username jin : ")
        i = 0
        jin_found = False # menandai apakah jin dengan username tersebut telah ditemukan
        while i < (array_length(user) - array_kosong_count(user)):
            if jin_username == user[i][0]:
                jin_found = True
                if user[i][2] != "Pembangun" and user[i][2] != "Pengumpul":
                    print("Bukan Jin! Tidak bisa dihapus!")
                    return
                choice = input("Apakah anda yakin ingin menghapus jin dengan username " + str(jin_username) + " (Y/N)? ")
                if choice == 'Y' or choice == 'y':
                    # hapus candi jika jin pembangun
                    if user[i][2] == "Pembangun":
                        candi = hapus_candi(jin_username, user, candi)
                    user[i] = []
                    user = geser_array(user, i)
                    print()
                    database_tabel = filter_array(user)
                    tabel_maker(database_tabel)
                    print("\nSelamat! Jin telah berhasil dihapus dari alam gaib.\n")
                else: # Pilih N/n
                    print()
                    break
            else:
                i += 1
        if not jin_found: # jika jin dengan username tersebut tidak ditemukan
            print("Maaf, Tidak ada jin dengan username tersebut.\n")

def hapus_candi(username, user, candi):
    
    # Loop melalui seluruh candi dan hapus semua candi dengan username yang sesuai
    i = 0
    while i < (array_length(candi) - array_kosong_count(candi)):
        if candi[i] and candi[i][1] == username:
            candi[i] = []
            candi = geser_array(candi, i)
        else:
            i += 1
    return candi

def cari_index(parameter, array):
    for i in range(array_length(array)):
        if array[i][0] == parameter:
            return i
    return
    
def filter_array(arr):
    # Inisialisasi array hasil dengan header
    result = [['username', 'role']]
    
    # Iterasi elemen di arr mulai dari indeks 1
    for i in range(1, array_length(arr)):
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