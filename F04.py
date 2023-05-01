from function import *

def hapusjin(role, user, candi, stack):
    if not stack:
        stack = []
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
                        candi, stack = hapus_candi(jin_username, user, candi, stack)
                    # Simpan array yang dihapus ke dalam stack sebelum dihapus
                    stack = arr_append(stack, ("hapus", (user[i], candi[i])))
                    # Simpan array yang digeser ke dalam stack sebelum digeser
                    user[i] = []
                    stack = arr_append(stack, ("geser", (user, candi)))
                    user = geser_array(user, i)
                    print()
                    database_tabel = filter_array(user)
                    tabel_maker(database_tabel)
                    print("\nSelamat! Jin telah berhasil dihapus dari alam gaib.")
                    return stack
                else: # Pilih N/n
                    break
            else:
                i += 1
        if not jin_found: # jika jin dengan username tersebut tidak ditemukan
            print("Maaf, Tidak ada jin dengan username tersebut.")

def hapus_candi(username, user, candi, stack):
    
    # Loop melalui seluruh candi dan hapus semua candi dengan username yang sesuai
    i = 0
    while i < (array_length(candi) - array_kosong_count(candi)):
        if candi[i] and candi[i][1] == username:
            # Simpan array yang dihapus ke dalam stack sebelum dihapus
            stack = arr_append(stack, ("hapus_candi", (candi[i])))
            candi[i] = []
            candi = geser_array(candi, i)
        else:
            i += 1
    return candi, stack

# B04 - Undo

def undo(user, candi, stack):
    # ambil perubahan terakhir dari stack
    if not stack:
        print("Tidak ada perubahan yang dapat di-undo.")
        return
    else:
        stack_last_idx = len(stack)-1
        perubahan_terakhir = stack[stack_last_idx]
        stack = stack[:stack_last_idx]

    # undo perubahan
    if perubahan_terakhir[0] == 'hapus_jin':
        # hapus jin dari user
        jin = perubahan_terakhir[1][0]
        index_jin = 0
        while index_jin < len(user):
            if user[index_jin][0] == jin[0]:
                user[index_jin] = jin
                break
            index_jin += 1

        # hapus candi yang berkaitan
        candi_jin = perubahan_terakhir[1][1]
        index_candi = 0
        while index_candi < len(candi):
            if candi[index_candi][0] == candi_jin[0]:
                candi[index_candi] = candi_jin
                break
            index_candi += 1

        print("Perubahan pada penghapusan jin telah di-undo.")
    elif perubahan_terakhir[0] == 'hapus_candi':
        # hapus candi dari candi
        candi_item = perubahan_terakhir[1][0]
        index_candi = 0
        while index_candi < len(candi):
            if candi[index_candi][0] == candi_item[0]:
                candi[index_candi] = candi_item
                break
            index_candi += 1

        print("Perubahan pada penghapusan candi telah di-undo.")

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