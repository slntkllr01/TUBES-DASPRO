def ubahjin():
    username = input('Masukkan username jin : ')
    for i in range(array_length(user)):
        if username == user[i][0]:
            if role == 'Pengumpul':
                konfirmasi = print(f"Jin ini bertipe {user[i][2]}. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
            else: # Role : Pengumpul
                konfirmasi = print(f"Jin ini bertipe {user[i][2]}. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")

            if konfirmasi == 'y' or konfirmasi == 'Y':
                print("\nJin telah berhasil diubah.")
                break
            else:
                break #ini gw masi bingung antara dia minta input lagi atau lgsg keluar
        else:
            print("\nTidak ada jin dengan username tersebut.")
            break



