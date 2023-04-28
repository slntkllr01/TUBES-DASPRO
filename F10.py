from F01 import *
from database import *
from csvfunction import *
from function import *

def harga_candi(candi, idx_candi) : 
    return  1000*candi[idx_candi][2] + 15000*candi[idx_candi][3]  + 7500*candi[idx_candi][4] 

def laporancandi() :
    harga_termurah = 9999999999 
    harga_termahal = 0
    id_termurah = id_termahal = 0 

    if login() == True :
        jumlah_pasir = 0
        jumlah_batu = 0 
        jumlah_air = 0
        total_candi = (array_length(candi) - array_kosong_count(candi)) - 1

        if total_candi != 0 : 
            for i in range(1, array_length(candi) + 1) : 
                jumlah_pasir += candi[i][2]
                jumlah_batu += candi[i][3] 
                jumlah_air += candi[i][4]

                harga_candi = harga_candi(candi,i)
                if harga_candi > harga_termahal : 
                    harga_termahal = harga_candi
                    id_termahal = i


                if harga_candi < harga_termurah : 
                    harga_termurah = harga_candi
                    id_termurah = i
        
        else :
            id_termurah = id_termahal = "-"

        print(f"> Total Candi: {total_candi}")
        print(f"> Total Pasir yang digunakan: {jumlah_pasir}")
        print(f"> Total Batu yang digunakan: {jumlah_batu}")
        print(f"> Total Air yang digunakan: {jumlah_air}")
        print("> ID Candi Termahal:" + str(id_termahal) + "Rp{:,.2f}".format(id_termahal))
        print("> ID Candi Termurah:" + str(id_termurah) + "Rp{:,.2f}".format(id_termurah))