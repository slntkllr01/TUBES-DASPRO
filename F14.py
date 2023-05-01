import os
from csvfunction import *
from function import *

def save(user, bb, candi):
    def save_data(file, data):
        data = array_to_csv(data)
        with open(file, "w") as f:
            f.write(data)

    directory = input("\nMasukkan nama folder penyimpanan: ")
    
    if not os.path.exists('./save'):
        os.mkdir('./save')
    
    os.chdir('./save')

    if not os.path.exists(directory): 
        os.mkdir(directory)

        print("Saving...")
        save_data(os.path.join(directory, "user.csv"), user)
        save_data(os.path.join(directory, "bahan_bangunan.csv"), bb)
        save_data(os.path.join(directory, "candi.csv"), candi)

        print()
        print("Membuat folder ./save/" + str(directory), "...")
        print()
        print("Berhasil menyimpan data di folder ./save/" + str(directory) + "\n")
    else:
        print()
        print("Saving...")
        save_data(os.path.join(directory, "user.csv"), user)
        save_data(os.path.join(directory, "bahan_bangunan.csv"), bb)
        save_data(os.path.join(directory, "candi.csv"), candi)

        print()
        print("Berhasil menyimpan data di folder ./save/" + str(directory) + "\n")

    os.chdir('../') 