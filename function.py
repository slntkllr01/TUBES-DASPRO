# Pengganti fungsi len(X) array (sementara krn ga bole pake for i in arr)
def length(arr):
  length = 0
  for i in arr:
    length += 1
  return length


# Pengganti Append
def append(arr, x):
  arr += [x]

# Pengganti Append versi 2
def append2(arr, x):
  i = 0
  while True :
    if arr[i] == []:
      arr[i] = x
      break
    i += 1
    

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
