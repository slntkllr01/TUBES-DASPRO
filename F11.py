from function import *

def hancurkancandi(role, candi):
    if role != 'roro_jonggrang':
        print("Maaf, Command ini hanya bisa diakses oleh Roro Jonggrang!")
    else:
        Validasi = True #anggapan yakin ingin menghapus candi
        while Validasi:
            IDcandi = int(input("Masukan ID candi: "))
            for i in range(1, (array_length(candi) - array_kosong_count(candi))):
                if candi[i][0] == str(IDcandi):
                    YN = input("Apakah anda yakin ingin menghancurkan candi ID: " + str(IDcandi) + " (Y/N)? ")
                    if YN == 'Y' or YN == 'y':
                        candi[i] = []
                        print("Candi telah berhasil dihancurkan.")
                        geser_array(candi, i)
                        Validasi = False
                        break
                    else:
                        Validasi = False
                        break
            else:
                print("ID tidak terdaftar!")
                break