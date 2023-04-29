from csvfunction import *
from function import *
from database import *

user_csv = csv_to_array('user.csv')
user_array = add_to_database(user, user_csv)

candi_csv = csv_to_array('candi.csv')
candi_array = add_to_database(candi, candi_csv)

stack = []

role = "bandung_bondowoso"

def hapusjin():
    global role, user_array, candi_array, stack
    if role != "bandung_bondowoso":
        print("Anda tidak memiliki wewenang untuk menghapus jin!")
        return
    else:
        jin_username = input("Masukkan username jin : ")
        i = 0
        jin_found = False # menandai apakah jin dengan username tersebut telah ditemukan
        while i < (array_length(user_array) - array_kosong_count(user_array)):
            if jin_username == user_array[i][0]:
                jin_found = True
                if user_array[i][2] != "Pembangun" and user_array[i][2] != "Pengumpul":
                    print("Bukan Jin! Tidak bisa dihapus!")
                    return
                choice = input("Apakah anda yakin ingin menghapus jin dengan username " + str(jin_username) + " (Y/N)? ")
                if choice == 'Y' or choice == 'y':
                    # hapus candi jika jin pembangun
                    if user_array[i][2] == "Pembangun":
                        hapus_candi(jin_username)
                    # Simpan array yang dihapus ke dalam stack sebelum dihapus
                    stack = arr_append(stack, ("hapus", (user_array[i], candi_array[i])))
                    print("\nSelamat! Jin telah berhasil dihapus dari alam gaib.")
                    # Simpan array yang digeser ke dalam stack sebelum digeser
                    user_array[i] = []
                    stack = arr_append(stack, ("geser", (user_array, candi_array)))
                    user_array = geser_array(user_array, i)
                    break
                else: # Pilih N/n
                    break
            else:
                i += 1
        if not jin_found: # jika jin dengan username tersebut tidak ditemukan
            print("Maaf, Tidak ada jin dengan username tersebut.")

def hapus_candi(username):
    global user_array, candi_array, stack
    
    # Loop melalui seluruh candi_array dan hapus semua candi dengan username yang sesuai
    i = 0
    while i < (array_length(candi_array) - array_kosong_count(candi_array)):
        if candi_array[i] and candi_array[i][1] == username:
            # Simpan array yang dihapus ke dalam stack sebelum dihapus
            stack = arr_append(stack, ("hapus_candi", (candi_array[i])))
            candi_array[i] = []
            candi_array = geser_array(candi_array, i)
        else:
            i += 1
    return candi_array, stack
            
    return arr

def undo():
    global user_array, candi_array, stack

    # ambil perubahan terakhir dari stack
    if not stack:
        print("Tidak ada perubahan yang dapat di-undo.")
        return
    else:
        stack_last_idx = (array_length(stack)-1)
        perubahan_terakhir = delete_elmt(stack, stack_last_idx)

    # undo perubahan
    if perubahan_terakhir[0] == 'hapus_jin':
        # hapus jin dari user_array
        jin = perubahan_terakhir[1][0]
        index_jin = cari_index(jin[0], user_array)
        user_array[index_jin] = jin
        # hapus candi yang berkaitan
        candi_array = perubahan_terakhir[1][1]
        hapus_candi(jin[0])
        # pergeseran array
        user_array = geser_array(user_array, index_jin)
        print("Perubahan pada penghapusan jin telah di-undo.")
    elif perubahan_terakhir[0] == 'hapus_candi':
        # hapus candi dari candi_array
        candi = perubahan_terakhir[1][0]
        index_candi = cari_index(candi[0], candi_array)
        candi_array[index_candi] = candi
        # pergeseran array
        candi_array = geser_array(candi_array, index_candi)
        print("Perubahan pada penghapusan candi telah di-undo.")

def cari_index(parameter, array):
    for i in range(array_length(array)):
        if array[i][0] == parameter:
            return i
        

print(cari_index())