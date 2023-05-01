from function import *
from Bonus import *

def bangun(role, username, user, bb, candi):
    if role != 'Pembangun':
        print("\nMaaf, Command ini hanya bisa diakses oleh Jin Pembangun!\n")
        return
    
    pasir_needed = lcg(1,5,3456789)
    batu_needed = lcg(1, 5, 123456)
    air_needed = lcg(1,5,765432)

    total_pasir = int(bb[1][2])
    total_batu = int(bb[2][2])
    total_air = int(bb[3][2])

    total_candi = 100
    candi_count = array_length(candi) - array_kosong_count(candi) - 1

    if candi_count < 100:
        if total_pasir >= pasir_needed and total_batu >= batu_needed and total_air >= air_needed:
            total_pasir -= pasir_needed; total_batu -= batu_needed; total_air -= air_needed 
            candi_idx = candi_count + 1
            candi = add_to_database(candi, [[candi_idx, username, pasir_needed, batu_needed, air_needed]])
            candi_count += 1 
            print("\nCandi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun:", total_candi - candi_count, "\n") 
        else:
            print("\nBahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun!\n") 

    else:
        if total_pasir >= pasir_needed and total_batu >= batu_needed and total_air >= air_needed:
            total_pasir -= pasir_needed
            total_batu -= batu_needed
            total_air -= air_needed
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun: 0\n")
        else:
            print("\nBahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun!\n")
            return

           
