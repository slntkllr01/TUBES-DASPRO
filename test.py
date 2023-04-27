# def gambar1():
#     a = print("""
#            ,
#         .--')
#        /    /     
#       |    /       Cepat
#    /`.\   (_.' /   Guys!
#    \          /
#     '--. .---'
#       ( " )
#        '-'
#                 ,
#                  \`-,      ,     =-
#     Ada      .-._/   \_____)  
#  Perintah!  ("              / =-
#              '-;   ,_____.-'       =-
#               /__.'


#        .-.
#       ( " )
#    /\_.' '._/]   Kami
#    |         |   Siap
#     \       /    Membangun
#      \    /`     Candi!
#    (__)  /
#    `.__.' """)    

# print(gambar1())

print(add_to_database([[3], [4], [5], [], [], [], []], [[1]]))  
def add_to_database(list_awal, list_tambahan):
    idx_tambahan = 0
    for i in range(len(list_awal)):
        if not list_awal[i]:
            list_awal[i] = list_tambahan[idx_tambahan]
            idx_tambahan += 1
            if idx_tambahan == len(list_tambahan):
                break
    return list_awal

def summonjin():
    if role == "bandung_bondowoso":
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - bertugas membangun candi")

        jenisjin = int(input("Masukkan nomor jenis jin yang dipanggil: "))

        while jenisjin != 1 and jenisjin != 2:
            
            print("Tidak ada jenis jin bernomor", "'" + str(jenisjin) + "'")
            print()
            jenisjin = int(input("Masukkan nomor jenis jin yang dipanggil: "))
            
        if jenisjin == 1:
            print('Memilih jin "Pengumpul".')
            username = input("Masukan username jin: ")
            password = input("Masukkan password jin: ")

            i = 0    
            while i <= (array_length(user)):
                if username != user[i][0] and user[i][0] != None:
                    i += 1
                    while len(password) < 5 or len(password) > 25 :
                        print("Password panjangnya harus 5-25 karakter!")
                        password = input("Masukkan password jin: ")
                    if 5 <= len(password) <= 25 :
                        user[i] = [username, password, "Pengumpul"]   
                        print("Mengumpulkan sesajen...")
                        print("Menyerahkan sesajen...")
                        print("Membacakan mantra...")
                        print()
                        print("Jin", username, "berhasil dipanggil!")
                        return user[i]
                else:
                    print("Username sudah digunakan.")
                    break
                        
        elif jenisjin == 2:
            print('Memilih jin "Pembangun". ')

            username = input("Masukan username jin: ")
            password = input("Masukkan password jin: ")

            i = 0    
            while i <= (array_length(user)):
                if username != user[i][0] and user[i][0] != None:
                    i += 1
                    while len(password) < 5 or len(password) > 25 :
                        print("Password panjangnya harus 5-25 karakter!")
                        password = input("Masukkan password jin: ")
                    if 5 <= len(password) <= 25 :
                        user[i] = [username, password, "Pembangun"]   
                        print("Mengumpulkan sesajen...")
                        print("Menyerahkan sesajen...")
                        print("Membacakan mantra...")
                        print()
                        print("Jin", username, "berhasil dipanggil!")
                        break       
                else:
                    print("Username sudah digunakan.")
                    break
    else:
        print("Woyy lu ga punya akses!")

 # inisialisasi
  # i = 0

#   while i < fx.array_length(arr) : 
#     if arr[i][0] == username_input :
#       if arr[i][1] == password_input :
#         loginstatus = True; username = username_input; password = password_input
#         role = arr[i][2]
#         print("\nselamat datang", username, "!")
#         print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.\n")
#         return loginstatus, username, password, role
#       else:
#         print("\nPassword salah! mohon input password yang benar!")
#         return login()
#     elif i == (fx.array_length(arr) - 1) :
#       print("\nMohon Maaf, Username tidak terdaftar!")
#       return login()
#     else :
#       i += 1   

# login()