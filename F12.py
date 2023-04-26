from function import *
from csvfunction import *

def ayamberkokok():
    global candi
    print("\nKukuruyuk.. Kukuruyuk..\n")

    jumlah_candi = array_length(candi)-1 #jumlah candi dikurangi header

    print("jumlah Candi:" + str(jumlah_candi)) # blm tau nama variabel nya apa

    if jumlah_candi < 100:
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("Roro jonggrang dikutuk menjadi candi.")
    else:
        print("Yah, Bandung Bondowoso memenangkan permainan")

    exit()