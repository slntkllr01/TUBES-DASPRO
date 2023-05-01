from csvfunction import *
from function import *
from database import *
import time

def login(arr) :

  # Program Login ini memiliki jumlah attempt maksimal sebanyak 3 kali
  max_attempts = 3
  remaining_attempts = max_attempts

  # Meminta input username dan password
  while remaining_attempts > 0:
    user_username = input("Masukkan Username: ")
    user_password = input("Masukkan Password: ")

    for i in range(array_length(arr) - array_kosong_count(arr)):
      if arr[i][0] == user_username:
        if arr[i][1] == user_password:
          print("\nSelamat datang,", user_username, "!")
          print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.\n")
          role = arr[i][2]
          loginstatus = True
          username = user_username
          password = user_password
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

  return False, '', '', ''