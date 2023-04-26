import csvfunction as cfx
import function as fx
import database
import time

# Membaca file CSV
arr = cfx.csv_to_array('user.csv')

def login() :

  # Meminta input username dan password
  username_input = input("Masukkan Username: ")
  password_input = input("Masukkan Password: ")

  # inisialisasi
  i = 0

  while i < fx.array_length(arr) : 
    if arr[i][0] == username_input :
      if arr[i][1] == password_input :
        loginstatus = True; username = username_input; password = password_input
        role = arr[i][2]
        print("\nselamat datang", username, "!")
        print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.\n")
        return loginstatus, username, password, role
      else:
        print("\nPassword salah! mohon input password yang benar!")
        return login()
    elif i == (fx.array_length(arr) - 1) :
      print("\nMohon Maaf, Username tidak terdaftar!")
      return login()
    else :
      i += 1   