import time, os

# Implementasi untuk menghitung jumlah Array
def array_length(arr):
    count = 0
    temp_arr = []
    while(temp_arr != arr):
        count += 1
        # Inisialisasi array pembanding
        temp_arr = [0 for i in range(count)]
        for i in range(count):
            temp_arr[i] = arr[i]
    return count  

def arr_append(arr, x):
    temp_arr = ['' for i in range(array_length(arr)+1)]
    for i in range (array_length(arr)):
        temp_arr[i] = arr[i]
    temp_arr[array_length(arr)] = x
    return temp_arr

def str_append(str, x):
    temp_arr = ['' for i in range(len(str)+1)]
    for i in range(len(str)):
        temp_arr[i] = str[i]
    temp_arr[len(str)] = x

    new_str = ''
    for i in range(len(str)+1):
        new_str += temp_arr[i]
    return new_str

def my_split(string , delimit):

    temp_arr = []
    word = ''

    i = 0
    while i < len(string):
        if(string[i] == delimit):
            temp_arr = arr_append(temp_arr, word)
            word = ''
        else:
            word = str_append(word, string[i])
        i += 1
    arr = arr_append(temp_arr, word)
    return arr 

# B01 - Random Number Generator

def randomseed(x):
    now = time.perf_counter()
    ProcessId = os.getpid()
    seed = int(now*ProcessId*x)

    return seed
    
def RandomNumber(min: int ,max: int ,x: int) -> int : 
    seed = randomseed(x)
    a = 1662533
    c = 1283463648
    m = 2**32
    r = (a*seed+c) % m
    hasil = min + int((max-min+1) * (r/(m+1)))

    return hasil

def add_to_database(list_awal : list, list_tambahan : list, indeks: int = 0) -> list:
    if indeks == array_length(list_tambahan):
        return list_awal
    else:
        for i in range(array_length(list_awal)):
            if not list_awal[i]:
                list_awal[i] = list_tambahan[indeks]
                break
        return add_to_database(list_awal, list_tambahan, indeks+1)

# implementasi pop
def delete_elmt(arr, indeks):
    if len(arr) == 0:
        return None
    last_index = len(arr) - 1
    last_element = arr[last_index]
    new_arr = []
    for i in range(len(arr)):
        if i != indeks:
            new_arr = arr_append(new_arr, arr[i])
    arr = new_arr
    return arr

def array_kosong_count(arr: list):
    count = 0
    for i in range (len(arr)):
        if len(arr[i]) == 0:
            count += 1
    return count

def geser_array(arr, index_jin):
    # menghapus elemen yang dihapus dengan menggeser seluruh elemen setelahnya ke kiri
    for i in range(index_jin, array_length(arr)-1):
        arr[i] = arr[i+1]
    arr[array_length(arr)-1] = []
    
    # menggeser elemen yang kosong ke kanan
    for i in range(len(arr)):
        if not arr[i]:
            j = i+1
            while j < len(arr) and not arr[j]:
                j += 1
            if j == len(arr):
                break
            arr[i] = arr[j]
            arr[j] = []  
    return arr

def tabel_maker(arr):
    # Mengecek apakah ada baris kosong di akhir array
    arr_len = len(arr)
    while arr_len > 0 and len(arr[arr_len-1]) == 0:
        arr_len -= 1
    
    if arr_len == 0:
        # Jika array kosong, keluar dari fungsi
        return

    max_lengths = []
    for j in range(len(arr[0])):
        max_len = 0
        for i in range(arr_len):
            if len(arr[i]) == 0:
                continue  # Skip baris kosong
            if len(arr[i][j]) > max_len:
                max_len = len(arr[i][j])
        max_lengths = arr_append(max_lengths, max_len)

    # Menampilkan header tabel
    separator = '+'
    for j in range(len(arr[0])):
        separator += '-' * (max_lengths[j] + 2) + '+'
    print(separator)

    row_format = '| '
    for j in range(len(arr[0])):
        row_format += '{:^{width}} | '.format(arr[0][j], width=max_lengths[j])
    print(row_format)

    # Menampilkan baris data
    print(separator)

    for i in range(1, arr_len):
        if len(arr[i]) == 0:
            continue  # Skip baris kosong

        row_format = '| '
        for j in range(len(arr[i])):
            row_format += '{:^{width}} | '.format(arr[i][j], width=max_lengths[j])
        print(row_format)

    # Menampilkan separator akhir tabel
    print(separator)

