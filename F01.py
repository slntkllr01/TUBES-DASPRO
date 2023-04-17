import csvfunction as cfx
import function as fx
from database import *
import time

# Membaca file CSV
arr = cfx.readcsv('user.csv', 3)
 
print(arr) 

def login() :
  
  global username, password, role

  # Meminta input username dan password
  print("Masukkan Username!")
  username_checker = input()
  print("Masukkan Password!")
  password_checker = input()

  # inisialisasi
  i = 0
  loginstatus = False

  while i < fx.array_length(arr) : 
    if arr[i][0] == username_checker :
      if arr[i][1] == password_checker :
        loginstatus = True
        username = username_checker
        password = password_checker
        role = arr[i][2]
        print("selamat datang", username, "!")
        print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
        break
      else:
        print("Alemong password salah WKWKWKWK")
        break
    elif i == (fx.array_length(arr) - 1) :
      print("Username tidak terdaftar!")
      break
    else :
      i += 1   


