import function as fx

# Baca File CSV
def readcsv(filename, col):
  with open(filename, 'r') as file:
    data = file.read()

  # simpan CSV di array
  arr, row = fx.splitcsv(data, "\n")

  # menghilangkan ";" pada Array
  i = 0
  while i < col:
    arr[i] = fx.split(arr[i], ";")
    i += 1
  return (arr, row)