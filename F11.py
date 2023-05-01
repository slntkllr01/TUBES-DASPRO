from function import *

def hancurkancandi(role, candi):
    if role != 'roro_jonggrang':
        print("\nMaaf, Command ini hanya bisa diakses oleh Roro Jonggrang!\n")
    else:
        Validasi = True #anggapan yakin ingin menghapus candi
        while Validasi:
            IDcandi = int(input("\nMasukan ID candi: "))
            for i in range(1, (array_length(candi) - array_kosong_count(candi))):
                if candi[i][0] == str(IDcandi):
                    YN = input("\nApakah anda yakin ingin menghancurkan candi ID: " + str(IDcandi) + " (Y/N)? ")
                    if YN == 'Y' or YN == 'y':
                        candi[i] = []
                        print("\nCandi telah berhasil dihancurkan.\n")
                        geser_array(candi, i)
                        Validasi = False
                        break
                    else:
                        Validasi = False
                        print()
                        break
            else:
                print("\nID tidak terdaftar!\n")
                break