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

# Implementasi untuk melakukan sortir data
def sort(arr: list) -> list :
  for i in range(array_length(arr)):
    swapped = False
    for j in range(0, array_length(arr)-i-1):
      if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
        swapped = True
    if not swapped:
      break
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
