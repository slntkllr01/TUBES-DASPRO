from csvfunction import *
from function import *
import argparse
import sys
import os

def load_csv(folder, filename):
    data = []
    with open(os.path.join(folder, filename), 'r') as file:
        data = csv_to_array(file)
    return data

def load(user, bahan_bangunan, candi):
    parser = argparse.ArgumentParser(prog="python main.py", usage= '%(prog)s ' "nama_folder")

    parser.add_argument("nama_folder",  type=str ,nargs = '?', default = "Tidak ada nama folder yang diberikan!")

    args = parser.parse_args()

    if os.path.isdir(args.nama_folder):
        print("\nloading...")
        print('\nSelamat datang di program "Manajerial Candi"\nMasukkan command "help" untuk daftar\ncommand yang dapat kamu panggil.')

        # load CSV files
        folder = args.nama_folder
        candi_csv = load_csv(folder, 'candi.csv')
        candi = add_to_database(candi, candi_csv)
        bb_csv = load_csv(folder, 'bahan_bangunan.csv')
        bb = add_to_database(bahan_bangunan, bb_csv)
        user_csv = load_csv(folder, 'user.csv')
        user = add_to_database(user, user_csv)
        return candi, bb, user
    else:
        if (args.nama_folder == "Tidak ada nama folder yang diberikan!"):
            print("Tidak ada nama folder yang diberikan!")
            parser.print_usage()
            sys.exit()
        else:
            print("Tidak ada Folder yang bernama", args.nama_folder, "pada sistem")
            parser.print_usage()
            sys.exit()

