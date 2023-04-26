from function import *

def hancurkancandi():
    global candi

    jumlah_baris = array_length(candi)

    YesNo = True #anggapan yakin ingin menghapus candi
    while YesNo == True:
            IDcandi: int(input("Masukan ID candi: "))
            YN : input("Apakah anda yakin ingin menghancurkan candi ID:" + str(IDcandi) + "(Y/N)? ")
            
            if YN == "Y":
                for i in range (1, jumlah_baris): #pengecekan dari indeks ke 1 (bukan header)
                     if candi[i][0] == str(IDcandi): #pencarian baris dari indeks yang ingin dihapus
                         IDhapus = i
                for j in range (5):
                     candi[IDhapus][j] = ""          
                print("Candi telah berhasil dihancurkan.")
                YesNo = False
            else:
                 YesNo = True

    if YesNo == False:
         if IDcandi == IDhapus:
              print("Tidak ada candi dengan ID tersebut.")