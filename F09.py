from F01 import *
from database import *
from csvfunction import *
from function import *

print(">>>laporan jin")
def laporanjin() :
    if login() == True :
        #Menghitung jin kumpul, jin bangun, dan total jin
        for i in range(1,array_length(user)) :
            jin_kumpul = 0
            jin_bangun = 0

            if user[i][2] == "Pengumpul" :
                jin_kumpul += 1
            elif user[i][2] == "Pembangun":
                jin_bangun += 1
        total_jin = jin_bangun + jin_kumpul


        #Mendapatkan Jin Terajin dan Jin Termalas
        if (array_length(candi) - array_kosong_count(candi)) - 1 > 0 :
            max_candi = -1 
            min_candi = 9999
            for i in range(1,array_length(user)) : 
                for j in range(1,array_length(candi)) : 
                    count = 0
                    if candi[j][1] == user[i][0] : 
                        count += 1
                    
                    # Mendapatkan jin terajin
                    if count > max_candi :
                        max_candi = count 
                        terajin = user[i][0]
                    elif count  == max_candi : 
                            if user[i][0] < terajin : 
                                terajin = user[i][0]
                                max_candi = count 
                    
                    # Mendapatkan jin termalas
                    if count < min_candi :
                        min_candi = count 
                        termalas = user[i][0]
                    elif count  == min_candi : 
                            if user[i][0] > termalas and user[i][2] == "Pembangun" : 
                                termalas = user[i][0]
                                min_candi = count 

            else : 
                terajin = termalas = "-"
                 

        #Mendapatkan jumlah pasir, jumlah air, jumlah batu yang tersedia
        jumlah_batu = bahan_bangunan[1][2]
        jumlah_pasir = bahan_bangunan[2][2]
        jumlah_air = bahan_bangunan[3][2]

        print(">>>laporan jin")
        print(f"Total Jin : {total_jin} ")
        print(f"Total Jin Pengumpul : {jin_kumpul} ")
        print(f"Total Jin Pembangun : {jin_bangun} ")
        print(f"Jin terajin : {terajin}")
        print(f"Jin termalas : {termalas}")
        print(f"Jumlah Batu :{jumlah_batu}")
        print(f"Jumlah Pasir :{jumlah_pasir}")
        print(f"Jumlah air :{jumlah_air} ")
        
    else :
        print("Laporan ini hanya bisa diakses oleh akun Bondowoso")

