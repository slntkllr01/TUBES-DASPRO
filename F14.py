from csvfunction import *
from function import *
from database import *
import os
from pathlib import Path

def save():
    def save_data(file,data):
        data = convert_datas_to_string(data)
        f = open(file,"w")
        f.write(data)
        f.close()

    def convert_datas_to_string(data):
        data_string = ""
        for arr_data in data:
            arr_data_all_string = [str(var) for var in arr_data]
            data_string += ";".join(arr_data_all_string)
            data_string += "\n"
        return data_string
    
    directory = input("Masukkan nama folder penyimpanan: ")
    try:
        save = [directory]
        for s in save:
            Path(f'save/{s}').mkdir(parents=True, exist_ok=True)
    except:
        FileExistsError

    os.chdir('save/' + directory)

    if not os.path.exists('save'): 
        if os.path.isdir(directory):
            print()
            print("Saving...")

            save_data("user.csv",user)
            save_data("bahan_bangunan.csv",bahan_bangunan)
            save_data("candi.csv",candi)

            print()
            print("Membuat folder save/" + str(directory), "...")
            print()
            print("Berhasil menyimpan data di folder save/" + str(directory))
        else:
            print()
            print("Saving...")

            save_data("user.csv",user)
            save_data("bahan_bangunan.csv",bahan_bangunan)
            save_data("candi.csv",candi)

            print()
            print("Membuat folder save...")
            print("Membuat folder save/" + str(directory),"...")
            print()
            print("Berhasil menyimpan data di folder save/" + str(directory))
    else:
        if os.path.isdir(directory):
            print()
            print("Saving...")

            save_data("user.csv",user)
            save_data("bahan_bangunan.csv",bahan_bangunan)
            save_data("candi.csv",candi)

            print()
            print("Berhasil menyimpan data di folder " + str(directory))
        else:
            print()
            print("Saving...")

            save_data("user.csv",user)
            save_data("bahan_bangunan.csv",bahan_bangunan)
            save_data("candi.csv",candi)

            print()
            print("Membuat folder save/" + str(directory), "...")
            print()
            print("Berhasil menyimpan data di folder save/" + str(directory))

    os.chdir('../')  