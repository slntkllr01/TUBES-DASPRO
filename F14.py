from csvfunction import *
from function import *
from database import *
import os
import argparse

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
    parent = os.getcwd()
    path = os.path.join(parent, directory)

    try:
        os.mkdir(path)
    except:
        FileExistsError

    os.chdir('./' + directory)
    print()
    print("Saving...")

    save_data("user.csv",user)
    save_data("bahan_bangunan.csv",bahan_bangunan)
    save_data("candi.csv",candi)

    print("Berhasil menyimpan data di folder " + str(directory))
    os.chdir('../')

save()
    