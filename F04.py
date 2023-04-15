from csvfunction import *
from function import *
from database import *

# Membaca CSV Candi dan User
user_arr = readcsv("user.csv", 3)
candi_arr = readcsv("candi.csv", 5)

print(append(user,user_arr))
print(append(candi,candi_arr))

print(user)
print(candi)
# print(candi_arr)
# role = 'bandung_bondowoso'

# def hapusjin():
#     global role
#     if role != "bandung_bondowoso":
#         print("Anda tidak memiliki wewenang untuk menghapus jin!")
#         return 0
#     else:
#         jin_username = input("Masukkan username jin : ")
#         i = 0
#         while i <= (array_length(user_arr)):
#             if jin_username == user_arr[i][0]:
#                 choice = print("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
#                 if choice == 'Y' or choice == 'y':
#                     print()
#                     print("Selamat! Jin telah berhasil dihapus dari alam gaib.")
#                     candi_arr = hapuscandi(i)
#                     break
#                 else: # Pilih N/n
#                     break
#             elif i == (array_length(user_arr)-1):
#                 print("Maaf, Tidak ada jin dengan username tersebut.")
#             else:
#                 i += 1

# def hapuscandi(candi_indeks):
#     for i in range(array_length(candi_arr)):
#         if i == candi_indeks:
#             candi_arr[i] = ['','','','','']
#         else:
#             i += 1               

                        