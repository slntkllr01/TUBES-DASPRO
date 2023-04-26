from function import *

# Baca File CSV
def csv_to_array(file_name):
  with open(file_name, 'r') as file:
    data = file.read()

  # simpan CSV di array
  arr = my_split(data, '\n')

  # menghilangkan ";" pada Array
  i = 0
  while i < array_length(arr):
    arr[i] = my_split(arr[i], ";")
    i += 1
  return arr    

# Tulis File CSV
def array_to_csv(arr):

    csv_string = ""

    row_length = array_length(arr)
    col_length = array_length(arr[0])
    
    i = 0
    while i < row_length:
        j = 0
        while j < col_length:
            csv_string += str(arr[i][j])
            if j != col_length-1:
                csv_string += ";"
            j += 1
        if i != row_length-1:
            csv_string += "\n"
        i += 1

    if row_length == 0:
        return str
  
