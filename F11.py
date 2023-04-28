# # from function import *
candi = [['id', 'pembuat','pasir','batu','air'],['','','','',''],['2','jinf','3','4','2'],['3','jinfarrasd','3','4','2']]

def array_length(candi):
    count = 0
    temp_arr = []
    while(temp_arr != candi):
        count += 1
        # Inisialisasi array pembanding
        temp_arr = [0 for i in range(count)]
        for i in range(count):
            temp_arr[i] = candi[i]
    return count  

def hancurkancandi():
    global candi
    print (candi)

    jumlah_baris = array_length(candi)
    print(jumlah_baris)

    YesNo = True #anggapan yakin ingin menghapus candi
    while YesNo == True:
            IDcandi= int(input("Masukan ID candi: "))
            YN = input("Apakah anda yakin ingin menghancurkan candi ID:" + str(IDcandi) + "(Y/N)? ")
            
            if YN == "Y":
                for i in range (1, jumlah_baris): #pengecekan dari indeks ke 1 (bukan header)
                     if candi[i][0] == str(IDcandi) and IDcandi !="": #pencarian baris dari indeks yang ingin dihapus
                         IDhapus = i
                         for j in range (5):
                            candi[IDhapus][j] = ""          
                         print("Candi telah berhasil dihancurkan.")
                         YesNo = False
                     elif candi[i][0] == "":
                          print("Tidak ada candi dengan ID tersebut.")
                          
            # else:
            #      YesNo = True

    # if YesNo == False:
    #      if IDcandi == IDhapus:
    #           print("Tidak ada candi dengan ID tersebut.")

print(hancurkancandi())