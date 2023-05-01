from function import *

# Baca File CSV
def csv_to_array(file):
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
def array_to_csv(arr, filename):
    if not arr:
        return ""

    csv_string = ""
    row_length = array_length(arr)
    col_length = array_length(arr[0])

    for i in range(row_length):
      row_data = ""
      for j in range(col_length):
          if j < array_length(arr):
              row_data += str(arr[i][j])
              if j < array_length(arr[i])-1:
                  row_data += ";"
          if j == col_length-1 and i < row_length-1 and array_length(arr[i+1]) > 0:
              row_data += "\n"
      csv_string += row_data

    with open(filename, 'w') as file:
      file.write(csv_string)