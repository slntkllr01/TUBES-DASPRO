from csvfunction import *
from function import *
from database import *

user_csv = csv_to_array('user.csv')
user = add_to_database(user, user_csv)

bb_csv = csv_to_array('bahan_bangunan.csv')
bb = add_to_database(bahan_bangunan, bb_csv)

candi_csv = csv_to_array('candi.csv')
candi = add_to_database(candi, candi_csv)

role = 'Pembangun'

username = 'jin1'

def bangun():
    global role, username, user, bb, candi
    if role != 'Pembangun':
        print("Maaf, Command ini hanya bisa diakses oleh Jin Pembangun!")
        return
    
    pasir_needed = RandomNumber(1,5,3456789)
    batu_needed = RandomNumber(1, 5, 123456)
    air_needed = RandomNumber(1,5,765432)

    total_pasir = int(bb[1][2])
    total_batu = int(bb[2][2])
    total_air = int(bb[3][2])

    total_candi = 100
    candi_count = len(candi) - array_kosong_count(candi) - 1

    if candi_count < 100:
        if total_pasir >= pasir_needed and total_batu >= batu_needed and total_air >= air_needed:
            total_pasir -= pasir_needed; total_batu -= batu_needed; total_air -= air_needed 
            candi_idx = candi_count + 1
            candi = add_to_database(candi, [[candi_idx, username, pasir_needed, batu_needed, air_needed]])
            candi_count += 1 
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun:", total_candi - candi_count, "\n") 
        else:
            print("Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun!") 

    else:
        if total_pasir >= pasir_needed and total_batu >= batu_needed and total_air >= air_needed:
            total_pasir -= pasir_needed
            total_batu -= batu_needed
            total_air -= air_needed
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun: 0\n")
        else:
            print("Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun!")
            return

bangun()  

           
