def summonjin():
    print("Jenis jin yang dapat dipanggil:")
    print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print(" (2) Pembangun - bertugas membangun candi")

    jenisjin = int(input("Masukkan nomor jenis jin yang dipanggil: "))

    if jenisjin == 1:
        print('Memilih jin "Pengumpul".')

        username = input("Masukan username jin: ")
        password = input("Masukkan password jin: ")

        validasi = False

        for i in range (row):
            if username != user[i][0]:
                if 5 <= len(password) <= 25 :
                    if user[i] != None:
                        i += 1
                    else:
                        user[i] = [username, password, "pengumpul"]   
                        print("Mengumpulkan sesajen...")
                        print("Menyerahkan sesajen...")
                        print("Membacakan mantra...")
                        print()
                        print("Jin", username, "berhasil dipanggil!")
                else:
                    print("Password panjangnya harus 5-25 karakter!")
            else:
                print("Username sudah digunakan.")    
    elif jenisjin == 2:
        print('Memilih jin "Pembangun". ')

        username = input("Masukan username jin: ")
        password = input("Masukkan password jin: ")

        validasi = False

        for i in range (row):
            if username != user[i][0]:
                if 5 <= len(password) <= 25 :
                    if user[i] != None:
                        i += 1
                    else:
                        user[i] = [username, password, "pembangun"]   
                        print("Mengumpulkan sesajen...")
                        print("Menyerahkan sesajen...")
                        print("Membacakan mantra...")
                        print()
                        print("Jin", username, "berhasil dipanggil!")
                else:
                    print("Password panjangnya harus 5-25 karakter!")
            else:
                print("Username sudah digunakan.")
    else:
        print("Tidak ada jenis jin bernomor", "'" + str(jenisjin) + "'")
        

    