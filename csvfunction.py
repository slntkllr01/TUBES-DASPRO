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
    if not arr:
        return ""

    csv_string = ""
    row_length = len(arr)
    col_length = len(arr[0])

    for i in range(row_length):
        row_data = ""
        for j in range(col_length):
            if j < len(arr[i]):
                row_data += str(arr[i][j])
                if j < len(arr[i])-1:
                    row_data += ";"
            if j == col_length-1 and i < row_length-1 and len(arr[i+1]) > 0:
                row_data += "\n"
        csv_string += row_data

    return csv_string