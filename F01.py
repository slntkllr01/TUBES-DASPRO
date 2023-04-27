from csvfunction import *
from function import *
from database import *
import time

# Membaca file CSV
arr = csv_to_array('user.csv')

def login() :

  # Program Login ini memiliki jumlah attempt maksimal sebanyak 3 kali
  max_attempts = 3
  remaining_attempts = max_attempts

  # Meminta input username dan password
  while remaining_attempts > 0:
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    for i in range(array_length(arr)):
      if arr[i][0] == username:
        if arr[i][1] == password:
          role = arr[i][2]
          loginstatus = True
          print("\nSelamat datang,", username, "!")
          print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.\n")
          return loginstatus, username, password, role
        else:
            remaining_attempts -= 1
            if remaining_attempts > 0:
                print("\nPassword salah! Mohon input password yang benar!")
                print("\nSisa attempt Anda sebanyak", remaining_attempts, "kali.\nPastikan Username dan Password yang Anda input Benar!\n")
            break
    else:
      remaining_attempts -= 1
      if remaining_attempts > 0:
        print("\nMohon maaf, Username tidak terdaftar!")
        print("\nSisa attempt Anda sebanyak", remaining_attempts, "kali.\nPastikan Username dan Password yang Anda input Benar!\n")
  print("\nMohon Maaf, Anda telah salah memasukkan username atau password sebanyak 3x.")
  print("Silakan coba lagi dalam 30 detik.")
  time.sleep(30)
  remaining_attempts = max_attempts

  return False, None, None, None

login()


