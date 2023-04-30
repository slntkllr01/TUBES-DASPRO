from csvfunction import *
from function import *
from database import *

def role_count(arr : list, role : str) -> int :
    count = 0
    for i in range(len(arr) - array_kosong_count(arr)):
        if arr[i][2] == role:
            count += 1
    return count

def laporanjin():
    global role
    if role == 'bandung_bondowoso':

        # mencari Total Jin
        jin_kumpul = role_count(user, "Pengumpul")
        jin_bangun = role_count(user, "Pembangun")
        total_jin = jin_kumpul + jin_bangun
        
        # mencari Jin Terajin dan Termalas
        database_pembangun = database_pembangun_candi(candi)
        terajin = max_occurence(database_pembangun)
        termalas = min_occurence(database_pembangun)

        # Mencari Jumlah Pasir, Air, dan Batu
        jumlah_pasir = bb[1][2]
        jumlah_air = bb[2][2]
        jumlah_batu = bb[3][2]

    else:
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")

    print()
    print("Total Jin :", total_jin)
    print("Total Jin Pengumpul :", jin_kumpul)
    print("Total Jin Pembangun :", jin_bangun)
    print("Jin Terajin :", terajin)
    print("Jin Termalas :",termalas)
    print("Jumlah Pasir :", jumlah_pasir, "unit")
    print("Jumlah Air :", jumlah_air, "unit") 
    print("Jumlah Batu :", jumlah_batu, "unit")   

def database_pembangun_candi(arr):
    result = []  # list kosong untuk menampung hasil
    for i in range(array_length(arr)):
        if array_length(arr[i]) >= 1:  # Tujuannya agar tidak indexerror karena terdapat array kosong
            result = arr_append(result, arr[i][1])  # menambahkan nilai index[i][0] ke dalam 
        
    result = delete_elmt(result, 0)

    return result

def max_occurence(arr):

    if array_length(arr) == 0:
        return "-"
    
    max_count = 0
    max_item = None
    i = 0
    while i < array_length(arr):
        item_count = 0
        j = 0
        while j < array_length(arr):
            if arr[i] == arr[j]:
                item_count += 1
            j += 1
        if item_count > max_count:
            max_count = item_count
            max_item = arr[i]
        i += 1
    return max_item

def min_occurence(arr):

    if array_length(arr) == 0:
        return "-"
    
    min_count = float('inf')
    min_item = None
    i = 0
    while i < array_length(arr):
        item_count = 0
        j = 0
        while j < array_length(arr):
            if arr[i] == arr[j]:
                item_count += 1
            j += 1
        if item_count < min_count or (item_count == min_count and arr[i] < min_item):
            min_count = item_count
            min_item = arr[i]
        i += 1
    return min_item
