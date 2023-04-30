from csvfunction import *
from function import *
from database import *

def ayamberkokok():
    global role
    if role == "roro_jonggrang":
        print("\nKukuruyuk.. Kukuruyuk..\n")

        # Menghitung Jumlah Candi (dikurangi Header dan Database Kosong)
        jumlah_candi = (array_length(candi) - array_kosong_count(candi) - 1) 

        print("jumlah Candi: " + str(jumlah_candi)) 

        if jumlah_candi < 100:
            print("\nSelamat, Roro Jonggrang memenangkan permainan!")
            print("Roro jonggrang dikutuk menjadi candi.")
        else:
            print("Yah, Bandung Bondowoso memenangkan permainan")
    else:
        print("Maaf, Command ini hanya bisa diakses oleh Roro Jonggrang!")