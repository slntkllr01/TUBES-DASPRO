from function import *

user = [['username','password','role'], ['Bondowoso','cintaroro','bandung_bondowoso'],['Roro','gasukabondo','roro_jonggrang']]

def summonjin():
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
                    break       
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

    