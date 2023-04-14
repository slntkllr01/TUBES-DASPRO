import csvfunction as cfx
import function as fx
from database import *

# Membaca file CSV
arr, nuser = tuple(cfx.readcsv('user.csv', 3))

# Masukkin data Array ke User
for i in range (nuser):
  fx.append2(user, arr[i])
 
def login() :
  
  global username, password, role
  
  # Meminta input username dan password
  print("Mohon input username ")
  cekusername = input("Username: ")
  cekpassword = input("Password: ")

  # inisialisasi
  i = 0
  loginstatus = False
  global nuser, user

  while i < nuser : 
    if user[i][0] == cekusername :
      if user[i][1] == cekpassword :
        loginstatus = True
        username = cekusername
        password = cekpassword
        role = user[i][2]
        print("selamat datang", username, "!")
        print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
        break
      else:
        print("Alemong password salah WKWKWKWK")
        break
    elif i == (nuser - 1) :
      print("Username tidak terdaftar!")
      break
    else :
      i += 1

