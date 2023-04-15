# Implementasi untuk menghitung jumlah Array
def array_length(arr: list) -> int:
    count = 0
    temp_arr = []
    while(temp_arr != arr):
        count += 1
        # Inisialisasi array pembanding
        temp_arr = [0 for i in range(count)]
        for i in range(count):
            temp_arr[i] = arr[i]
    return count

# # Pengganti Append
# def append(arr, x):
#   arr += [x]

# Pengganti Append
def append(arr, x): 
    arr2 = [0 for i in range(array_length(arr) + 1)]
    for i in range(array_length(arr2)): 
        if i != array_length(arr2) - 1:
            arr2[i] = arr[i]
        else: 
            arr2[i] = x
    return arr2

# Pengganti Split
def split(str, delimit):
  
  word = []
  word2 = ""
  
  i = 0
  while i < len(str):
    if str[i] == delimit:
      append(word, word2)
      word2 = ""
    else:
      word2 += str[i]
      
    i += 1
  append(word, word2)
  return word

print(split("split;split;split", ';'))

# # Split untuk CSV
# def splitcsv(str, delimit):
  
#   word = []
#   word2 = ""
#   row = 0

#   i = 0
#   while i < len(str):
#     if str[i] == delimit :
#       append(word, word2)
#       word2 = ""
#     else:
#       word2 += str[i]
#     i += 1
#   append(word, word2)
#   return word



# Implementasi untuk melakukan sortir data
def sort(arr):
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