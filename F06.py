from csvfunction import *
from function import *
from database import *

bb_csv = csv_to_array('bahan_bangunan.csv')
bb_array = add_to_database(bahan_bangunan, bb_csv)

print(bb_array)

def bangun():
    global role
    if role != 'Pembangun':
        print("Ga punya akses!")
        return
    
    pasir_needed = RandomNumber(1,5,3456789)
    batu_needed = RandomNumber(1, 5, 123456)
    air_needed = RandomNumber(1,5,765432)

    total_pasir = int(bahan_bangunan[1][2])
    total_batu = int(bahan_bangunan[2][2])
    total_air = int(bahan_bangunan[3][2])

    total_candi = 100
    candi_count = 0

    if total_pasir >= pasir_needed and total_batu >= batu_needed and total_air >= air_needed:
        total_pasir -= pasir_needed
        total_batu -= batu_needed
        total_air -= air_needed 
        candi_count += 1  
    else:
        print("Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun!") 
    

           
